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
  Cpu, 
  Moon, 
  Sun, 
  Search, 
  Sliders,
  Database
} from 'lucide-react';
import { ChatConversation, ChatMessage, ChatAttachment, ModelSettings } from '@/types/chat';
import { ChatSidebar } from '@/components/chat/ChatSidebar';
import { ChatMessageList } from '@/components/chat/ChatMessageList';
import { ChatInput } from '@/components/chat/ChatInput';
import { ImageLightbox } from '@/components/chat/ImageLightbox';
import { DocumentViewerModal } from '@/components/chat/DocumentViewerModal';
import { ShortcutsModal } from '@/components/chat/ShortcutsModal';
import { SettingsModal } from '@/components/chat/SettingsModal';
import { playSendSound, playCompleteSound } from '@/lib/soundEffects';
import { ToastProvider, useToast } from '@/components/chat/ToastNotification';
import { getSocraticAssistantResponse } from '@/lib/socraticEngine';

const LOCAL_STORAGE_KEY = 'ai_coding_tutor_chat_sessions_v2';
const LOCAL_STORAGE_ACTIVE_KEY = 'ai_coding_tutor_active_chat_id_v2';
const LOCAL_STORAGE_SETTINGS_KEY = 'ai_coding_tutor_settings_v1';
const LOCAL_STORAGE_THEME_KEY = 'ai_coding_tutor_theme_v1';

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
    aiProvider: 'backend_rag',
  });

  const [isDarkMode, setIsDarkMode] = useState<boolean>(false);
  const [isDesktopSidebarOpen, setIsDesktopSidebarOpen] = useState<boolean>(true);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  
  // Essential Modals state
  const [lightboxData, setLightboxData] = useState<{ url: string; name: string } | null>(null);
  const [viewingDocAttachment, setViewingDocAttachment] = useState<ChatAttachment | null>(null);
  const [isShortcutsOpen, setIsShortcutsOpen] = useState<boolean>(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  
  // Header inline renaming state
  const [isEditingHeaderTitle, setIsEditingHeaderTitle] = useState<boolean>(false);
  const [headerTitleInput, setHeaderTitleInput] = useState<string>('');

  // In-chat message search
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [injectedText, setInjectedText] = useState<string>('');
  const searchInputRef = useRef<HTMLInputElement>(null);

  const generationTimerRef = useRef<NodeJS.Timeout | null>(null);
  const streamIntervalRef = useRef<NodeJS.Timeout | null>(null);

  // Active conversation getter
  const activeConversation = useMemo(() => {
    return (
      conversations.find((c) => c.id === activeConversationId) || conversations[0]
    );
  }, [conversations, activeConversationId]);

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
    } catch (err) {
      console.warn('Could not read from localStorage:', err);
    }
  }, []);

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

    // Fetch response from Socratic Engine
    getSocraticAssistantResponse(text, attachments, modelSettings, 'gemini-3-flash-preview')
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
  }, [activeConversationId, modelSettings, showToast]);

  // Edit user message and regenerate from that point
  const handleEditUserMessage = useCallback((messageId: string, newContent: string) => {
    const msgIdx = activeConversation.messages.findIndex((m) => m.id === messageId);
    if (msgIdx === -1) return;

    const targetMsg = activeConversation.messages[msgIdx];
    const attachments = targetMsg.attachments || [];

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

    getSocraticAssistantResponse(lastUserMsg.content, lastUserMsg.attachments || [], modelSettings, 'gemini-3-flash-preview')
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
  }, [activeConversation, activeConversationId, modelSettings, showToast]);

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
    <div className={`flex h-screen w-full overflow-hidden transition-colors duration-200 ${isDarkMode ? 'dark bg-slate-950 text-slate-100' : 'bg-slate-50 text-slate-900'}`}>
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
        onImportConversation={handleImportConversation}
        isOpen={isDesktopSidebarOpen}
        onToggle={() => setIsDesktopSidebarOpen((prev) => !prev)}
        isMobileOpen={isMobileSidebarOpen}
        onCloseMobile={() => setIsMobileSidebarOpen(false)}
      />

      {/* Main Chat Interface */}
      <div className="flex-1 flex flex-col h-full min-w-0 bg-white dark:bg-slate-900 transition-colors duration-200">
        {/* Top Navbar */}
        <header className="h-14 border-b border-slate-200/80 dark:border-slate-800 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md flex items-center justify-between px-4 shrink-0 z-10">
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
                    title="Đổi tên cuộc trò chuyện"
                  >
                    <Edit3 className="h-3.5 w-3.5" />
                  </button>
                </div>
              )}
            </div>

            {/* System Status Badges */}
            <div className="hidden sm:flex items-center gap-1.5 ml-2">
              <span className="inline-flex items-center gap-1 rounded-full border border-blue-200 dark:border-blue-800/60 bg-blue-50 dark:bg-blue-950/40 px-2 py-0.5 text-[10px] font-semibold text-blue-700 dark:text-blue-300">
                <Cpu className="h-3 w-3" />
                Gemini 3 Flash
              </span>
              <span className="inline-flex items-center gap-1 rounded-full border border-emerald-200 dark:border-emerald-800/60 bg-emerald-50 dark:bg-emerald-950/40 px-2 py-0.5 text-[10px] font-semibold text-emerald-700 dark:text-emerald-300">
                <Database className="h-3 w-3" />
                RAG 5,230 Chunks
              </span>
            </div>
          </div>

          {/* Right Header Controls */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            {/* In-chat search toggle */}
            <button
              type="button"
              onClick={() => { setIsSearchOpen((v) => !v); setTimeout(() => searchInputRef.current?.focus(), 50); }}
              className={`rounded-xl border p-2 transition ${
                isSearchOpen
                  ? 'border-blue-400 bg-blue-50 dark:bg-blue-950 text-blue-600'
                  : 'border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
              }`}
              title="Tìm kiếm trong cuộc trò chuyện (Ctrl + F)"
            >
              <Search className="h-4 w-4" />
            </button>

            {/* Dark Mode toggle */}
            <button
              type="button"
              onClick={() => setIsDarkMode(!isDarkMode)}
              className="rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 p-2 text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700 transition"
              title={isDarkMode ? 'Chuyển sang giao diện Sáng' : 'Chuyển sang giao diện Tối'}
            >
              {isDarkMode 
                ? <Sun className="h-4 w-4 text-amber-400" /> 
                : <Moon className="h-4 w-4 text-slate-600" />
              }
            </button>

            {/* Settings Button */}
            <button
              type="button"
              onClick={() => setIsSettingsOpen(true)}
              className="rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800 p-2 text-slate-600 dark:text-slate-300 hover:text-blue-600 hover:bg-white dark:hover:bg-slate-700 transition"
              title="Cài đặt AI Socratic"
            >
              <Sliders className="h-4 w-4" />
            </button>

            {/* New Chat quick button */}
            <button
              type="button"
              onClick={handleNewConversation}
              className="flex items-center gap-1.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white px-3 py-1.5 text-xs font-bold shadow-xs transition active:scale-95"
              title="Tạo cuộc trò chuyện mới (Ctrl + Shift + O)"
            >
              <Plus className="h-3.5 w-3.5" />
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
          externalInputText={injectedText}
        />
      </div>
    </div>
  );
}
