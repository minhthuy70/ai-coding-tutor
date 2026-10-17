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
  BarChart3,
  Upload,
  Printer,
  FileCode,
  FileText,
  Compass,
  Trophy,
  ShieldCheck,
  Code2,
  GraduationCap,
  ScanSearch,
  User as UserIcon,
  Award
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
  onOpenAnalytics?: () => void;
  onImportConversation?: (imported: ChatConversation) => void;
  isOpen: boolean;
  onToggle: () => void;
  isMobileOpen: boolean;
  onCloseMobile: () => void;
  onOpenRoadmap?: () => void;
  onOpenProblemSet?: () => void;
  onOpenCodeQuality?: () => void;
  onOpenSandbox?: () => void;
  onOpenInstructor?: () => void;
  onOpenPlagiarism?: () => void;
  onOpenProfile?: () => void;
  userRole?: 'student' | 'instructor';
  solvedCount?: number;
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
  onOpenAnalytics,
  onImportConversation,
  isOpen,
  onToggle,
  isMobileOpen,
  onCloseMobile,
  onOpenRoadmap,
  onOpenProblemSet,
  onOpenCodeQuality,
  onOpenSandbox,
  onOpenInstructor,
  onOpenPlagiarism,
  onOpenProfile,
  userRole = 'student',
  solvedCount = 0,
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
    setExportingConv(null);
  };

  const handleExportMarkdown = (conv: ChatConversation) => {
    let md = `# ${conv.title}\n\n`;
    md += `> **Nền tảng AI Coding Tutor & Auto-Grader**  \n`;
    md += `> Ngày tạo: ${new Date(conv.createdAt).toLocaleString('vi-VN')}  \n`;
    md += `> Lần cập nhật: ${new Date(conv.updatedAt).toLocaleString('vi-VN')}  \n\n---\n\n`;

    conv.messages.forEach((m) => {
      const role = m.role === 'user' ? '🧑 **Sinh viên (Bạn)**' : '🤖 **Trợ lý AI Coding Tutor**';
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
        console.error('Lỗi tệp JSON:', err);
      }
    };
    reader.readAsText(file);
    if (importInputRef.current) {
      importInputRef.current.value = '';
    }
  };

  const sidebarContent = (
    <div className="flex flex-col h-full bg-[#F4F4F6] dark:bg-[#090d16] text-slate-900 dark:text-slate-100 transition-colors duration-300">
      {/* Top Header — gradient accent */}
      <div className="relative px-4 py-3.5 border-b border-slate-200/80 dark:border-slate-800 flex items-center justify-between overflow-hidden">
        {/* Subtle gradient background */}
        <div className="absolute inset-0 bg-gradient-to-r from-blue-600/5 via-indigo-600/3 to-transparent dark:from-blue-600/10 dark:via-indigo-600/6 pointer-events-none" />

        <div className="relative flex items-center gap-2.5">
          {/* Animated logo */}
          <div className="relative flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-blue-600 to-indigo-600 text-white shadow-lg shadow-blue-500/25">
            <Terminal className="h-4.5 w-4.5" />
            <span className="absolute inset-0 rounded-xl bg-white/10 opacity-0 hover:opacity-100 transition-opacity" />
          </div>
          <div className="flex flex-col">
            <span className="font-extrabold text-sm tracking-tight text-slate-900 dark:text-slate-100 leading-tight">
              AI Coding Tutor
            </span>
            <span className="text-[10px] font-bold uppercase tracking-wider bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Multimodal Studio
            </span>
          </div>
        </div>

        {/* Mobile close button */}
        <button
          type="button"
          onClick={onCloseMobile}
          className="relative md:hidden rounded-lg p-1.5 text-slate-500 hover:bg-slate-200 dark:hover:bg-slate-800 focus:outline-none transition"
          aria-label="Đóng thanh bên"
        >
          <X className="h-5 w-5" />
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
          className="group flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 px-3 py-2.5 text-sm font-bold text-white shadow-md shadow-blue-500/25 hover:shadow-lg hover:shadow-blue-500/30 active:scale-[0.98] focus:outline-none focus:ring-2 focus:ring-blue-500/30 transition-all duration-200"
        >
          <Plus className="h-4 w-4 transition-transform group-hover:rotate-90 duration-200" />
          <span>Cuộc trò chuyện mới</span>
        </button>
      </div>

      {/* Studio Learning & Practice Hub Tools */}
      <div className="px-3 pb-2 space-y-1.5">
        <div className="grid grid-cols-2 gap-1.5 text-xs font-bold">
          {onOpenRoadmap && (
            <button
              type="button"
              onClick={() => { onOpenRoadmap(); onCloseMobile(); }}
              className="flex items-center gap-1.5 px-2.5 py-2 rounded-xl bg-blue-50/70 hover:bg-blue-100 dark:bg-blue-950/40 dark:hover:bg-blue-900/60 text-blue-700 dark:text-blue-300 border border-blue-200/60 dark:border-blue-800/60 transition shadow-2xs"
              title="Lộ trình học tập & Cây kỹ năng"
            >
              <Compass className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400 shrink-0" />
              <span className="truncate">Lộ trình</span>
            </button>
          )}

          {onOpenProblemSet && (
            <button
              type="button"
              onClick={() => { onOpenProblemSet(); onCloseMobile(); }}
              className="flex items-center gap-1.5 px-2.5 py-2 rounded-xl bg-amber-50/70 hover:bg-amber-100 dark:bg-amber-950/40 dark:hover:bg-amber-900/60 text-amber-700 dark:text-amber-300 border border-amber-200/60 dark:border-amber-800/60 transition shadow-2xs"
              title="Đấu trường & Kho bài tập LeetCode"
            >
              <Trophy className="h-3.5 w-3.5 text-amber-600 dark:text-amber-400 shrink-0" />
              <span className="truncate">Kho bài tập</span>
            </button>
          )}
        </div>

        <div className="grid grid-cols-2 gap-1.5 text-xs font-bold">
          {onOpenSandbox && (
            <button
              type="button"
              onClick={() => { onOpenSandbox(); onCloseMobile(); }}
              className="flex items-center gap-1.5 px-2.5 py-2 rounded-xl bg-emerald-50/70 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200/60 dark:border-emerald-800/60 transition shadow-2xs"
              title="Mở Code Sandbox để chạy thử nghiệm"
            >
              <Code2 className="h-3.5 w-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
              <span className="truncate">Sandbox</span>
            </button>
          )}

          {onOpenCodeQuality && (
            <button
              type="button"
              onClick={() => { onOpenCodeQuality(); onCloseMobile(); }}
              className="flex items-center gap-1.5 px-2.5 py-2 rounded-xl bg-indigo-50/70 hover:bg-indigo-100 dark:bg-indigo-950/40 dark:hover:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300 border border-indigo-200/60 dark:border-indigo-800/60 transition shadow-2xs"
              title="Đánh giá & Phân tích chất lượng mã nguồn"
            >
              <ShieldCheck className="h-3.5 w-3.5 text-indigo-600 dark:text-indigo-400 shrink-0" />
              <span className="truncate">Đánh giá code</span>
            </button>
          )}
        </div>

        <div className="grid grid-cols-2 gap-1.5 text-xs font-bold">
          {onOpenInstructor && (
            <button
              type="button"
              onClick={() => { onOpenInstructor(); onCloseMobile(); }}
              className="flex items-center gap-1.5 px-2.5 py-2 rounded-xl bg-sky-50/70 hover:bg-sky-100 dark:bg-sky-950/40 dark:hover:bg-sky-900/60 text-sky-700 dark:text-sky-300 border border-sky-200/60 dark:border-sky-800/60 transition shadow-2xs"
              title="Bảng điểm & Quản lý lớp học Giảng viên"
            >
              <GraduationCap className="h-3.5 w-3.5 text-sky-600 dark:text-sky-400 shrink-0" />
              <span className="truncate">Bảng điểm GV</span>
            </button>
          )}

          {onOpenPlagiarism && (
            <button
              type="button"
              onClick={() => { onOpenPlagiarism(); onCloseMobile(); }}
              className="flex items-center gap-1.5 px-2.5 py-2 rounded-xl bg-rose-50/70 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/60 text-rose-700 dark:text-rose-300 border border-rose-200/60 dark:border-rose-800/60 transition shadow-2xs"
              title="So trùng mã nguồn & Kiểm tra đạo văn"
            >
              <ScanSearch className="h-3.5 w-3.5 text-rose-600 dark:text-rose-400 shrink-0" />
              <span className="truncate">So trùng code</span>
            </button>
          )}
        </div>
      </div>

      {/* Search Bar */}
      {conversations.length > 1 && (
        <div className="px-3 pb-2">
          <div className="relative flex items-center">
            <Search className="absolute left-3 h-3.5 w-3.5 text-slate-400 dark:text-slate-500" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm kiếm cuộc trò chuyện..."
              className="w-full rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/80 pl-9 pr-3 py-2 text-xs text-slate-700 dark:text-slate-200 placeholder-slate-400 dark:placeholder-slate-500 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500/15 transition-all"
            />
          </div>
        </div>
      )}

      {/* Recent Chats List */}
      <div className="flex-1 overflow-y-auto px-2 py-1 space-y-0.5">
        <div className="flex items-center justify-between px-3 py-2 text-[10.5px] font-bold uppercase tracking-widest text-slate-400 dark:text-slate-600">
          <span>Gần đây · {filteredConversations.length}</span>
          {conversations.length > 1 && onClearAll && (
            <button
              type="button"
              onClick={onClearAll}
              className="text-[10px] text-slate-400 dark:text-slate-600 hover:text-rose-500 dark:hover:text-rose-400 transition-colors"
              title="Xóa tất cả"
            >
              Xóa tất cả
            </button>
          )}
        </div>

        {filteredConversations.length === 0 ? (
          <div className="px-3 py-6 text-center text-xs text-slate-400 dark:text-slate-500">
            {searchQuery ? 'Không tìm thấy cuộc trò chuyện' : 'Chưa có cuộc trò chuyện nào'}
          </div>
        ) : (
          filteredConversations.map((conv) => {
            const isActive = conv.id === activeConversationId;
            const isEditing = editingId === conv.id;

            return (
              <div
                key={conv.id}
                className={`group relative flex items-center justify-between rounded-xl px-2.5 py-2.5 text-xs font-medium transition-all duration-150 cursor-pointer ${
                  isActive
                    ? 'bg-white dark:bg-slate-800/80 text-blue-700 dark:text-blue-400 shadow-sm border border-blue-200/60 dark:border-blue-800/40 font-semibold'
                    : 'text-slate-600 dark:text-slate-400 hover:bg-white/70 dark:hover:bg-slate-800/50 hover:text-slate-900 dark:hover:text-slate-200 border border-transparent'
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
                      title="Lưu tên (Enter)"
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
                    <div className="flex items-center gap-2 min-w-0 pr-20">
                      {conv.isPinned ? (
                        <Pin className="h-3.5 w-3.5 shrink-0 text-amber-500 fill-amber-500" />
                      ) : (
                        <MessageSquare className={`h-3.5 w-3.5 shrink-0 ${isActive ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400 dark:text-slate-500'}`} />
                      )}
                      <span className="truncate" title={conv.title}>
                        {conv.title}
                      </span>
                    </div>

                    {/* Quick actions row */}
                    <div className="opacity-0 group-hover:opacity-100 flex items-center gap-0.5 transition absolute right-1.5 bg-white/95 dark:bg-slate-900/95 backdrop-blur-xs rounded-lg px-1 py-0.5 border border-slate-200/60 dark:border-slate-800/80 shadow-2xs">
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
                          title="Tùy chọn xuất (Markdown, JSON, TXT, PDF)"
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
      <div className="p-3 border-t border-slate-200/80 dark:border-slate-800 bg-gradient-to-b from-transparent to-slate-100/80 dark:to-slate-900/60 space-y-1">
        {/* Row 1: Settings + Shortcuts */}
        <div className="grid grid-cols-2 gap-1">
          <button
            type="button"
            onClick={onOpenSettings}
            className="flex items-center gap-1.5 rounded-xl px-2.5 py-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 hover:shadow-sm transition-all border border-transparent hover:border-slate-200 dark:hover:border-slate-700"
            title="Cài đặt thông số AI và giao diện"
          >
            <Sliders className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400 shrink-0" />
            <span>Cài đặt AI</span>
          </button>

          <button
            type="button"
            onClick={onOpenShortcuts}
            className="flex items-center gap-1.5 rounded-xl px-2.5 py-2 text-xs font-semibold text-slate-500 dark:text-slate-400 hover:bg-white dark:hover:bg-slate-800 hover:text-slate-800 dark:hover:text-slate-200 hover:shadow-sm transition-all border border-transparent hover:border-slate-200 dark:hover:border-slate-700"
            title="Xem danh sách phím tắt"
          >
            <Keyboard className="h-3.5 w-3.5 shrink-0" />
            <span>Phím tắt</span>
          </button>
        </div>

        {/* Row 2: Analytics + Import */}
        <div className="grid grid-cols-2 gap-1 pt-1 border-t border-slate-200/50 dark:border-slate-800/50">
          {onOpenAnalytics && (
            <button
              type="button"
              onClick={onOpenAnalytics}
              className="flex items-center gap-1.5 rounded-xl px-2.5 py-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-800 hover:text-emerald-600 dark:hover:text-emerald-400 hover:shadow-sm transition-all border border-transparent hover:border-slate-200 dark:hover:border-slate-700"
              title="Xem thống kê hội thoại và ước lượng token"
            >
              <BarChart3 className="h-3.5 w-3.5 text-emerald-500 shrink-0" />
              <span className="truncate">Thống kê</span>
            </button>
          )}

          {onImportConversation && (
            <>
              <button
                type="button"
                onClick={() => importInputRef.current?.click()}
                className="flex items-center gap-1.5 rounded-xl px-2.5 py-2 text-xs font-semibold text-slate-500 dark:text-slate-400 hover:bg-white dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 hover:shadow-sm transition-all border border-transparent hover:border-slate-200 dark:hover:border-slate-700"
                title="Khôi phục cuộc trò chuyện từ tệp .json"
              >
                <Upload className="h-3.5 w-3.5 shrink-0" />
                <span>Nạp JSON</span>
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

        {/* User Profile Card */}
        {onOpenProfile && (
          <button
            type="button"
            onClick={() => {
              onOpenProfile();
              onCloseMobile();
            }}
            className="w-full mt-1.5 flex items-center justify-between p-2 rounded-xl bg-gradient-to-r from-blue-500/10 via-indigo-500/5 to-purple-500/10 hover:from-blue-500/15 hover:to-purple-500/15 border border-blue-200/50 dark:border-blue-800/40 text-left transition-all group"
            title="Xem Hồ sơ học viên & Huy hiệu thành tích"
          >
            <div className="flex items-center gap-2 min-w-0">
              <div className="relative">
                <div className="h-8 w-8 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-600 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                  {userRole === 'instructor' ? 'TS' : 'A'}
                </div>
                <span className="absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-emerald-500 ring-2 ring-white dark:ring-slate-900" />
              </div>
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-1.5">
                  <span className="text-xs font-bold text-slate-800 dark:text-slate-100 truncate group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                    {userRole === 'instructor' ? 'TS. Trần Minh Trí' : 'Nguyễn Văn An'}
                  </span>
                </div>
                <div className="flex items-center gap-1 text-[10px] text-slate-500 dark:text-slate-400">
                  <span className={`px-1 rounded text-[9px] font-bold ${
                    userRole === 'instructor' 
                      ? 'bg-purple-100 text-purple-700 dark:bg-purple-900/60 dark:text-purple-300' 
                      : 'bg-blue-100 text-blue-700 dark:bg-blue-900/60 dark:text-blue-300'
                  }`}>
                    {userRole === 'instructor' ? 'Giảng viên' : 'Học viên'}
                  </span>
                  <span>· {solvedCount} bài giải</span>
                </div>
              </div>
            </div>
            <Award className="h-4 w-4 text-amber-500 shrink-0 group-hover:scale-110 transition-transform" />
          </button>
        )}

        {/* Version badge */}
        <p className="text-center text-[10px] text-slate-400 dark:text-slate-600 pt-1 font-medium">
          AI Coding Tutor · v4.0 Perfect Master Edition
        </p>
      </div>
    </div>
  );

  return (
    <>
      {/* Mobile Drawer Overlay */}
      {isMobileOpen && (
        <div
          className="fixed inset-0 z-40 modal-backdrop md:hidden animate-fade-in"
          onClick={onCloseMobile}
          aria-hidden="true"
        />
      )}

      {/* Mobile Drawer */}
      <div
        className={`fixed inset-y-0 left-0 z-50 w-72 transform transition-transform duration-300 ease-in-out md:hidden shadow-2xl ${
          isMobileOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        {sidebarContent}
      </div>

      {/* Desktop Sidebar */}
      <aside
        className={`hidden md:flex flex-col shrink-0 border-r border-slate-200/80 dark:border-slate-800 transition-all duration-300 ease-in-out ${
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
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-150"
          onClick={() => setExportingConv(null)}
        >
          <div
            className="w-full max-w-md rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-2xl space-y-4"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
              <div className="flex items-center gap-2">
                <Download className="h-5 w-5 text-blue-600 dark:text-blue-400" />
                <h3 className="font-bold text-sm text-slate-900 dark:text-slate-100">
                  Xuất cuộc trò chuyện: &ldquo;{exportingConv.title}&rdquo;
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

            <p className="text-xs text-slate-500 dark:text-slate-400">
              Lựa chọn định dạng xuất phù hợp với mục đích lưu trữ hoặc nộp báo cáo:
            </p>

            <div className="grid grid-cols-1 gap-2 text-xs">
              <button
                type="button"
                onClick={() => handleExportMarkdown(exportingConv)}
                className="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-blue-500 hover:bg-blue-50/50 dark:hover:bg-blue-950/30 transition text-left group"
              >
                <div className="flex items-center gap-2.5">
                  <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-100 dark:bg-blue-900/60 text-blue-600 dark:text-blue-400">
                    <FileCode className="h-4 w-4" />
                  </div>
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100 group-hover:text-blue-600 dark:group-hover:text-blue-400">
                      Tệp Markdown (.md)
                    </div>
                    <div className="text-[11px] text-slate-500 dark:text-slate-400">
                      Giữ nguyên tiêu đề, in đậm, danh sách và các khối mã nguồn
                    </div>
                  </div>
                </div>
                <Download className="h-4 w-4 text-slate-400 group-hover:text-blue-600" />
              </button>

              <button
                type="button"
                onClick={() => handleExportJSON(exportingConv)}
                className="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-purple-500 hover:bg-purple-50/50 dark:hover:bg-purple-950/30 transition text-left group"
              >
                <div className="flex items-center gap-2.5">
                  <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-purple-100 dark:bg-purple-900/60 text-purple-600 dark:text-purple-400">
                    <Download className="h-4 w-4" />
                  </div>
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100 group-hover:text-purple-600 dark:group-hover:text-purple-400">
                      Tệp JSON Sao lưu (.json)
                    </div>
                    <div className="text-[11px] text-slate-500 dark:text-slate-400">
                      Đầy đủ cấu trúc tin nhắn để khôi phục hoặc chuyển đổi thiết bị
                    </div>
                  </div>
                </div>
                <Download className="h-4 w-4 text-slate-400 group-hover:text-purple-600" />
              </button>

              <button
                type="button"
                onClick={() => handleExportText(exportingConv)}
                className="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800 transition text-left group"
              >
                <div className="flex items-center gap-2.5">
                  <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    <FileText className="h-4 w-4" />
                  </div>
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100 group-hover:text-slate-800 dark:group-hover:text-white">
                      Văn bản thô (.txt)
                    </div>
                    <div className="text-[11px] text-slate-500 dark:text-slate-400">
                      Văn bản thuần túy có ghi rõ mốc thời gian từng tin nhắn
                    </div>
                  </div>
                </div>
                <Download className="h-4 w-4 text-slate-400 group-hover:text-slate-700" />
              </button>

              <button
                type="button"
                onClick={handlePrint}
                className="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-emerald-500 hover:bg-emerald-50/50 dark:hover:bg-emerald-950/30 transition text-left group"
              >
                <div className="flex items-center gap-2.5">
                  <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-emerald-100 dark:bg-emerald-900/60 text-emerald-600 dark:text-emerald-400">
                    <Printer className="h-4 w-4" />
                  </div>
                  <div>
                    <div className="font-bold text-slate-900 dark:text-slate-100 group-hover:text-emerald-600 dark:group-hover:text-emerald-400">
                      In / Lưu thành PDF
                    </div>
                    <div className="text-[11px] text-slate-500 dark:text-slate-400">
                      Mở hộp thoại in của trình duyệt để lưu dạng PDF
                    </div>
                  </div>
                </div>
                <Printer className="h-4 w-4 text-slate-400 group-hover:text-emerald-600" />
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
