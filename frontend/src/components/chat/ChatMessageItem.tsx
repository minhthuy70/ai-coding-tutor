'use client';

import React, { useState } from 'react';
import { 
  User, 
  Bot, 
  Check, 
  Copy, 
  Info, 
  Clock, 
  FileCheck 
} from 'lucide-react';
import { ChatMessage } from '@/types/chat';
import { AttachmentBadge } from './AttachmentBadge';

interface ChatMessageItemProps {
  message: ChatMessage;
}

export const ChatMessageItem: React.FC<ChatMessageItemProps> = ({ message }) => {
  const [copied, setCopied] = useState(false);
  const isUser = message.role === 'user';

  const handleCopy = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const formattedTime = new Date(message.timestamp).toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
  });

  return (
    <div
      className={`group w-full py-5 px-4 md:px-6 transition-colors ${
        isUser ? 'bg-white' : 'bg-[#F9FAFB] border-y border-slate-100'
      }`}
    >
      <div className="max-w-4xl mx-auto flex gap-4 items-start">
        {/* Avatar */}
        <div
          className={`h-8 w-8 rounded-full flex items-center justify-center shrink-0 text-white font-medium shadow-xs ${
            isUser ? 'bg-slate-700' : 'bg-blue-600'
          }`}
          aria-hidden="true"
        >
          {isUser ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
        </div>

        {/* Content Body */}
        <div className="flex-1 min-w-0 space-y-3">
          {/* Header Row: Role name + Timestamp + Actions */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-xs font-semibold text-slate-900">
                {isUser ? 'Bạn' : 'Trợ lý AI (Chế độ Thử nghiệm)'}
              </span>
              <span className="text-[11px] text-slate-400 flex items-center gap-1">
                <Clock className="h-3 w-3" />
                {formattedTime}
              </span>
            </div>

            {/* Quick action copy button */}
            {message.content && (
              <button
                type="button"
                onClick={handleCopy}
                className="opacity-0 group-hover:opacity-100 rounded p-1 text-slate-400 hover:bg-slate-200/50 hover:text-slate-700 focus:opacity-100 transition"
                title="Sao chép nội dung"
                aria-label="Sao chép nội dung tin nhắn"
              >
                {copied ? (
                  <Check className="h-3.5 w-3.5 text-emerald-600" />
                ) : (
                  <Copy className="h-3.5 w-3.5" />
                )}
              </button>
            )}
          </div>

          {/* Text Content */}
          {message.content && (
            <div className="text-sm text-[#202123] whitespace-pre-wrap leading-relaxed break-words font-normal">
              {message.content}
            </div>
          )}

          {/* Attachments Section */}
          {message.attachments && message.attachments.length > 0 && (
            <div className="space-y-1.5 pt-1">
              <div className="flex items-center gap-1.5 text-xs font-medium text-slate-500">
                <FileCheck className="h-3.5 w-3.5 text-blue-600" />
                <span>Tệp đính kèm ({message.attachments.length}):</span>
              </div>
              <div className="flex flex-wrap gap-2 pt-1">
                {message.attachments.map((att) => (
                  <AttachmentBadge
                    key={att.id}
                    attachment={att}
                    readOnly
                  />
                ))}
              </div>
            </div>
          )}

          {/* Assistant Demo Status Banner (Mandatory Notice) */}
          {!isUser && (
            <div className="rounded-lg border border-blue-100 bg-blue-50/70 p-3 text-xs text-blue-900 flex items-start gap-2.5">
              <Info className="h-4 w-4 text-blue-600 shrink-0 mt-0.5" />
              <div className="space-y-1 text-slate-700">
                <p className="font-semibold text-blue-900">
                  Tin nhắn đã được ghi nhận trong giao diện thử nghiệm.
                </p>
                <p className="text-[12px] leading-relaxed">
                  Hệ thống hiện tại chưa tích hợp LLM hoặc RAG để phân tích nội dung hay đọc hiểu tài liệu. Sau khi nhóm hoàn tất thiết kế giao diện, tính năng kết nối mô hình ngôn ngữ lớn (Gemini / OpenAI / Ollama) và kho tri thức Vector DB sẽ được bổ sung độc lập ở giai đoạn tiếp theo.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
