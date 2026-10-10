'use client';

import React, { useEffect, useRef } from 'react';
import { 
  Sparkles, 
  HelpCircle, 
  FileText, 
  Image as ImageIcon, 
  Code2 
} from 'lucide-react';
import { ChatMessage } from '@/types/chat';
import { ChatMessageItem } from './ChatMessageItem';

interface ChatMessageListProps {
  messages: ChatMessage[];
  onSelectSuggestion?: (text: string) => void;
}

export const ChatMessageList: React.FC<ChatMessageListProps> = ({
  messages,
  onSelectSuggestion,
}) => {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  if (messages.length === 0) {
    const suggestions = [
      {
        icon: Code2,
        title: 'Phân tích lỗi giải thuật',
        desc: 'Hỏi về độ phức tạp Big-O, đệ quy hoặc tối ưu vòng lặp',
        query: 'Hãy giải thích sự khác biệt về độ phức tạp thời gian giữa Bubble Sort và Merge Sort.',
      },
      {
        icon: FileText,
        title: 'Đính kèm tài liệu mã nguồn',
        desc: 'Tải tệp .pdf, .docx, .py để chuẩn bị bối cảnh cho RAG sau này',
        query: 'Tôi chuẩn bị tải lên tài liệu đặc tả bài tập môn Cấu trúc dữ liệu để làm bối cảnh.',
      },
      {
        icon: ImageIcon,
        title: 'Đính kèm ảnh chụp màn hình',
        desc: 'Gửi ảnh terminal hoặc sơ đồ lớp cần hỗ trợ phân tích',
        query: 'Tôi muốn đính kèm ảnh chụp màn hình thông báo lỗi Runtime Error để nhờ phân tích nguyên nhân.',
      },
      {
        icon: HelpCircle,
        title: 'Gợi mở sư phạm Socratic',
        desc: 'Nhận gợi ý từng bước thay vì lấy ngay đáp án giải sẵn',
        query: 'Làm thế nào để phát hiện tràn bộ nhớ khi thao tác với con trỏ trong C++?',
      },
    ];

    return (
      <div className="flex-1 flex flex-col items-center justify-center p-6 md:p-10 max-w-4xl mx-auto w-full text-center select-none">
        {/* Welcome Icon */}
        <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-blue-50 text-blue-600 mb-4 shadow-xs border border-blue-100">
          <Sparkles className="h-7 w-7" />
        </div>

        {/* Heading */}
        <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-[#202123]">
          Bạn muốn tìm hiểu điều gì hôm nay?
        </h1>
        <p className="mt-2 text-sm text-[#6B7280] max-w-lg leading-relaxed">
          Giao diện tiếp nhận văn bản, hình ảnh và tài liệu đa phương thức. Nhập câu hỏi bên dưới hoặc chọn một chủ đề gợi ý để bắt đầu.
        </p>

        {/* Suggestion Cards Grid */}
        <div className="mt-8 grid grid-cols-1 sm:grid-cols-2 gap-3 w-full text-left">
          {suggestions.map((item, idx) => {
            const Icon = item.icon;
            return (
              <button
                key={idx}
                type="button"
                onClick={() => onSelectSuggestion && onSelectSuggestion(item.query)}
                className="group flex flex-col justify-between rounded-xl border border-slate-200 bg-white p-4 text-left shadow-xs transition hover:border-blue-400 hover:shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20"
              >
                <div className="flex items-center gap-2.5 mb-1.5">
                  <div className="flex h-7 w-7 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-slate-600 group-hover:bg-blue-50 group-hover:text-blue-600 transition">
                    <Icon className="h-4 w-4" />
                  </div>
                  <span className="text-xs font-semibold text-slate-800 group-hover:text-blue-600 transition">
                    {item.title}
                  </span>
                </div>
                <p className="text-[12px] text-slate-500 line-clamp-2">
                  {item.desc}
                </p>
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
        {messages.map((msg) => (
          <ChatMessageItem key={msg.id} message={msg} />
        ))}
        <div ref={bottomRef} className="h-4" />
      </div>
    </div>
  );
};
