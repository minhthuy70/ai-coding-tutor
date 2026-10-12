'use client';

import React, { useEffect, useRef } from 'react';
import { 
  Sparkles, 
  HelpCircle, 
  FileText, 
  Image as ImageIcon, 
  Code2,
  Bot
} from 'lucide-react';
import { ChatMessage, ChatAttachment } from '@/types/chat';
import { ChatMessageItem } from './ChatMessageItem';

interface ChatMessageListProps {
  messages: ChatMessage[];
  isGenerating?: boolean;
  onSelectSuggestion?: (text: string) => void;
  onViewImage?: (url: string, name: string) => void;
  onViewDocument?: (attachment: ChatAttachment) => void;
  onRegenerate?: () => void;
  onDeleteMessage?: (id: string) => void;
  onEditUserMessage?: (id: string, newContent: string) => void;
  onRunCode?: (code: string, language: string) => void;
}

export const ChatMessageList: React.FC<ChatMessageListProps> = ({
  messages,
  isGenerating = false,
  onSelectSuggestion,
  onViewImage,
  onViewDocument,
  onRegenerate,
  onDeleteMessage,
  onEditUserMessage,
  onRunCode,
}) => {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isGenerating]);

  const lastAssistantIndex = messages.map((m) => m.role).lastIndexOf('assistant');

  if (messages.length === 0) {
    const suggestions = [
      {
        icon: Code2,
        title: 'Phân tích thuật toán & Đệ quy',
        desc: 'Đo độ phức tạp Big-O, phát hiện vòng lặp vô hạn và tối ưu mảng',
        query: 'Hãy phân tích độ phức tạp thời gian và không gian của thuật toán QuickSort.',
        gradient: 'from-blue-500 to-indigo-600',
      },
      {
        icon: FileText,
        title: 'Đính kèm tài liệu đề bài & code',
        desc: 'Tải tệp .pdf, .docx, .py, .cpp để làm cơ sở tri thức cho RAG',
        query: 'Tôi chuẩn bị tải lên tài liệu đề bài thực hành môn Cấu trúc dữ liệu để làm bối cảnh.',
        gradient: 'from-emerald-500 to-teal-600',
      },
      {
        icon: ImageIcon,
        title: 'Dán ảnh màn hình trực tiếp (Ctrl + V)',
        desc: 'Chụp màn hình thông báo lỗi Terminal rồi nhấn Ctrl + V để tải lên ngay',
        query: 'Tôi vừa chụp ảnh màn hình lỗi Segmentation Fault (core dumped), hãy xem ảnh đính kèm giúp tôi.',
        gradient: 'from-amber-500 to-orange-600',
      },
      {
        icon: HelpCircle,
        title: 'Phương pháp sư phạm Socratic',
        desc: 'Hỏi gợi mở từng bước, không đưa trực tiếp mã nguồn giải sẵn',
        query: 'Làm thế nào để phát hiện rò rỉ bộ nhớ (memory leak) khi dùng malloc/free trong C?',
        gradient: 'from-purple-500 to-pink-600',
      },
    ];

    return (
      <div className="flex-1 flex flex-col items-center justify-center p-6 md:p-10 max-w-4xl mx-auto w-full text-center select-none">
        {/* Welcome Icon with radiant glow */}
        <div className="relative flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-tr from-blue-600 to-indigo-500 text-white mb-5 shadow-lg shadow-blue-500/20 ring-4 ring-blue-50 dark:ring-blue-950/60">
          <Sparkles className="h-8 w-8 animate-pulse" />
        </div>

        {/* Heading */}
        <h1 className="text-2xl md:text-3xl font-extrabold tracking-tight text-slate-900 dark:text-slate-100">
          Bạn muốn tìm hiểu điều gì hôm nay?
        </h1>
        <p className="mt-2.5 text-sm text-slate-500 dark:text-slate-400 max-w-lg leading-relaxed">
          Giao diện tiếp nhận đa phương thức thế hệ mới. Nhập câu hỏi, <span className="font-semibold text-blue-600 dark:text-blue-400">chụp màn hình dán ảnh (Ctrl + V)</span> hoặc kéo thả tài liệu để bắt đầu.
        </p>

        {/* Suggestion Cards Grid */}
        <div className="mt-8 grid grid-cols-1 sm:grid-cols-2 gap-3.5 w-full text-left">
          {suggestions.map((item, idx) => {
            const Icon = item.icon;
            return (
              <button
                key={idx}
                type="button"
                onClick={() => onSelectSuggestion && onSelectSuggestion(item.query)}
                className="group relative flex flex-col justify-between rounded-2xl border border-slate-200/90 dark:border-slate-700/80 bg-white dark:bg-slate-800/90 p-4.5 text-left shadow-2xs transition-all duration-200 hover:border-blue-400 dark:hover:border-blue-500 hover:bg-slate-50/50 dark:hover:bg-slate-700/80 hover:shadow-md hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
              >
                <div>
                  <div className="flex items-center gap-2.5 mb-2">
                    <div className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-gradient-to-tr ${item.gradient} text-white shadow-xs`}>
                      <Icon className="h-4 w-4" />
                    </div>
                    <span className="text-xs font-bold text-slate-800 dark:text-slate-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">
                      {item.title}
                    </span>
                  </div>
                  <p className="text-[12px] text-slate-500 dark:text-slate-400 line-clamp-2 leading-relaxed">
                    {item.desc}
                  </p>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 overflow-y-auto">
      <div className="flex flex-col">
        {messages.map((msg, idx) => (
          <ChatMessageItem 
            key={msg.id} 
            message={msg} 
            isLastAssistantMessage={idx === lastAssistantIndex}
            onViewImage={onViewImage}
            onViewDocument={onViewDocument}
            onRegenerate={onRegenerate}
            onDeleteMessage={onDeleteMessage}
            onEditUserMessage={onEditUserMessage}
            onSelectFollowUp={onSelectSuggestion}
            onRunCode={onRunCode}
          />
        ))}

        {/* Typing indicator */}
        {isGenerating && (
          <div className="w-full py-4 px-4 md:px-6 bg-[#F9FAFB] dark:bg-slate-900/70 border-y border-slate-100 dark:border-slate-800/80 animate-in fade-in duration-200">
            <div className="max-w-4xl mx-auto flex items-center gap-3">
              <div className="h-8 w-8 rounded-full bg-blue-600 flex items-center justify-center text-white shrink-0 shadow-xs">
                <Bot className="h-4 w-4" />
              </div>
              <div className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-2xs">
                <span className="h-2 w-2 rounded-full bg-blue-600 animate-bounce" style={{ animationDelay: '0ms' }} />
                <span className="h-2 w-2 rounded-full bg-blue-600 animate-bounce" style={{ animationDelay: '150ms' }} />
                <span className="h-2 w-2 rounded-full bg-blue-600 animate-bounce" style={{ animationDelay: '300ms' }} />
                <span className="text-xs text-slate-400 dark:text-slate-400 ml-2 font-medium">Đang phản hồi...</span>
              </div>
            </div>
          </div>
        )}

        <div ref={bottomRef} className="h-4" />
      </div>
    </div>
  );
};
