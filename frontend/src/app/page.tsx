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
  Search
} from 'lucide-react';
import { ChatConversation, ChatMessage, ChatAttachment, ModelSettings } from '@/types/chat';
import { ChatSidebar } from '@/components/chat/ChatSidebar';
import { ChatMessageList } from '@/components/chat/ChatMessageList';
import { ChatInput } from '@/components/chat/ChatInput';
import { ImageLightbox } from '@/components/chat/ImageLightbox';
import { DocumentViewerModal } from '@/components/chat/DocumentViewerModal';
import { ShortcutsModal } from '@/components/chat/ShortcutsModal';
import { SettingsModal } from '@/components/chat/SettingsModal';
import { ToastProvider, useToast } from '@/components/chat/ToastNotification';

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
  const [conversations, setConversations] = useState<ChatConversation[]>(() => {
    if (typeof window !== 'undefined') {
      try {
        const saved = localStorage.getItem(LOCAL_STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved);
          if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        }
      } catch {}
    }
    return [
      {
        id: 'conv-initial',
        title: 'Cuộc trò chuyện mới',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        messages: [],
      },
    ];
  });

  const [activeConversationId, setActiveConversationId] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      try {
        const saved = localStorage.getItem(LOCAL_STORAGE_ACTIVE_KEY);
        if (saved) return saved;
      } catch {}
    }
    return 'conv-initial';
  });

  const [modelSettings, setModelSettings] = useState<ModelSettings>(() => {
    if (typeof window !== 'undefined') {
      try {
        const saved = localStorage.getItem(LOCAL_STORAGE_SETTINGS_KEY);
        if (saved) return JSON.parse(saved);
      } catch {}
    }
    return {
      temperature: 0.7,
      maxTokens: 2048,
      persona: 'socratic',
    };
  });

  const [isDarkMode, setIsDarkMode] = useState<boolean>(() => {
    if (typeof window !== 'undefined') {
      try {
        const saved = localStorage.getItem(LOCAL_STORAGE_THEME_KEY);
        if (saved) return saved === 'dark';
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
          return true;
        }
      } catch {}
    }
    return false;
  });

  const [isDesktopSidebarOpen, setIsDesktopSidebarOpen] = useState<boolean>(true);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  
  // Modals state
  const [lightboxData, setLightboxData] = useState<{ url: string; name: string } | null>(null);
  const [viewingDocAttachment, setViewingDocAttachment] = useState<ChatAttachment | null>(null);
  const [isShortcutsOpen, setIsShortcutsOpen] = useState<boolean>(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  
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
    try {
      localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(conversations));
      localStorage.setItem(LOCAL_STORAGE_ACTIVE_KEY, activeConversationId);
    } catch {}
  }, [conversations, activeConversationId]);

  // Persist model settings
  useEffect(() => {
    try {
      localStorage.setItem(LOCAL_STORAGE_SETTINGS_KEY, JSON.stringify(modelSettings));
    } catch {}
  }, [modelSettings]);

  // Persist theme & sync documentElement dark class
  useEffect(() => {
    try {
      localStorage.setItem(LOCAL_STORAGE_THEME_KEY, isDarkMode ? 'dark' : 'light');
      if (isDarkMode) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    } catch {}
  }, [isDarkMode]);

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

    // Contextual follow-ups
    const followUps: string[] = [];
    if (text.toLowerCase().includes('sort') || text.toLowerCase().includes('thuật toán')) {
      followUps.push('Đi sâu vào phân tích Time Complexity O(n log n)', 'Cách viết bằng ngôn ngữ C++', 'Tối ưu hóa bộ nhớ phụ');
    } else if (text.toLowerCase().includes('error') || text.toLowerCase().includes('lỗi')) {
      followUps.push('Xem nguyên nhân gây tràn bộ nhớ Stack', 'Các bước debug với gdb', 'Gợi ý cách sửa mã an toàn');
    } else {
      followUps.push('Giải thích chi tiết hơn về phần này', 'Đưa ra ví dụ minh họa bằng Python', 'Kiểm tra lỗi tiềm ẩn theo CWE');
    }

    // Delay before AI starts "typing"
    generationTimerRef.current = setTimeout(() => {
      const fileCountText = attachments.length > 0
        ? ` cùng **${attachments.length} tệp đính kèm** (${attachments.map((a) => a.name).join(', ')})`
        : '';

      const sampleCodeDemo =
        text.toLowerCase().includes('sort') || text.toLowerCase().includes('thuật toán')
          ? `\n\n### Đoạn mã tham khảo thuật toán:\n\`\`\`python\ndef quick_sort(arr):\n    """Thuật toán phân hoạch QuickSort - O(n log n)"""\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n\`\`\``
          : '';

      const personaLabel =
        modelSettings.persona === 'socratic'
          ? 'Trợ giảng Socratic'
          : modelSettings.persona === 'algorithm_expert'
          ? 'Chuyên gia Giải thuật'
          : 'Rà soát Clean Code';

      const fullContent = `**[Mô hình: ${selectedModel.name} | Phong cách: ${personaLabel}]**\n\nHệ thống đã tiếp nhận dữ liệu văn bản${fileCountText}.${sampleCodeDemo}\n\n> Lưu ý: Tính năng LLM và RAG (ChromaDB) đang sẵn sàng kết nối. Yêu cầu của bạn đã được ghi nhận trong phiên làm việc.`;

      const aiMsgId = `msg-ai-${Date.now()}`;

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
                  isDemoNotice: true,
                  isStreaming: true,
                  suggestedFollowUps: followUps,
                },
              ],
            };
          }
          return conv;
        })
      );

      // Typewriter character-by-character streaming
      let charIdx = 0;
      const CHUNK = 4; // characters per tick
      const SPEED = 18; // ms per tick

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
        }
      }, SPEED);
    }, 400);
  }, [activeConversationId, selectedModel, modelSettings]);

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

    generationTimerRef.current = setTimeout(() => {
      const fullContent = `**[Mô hình: ${selectedModel.name} | Tạo lại]**\n\nĐã tạo lại phản hồi mới cho yêu cầu của bạn.\n\n> Hệ thống phản hồi theo phong cách ${
        modelSettings.persona === 'socratic' ? 'Socratic' : 'Chuyên gia'
      }. Khi backend kích hoạt, nội dung sẽ được xử lý qua RAG.`;

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
                isDemoNotice: true,
                isStreaming: true,
                suggestedFollowUps: ['Đi sâu vào phân tích Time Complexity O(n log n)', 'Cách viết bằng ngôn ngữ C++', 'Tối ưu hóa bộ nhớ phụ'],
              },
            ],
          };
        })
      );

      let charIdx = 0;
      const CHUNK = 4;
      const SPEED = 18;
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
        }
      }, SPEED);
    }, 400);
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
    <div className={`flex h-screen w-full overflow-hidden transition-colors ${isDarkMode ? 'dark bg-slate-950 text-slate-100' : 'bg-white text-[#202123]'}`}>
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
        isOpen={isDesktopSidebarOpen}
        onToggle={() => setIsDesktopSidebarOpen((prev) => !prev)}
        isMobileOpen={isMobileSidebarOpen}
        onCloseMobile={() => setIsMobileSidebarOpen(false)}
      />

      {/* Main Chat Interface */}
      <div className="flex-1 flex flex-col h-full min-w-0 bg-white dark:bg-slate-900 transition-colors">
        {/* Top Navbar */}
        <header className="h-14 border-b border-[#E5E7EB] dark:border-slate-800 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md flex items-center justify-between px-4 shrink-0 z-10">
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
          <div className="flex items-center gap-2">
            {/* Quick Dark Mode toggle */}
            <button
              type="button"
              onClick={() => setIsDarkMode(!isDarkMode)}
              className="rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 p-2 text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700 transition"
              title={isDarkMode ? 'Chuyển sang giao diện Sáng' : 'Chuyển sang giao diện Tối'}
            >
              {isDarkMode ? <Sun className="h-4 w-4 text-amber-400" /> : <Moon className="h-4 w-4 text-slate-600" />}
            </button>

            {/* Model Selector Dropdown */}
            <div className="relative">
              <button
                type="button"
                onClick={() => setIsModelDropdownOpen(!isModelDropdownOpen)}
                className="flex items-center gap-1.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 px-2.5 py-1.5 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:bg-white dark:hover:bg-slate-700 transition"
                title="Chọn mô hình AI thử nghiệm"
              >
                <Cpu className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400" />
                <span className="hidden sm:inline">{selectedModel.name}</span>
                <span className="rounded bg-blue-100 dark:bg-blue-900/60 px-1 py-0.2 text-[9px] font-bold text-blue-700 dark:text-blue-300">
                  {selectedModel.badge}
                </span>
                <ChevronDown className="h-3 w-3 text-slate-400" />
              </button>

              {isModelDropdownOpen && (
                <div 
                  className="absolute right-0 mt-1.5 w-56 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 p-1.5 shadow-lg z-20 animate-in fade-in zoom-in-95 duration-150"
                  onClick={() => setIsModelDropdownOpen(false)}
                >
                  <div className="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-400">
                    Mô hình AI dự kiến
                  </div>
                  {AI_MODELS.map((model) => (
                    <button
                      key={model.id}
                      type="button"
                      onClick={() => setSelectedModel(model)}
                      className={`flex w-full items-center justify-between rounded-lg px-2.5 py-2 text-xs font-medium transition ${
                        selectedModel.id === model.id
                          ? 'bg-blue-50 dark:bg-blue-950 text-blue-700 dark:text-blue-300 font-bold'
                          : 'text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700'
                      }`}
                    >
                      <span>{model.name}</span>
                      <span className="rounded bg-slate-100 dark:bg-slate-700 px-1.5 py-0.5 text-[9px] font-medium text-slate-600 dark:text-slate-300">
                        {model.badge}
                      </span>
                    </button>
                  ))}
                </div>
              )}
            </div>

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
        />

        {/* Bottom Composer Box */}
        <ChatInput
          onSendMessage={handleSendMessage}
          onViewImage={(url, name) => setLightboxData({ url, name })}
          onViewDocument={(att) => setViewingDocAttachment(att)}
          isGenerating={isGenerating}
          onStopGenerating={handleStopGenerating}
          disabled={isSearchOpen && !!searchQuery}
        />
      </div>
    </div>
  );
}
