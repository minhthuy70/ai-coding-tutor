'use client';

import React, { useState, useRef, useEffect } from 'react';
import { 
  Plus, 
  MessageSquare, 
  Trash2, 
  X, 
  Terminal, 
  Sparkles, 
  Search, 
  Download, 
  Edit3, 
  Check,
  Pin,
  Sliders,
  Keyboard,
  Upload,
  Printer,
  FileCode,
  FileText,
  BookOpen
} from 'lucide-react';
import { ChatConversation } from '@/types/chat';

interface ChatSidebarProps {
  conversations: ChatConversation[];
  activeConversationId: string;
  onSelectConversation: (id: string) => void;
  onNewConversation: () => void;
  onDeleteConversation: (id: string) => void;
  onRenameConversation: (id: string, newTitle: string) => void;
  onTogglePinConversation: (id: string) => void;
  onClearAll?: () => void;
  onOpenShortcuts: () => void;
  onOpenSettings: () => void;
  onOpenInstructorKnowledge?: () => void;
  onImportConversation?: (imported: ChatConversation) => void;
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
  onRenameConversation,
  onTogglePinConversation,
  onClearAll,
  onOpenShortcuts,
  onOpenSettings,
  onOpenInstructorKnowledge,
  onImportConversation,
  isOpen,
  onToggle,
  isMobileOpen,
  onCloseMobile,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editTitleInput, setEditTitleInput] = useState('');
  const [exportingConv, setExportingConv] = useState<ChatConversation | null>(null);
  const editInputRef = useRef<HTMLInputElement>(null);
  const importInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (editingId && editInputRef.current) {
      editInputRef.current.focus();
      editInputRef.current.select();
    }
  }, [editingId]);

  const handleStartRename = (conv: ChatConversation) => {
    setEditingId(conv.id);
    setEditTitleInput(conv.title);
  };

  const handleSaveRename = (id: string) => {
    const trimmed = editTitleInput.trim();
    if (trimmed) {
      onRenameConversation(id, trimmed);
    }
    setEditingId(null);
  };

  const handleCancelRename = () => {
    setEditingId(null);
  };

  const handleKeyDownRename = (e: React.KeyboardEvent, id: string) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSaveRename(id);
    } else if (e.key === 'Escape') {
      e.preventDefault();
      handleCancelRename();
    }
  };

  // Sort pinned conversations to the top
  const sortedConversations = [...conversations].sort((a, b) => {
    if (a.isPinned && !b.isPinned) return -1;
    if (!a.isPinned && b.isPinned) return 1;
    return new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime();
  });

  const filteredConversations = sortedConversations.filter((c) =>
    c.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Export handlers
  const handleExportText = (conv: ChatConversation) => {
    const textContent = conv.messages
      .map((m) => {
        const time = new Date(m.timestamp).toLocaleString('vi-VN');
        const role = m.role === 'user' ? 'BẠN' : 'TRỢ LÝ AI (SOCRATIC)';
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
    setExportingConv(null);
  };

  const handleExportMarkdown = (conv: ChatConversation) => {
    let md = `# ${conv.title}\n\n`;
    md += `> **AI Socratic Coding Tutor**  \n`;
    md += `> Ngày tạo: ${new Date(conv.createdAt).toLocaleString('vi-VN')}  \n`;
    md += `> Cập nhật: ${new Date(conv.updatedAt).toLocaleString('vi-VN')}  \n\n---\n\n`;

    conv.messages.forEach((m) => {
      const role = m.role === 'user' ? '🧑 **Người học**' : '🤖 **AI Socratic Tutor**';
      const time = new Date(m.timestamp).toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
      md += `### ${role} *(${time})*\n\n${m.content}\n\n`;
      if (m.attachments?.length) {
        md += `**Tệp đính kèm:**\n`;
        m.attachments.forEach(a => {
          md += `- \`${a.name}\` (${(a.size / 1024).toFixed(1)} KB)\n`;
        });
        md += `\n`;
      }
      md += `---\n\n`;
    });

    const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${conv.title.replace(/[^a-z0-9]/gi, '_').toLowerCase()}.md`;
    a.click();
    URL.revokeObjectURL(url);
    setExportingConv(null);
  };

  const handleExportJSON = (conv: ChatConversation) => {
    const jsonStr = JSON.stringify(conv, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${conv.title.replace(/[^a-z0-9]/gi, '_').toLowerCase()}_backup.json`;
    a.click();
    URL.revokeObjectURL(url);
    setExportingConv(null);
  };

  const handlePrint = () => {
    window.print();
    setExportingConv(null);
  };

  const handleImportFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(reader.result as string);
        if (parsed && parsed.id && parsed.title && Array.isArray(parsed.messages)) {
          if (onImportConversation) {
            onImportConversation(parsed);
          }
        }
      } catch (err) {
        console.error('Lỗi đọc tệp JSON:', err);
      }
    };
    reader.readAsText(file);
    if (importInputRef.current) {
      importInputRef.current.value = '';
    }
  };

  const sidebarContent = (
    <div className="flex flex-col h-full bg-slate-50/90 dark:bg-[#0c101c] text-slate-800 dark:text-slate-100 transition-colors duration-200">
      {/* Top Header */}
      <div className="px-4 py-3.5 border-b border-slate-200/80 dark:border-slate-800/80 flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="flex h-8 w-8 items-center justify-center rounded-xl bg-gradient-to-br from-blue-600 to-indigo-600 text-white shadow-md shadow-blue-500/20">
            <Terminal className="h-4 w-4" />
          </div>
          <div className="flex flex-col">
            <span className="font-extrabold text-sm tracking-tight text-slate-900 dark:text-slate-100 leading-tight">
              AI Coding Tutor
            </span>
            <span className="text-[10px] font-semibold text-blue-600 dark:text-blue-400">
              Socratic Assistant
            </span>
          </div>
        </div>

        {/* Mobile close button */}
        <button
          type="button"
          onClick={onCloseMobile}
          className="md:hidden rounded-lg p-1.5 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800 focus:outline-none transition"
          aria-label="Đóng thanh bên"
        >
          <X className="h-4 w-4" />
        </button>
      </div>

      {/* New Chat Button */}
      <div className="p-3 pb-2">
        <button
          type="button"
          onClick={() => {
            onNewConversation();
            onCloseMobile();
          }}
          className="group flex w-full items-center justify-center gap-2 rounded-xl bg-blue-600 hover:bg-blue-500 dark:bg-blue-600 dark:hover:bg-blue-500 px-3 py-2 text-xs font-bold text-white shadow-sm hover:shadow-md transition-all active:scale-[0.98]"
        >
          <Plus className="h-4 w-4 transition-transform group-hover:rotate-90 duration-200" />
          <span>Cuộc trò chuyện mới</span>
        </button>
      </div>

      {/* Search Bar */}
      {conversations.length > 2 && (
        <div className="px-3 pb-2">
          <div className="relative flex items-center">
            <Search className="absolute left-3 h-3.5 w-3.5 text-slate-400 dark:text-slate-500" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm kiếm hội thoại..."
              className="w-full rounded-xl border border-slate-200 dark:border-slate-800/80 bg-white dark:bg-slate-900/60 pl-8 pr-3 py-1.5 text-xs text-slate-700 dark:text-slate-200 placeholder-slate-400 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500 transition-all"
            />
          </div>
        </div>
      )}

      {/* Recent Chats List */}
      <div className="flex-1 overflow-y-auto px-2 py-1 space-y-0.5">
        <div className="flex items-center justify-between px-3 py-2 text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
          <span>Lịch sử trò chuyện ({filteredConversations.length})</span>
          {conversations.length > 1 && onClearAll && (
            <button
              type="button"
              onClick={onClearAll}
              className="text-[10px] font-semibold text-slate-400 hover:text-rose-500 dark:hover:text-rose-400 transition-colors"
              title="Xóa tất cả các cuộc trò chuyện"
            >
              Xóa tất cả
            </button>
          )}
        </div>

        {filteredConversations.length === 0 ? (
          <div className="px-3 py-8 text-center text-xs text-slate-400 dark:text-slate-500">
            {searchQuery ? 'Không tìm thấy cuộc trò chuyện' : 'Chưa có cuộc trò chuyện nào'}
          </div>
        ) : (
          filteredConversations.map((conv) => {
            const isActive = conv.id === activeConversationId;
            const isEditing = editingId === conv.id;

            return (
              <div
                key={conv.id}
                className={`group relative flex items-center justify-between rounded-xl px-2.5 py-2 text-xs font-medium transition-all cursor-pointer ${
                  isActive
                    ? 'bg-blue-50/80 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 font-semibold border border-blue-200/80 dark:border-blue-800/60'
                    : 'text-slate-600 dark:text-slate-400 hover:bg-white dark:hover:bg-slate-800/60 hover:text-slate-900 dark:hover:text-slate-200 border border-transparent'
                }`}
                onClick={() => {
                  if (!isEditing) {
                    onSelectConversation(conv.id);
                    onCloseMobile();
                  }
                }}
              >
                {/* Editing Inline Mode */}
                {isEditing ? (
                  <div className="flex items-center gap-1.5 w-full" onClick={(e) => e.stopPropagation()}>
                    <input
                      ref={editInputRef}
                      type="text"
                      value={editTitleInput}
                      onChange={(e) => setEditTitleInput(e.target.value)}
                      onKeyDown={(e) => handleKeyDownRename(e, conv.id)}
                      className="flex-1 rounded-md border border-blue-400 bg-white dark:bg-slate-800 px-2 py-1 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                    <button
                      type="button"
                      onClick={() => handleSaveRename(conv.id)}
                      className="rounded p-1 text-emerald-600 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950 transition"
                      title="Lưu (Enter)"
                    >
                      <Check className="h-3.5 w-3.5" />
                    </button>
                    <button
                      type="button"
                      onClick={handleCancelRename}
                      className="rounded p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                      title="Hủy (Esc)"
                    >
                      <X className="h-3.5 w-3.5" />
                    </button>
                  </div>
                ) : (
                  <>
                    <div className="flex items-center gap-2 min-w-0 pr-18">
                      {conv.isPinned ? (
                        <Pin className="h-3.5 w-3.5 shrink-0 text-amber-500 fill-amber-500" />
                      ) : (
                        <MessageSquare className={`h-3.5 w-3.5 shrink-0 ${isActive ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400'}`} />
                      )}
                      <span className="truncate" title={conv.title}>
                        {conv.title}
                      </span>
                    </div>

                    {/* Quick actions hover row */}
                    <div className="opacity-0 group-hover:opacity-100 flex items-center gap-0.5 transition absolute right-1.5 bg-white/95 dark:bg-slate-900/95 backdrop-blur-xs rounded-lg px-1 py-0.5 border border-slate-200/80 dark:border-slate-800/80 shadow-xs">
                      {/* Pin Button */}
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          onTogglePinConversation(conv.id);
                        }}
                        className={`rounded p-1 transition ${
                          conv.isPinned ? 'text-amber-500' : 'text-slate-400 hover:text-amber-500 hover:bg-slate-100 dark:hover:bg-slate-800'
                        }`}
                        title={conv.isPinned ? 'Bỏ ghim' : 'Ghim lên đầu'}
                      >
                        <Pin className="h-3 w-3" />
                      </button>

                      {/* Rename Button */}
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleStartRename(conv);
                        }}
                        className="rounded p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 transition"
                        title="Đổi tên"
                      >
                        <Edit3 className="h-3 w-3" />
                      </button>

                      {/* Export Button */}
                      {conv.messages.length > 0 && (
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            setExportingConv(conv);
                          }}
                          className="rounded p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 transition"
                          title="Tùy chọn xuất (Markdown, JSON, TXT)"
                        >
                          <Download className="h-3 w-3" />
                        </button>
                      )}

                      {/* Delete Button */}
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          onDeleteConversation(conv.id);
                        }}
                        className="rounded p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-rose-600 dark:hover:text-rose-400 transition"
                        title="Xóa"
                      >
                        <Trash2 className="h-3 w-3" />
                      </button>
                    </div>
                  </>
                )}
              </div>
            );
          })
        )}
      </div>

      {/* Bottom Footer Section */}
      <div className="p-3 border-t border-slate-200/80 dark:border-slate-800/80 bg-slate-100/50 dark:bg-slate-900/50 space-y-1.5">
        {onOpenInstructorKnowledge && (
          <button
            type="button"
            onClick={() => {
              onOpenInstructorKnowledge();
              onCloseMobile();
            }}
            className="w-full flex items-center justify-center gap-1.5 rounded-xl border border-emerald-200 dark:border-emerald-800/80 bg-emerald-50/80 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 hover:bg-emerald-100 dark:hover:bg-emerald-900/60 py-2 text-xs font-bold transition shadow-2xs"
            title="Dành cho Giảng viên: Kéo thả nạp thêm tài liệu giáo trình vào ChromaDB"
          >
            <BookOpen className="h-3.5 w-3.5" />
            <span>Nạp giáo trình mới (GV)</span>
          </button>
        )}

        <div className="flex items-center justify-between text-xs font-medium text-slate-600 dark:text-slate-400">
          <button
            type="button"
            onClick={onOpenSettings}
            className="flex items-center gap-1.5 rounded-lg px-2 py-1.5 hover:bg-white dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 transition"
            title="Cài đặt thông số AI"
          >
            <Sliders className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400 shrink-0" />
            <span>Cài đặt</span>
          </button>

          <button
            type="button"
            onClick={onOpenShortcuts}
            className="flex items-center gap-1.5 rounded-lg px-2 py-1.5 hover:bg-white dark:hover:bg-slate-800 hover:text-slate-800 dark:hover:text-slate-200 transition"
            title="Xem phím tắt (Ctrl + /)"
          >
            <Keyboard className="h-3.5 w-3.5 shrink-0" />
            <span>Phím tắt</span>
          </button>

          {onImportConversation && (
            <>
              <button
                type="button"
                onClick={() => importInputRef.current?.click()}
                className="flex items-center gap-1 rounded-lg px-2 py-1.5 hover:bg-white dark:hover:bg-slate-800 hover:text-blue-600 transition"
                title="Khôi phục cuộc trò chuyện từ tệp .json"
              >
                <Upload className="h-3.5 w-3.5 shrink-0" />
                <span>Nạp</span>
              </button>
              <input
                ref={importInputRef}
                type="file"
                accept=".json"
                onChange={handleImportFile}
                className="hidden"
              />
            </>
          )}
        </div>

        <div className="flex items-center justify-between pt-1 px-1 text-[10px] text-slate-400 dark:text-slate-500">
          <span className="flex items-center gap-1">
            <span className="h-1.5 w-1.5 rounded-full bg-emerald-500" />
            FastAPI + ChromaDB
          </span>
          <span>v4.0 Socratic</span>
        </div>
      </div>
    </div>
  );

  return (
    <>
      {/* Mobile Drawer Overlay */}
      {isMobileOpen && (
        <div
          className="fixed inset-0 z-40 bg-black/50 backdrop-blur-xs md:hidden"
          onClick={onCloseMobile}
          aria-hidden="true"
        />
      )}

      {/* Mobile Drawer */}
      <div
        className={`fixed inset-y-0 left-0 z-50 w-72 transform transition-transform duration-200 ease-in-out md:hidden shadow-xl ${
          isMobileOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        {sidebarContent}
      </div>

      {/* Desktop Sidebar */}
      <aside
        className={`hidden md:flex flex-col shrink-0 border-r border-slate-200/80 dark:border-slate-800/80 transition-all duration-200 ease-in-out ${
          isOpen ? 'w-64' : 'w-0 overflow-hidden border-r-0'
        }`}
      >
        <div className="w-64 h-full">
          {sidebarContent}
        </div>
      </aside>

      {/* Export Options Modal */}
      {exportingConv && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-xs"
          onClick={() => setExportingConv(null)}
        >
          <div
            className="w-full max-w-sm rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 shadow-xl space-y-3"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
              <div className="flex items-center gap-2">
                <Download className="h-4 w-4 text-blue-600 dark:text-blue-400" />
                <h3 className="font-bold text-xs text-slate-900 dark:text-slate-100 truncate">
                  Xuất: &ldquo;{exportingConv.title}&rdquo;
                </h3>
              </div>
              <button
                type="button"
                onClick={() => setExportingConv(null)}
                className="rounded-lg p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            <div className="grid grid-cols-1 gap-1.5 text-xs">
              <button
                type="button"
                onClick={() => handleExportMarkdown(exportingConv)}
                className="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-blue-500 hover:bg-blue-50/50 dark:hover:bg-blue-950/30 transition text-left"
              >
                <div className="flex items-center gap-2">
                  <FileCode className="h-4 w-4 text-blue-600" />
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100">Markdown (.md)</div>
                    <div className="text-[10px] text-slate-400">Định dạng chuẩn cho ghi chú và báo cáo</div>
                  </div>
                </div>
                <Download className="h-3.5 w-3.5 text-slate-400" />
              </button>

              <button
                type="button"
                onClick={() => handleExportJSON(exportingConv)}
                className="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-purple-500 hover:bg-purple-50/50 dark:hover:bg-purple-950/30 transition text-left"
              >
                <div className="flex items-center gap-2">
                  <Download className="h-4 w-4 text-purple-600" />
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100">JSON Backup (.json)</div>
                    <div className="text-[10px] text-slate-400">Sao lưu đầy đủ dữ liệu hội thoại</div>
                  </div>
                </div>
                <Download className="h-3.5 w-3.5 text-slate-400" />
              </button>

              <button
                type="button"
                onClick={() => handleExportText(exportingConv)}
                className="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800 transition text-left"
              >
                <div className="flex items-center gap-2">
                  <FileText className="h-4 w-4 text-slate-500" />
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100">Văn bản thô (.txt)</div>
                    <div className="text-[10px] text-slate-400">Dễ đọc trên mọi thiết bị</div>
                  </div>
                </div>
                <Download className="h-3.5 w-3.5 text-slate-400" />
              </button>

              <button
                type="button"
                onClick={handlePrint}
                className="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-emerald-500 hover:bg-emerald-50/50 dark:hover:bg-emerald-950/30 transition text-left"
              >
                <div className="flex items-center gap-2">
                  <Printer className="h-4 w-4 text-emerald-600" />
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100">In / Lưu PDF</div>
                    <div className="text-[10px] text-slate-400">Mở hộp thoại in trình duyệt</div>
                  </div>
                </div>
                <Printer className="h-3.5 w-3.5 text-slate-400" />
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
