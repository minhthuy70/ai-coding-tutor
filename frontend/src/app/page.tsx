'use client';

import React, { useState, useCallback, useMemo, useEffect } from 'react';
import { 
  Menu, 
  PanelLeftClose, 
  PanelLeftOpen, 
  Plus, 
  Sparkles, 
  Terminal,
  Edit3,
  Check,
  X,
  ChevronDown,
  Cpu
} from 'lucide-react';
import { ChatConversation, ChatMessage, ChatAttachment } from '@/types/chat';
import { ChatSidebar } from '@/components/chat/ChatSidebar';
import { ChatMessageList } from '@/components/chat/ChatMessageList';
import { ChatInput } from '@/components/chat/ChatInput';
import { ImageLightbox } from '@/components/chat/ImageLightbox';

const LOCAL_STORAGE_KEY = 'ai_coding_tutor_chat_sessions_v1';
const LOCAL_STORAGE_ACTIVE_KEY = 'ai_coding_tutor_active_chat_id';

const AI_MODELS = [
  { id: 'gemini-1.5-flash', name: 'Gemini 1.5 Flash', badge: 'Cloud Free' },
  { id: 'gpt-4o-mini', name: 'GPT-4o-mini', badge: 'Fallback' },
  { id: 'ollama-llama3', name: 'Ollama Llama 3', badge: 'Local Offline' },
];

