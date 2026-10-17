'use client';

import React, { useState, useCallback, useMemo, useEffect, useRef } from 'react';
import { 
  Menu, 
  PanelLeftClose, 
  PanelLeftOpen, 
  Plus, 
  Edit3, 
  Check, 
  X, 
  ChevronDown, 
  Cpu, 
  Moon, 
  Sun, 
  Search, 
  BarChart3, 
  Sparkles,
  Compass,
  Trophy,
  ShieldCheck,
  Code2
} from 'lucide-react';
import { ChatConversation, ChatMessage, ChatAttachment, ModelSettings } from '@/types/chat';
import { ChatSidebar } from '@/components/chat/ChatSidebar';
import { ChatMessageList } from '@/components/chat/ChatMessageList';
import { ChatInput } from '@/components/chat/ChatInput';
import { ImageLightbox } from '@/components/chat/ImageLightbox';
import { DocumentViewerModal } from '@/components/chat/DocumentViewerModal';
import { ShortcutsModal } from '@/components/chat/ShortcutsModal';
import { SettingsModal } from '@/components/chat/SettingsModal';
import { CodeSandboxModal } from '@/components/chat/CodeSandboxModal';
import { PromptTemplatesModal } from '@/components/chat/PromptTemplatesModal';
import { AnalyticsModal } from '@/components/chat/AnalyticsModal';
import { LearningRoadmapModal } from '@/components/chat/LearningRoadmapModal';
import { ProblemSetModal, CodingProblem } from '@/components/chat/ProblemSetModal';
import { CodeQualityModal } from '@/components/chat/CodeQualityModal';
import { playSendSound, playCompleteSound } from '@/lib/soundEffects';
import { ToastProvider, useToast } from '@/components/chat/ToastNotification';
import { getSocraticAssistantResponse } from '@/lib/socraticEngine';

const LOCAL_STORAGE_KEY = 'ai_coding_tutor_chat_sessions_v2';
const LOCAL_STORAGE_ACTIVE_KEY = 'ai_coding_tutor_active_chat_id_v2';
const LOCAL_STORAGE_SETTINGS_KEY = 'ai_coding_tutor_settings_v1';
const LOCAL_STORAGE_THEME_KEY = 'ai_coding_tutor_theme_v1';

const AI_MODELS = [
  { id: 'gemini-1.5-flash', name: 'Gemini 1.5 Flash', badge: 'Cloud Free' },
  { id: 'gpt-4o-mini', name: 'GPT-4o-mini', badge: 'Fallback' },
  { id: 'ollama-llama3', name: 'Ollama Llama 3', badge: 'Local Offline' },
];

export default function HomePage() {
  return (
    <ToastProvider>
      <HomePageInner />
    </ToastProvider>
  );
}

