'use client';

import React from 'react';
import Link from 'next/link';
import { 
  Plus, 
  MessageSquare, 
  Trash2, 
  LayoutDashboard, 
  X, 
  ChevronLeft, 
  ChevronRight,
  Terminal,
  Clock
} from 'lucide-react';
import { ChatConversation } from '@/types/chat';

interface ChatSidebarProps {
  conversations: ChatConversation[];
  activeConversationId: string;
  onSelectConversation: (id: string) => void;
  onNewConversation: () => void;
  onDeleteConversation: (id: string) => void;
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
  isOpen,
  onToggle,
  isMobileOpen,
  onCloseMobile,
}) => {
  const sidebarContent = (
    <div className="flex flex-col h-full bg-[#F7F7F8] border-r border-[#E5E7EB] text-[#202123]">
      {/* Top Header: Branding + Close button (Mobile) or Collapse (Desktop) */}
      <div className="p-3 border-b border-[#E5E7EB] flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-white shadow-xs">
            <Terminal className="h-4 w-4" />
          </div>
          <div className="flex flex-col">
            <span className="font-bold text-sm tracking-tight text-slate-900 leading-tight">
              AI Coding Tutor
            </span>
            <span className="text-[10px] text-blue-600 font-medium">
              Multimodal Chat Studio
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
          className="flex w-full items-center justify-center gap-2 rounded-xl border border-slate-300 bg-white px-3 py-2.5 text-sm font-semibold text-slate-700 shadow-2xs hover:bg-slate-50 hover:border-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 transition"
        >
          <Plus className="h-4 w-4 text-blue-600" />
          <span>Cuộc trò chuyện mới</span>
        </button>
      </div>

      {/* Recent Chats List */}
      <div className="flex-1 overflow-y-auto px-2 py-1 space-y-1">
        <div className="px-3 py-1.5 text-[11px] font-semibold uppercase tracking-wider text-slate-400">
          Gần đây ({conversations.length})
        </div>

        {conversations.length === 0 ? (
          <div className="px-3 py-4 text-center text-xs text-slate-400">
            Chưa có cuộc trò chuyện nào
          </div>
        ) : (
          conversations.map((conv) => {
            const isActive = conv.id === activeConversationId;
            return (
              <div
                key={conv.id}
                className={`group relative flex items-center justify-between rounded-lg px-3 py-2 text-xs font-medium transition cursor-pointer ${
                  isActive
                    ? 'bg-white text-blue-700 shadow-2xs border border-slate-200/80 font-semibold'
                    : 'text-slate-600 hover:bg-slate-200/50 hover:text-slate-900'
                }`}
                onClick={() => {
                  onSelectConversation(conv.id);
                  onCloseMobile();
                }}
              >
                <div className="flex items-center gap-2.5 min-w-0 pr-6">
                  <MessageSquare className={`h-3.5 w-3.5 shrink-0 ${isActive ? 'text-blue-600' : 'text-slate-400'}`} />
                  <span className="truncate" title={conv.title}>
                    {conv.title}
                  </span>
                </div>

                {/* Delete button (visible on hover or active) */}
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    onDeleteConversation(conv.id);
                  }}
                  className="opacity-0 group-hover:opacity-100 rounded p-1 text-slate-400 hover:bg-slate-100 hover:text-rose-600 focus:opacity-100 transition absolute right-2"
                  title="Xóa cuộc trò chuyện này"
                  aria-label={`Xóa ${conv.title}`}
                >
                  <Trash2 className="h-3.5 w-3.5" />
                </button>
              </div>
            );
          })
        )}
      </div>

      {/* Bottom Footer Section */}
      <div className="p-3 border-t border-[#E5E7EB] bg-slate-100/50 space-y-2">
        <Link
          href="/"
          className="flex w-full items-center gap-2 rounded-lg px-2.5 py-2 text-xs font-medium text-slate-600 hover:bg-white hover:text-slate-900 transition"
        >
          <LayoutDashboard className="h-4 w-4 text-slate-500" />
          <span>Về Dashboard chính (Ngày 1)</span>
        </Link>
        <div className="px-2.5 text-[11px] text-slate-400">
          Chế độ: UI Demo (Client State)
        </div>
      </div>
    </div>
  );

  return (
    <>
      {/* Mobile Drawer Overlay */}
      {isMobileOpen && (
        <div
          className="fixed inset-0 z-40 bg-slate-900/40 backdrop-blur-xs md:hidden"
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
