'use client';

import React, { useState, useCallback, useMemo } from 'react';
import { 
  Menu, 
  PanelLeftClose, 
  PanelLeftOpen, 
  Plus, 
  Sparkles, 
  Terminal,
  Share2,
  Trash2
} from 'lucide-react';
import { ChatConversation, ChatMessage, ChatAttachment } from '@/types/chat';
import { ChatSidebar } from '@/components/chat/ChatSidebar';
import { ChatMessageList } from '@/components/chat/ChatMessageList';
import { ChatInput } from '@/components/chat/ChatInput';
import { ImageLightbox } from '@/components/chat/ImageLightbox';

export default function HomePage() {
  const [conversations, setConversations] = useState<ChatConversation[]>(() => [
    {
      id: 'conv-initial',
      title: 'Cuộc trò chuyện mới',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      messages: [],
    },
  ]);

  const [activeConversationId, setActiveConversationId] = useState<string>('conv-initial');
  const [isDesktopSidebarOpen, setIsDesktopSidebarOpen] = useState<boolean>(true);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  const [lightboxData, setLightboxData] = useState<{ url: string; name: string } | null>(null);

  // Active conversation getter
  const activeConversation = useMemo(() => {
    return (
      conversations.find((c) => c.id === activeConversationId) || conversations[0]
    );
  }, [conversations, activeConversationId]);

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

  // Handle message sending (User -> Assistant demo reply with typing indicator)
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
          // Update title if it's the first message and currently has default title
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

    // Generate Demo Assistant Response after a simulated thinking delay
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
        content: `Hệ thống đã tiếp nhận dữ liệu văn bản${fileCountText}.${sampleCodeDemo}\n\nHiện tại, tính năng LLM (Gemini / OpenAI / Ollama) và RAG (ChromaDB) đang trong giai đoạn sẵn sàng kết nối. Yêu cầu và tệp tin của bạn đã được ghi nhận trong danh sách hội thoại giao diện thử nghiệm.`,
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
  }, [activeConversationId]);

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

            {/* Active Conversation Title */}
            <div className="flex items-center gap-2 truncate pl-1">
              <span className="font-bold text-sm text-slate-900 truncate">
                {activeConversation?.title || 'Cuộc trò chuyện'}
              </span>
              <span className="hidden sm:inline-flex items-center rounded-full bg-blue-50 px-2 py-0.5 text-[11px] font-semibold text-blue-700 border border-blue-200">
                Studio UI
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* New Chat quick button */}
            <button
              type="button"
              onClick={handleNewConversation}
              className="flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold text-slate-700 hover:bg-slate-50 hover:border-slate-300 shadow-2xs transition"
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