function HomePageInner() {
  const { showToast, confirm } = useToast();
  const [mounted, setMounted] = useState<boolean>(false);

  const [conversations, setConversations] = useState<ChatConversation[]>([
    {
      id: 'conv-initial',
      title: 'Cuộc trò chuyện mới',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      messages: [],
    },
  ]);

  const [activeConversationId, setActiveConversationId] = useState<string>('conv-initial');

  const [modelSettings, setModelSettings] = useState<ModelSettings>({
    temperature: 0.7,
    maxTokens: 2048,
    persona: 'socratic',
  });

  const [isDarkMode, setIsDarkMode] = useState<boolean>(false);

  // Load persisted state from localStorage safely on mount
  useEffect(() => {
    setMounted(true);
    try {
      const savedTheme = localStorage.getItem(LOCAL_STORAGE_THEME_KEY);
      if (savedTheme) {
        setIsDarkMode(savedTheme === 'dark');
      } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        setIsDarkMode(true);
      }

      const savedConv = localStorage.getItem(LOCAL_STORAGE_KEY);
      if (savedConv) {
        const parsed = JSON.parse(savedConv);
        if (Array.isArray(parsed) && parsed.length > 0) {
          setConversations(parsed);
        }
      }

        const savedActive = localStorage.getItem(LOCAL_STORAGE_ACTIVE_KEY);
        if (savedActive) {
          setActiveConversationId(savedActive);
        }

        const savedSettings = localStorage.getItem(LOCAL_STORAGE_SETTINGS_KEY);
        if (savedSettings) {
          setModelSettings(JSON.parse(savedSettings));
        }

        const savedSolved = localStorage.getItem('ai_coding_tutor_solved_problems_v1');
        if (savedSolved) {
          try {
            setSolvedProblemIds(JSON.parse(savedSolved));
          } catch {}
        }
      } catch (err) {
        console.warn('Could not read from localStorage:', err);
      }
    }, []);

    const [isDesktopSidebarOpen, setIsDesktopSidebarOpen] = useState<boolean>(true);
    const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);
    const [isGenerating, setIsGenerating] = useState<boolean>(false);
    
    // Modals state
    const [lightboxData, setLightboxData] = useState<{ url: string; name: string } | null>(null);
    const [viewingDocAttachment, setViewingDocAttachment] = useState<ChatAttachment | null>(null);
    const [isShortcutsOpen, setIsShortcutsOpen] = useState<boolean>(false);
    const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);

    // Upgraded Modals state: Code Sandbox, Prompt Templates, Analytics
    const [isSandboxOpen, setIsSandboxOpen] = useState<boolean>(false);
    const [sandboxCode, setSandboxCode] = useState<string>('');
    const [sandboxLang, setSandboxLang] = useState<string>('python');
    const [sandboxProblemTitle, setSandboxProblemTitle] = useState<string>('');
    const [sandboxProblemDesc, setSandboxProblemDesc] = useState<string>('');
    const [sandboxTestCases, setSandboxTestCases] = useState<Array<{id:number; name:string; input:string; expectedOutput:string}>>([]);
    const [solvedProblemIds, setSolvedProblemIds] = useState<string[]>([]);
    const [isPromptTemplatesOpen, setIsPromptTemplatesOpen] = useState<boolean>(false);
    const [isAnalyticsOpen, setIsAnalyticsOpen] = useState<boolean>(false);
    const [isRoadmapOpen, setIsRoadmapOpen] = useState<boolean>(false);
    const [isProblemSetOpen, setIsProblemSetOpen] = useState<boolean>(false);
    const [isCodeQualityOpen, setIsCodeQualityOpen] = useState<boolean>(false);
    const [codeQualityCode, setCodeQualityCode] = useState<string>('');
    const [codeQualityLang, setCodeQualityLang] = useState<string>('python');
    const [injectedText, setInjectedText] = useState<string>('');
    
    // Header inline renaming state
    const [isEditingHeaderTitle, setIsEditingHeaderTitle] = useState<boolean>(false);
  const [headerTitleInput, setHeaderTitleInput] = useState<string>('');

  // Selected AI Model state
  const [selectedModel, setSelectedModel] = useState(AI_MODELS[0]);
  const [isModelDropdownOpen, setIsModelDropdownOpen] = useState(false);

  // In-chat message search
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const searchInputRef = useRef<HTMLInputElement>(null);

  const generationTimerRef = useRef<NodeJS.Timeout | null>(null);
  const streamIntervalRef = useRef<NodeJS.Timeout | null>(null);

  // Active conversation getter
  const activeConversation = useMemo(() => {
    return (
      conversations.find((c) => c.id === activeConversationId) || conversations[0]
    );
  }, [conversations, activeConversationId]);

  // Persist conversations
  useEffect(() => {
    if (!mounted) return;
    try {
      localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(conversations));
      localStorage.setItem(LOCAL_STORAGE_ACTIVE_KEY, activeConversationId);
    } catch {}
  }, [conversations, activeConversationId, mounted]);

  // Persist model settings
  useEffect(() => {
    if (!mounted) return;
    try {
      localStorage.setItem(LOCAL_STORAGE_SETTINGS_KEY, JSON.stringify(modelSettings));
    } catch {}
  }, [modelSettings, mounted]);

  // Persist theme & sync documentElement dark class
  useEffect(() => {
    if (!mounted) return;
    try {
      localStorage.setItem(LOCAL_STORAGE_THEME_KEY, isDarkMode ? 'dark' : 'light');
      if (isDarkMode) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    } catch {}
  }, [isDarkMode, mounted]);

  // Global Keyboard Shortcuts (Ctrl+B, Ctrl+Shift+O, Ctrl+/)
  useEffect(() => {
    const handleGlobalShortcuts = (e: KeyboardEvent) => {
      // Toggle sidebar: Ctrl + B
      if (e.ctrlKey && e.key.toLowerCase() === 'b') {
        e.preventDefault();
        setIsDesktopSidebarOpen((prev) => !prev);
      }
      // New chat: Ctrl + Shift + O
      if (e.ctrlKey && e.shiftKey && e.key.toLowerCase() === 'o') {
        e.preventDefault();
        handleNewConversation();
      }
      // Shortcuts modal: Ctrl + / or ?
      if ((e.ctrlKey && e.key === '/') || (e.key === '?' && !['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName))) {
        e.preventDefault();
        setIsShortcutsOpen((prev) => !prev);
      }
    };

    window.addEventListener('keydown', handleGlobalShortcuts);
    return () => window.removeEventListener('keydown', handleGlobalShortcuts);
  }, []);

  // Rename a conversation
  const handleRenameConversation = useCallback((id: string, newTitle: string) => {
    setConversations((prev) =>
      prev.map((c) => (c.id === id ? { ...c, title: newTitle, updatedAt: new Date().toISOString() } : c))
    );
  }, []);

  // Pin/Unpin conversation
  const handleTogglePin = useCallback((id: string) => {
    setConversations((prev) =>
      prev.map((c) => (c.id === id ? { ...c, isPinned: !c.isPinned, updatedAt: new Date().toISOString() } : c))
    );
  }, []);

  // Start Header renaming
  const handleStartHeaderRename = () => {
    if (activeConversation) {
      setHeaderTitleInput(activeConversation.title);
      setIsEditingHeaderTitle(true);
    }
  };

  const handleSaveHeaderRename = () => {
    const trimmed = headerTitleInput.trim();
    if (trimmed && activeConversation) {
      handleRenameConversation(activeConversation.id, trimmed);
    }
    setIsEditingHeaderTitle(false);
  };

  // Create a new conversation
  const handleNewConversation = useCallback(() => {
    const newId = `conv-${Date.now()}`;
    const newConv: ChatConversation = {
      id: newId,
      title: 'Cuộc trò chuyện mới',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      messages: [],
    };
    setConversations((prev) => [newConv, ...prev]);
    setActiveConversationId(newId);
  }, []);

  // Delete a conversation
  const handleDeleteConversation = useCallback((id: string) => {
    setConversations((prev) => {
      const remaining = prev.filter((c) => c.id !== id);
      if (remaining.length === 0) {
        const freshId = `conv-${Date.now()}`;
        return [
          {
            id: freshId,
            title: 'Cuộc trò chuyện mới',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString(),
            messages: [],
          },
        ];
      }
      return remaining;
    });

    if (activeConversationId === id) {
      setConversations((prev) => {
        setActiveConversationId(prev[0]?.id || '');
        return prev;
      });
    }
  }, [activeConversationId]);

  // Code Sandbox handler
  const handleRunCode = useCallback((code: string, language: string) => {
    setSandboxCode(code);
    setSandboxLang(language);
    setSandboxProblemTitle('');
    setSandboxProblemDesc('');
    setSandboxTestCases([]);
    setIsSandboxOpen(true);
  }, []);

  const handleSolveInSandbox = useCallback((problem: CodingProblem, language: string) => {
    const starterCode = language === 'javascript'
      ? (problem.starterCode.javascript || problem.starterCode.python)
      : (problem.starterCode.python);
    setSandboxCode(starterCode || '');
    setSandboxLang(language);
    setSandboxProblemTitle(`Bài tập #${problem.number}: ${problem.title}`);
    setSandboxProblemDesc(problem.description);
    setSandboxTestCases(problem.testCases);
    setIsSandboxOpen(true);
  }, []);

  const handleProblemSolved = useCallback((problemTitle: string) => {
    setSolvedProblemIds((prev) => {
      if (!prev.includes(problemTitle)) {
        const next = [...prev, problemTitle];
        try {
          localStorage.setItem('ai_coding_tutor_solved_problems_v1', JSON.stringify(next));
        } catch {}
        showToast({
          type: 'success',
          title: 'Vượt qua 100% Test Cases!',
          message: `Chúc mừng bạn đã hoàn thành xuất sắc: "${problemTitle}" (+50 XP)`,
          duration: 5000,
        });
        return next;
      }
      return prev;
    });
  }, [showToast]);

  const handleOpenCodeQuality = useCallback((code?: string, language?: string) => {
    setCodeQualityCode(code || sandboxCode || '# Dán mã nguồn cần đánh giá vào đây\n');
    setCodeQualityLang(language || sandboxLang || 'python');
    setIsCodeQualityOpen(true);
  }, [sandboxCode, sandboxLang]);

  const handleAskAIAboutCode = useCallback((code: string, language: string) => {
    const formatted = `Hãy phân tích và hướng dẫn giải thích giúp tôi đoạn mã ${language.toUpperCase()} này:\n\n\`\`\`${language}\n${code}\n\`\`\``;
    setInjectedText(formatted);
  }, []);

  const handleSelectPromptTemplate = useCallback((promptText: string) => {
    setInjectedText(promptText);
  }, []);

  const handleStartLessonFromRoadmap = useCallback((lessonPrompt: string) => {
    setInjectedText(lessonPrompt);
    showToast({ type: 'info', title: 'Bắt đầu bài học Socratic', message: 'Câu hỏi đã được điền vào ô nhập. Nhấn Enter để gửi!', duration: 3000 });
  }, [showToast]);

  const handleImportConversation = useCallback((imported: ChatConversation) => {
    setConversations((prev) => {
      const existing = prev.filter((c) => c.id !== imported.id);
      return [imported, ...existing];
    });
    setActiveConversationId(imported.id);
    showToast({
      type: 'success',
      title: 'Khôi phục thành công',
      message: `Đã nạp cuộc trò chuyện: "${imported.title}"`,
    });
  }, [showToast]);

  // Delete an individual message
  const handleDeleteMessage = useCallback((messageId: string) => {
    setConversations((prev) =>
      prev.map((conv) => {
        if (conv.id === activeConversationId) {
          return {
            ...conv,
            messages: conv.messages.filter((m) => m.id !== messageId),
          };
        }
        return conv;
      })
    );
  }, [activeConversationId]);

  // Clear all conversations
  const handleClearAll = useCallback(() => {
    confirm(
      'Bạn có chắc chắn muốn xóa toàn bộ lịch sử các cuộc trò chuyện? Hành động này không thể hoàn tác.',
      () => {
        const freshId = `conv-${Date.now()}`;
        setConversations([
          {
            id: freshId,
            title: 'Cuộc trò chuyện mới',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString(),
            messages: [],
          },
        ]);
        setActiveConversationId(freshId);
        showToast({ type: 'success', title: 'Đã xóa tất cả', message: 'Lịch sử hội thoại đã được xóa sạch.' });
      }
    );
  }, [confirm, showToast]);

  // Stop Generating
  const handleStopGenerating = useCallback(() => {
    if (generationTimerRef.current) {
      clearTimeout(generationTimerRef.current);
      generationTimerRef.current = null;
    }
    if (streamIntervalRef.current) {
      clearInterval(streamIntervalRef.current);
      streamIntervalRef.current = null;
    }
    // Finalize any streaming message
    setConversations((prev) =>
      prev.map((conv) => ({
        ...conv,
        messages: conv.messages.map((m) =>
          m.isStreaming ? { ...m, isStreaming: false } : m
        ),
      }))
    );
    setIsGenerating(false);
    showToast({ type: 'info', title: 'Đã dừng phản hồi', duration: 2000 });
  }, [showToast]);

  // Handle message sending with typewriter streaming effect
  const handleSendMessage = useCallback((text: string, attachments: ChatAttachment[]) => {
    const userMsg: ChatMessage = {
      id: `msg-user-${Date.now()}`,
      role: 'user',
      content: text,
      attachments: attachments.length > 0 ? attachments : undefined,
      timestamp: new Date().toISOString(),
    };

    let convTitle = '';
    setConversations((prev) =>
      prev.map((conv) => {
        if (conv.id === activeConversationId) {
          let newTitle = conv.title;
          if (conv.messages.length === 0 && conv.title === 'Cuộc trò chuyện mới') {
            if (text.trim()) {
              newTitle = text.trim().slice(0, 40) + (text.trim().length > 40 ? '...' : '');
            } else if (attachments.length > 0) {
              newTitle = `Đính kèm: ${attachments[0].name}`;
            }
          }
          convTitle = newTitle;
          return {
            ...conv,
            title: newTitle,
            updatedAt: new Date().toISOString(),
            messages: [...conv.messages, userMsg],
          };
        }
        return conv;
      })
    );

    setIsGenerating(true);
    playSendSound();
    setInjectedText('');

    // Fetch response from Socratic Engine (Live Gemini, Ollama, or Built-in Pedagogical Matrix)
    getSocraticAssistantResponse(text, attachments, modelSettings, selectedModel.name)
      .then((aiResponse) => {
        const aiMsgId = `msg-ai-${Date.now()}`;
        const fullContent = aiResponse.content;

        // Insert empty streaming placeholder
        setConversations((prev) =>
          prev.map((conv) => {
            if (conv.id === activeConversationId) {
              return {
                ...conv,
                updatedAt: new Date().toISOString(),
                messages: [
                  ...conv.messages,
                  {
                    id: aiMsgId,
                    role: 'assistant' as const,
                    content: '',
                    timestamp: new Date().toISOString(),
                    isDemoNotice: false,
                    isStreaming: true,
                    suggestedFollowUps: aiResponse.followUps,
                  },
                ],
              };
            }
            return conv;
          })
        );

        // Typewriter character-by-character streaming
        let charIdx = 0;
        const CHUNK = 5; // characters per tick
        const SPEED = 16; // ms per tick

        if (streamIntervalRef.current) clearInterval(streamIntervalRef.current);

        streamIntervalRef.current = setInterval(() => {
          charIdx += CHUNK;
          const slicedContent = fullContent.slice(0, charIdx);
          const done = charIdx >= fullContent.length;

          setConversations((prev) =>
            prev.map((conv) => {
              if (conv.id !== activeConversationId) return conv;
              return {
                ...conv,
                messages: conv.messages.map((m) =>
                  m.id === aiMsgId
                    ? { ...m, content: slicedContent, isStreaming: !done }
                    : m
                ),
              };
            })
          );

          if (done) {
            clearInterval(streamIntervalRef.current!);
            streamIntervalRef.current = null;
            generationTimerRef.current = null;
            setIsGenerating(false);
            playCompleteSound();
          }
        }, SPEED);
      })
      .catch((err: any) => {
        setIsGenerating(false);
        showToast({ type: 'error', title: 'Lỗi sinh phản hồi AI', message: err?.message || 'Không thể tạo câu trả lời' });
      });
  }, [activeConversationId, selectedModel, modelSettings, showToast]);

  // Edit user message and regenerate from that point
  const handleEditUserMessage = useCallback((messageId: string, newContent: string) => {
    // Find index of message
    const msgIdx = activeConversation.messages.findIndex((m) => m.id === messageId);
    if (msgIdx === -1) return;

    const targetMsg = activeConversation.messages[msgIdx];
    const attachments = targetMsg.attachments || [];

    // Cut off messages after this one
    setConversations((prev) =>
      prev.map((conv) => {
        if (conv.id === activeConversationId) {
          return {
            ...conv,
            messages: conv.messages.slice(0, msgIdx),
          };
        }
        return conv;
      })
    );

    // Resend with new content
    setTimeout(() => {
      handleSendMessage(newContent, attachments);
    }, 50);
  }, [activeConversation, activeConversationId, handleSendMessage]);

  // Regenerate Response with typewriter effect
  const handleRegenerateResponse = useCallback(() => {
    if (!activeConversation || activeConversation.messages.length === 0) return;
    const lastUserMsg = [...activeConversation.messages].reverse().find((m) => m.role === 'user');
    if (!lastUserMsg) return;

    showToast({ type: 'info', title: 'Đang tạo lại câu trả lời...', duration: 2500 });
    setIsGenerating(true);

    getSocraticAssistantResponse(lastUserMsg.content, lastUserMsg.attachments || [], modelSettings, selectedModel.name)
      .then((aiResponse) => {
        const fullContent = aiResponse.content;
        const aiMsgId = `msg-ai-regen-${Date.now()}`;

        setConversations((prev) =>
          prev.map((conv) => {
            if (conv.id !== activeConversationId) return conv;
            return {
              ...conv,
              updatedAt: new Date().toISOString(),
              messages: [
                ...conv.messages,
                {
                  id: aiMsgId,
                  role: 'assistant' as const,
                  content: '',
                  timestamp: new Date().toISOString(),
                  isDemoNotice: false,
                  isStreaming: true,
                  suggestedFollowUps: aiResponse.followUps,
                },
              ],
            };
          })
        );

        let charIdx = 0;
        const CHUNK = 5;
        const SPEED = 16;
        if (streamIntervalRef.current) clearInterval(streamIntervalRef.current);

        streamIntervalRef.current = setInterval(() => {
          charIdx += CHUNK;
          const slicedContent = fullContent.slice(0, charIdx);
          const done = charIdx >= fullContent.length;
          setConversations((prev) =>
            prev.map((conv) => {
              if (conv.id !== activeConversationId) return conv;
              return {
                ...conv,
                messages: conv.messages.map((m) =>
                  m.id === aiMsgId ? { ...m, content: slicedContent, isStreaming: !done } : m
                ),
              };
            })
          );
          if (done) {
            clearInterval(streamIntervalRef.current!);
            streamIntervalRef.current = null;
            generationTimerRef.current = null;
            setIsGenerating(false);
            playCompleteSound();
          }
        }, SPEED);
      })
      .catch((err: any) => {
        setIsGenerating(false);
        showToast({ type: 'error', title: 'Lỗi tạo lại phản hồi', message: err?.message });
      });
  }, [activeConversation, activeConversationId, selectedModel, modelSettings, showToast]);

  // Filtered messages for in-chat search
  const filteredMessages = useMemo(() => {
    const msgs = activeConversation?.messages || [];
    if (!searchQuery.trim()) return msgs;
    const q = searchQuery.toLowerCase();
    return msgs.filter((m) => m.content.toLowerCase().includes(q));
  }, [activeConversation?.messages, searchQuery]);

  // Open search with keyboard shortcut Ctrl+F inside chat
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.key.toLowerCase() === 'f') {
        e.preventDefault();
        setIsSearchOpen((prev) => !prev);
        setTimeout(() => searchInputRef.current?.focus(), 50);
      }
      if (e.key === 'Escape' && isSearchOpen) {
        setIsSearchOpen(false);
        setSearchQuery('');
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [isSearchOpen]);

  return (
    <div className={`flex h-screen w-full overflow-hidden transition-colors duration-300 ${isDarkMode ? 'dark bg-slate-950 text-slate-100' : 'bg-slate-50 text-slate-900'}`}>
      {/* Lightbox Modal for Images */}
      <ImageLightbox
        imageUrl={lightboxData?.url || null}
        imageName={lightboxData?.name || null}
        onClose={() => setLightboxData(null)}
      />

      {/* Document Viewer Modal for Code/Text files */}
      <DocumentViewerModal
        attachment={viewingDocAttachment}
        onClose={() => setViewingDocAttachment(null)}
      />

      {/* Keyboard Shortcuts Modal */}
      <ShortcutsModal
        isOpen={isShortcutsOpen}
        onClose={() => setIsShortcutsOpen(false)}
      />

      {/* Settings Modal */}
      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
        settings={modelSettings}
        onUpdateSettings={setModelSettings}
        isDarkMode={isDarkMode}
        onToggleDarkMode={() => setIsDarkMode(!isDarkMode)}
      />

      {/* Interactive Code Sandbox Modal */}
      <CodeSandboxModal
        isOpen={isSandboxOpen}
        onClose={() => setIsSandboxOpen(false)}
        initialCode={sandboxCode}
        initialLanguage={sandboxLang}
        onAskAIAboutCode={handleAskAIAboutCode}
        problemTitle={sandboxProblemTitle}
        problemDescription={sandboxProblemDesc}
        initialTestCases={sandboxTestCases}
        onOpenCodeQuality={handleOpenCodeQuality}
        onProblemSolved={handleProblemSolved}
      />

      {/* Socratic Prompt Templates Modal */}
      <PromptTemplatesModal
        isOpen={isPromptTemplatesOpen}
        onClose={() => setIsPromptTemplatesOpen(false)}
        onSelectPrompt={handleSelectPromptTemplate}
      />

      {/* Analytics & Token Usage Modal */}
      <AnalyticsModal
        isOpen={isAnalyticsOpen}
        onClose={() => setIsAnalyticsOpen(false)}
        conversations={conversations}
      />

      {/* Learning Roadmap Modal */}
      <LearningRoadmapModal
        isOpen={isRoadmapOpen}
        onClose={() => setIsRoadmapOpen(false)}
        onStartLesson={handleStartLessonFromRoadmap}
        onOpenPracticeInSandbox={(code, lang) => { setSandboxCode(code); setSandboxLang(lang); setSandboxProblemTitle(''); setSandboxTestCases([]); setIsSandboxOpen(true); setIsRoadmapOpen(false); }}
      />

      {/* Problem Set & Arena Modal */}
      <ProblemSetModal
        isOpen={isProblemSetOpen}
        onClose={() => setIsProblemSetOpen(false)}
        onSolveInSandbox={handleSolveInSandbox}
        onAskAIHint={(prompt) => { setInjectedText(prompt); setIsProblemSetOpen(false); }}
        solvedProblemIds={solvedProblemIds}
      />

      {/* Code Quality Analysis Modal */}
      <CodeQualityModal
        isOpen={isCodeQualityOpen}
        onClose={() => setIsCodeQualityOpen(false)}
        initialCode={codeQualityCode}
        initialLanguage={codeQualityLang}
        onApplyRefactoredCode={(code) => { setSandboxCode(code); setIsSandboxOpen(true); setIsCodeQualityOpen(false); }}
        onAskAIAboutQuality={(prompt) => { setInjectedText(prompt); setIsCodeQualityOpen(false); }}
      />

      {/* Left Sidebar */}
      <ChatSidebar
        conversations={conversations}
        activeConversationId={activeConversation?.id || ''}
        onSelectConversation={setActiveConversationId}
        onNewConversation={handleNewConversation}
        onDeleteConversation={handleDeleteConversation}
        onRenameConversation={handleRenameConversation}
        onTogglePinConversation={handleTogglePin}
        onClearAll={handleClearAll}
        onOpenShortcuts={() => setIsShortcutsOpen(true)}
        onOpenSettings={() => setIsSettingsOpen(true)}
        onOpenAnalytics={() => setIsAnalyticsOpen(true)}
        onImportConversation={handleImportConversation}
        isOpen={isDesktopSidebarOpen}
        onToggle={() => setIsDesktopSidebarOpen((prev) => !prev)}
        isMobileOpen={isMobileSidebarOpen}
        onCloseMobile={() => setIsMobileSidebarOpen(false)}
        onOpenRoadmap={() => setIsRoadmapOpen(true)}
        onOpenProblemSet={() => setIsProblemSetOpen(true)}
        onOpenCodeQuality={() => { setCodeQualityCode(sandboxCode || '# Dán mã nguồn cần đánh giá vào đây\n'); setCodeQualityLang(sandboxLang); setIsCodeQualityOpen(true); }}
        onOpenSandbox={() => { setSandboxCode('# Mở Sandbox trống để viết code mới\nprint("Xin chào, Gia sư AI!")'); setSandboxLang('python'); setSandboxProblemTitle(''); setSandboxTestCases([]); setIsSandboxOpen(true); }}
      />

      {/* Main Chat Interface */}
      <div className="flex-1 flex flex-col h-full min-w-0 bg-white dark:bg-slate-900 transition-colors duration-300">
        {/* Top Navbar — glassmorphism */}
        <header className="h-14 border-b border-slate-200/80 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 backdrop-blur-xl flex items-center justify-between px-4 shrink-0 z-10 shadow-sm">
          <div className="flex items-center gap-2 min-w-0">
            {/* Mobile menu trigger */}
            <button
              type="button"
              onClick={() => setIsMobileSidebarOpen(true)}
              className="md:hidden rounded-lg p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 focus:outline-none transition"
              aria-label="Mở danh sách cuộc trò chuyện"
            >
              <Menu className="h-5 w-5" />
            </button>

            {/* Desktop collapse toggle */}
            <button
              type="button"
              onClick={() => setIsDesktopSidebarOpen((prev) => !prev)}
              className="hidden md:flex rounded-lg p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 focus:outline-none transition"
              title={isDesktopSidebarOpen ? 'Thu gọn thanh bên (Ctrl + B)' : 'Mở rộng thanh bên (Ctrl + B)'}
              aria-label="Thu gọn hoặc mở rộng thanh bên"
            >
              {isDesktopSidebarOpen ? (
                <PanelLeftClose className="h-5 w-5" />
              ) : (
                <PanelLeftOpen className="h-5 w-5" />
              )}
            </button>

            {/* Active Title with inline editing */}
            <div className="flex items-center gap-2 truncate pl-1">
              {isEditingHeaderTitle ? (
                <div className="flex items-center gap-1.5">
                  <input
                    type="text"
                    value={headerTitleInput}
                    onChange={(e) => setHeaderTitleInput(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') handleSaveHeaderRename();
                      if (e.key === 'Escape') setIsEditingHeaderTitle(false);
                    }}
                    autoFocus
                    className="rounded-md border border-blue-400 bg-white dark:bg-slate-800 px-2 py-0.5 text-sm font-bold text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500/20"
                  />
                  <button
                    type="button"
                    onClick={handleSaveHeaderRename}
                    className="rounded p-1 text-emerald-600 hover:bg-emerald-50 dark:hover:bg-emerald-950 transition"
                    title="Lưu (Enter)"
                  >
                    <Check className="h-4 w-4" />
                  </button>
                  <button
                    type="button"
                    onClick={() => setIsEditingHeaderTitle(false)}
                    className="rounded p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                    title="Hủy (Esc)"
                  >
                    <X className="h-4 w-4" />
                  </button>
                </div>
              ) : (
                <div className="group/title flex items-center gap-1.5 truncate">
                  <span className="font-extrabold text-sm text-slate-900 dark:text-slate-100 truncate">
                    {activeConversation?.title || 'Cuộc trò chuyện'}
                  </span>
                  <button
                    type="button"
                    onClick={handleStartHeaderRename}
                    className="opacity-0 group-hover/title:opacity-100 rounded p-1 text-slate-400 hover:text-blue-600 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                    title="Đổi tên cuộc trò chuyện này"
                  >
                    <Edit3 className="h-3.5 w-3.5" />
                  </button>
                </div>
              )}
            </div>
          </div>

          {/* Right Header Controls */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            {/* Quick Studio Tools */}
            <div className="hidden lg:flex items-center gap-1 mr-1 border-r border-slate-200 dark:border-slate-800 pr-2">
              <button
                type="button"
                onClick={() => setIsRoadmapOpen(true)}
                className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-blue-50/70 dark:hover:bg-blue-950/50 transition border border-transparent hover:border-blue-200 dark:hover:border-blue-800/60"
                title="Lộ trình học tập & Cây kỹ năng lập trình"
              >
                <Compass className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400" />
                <span>Lộ trình</span>
              </button>

              <button
                type="button"
                onClick={() => setIsProblemSetOpen(true)}
                className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-amber-600 dark:hover:text-amber-400 hover:bg-amber-50/70 dark:hover:bg-amber-950/50 transition border border-transparent hover:border-amber-200 dark:hover:border-amber-800/60"
                title="Kho bài tập thuật toán & Đấu trường code"
              >
                <Trophy className="h-3.5 w-3.5 text-amber-500" />
                <span>Bài tập</span>
              </button>

              <button
                type="button"
                onClick={() => {
                  setSandboxCode('# Mở Code Sandbox trực tiếp\nprint("Hello, AI Coding Tutor!")');
                  setSandboxLang('python');
                  setSandboxProblemTitle('');
                  setSandboxTestCases([]);
                  setIsSandboxOpen(true);
                }}
                className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-emerald-50/70 dark:hover:bg-emerald-950/50 transition border border-transparent hover:border-emerald-200 dark:hover:border-emerald-800/60"
                title="Mở trình thực thi code & Sandbox test case"
              >
                <Code2 className="h-3.5 w-3.5 text-emerald-500" />
                <span>Sandbox</span>
              </button>

              <button
                type="button"
                onClick={() => {
                  setCodeQualityCode(sandboxCode || '# Dán mã nguồn cần đánh giá vào đây\n');
                  setCodeQualityLang(sandboxLang);
                  setIsCodeQualityOpen(true);
                }}
                className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-indigo-600 dark:hover:text-indigo-400 hover:bg-indigo-50/70 dark:hover:bg-indigo-950/50 transition border border-transparent hover:border-indigo-200 dark:hover:border-indigo-800/60"
                title="Kiểm tra chất lượng code, PEP 8 & Big-O"
              >
                <ShieldCheck className="h-3.5 w-3.5 text-indigo-500" />
                <span>Soát lỗi</span>
              </button>
            </div>
            {/* Quick Dark Mode toggle */}
            <button
              type="button"
              onClick={() => setIsDarkMode(!isDarkMode)}
              className="relative rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 p-2 text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700 transition-all group overflow-hidden"
              title={isDarkMode ? 'Chuyển sang giao diện Sáng' : 'Chuyển sang giao diện Tối'}
            >
              <span className="absolute inset-0 opacity-0 group-hover:opacity-100 bg-gradient-to-br from-amber-400/10 to-blue-500/10 transition-opacity" />
              {isDarkMode 
                ? <Sun className="h-4 w-4 text-amber-400 drop-shadow-sm" /> 
                : <Moon className="h-4 w-4 text-slate-600" />
              }
            </button>

            {/* Model Selector Dropdown */}
            <div className="relative">
              <button
                type="button"
                onClick={() => setIsModelDropdownOpen(!isModelDropdownOpen)}
                className="flex items-center gap-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-2.5 py-1.5 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:border-blue-400 dark:hover:border-blue-600 hover:shadow-sm transition-all"
                title="Chọn mô hình AI thử nghiệm"
              >
                <Cpu className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400" />
                <span className="hidden sm:inline">{selectedModel.name}</span>
                <span className="rounded-full bg-blue-100 dark:bg-blue-900/60 px-1.5 py-0.5 text-[9px] font-bold text-blue-700 dark:text-blue-300">
                  {selectedModel.badge}
                </span>
                <ChevronDown className={`h-3 w-3 text-slate-400 transition-transform duration-200 ${isModelDropdownOpen ? 'rotate-180' : ''}`} />
              </button>

              {isModelDropdownOpen && (
                <div 
                  className="absolute right-0 mt-2 w-56 rounded-2xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-1.5 shadow-xl dark:shadow-black/40 z-20 animate-scale-in"
                  onClick={() => setIsModelDropdownOpen(false)}
                >
                  <div className="px-2.5 py-1.5 text-[10px] font-bold uppercase tracking-widest text-slate-400 dark:text-slate-500">
                    Mô hình AI dự kiến
                  </div>
                  {AI_MODELS.map((model) => (
                    <button
                      key={model.id}
                      type="button"
                      onClick={() => setSelectedModel(model)}
                      className={`flex w-full items-center justify-between rounded-xl px-2.5 py-2 text-xs font-medium transition-all ${
                        selectedModel.id === model.id
                          ? 'bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 font-bold'
                          : 'text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700'
                      }`}
                    >
                      <span>{model.name}</span>
                      <span className="rounded-full bg-slate-100 dark:bg-slate-700 px-2 py-0.5 text-[9px] font-semibold text-slate-500 dark:text-slate-400">
                        {model.badge}
                      </span>
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* Prompt Templates quick trigger */}
            <button
              type="button"
              onClick={() => setIsPromptTemplatesOpen(true)}
              className="rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 p-2 text-slate-600 dark:text-slate-300 hover:text-amber-500 dark:hover:text-amber-400 hover:bg-white dark:hover:bg-slate-700 transition"
              title="Kho mẫu câu hỏi Socratic & Thuật toán"
            >
              <Sparkles className="h-4 w-4 text-amber-500" />
            </button>

            {/* Analytics & Token Usage button */}
            <button
              type="button"
              onClick={() => setIsAnalyticsOpen(true)}
              className="rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 p-2 text-slate-600 dark:text-slate-300 hover:text-emerald-500 dark:hover:text-emerald-400 hover:bg-white dark:hover:bg-slate-700 transition"
              title="Thống kê hoạt động & Token"
            >
              <BarChart3 className="h-4 w-4 text-emerald-500" />
            </button>

            {/* In-chat search toggle */}
            <button
              type="button"
              onClick={() => { setIsSearchOpen((v) => !v); setTimeout(() => searchInputRef.current?.focus(), 50); }}
              className={`rounded-xl border p-2 transition ${
                isSearchOpen
                  ? 'border-blue-400 bg-blue-50 dark:bg-blue-950 text-blue-600'
                  : 'border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
              }`}
              title="Tìm kiếm trong hội thoại (Ctrl + F)"
            >
              <Search className="h-4 w-4" />
            </button>

            {/* New Chat quick button */}
            <button
              type="button"
              onClick={handleNewConversation}
              className="flex items-center gap-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-1.5 text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-700 shadow-2xs transition active:scale-95"
              title="Tạo cuộc trò chuyện mới (Ctrl + Shift + O)"
            >
              <Plus className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400" />
              <span className="hidden sm:inline">Đoạn chat mới</span>
            </button>
          </div>
        </header>

        {/* In-chat search bar */}
        {isSearchOpen && (
          <div className="flex items-center gap-2 px-4 py-2 border-b border-slate-200 dark:border-slate-700 bg-slate-50/90 dark:bg-slate-800/90 backdrop-blur-sm animate-in slide-in-from-top-2 duration-200">
            <Search className="h-3.5 w-3.5 text-slate-400 shrink-0" />
            <input
              ref={searchInputRef}
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm kiếm tin nhắn trong cuộc hội thoại..."
              className="flex-1 bg-transparent text-sm text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none"
            />
            {searchQuery && (
              <span className="text-[11px] text-slate-400 font-medium">
                {filteredMessages.length} kết quả
              </span>
            )}
            <button
              type="button"
              onClick={() => { setIsSearchOpen(false); setSearchQuery(''); }}
              className="rounded-md p-1 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 transition"
            >
              <X className="h-3.5 w-3.5" />
            </button>
          </div>
        )}

        {/* Message Thread Area */}
        <ChatMessageList
          messages={searchQuery.trim() ? filteredMessages : (activeConversation?.messages || [])}
          isGenerating={isGenerating && !searchQuery}
          onSelectSuggestion={(q) => handleSendMessage(q, [])}
          onViewImage={(url, name) => setLightboxData({ url, name })}
          onViewDocument={(att) => setViewingDocAttachment(att)}
          onRegenerate={handleRegenerateResponse}
          onDeleteMessage={handleDeleteMessage}
          onEditUserMessage={handleEditUserMessage}
          onRunCode={handleRunCode}
          onOpenRoadmap={() => setIsRoadmapOpen(true)}
          onOpenProblemSet={() => setIsProblemSetOpen(true)}
          onOpenSandbox={() => {
            setSandboxCode('# Mở Code Sandbox trực tiếp\nprint("Hello World!")');
            setSandboxLang('python');
            setSandboxProblemTitle('');
            setSandboxTestCases([]);
            setIsSandboxOpen(true);
          }}
          onOpenCodeQuality={handleOpenCodeQuality}
        />

        {/* Bottom Composer Box */}
        <ChatInput
          onSendMessage={handleSendMessage}
          onViewImage={(url, name) => setLightboxData({ url, name })}
          onViewDocument={(att) => setViewingDocAttachment(att)}
          isGenerating={isGenerating}
          onStopGenerating={handleStopGenerating}
          disabled={isSearchOpen && !!searchQuery}
          onOpenPromptTemplates={() => setIsPromptTemplatesOpen(true)}
          externalInputText={injectedText}
        />
      </div>
    </div>
  );
}