export default function HomePage() {
  const [conversations, setConversations] = useState<ChatConversation[]>(() => {
    // Attempt to load from localStorage on client side
    if (typeof window !== 'undefined') {
      try {
        const saved = localStorage.getItem(LOCAL_STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved);
          if (Array.isArray(parsed) && parsed.length > 0) {
            return parsed;
          }
        }
      } catch {
        // Fallback to default
      }
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
        const savedActive = localStorage.getItem(LOCAL_STORAGE_ACTIVE_KEY);
        if (savedActive) return savedActive;
      } catch {
        // Fallback
      }
    }
    return 'conv-initial';
  });

  const [isDesktopSidebarOpen, setIsDesktopSidebarOpen] = useState<boolean>(true);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  const [lightboxData, setLightboxData] = useState<{ url: string; name: string } | null>(null);
  
  // Header inline renaming state
  const [isEditingHeaderTitle, setIsEditingHeaderTitle] = useState<boolean>(false);
  const [headerTitleInput, setHeaderTitleInput] = useState<string>('');

  // Selected AI Model state
  const [selectedModel, setSelectedModel] = useState(AI_MODELS[0]);
  const [isModelDropdownOpen, setIsModelDropdownOpen] = useState(false);

  // Active conversation getter
  const activeConversation = useMemo(() => {
    return (
      conversations.find((c) => c.id === activeConversationId) || conversations[0]
    );
  }, [conversations, activeConversationId]);

  // Persist conversations to localStorage whenever changed
  useEffect(() => {
    try {
      localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(conversations));
      localStorage.setItem(LOCAL_STORAGE_ACTIVE_KEY, activeConversationId);
    } catch {
      // Storage quota or private mode
    }
  }, [conversations, activeConversationId]);

  // Rename a conversation
  const handleRenameConversation = useCallback((id: string, newTitle: string) => {
    setConversations((prev) =>
      prev.map((c) => (c.id === id ? { ...c, title: newTitle, updatedAt: new Date().toISOString() } : c))
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

  // Clear all conversations
  const handleClearAll = useCallback(() => {
    if (window.confirm('Bạn có chắc chắn muốn xóa toàn bộ lịch sử các cuộc trò chuyện?')) {
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
    }
  }, []);

  // View image in Lightbox
  const handleViewImage = useCallback((url: string, name: string) => {
    setLightboxData({ url, name });
  }, []);

  // Handle message sending
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
          // Auto update title if first message
          let newTitle = conv.title;
          if (conv.messages.length === 0 && conv.title === 'Cuộc trò chuyện mới') {
            if (text.trim()) {
              newTitle = text.trim().slice(0, 32) + (text.trim().length > 32 ? '...' : '');
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

    // Turn on generating state
    setIsGenerating(true);

    // Simulate AI response
    setTimeout(() => {
      const fileCountText = attachments.length > 0 
        ? ` cùng **${attachments.length} tệp đính kèm** (${attachments.map(a => a.name).join(', ')})`
        : '';

      const sampleCodeDemo = text.toLowerCase().includes('sort') || text.toLowerCase().includes('thuật toán')
        ? `\n\nVí dụ mã nguồn minh họa về độ phức tạp:\n\`\`\`python\ndef quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n\`\`\``
        : '';

      const assistantMsg: ChatMessage = {
        id: `msg-ai-${Date.now()}`,
        role: 'assistant',
        content: `[Mô hình: ${selectedModel.name}]\nHệ thống đã tiếp nhận dữ liệu văn bản${fileCountText}.${sampleCodeDemo}\n\nHiện tại, tính năng LLM và RAG (ChromaDB) đang trong giai đoạn sẵn sàng kết nối. Yêu cầu và tệp tin của bạn đã được ghi nhận trong danh sách hội thoại giao diện thử nghiệm.`,
        timestamp: new Date().toISOString(),
        isDemoNotice: true,
      };

      setConversations((prev) =>
        prev.map((conv) => {
          if (conv.id === activeConversationId) {
            return {
              ...conv,
              updatedAt: new Date().toISOString(),
              messages: [...conv.messages, assistantMsg],
            };
          }
          return conv;
        })
      );
      setIsGenerating(false);
    }, 600);
  }, [activeConversationId, selectedModel]);

  // Handle Regenerate Response
  const handleRegenerateResponse = useCallback(() => {
    if (!activeConversation || activeConversation.messages.length === 0) return;

    // Find the last user message
    const lastUserMsg = [...activeConversation.messages].reverse().find((m) => m.role === 'user');
    if (!lastUserMsg) return;

    setIsGenerating(true);

    setTimeout(() => {
      const regeneratedMsg: ChatMessage = {
        id: `msg-ai-regen-${Date.now()}`,
        role: 'assistant',
        content: `[Mô hình: ${selectedModel.name} - Tạo lại]\nĐã tạo lại câu trả lời phản hồi cho yêu cầu: "${lastUserMsg.content.slice(0, 50)}...".\n\nGiao diện đã sẵn sàng kết nối pipeline LLM & RAG khi backend kích hoạt.`,
        timestamp: new Date().toISOString(),
        isDemoNotice: true,
      };

      setConversations((prev) =>
        prev.map((conv) => {
          if (conv.id === activeConversationId) {
            return {
              ...conv,
              updatedAt: new Date().toISOString(),
              messages: [...conv.messages, regeneratedMsg],
            };
          }
          return conv;
        })
      );
      setIsGenerating(false);
    }, 600);
  }, [activeConversation, activeConversationId, selectedModel]);

  const handleSelectSuggestion = useCallback((query: string) => {
    handleSendMessage(query, []);
  }, [handleSendMessage]);

  return (
    <div className="flex h-screen w-full overflow-hidden bg-white text-[#202123]">
      {/* Lightbox Modal */}
      <ImageLightbox
        imageUrl={lightboxData?.url || null}
        imageName={lightboxData?.name || null}
        onClose={() => setLightboxData(null)}
      />

      {/* Left Sidebar */}
      <ChatSidebar
        conversations={conversations}
        activeConversationId={activeConversation?.id || ''}
        onSelectConversation={setActiveConversationId}
        onNewConversation={handleNewConversation}
        onDeleteConversation={handleDeleteConversation}
        onRenameConversation={handleRenameConversation}
        onClearAll={handleClearAll}
        isOpen={isDesktopSidebarOpen}
        onToggle={() => setIsDesktopSidebarOpen((prev) => !prev)}
        isMobileOpen={isMobileSidebarOpen}
        onCloseMobile={() => setIsMobileSidebarOpen(false)}
      />

      {/* Main Chat Interface */}
      <div className="flex-1 flex flex-col h-full min-w-0 bg-white">
        {/* Top Navbar */}
        <header className="h-14 border-b border-[#E5E7EB] bg-white/95 backdrop-blur-md flex items-center justify-between px-4 shrink-0 z-10">
          <div className="flex items-center gap-2 min-w-0">
            {/* Mobile menu trigger */}
            <button
              type="button"
              onClick={() => setIsMobileSidebarOpen(true)}
              className="md:hidden rounded-lg p-2 text-slate-500 hover:bg-slate-100 focus:outline-none transition"
              aria-label="Mở danh sách cuộc trò chuyện"
            >
              <Menu className="h-5 w-5" />
            </button>

            {/* Desktop collapse toggle */}
            <button
              type="button"
              onClick={() => setIsDesktopSidebarOpen((prev) => !prev)}
              className="hidden md:flex rounded-lg p-2 text-slate-500 hover:bg-slate-100 focus:outline-none transition"
              title={isDesktopSidebarOpen ? 'Thu gọn thanh bên' : 'Mở rộng thanh bên'}
              aria-label="Thu gọn hoặc mở rộng thanh bên"
            >
              {isDesktopSidebarOpen ? (
                <PanelLeftClose className="h-5 w-5" />
              ) : (
                <PanelLeftOpen className="h-5 w-5" />
              )}
            </button>

            {/* Active Conversation Title with Quick Rename */}
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
                    className="rounded-md border border-blue-400 bg-white px-2 py-0.5 text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
                  />
                  <button
                    type="button"
                    onClick={handleSaveHeaderRename}
                    className="rounded p-1 text-emerald-600 hover:bg-emerald-50 transition"
                    title="Lưu (Enter)"
                  >
                    <Check className="h-4 w-4" />
                  </button>
                  <button
                    type="button"
                    onClick={() => setIsEditingHeaderTitle(false)}
                    className="rounded p-1 text-slate-400 hover:bg-slate-100 transition"
                    title="Hủy (Esc)"
                  >
                    <X className="h-4 w-4" />
                  </button>
                </div>
              ) : (
                <div className="group/title flex items-center gap-1.5 truncate">
                  <span className="font-extrabold text-sm text-slate-900 truncate">
                    {activeConversation?.title || 'Cuộc trò chuyện'}
                  </span>
                  <button
                    type="button"
                    onClick={handleStartHeaderRename}
                    className="opacity-0 group-hover/title:opacity-100 rounded p-1 text-slate-400 hover:text-blue-600 hover:bg-slate-100 transition"
                    title="Đổi tên cuộc trò chuyện này"
                  >
                    <Edit3 className="h-3.5 w-3.5" />
                  </button>
                </div>
              )}
            </div>
          </div>

          {/* Right Header: Model Selector & New Chat */}
          <div className="flex items-center gap-2">
            {/* Model Selector Dropdown */}
            <div className="relative">
              <button
                type="button"
                onClick={() => setIsModelDropdownOpen(!isModelDropdownOpen)}
                className="flex items-center gap-1.5 rounded-xl border border-slate-200 bg-slate-50/80 px-2.5 py-1.5 text-xs font-semibold text-slate-700 hover:bg-white hover:border-slate-300 transition"
                title="Chọn mô hình AI thử nghiệm"
              >
                <Cpu className="h-3.5 w-3.5 text-blue-600" />
                <span className="hidden sm:inline">{selectedModel.name}</span>
                <span className="rounded bg-blue-100 px-1 py-0.2 text-[9px] font-bold text-blue-700">
                  {selectedModel.badge}
                </span>
                <ChevronDown className="h-3 w-3 text-slate-400" />
              </button>

              {isModelDropdownOpen && (
                <div 
                  className="absolute right-0 mt-1.5 w-56 rounded-xl border border-slate-200 bg-white p-1.5 shadow-lg z-20 animate-in fade-in zoom-in-95 duration-150"
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
                          ? 'bg-blue-50 text-blue-700 font-bold'
                          : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                      }`}
                    >
                      <span>{model.name}</span>
                      <span className="rounded bg-slate-100 px-1.5 py-0.5 text-[9px] font-medium text-slate-600">
                        {model.badge}
                      </span>
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* New Chat quick button */}
            <button
              type="button"
              onClick={handleNewConversation}
              className="flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-1.5 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:border-slate-300 shadow-2xs transition active:scale-95"
              title="Tạo cuộc trò chuyện mới"
            >
              <Plus className="h-3.5 w-3.5 text-blue-600" />
              <span className="hidden sm:inline">Đoạn chat mới</span>
            </button>
          </div>
        </header>

        {/* Message Thread Area */}
        <ChatMessageList
          messages={activeConversation?.messages || []}
          isGenerating={isGenerating}
          onSelectSuggestion={handleSelectSuggestion}
          onViewImage={handleViewImage}
          onRegenerate={handleRegenerateResponse}
        />

        {/* Bottom Composer Box */}
        <ChatInput
          onSendMessage={handleSendMessage}
          onViewImage={handleViewImage}
        />
      </div>
    </div>
  );
}
