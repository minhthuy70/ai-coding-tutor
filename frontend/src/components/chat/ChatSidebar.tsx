'use client';

import React, { useState } from 'react';
import { 
  Plus, 
  MessageSquare, 
  Trash2, 
  X, 
  Terminal,
  Sparkles,
  Search,
  Download,
  RotateCcw
} from 'lucide-react';
import { ChatConversation } from '@/types/chat';

interface ChatSidebarProps {
  conversations: ChatConversation[];
  activeConversationId: string;
  onSelectConversation: (id: string) => void;
  onNewConversation: () => void;
  onDeleteConversation: (id: string) => void;
  onClearAll?: () => void;
  isOpen: boolean;
  onToggle: () => void;
  isMobileOpen: boolean;
  onCloseMobile: () => void;
}

export const ChatSidebar: React.FC<ChatSidebarProps> = ({
  conversations,
  activeConversationId,
  onSelectConversation,
  onNewConversation,
  onDeleteConversation,
  onClearAll,
  isOpen,
  onToggle,
  isMobileOpen,
  onCloseMobile,
}) => {
  const [searchQuery, setSearchQuery] = useState('');

  const filteredConversations = conversations.filter((c) =>
    c.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleExportChat = (conv: ChatConversation) => {
    const textContent = conv.messages
      .map((m) => {
        const time = new Date(m.timestamp).toLocaleString();
        const role = m.role === 'user' ? 'BẠN' : 'TRỢ LÝ AI';
        const files = m.attachments?.length ? `\n[Tệp đính kèm: ${m.attachments.map(a => a.name).join(', ')}]` : '';
        return `[${time}] ${role}:\n${m.content}${files}\n----------------------------------------`;
      })
      .join('\n\n');

    const blob = new Blob([textContent || 'Chưa có nội dung'], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${conv.title.replace(/[^a-z0-9]/gi, '_').toLowerCase()}_export.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const sidebarContent = (
    <div className="flex flex-col h-full bg-[#F7F7F8] border-r border-[#E5E7EB] text-[#202123]">
      {/* Top Header: Branding + Close button (Mobile) */}
      <div className="p-3.5 border-b border-[#E5E7EB] flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white shadow-xs">
            <Terminal className="h-4.5 w-4.5" />
          </div>
          <div className="flex flex-col">
            <span className="font-extrabold text-sm tracking-tight text-slate-900 leading-tight">
              AI Coding Tutor
            </span>
            <span className="text-[10px] text-blue-600 font-bold uppercase tracking-wider">
              Multimodal Studio
            </span>
          </div>
        </div>

        {/* Mobile close button */}
        <button
          type="button"
          onClick={onCloseMobile}
          className="md:hidden rounded-lg p-1.5 text-slate-500 hover:bg-slate-200 focus:outline-none transition"
          aria-label="Đóng thanh bên"
        >
          <X className="h-5 w-5" />
        </button>
      </div>

      {/* New Chat Button */}
      <div className="p-3">
        <button
          type="button"
          onClick={() => {
            onNewConversation();
            onCloseMobile();
          }}
          className="flex w-full items-center justify-center gap-2 rounded-xl border border-slate-300 bg-white px-3 py-2.5 text-sm font-bold text-slate-700 shadow-2xs hover:bg-slate-50 hover:border-blue-400 hover:text-blue-600 active:scale-[0.99] focus:outline-none focus:ring-2 focus:ring-blue-500/20 transition-all"
        >
          <Plus className="h-4 w-4 text-blue-600" />
          <span>Cuộc trò chuyện mới</span>
        </button>
      </div>

      {/* Search Bar */}
      {conversations.length > 2 && (
        <div className="px-3 pb-2">
          <div className="relative flex items-center">
            <Search className="absolute left-2.5 h-3.5 w-3.5 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm cuộc trò chuyện..."
              className="w-full rounded-lg border border-slate-200 bg-white pl-8 pr-2.5 py-1.5 text-xs text-slate-700 placeholder-slate-400 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500/20 transition"
            />
          </div>
        </div>
      )}

      {/* Recent Chats List */}
      <div className="flex-1 overflow-y-auto px-2 py-1 space-y-1">
        <div className="flex items-center justify-between px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider text-slate-400">
          <span>Gần đây ({filteredConversations.length})</span>
          {conversations.length > 1 && onClearAll && (
            <button
              type="button"
              onClick={onClearAll}
              className="text-[10px] text-slate-400 hover:text-rose-600 transition"
              title="Xóa tất cả các cuộc trò chuyện"
            >
              Xóa tất cả
            </button>
          )}
        </div>

        {filteredConversations.length === 0 ? (
          <div className="px-3 py-6 text-center text-xs text-slate-400">
            {searchQuery ? 'Không tìm thấy cuộc trò chuyện phù hợp' : 'Chưa có cuộc trò chuyện nào'}
          </div>
        ) : (
          filteredConversations.map((conv) => {
            const isActive = conv.id === activeConversationId;
            return (
              <div
                key={conv.id}
                className={`group relative flex items-center justify-between rounded-xl px-3 py-2.5 text-xs font-medium transition cursor-pointer ${
                  isActive
                    ? 'bg-white text-blue-700 shadow-2xs border border-slate-200 font-semibold'
                    : 'text-slate-600 hover:bg-slate-200/50 hover:text-slate-900'
                }`}
                onClick={() => {
                  onSelectConversation(conv.id);
                  onCloseMobile();
                }}
              >
                <div className="flex items-center gap-2.5 min-w-0 pr-12">
                  <MessageSquare className={`h-4 w-4 shrink-0 ${isActive ? 'text-blue-600' : 'text-slate-400'}`} />
                  <span className="truncate" title={conv.title}>
                    {conv.title}
                  </span>
                </div>

                {/* Quick actions (visible on hover or active) */}
                <div className="opacity-0 group-hover:opacity-100 flex items-center gap-1 transition absolute right-2">
                  {conv.messages.length > 0 && (
                    <button
                      type="button"
                      onClick={(e) => {
                        e.stopPropagation();
                        handleExportChat(conv);
                      }}
                      className="rounded p-1 text-slate-400 hover:bg-slate-100 hover:text-blue-600 focus:opacity-100 transition"
                      title="Xuất nội dung chat (.txt)"
                    >
                      <Download className="h-3.5 w-3.5" />
                    </button>
                  )}
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      onDeleteConversation(conv.id);
                    }}
                    className="rounded p-1 text-slate-400 hover:bg-slate-100 hover:text-rose-600 focus:opacity-100 transition"
                    title="Xóa cuộc trò chuyện này"
                    aria-label={`Xóa ${conv.title}`}
                  >
                    <Trash2 className="h-3.5 w-3.5" />
                  </button>
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* Bottom Footer Section */}
      <div className="p-3 border-t border-[#E5E7EB] bg-slate-100/60 space-y-2">
        <div className="flex items-center gap-2 rounded-xl bg-white p-2.5 border border-slate-200 text-xs text-slate-600 shadow-2xs">
          <Sparkles className="h-4 w-4 text-blue-600 shrink-0" />
          <div className="flex flex-col min-w-0">
            <span className="font-bold text-slate-800 text-[11px]">Đa phương thức</span>
            <span className="text-[10px] text-slate-400 truncate">Text + Ảnh (Ctrl+V) + File</span>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <>
      {/* Mobile Drawer Overlay */}
      {isMobileOpen && (
        <div
          className="fixed inset-0 z-40 bg-slate-900/50 backdrop-blur-xs md:hidden animate-in fade-in duration-200"
          onClick={onCloseMobile}
          aria-hidden="true"
        />
      )}

      {/* Mobile Drawer */}
      <div
        className={`fixed inset-y-0 left-0 z-50 w-72 transform transition-transform duration-300 ease-in-out md:hidden ${
          isMobileOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        {sidebarContent}
      </div>

      {/* Desktop Sidebar */}
      <aside
        className={`hidden md:flex flex-col shrink-0 border-r border-[#E5E7EB] transition-all duration-300 ease-in-out ${
          isOpen ? 'w-64' : 'w-0 overflow-hidden border-r-0'
        }`}
      >
        <div className="w-64 h-full">
          {sidebarContent}
        </div>
      </aside>
    </>
  );
};
