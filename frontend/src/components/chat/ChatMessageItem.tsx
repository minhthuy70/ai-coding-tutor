'use client';

import React, { useState } from 'react';
import { 
  User, 
  Bot, 
  Check, 
  Copy, 
  Info, 
  Clock, 
  FileCheck,
  ThumbsUp,
  ThumbsDown,
  Terminal
} from 'lucide-react';
import { ChatMessage } from '@/types/chat';
import { AttachmentBadge } from './AttachmentBadge';

interface ChatMessageItemProps {
  message: ChatMessage;
  onViewImage?: (url: string, name: string) => void;
  onReaction?: (messageId: string, reaction: 'like' | 'dislike') => void;
}

export const ChatMessageItem: React.FC<ChatMessageItemProps> = ({ 
  message, 
  onViewImage,
  onReaction 
}) => {
  const [copied, setCopied] = useState(false);
  const [copiedCodeBlockIdx, setCopiedCodeBlockIdx] = useState<number | null>(null);
  const [reaction, setReaction] = useState<'like' | 'dislike' | null>(message.reaction || null);

  const isUser = message.role === 'user';

  const handleCopyMessage = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleCopyCode = (code: string, idx: number) => {
    navigator.clipboard.writeText(code);
    setCopiedCodeBlockIdx(idx);
    setTimeout(() => setCopiedCodeBlockIdx(null), 2000);
  };

  const handleReactionClick = (type: 'like' | 'dislike') => {
    const nextReaction = reaction === type ? null : type;
    setReaction(nextReaction);
    if (onReaction) {
      onReaction(message.id, type);
    }
  };

  const formattedTime = new Date(message.timestamp).toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
  });

  // Render markdown-like text with code blocks formatted cleanly
  const renderFormattedContent = (content: string) => {
    // Check if contains code blocks ```...```
    const parts = content.split(/(```[\s\S]*?```)/g);

    return parts.map((part, index) => {
      if (part.startsWith('```') && part.endsWith('```')) {
        // Extract language and code
        const lines = part.slice(3, -3).trim().split('\n');
        const firstLine = lines[0].trim();
        const hasLang = /^[a-zA-Z0-9_-]+$/.test(firstLine);
        const language = hasLang ? firstLine : 'code';
        const codeText = hasLang ? lines.slice(1).join('\n') : lines.join('\n');

        return (
          <div key={index} className="my-3 rounded-xl overflow-hidden border border-slate-800 bg-slate-900 shadow-md">
            <div className="flex items-center justify-between px-3.5 py-1.5 bg-slate-950 text-slate-400 text-xs font-mono border-b border-slate-800">
              <div className="flex items-center gap-1.5">
                <Terminal className="h-3.5 w-3.5 text-blue-400" />
                <span className="uppercase font-semibold tracking-wider text-[11px] text-slate-300">{language}</span>
              </div>
              <button
                type="button"
                onClick={() => handleCopyCode(codeText, index)}
                className="flex items-center gap-1 rounded px-2 py-0.5 text-[11px] text-slate-400 hover:text-white hover:bg-slate-800 transition"
              >
                {copiedCodeBlockIdx === index ? (
                  <>
                    <Check className="h-3 w-3 text-emerald-400" />
                    <span className="text-emerald-400">Đã chép</span>
                  </>
                ) : (
                  <>
                    <Copy className="h-3 w-3" />
                    <span>Sao chép</span>
                  </>
                )}
              </button>
            </div>
            <pre className="p-3.5 overflow-x-auto text-xs font-mono text-emerald-300 leading-relaxed">
              <code>{codeText}</code>
            </pre>
          </div>
        );
      }

      // Regular text
      return (
        <span key={index} className="whitespace-pre-wrap leading-relaxed">
          {part}
        </span>
      );
    });
  };

  return (
    <div
      className={`group w-full py-5 px-4 md:px-6 transition-colors animate-in fade-in duration-200 ${
        isUser ? 'bg-white' : 'bg-[#F9FAFB] border-y border-slate-100'
      }`}
    >
      <div className="max-w-4xl mx-auto flex gap-4 items-start">
        {/* Avatar */}
        <div
          className={`h-8 w-8 rounded-full flex items-center justify-center shrink-0 text-white font-medium shadow-xs ${
            isUser ? 'bg-slate-800 ring-2 ring-slate-200' : 'bg-blue-600 ring-2 ring-blue-100'
          }`}
          aria-hidden="true"
        >
          {isUser ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
        </div>

        {/* Content Body */}
        <div className="flex-1 min-w-0 space-y-2.5">
          {/* Header Row */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-900">
                {isUser ? 'Bạn' : 'Trợ lý AI (Chế độ Thử nghiệm)'}
              </span>
              <span className="text-[11px] text-slate-400 flex items-center gap-1">
                <Clock className="h-3 w-3" />
                {formattedTime}
              </span>
            </div>

            {/* Quick action copy button */}
            {message.content && (
              <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition">
                <button
                  type="button"
                  onClick={handleCopyMessage}
                  className="rounded-md p-1.5 text-slate-400 hover:bg-slate-200/60 hover:text-slate-700 transition"
                  title="Sao chép toàn bộ nội dung"
                  aria-label="Sao chép nội dung tin nhắn"
                >
                  {copied ? (
                    <Check className="h-3.5 w-3.5 text-emerald-600" />
                  ) : (
                    <Copy className="h-3.5 w-3.5" />
                  )}
                </button>
              </div>
            )}
          </div>

          {/* Text Content */}
          {message.content && (
            <div className="text-sm text-[#202123] break-words font-normal">
              {renderFormattedContent(message.content)}
            </div>
          )}

          {/* Attachments Section */}
          {message.attachments && message.attachments.length > 0 && (
            <div className="space-y-1.5 pt-1">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-600">
                <FileCheck className="h-3.5 w-3.5 text-blue-600" />
                <span>Tệp đính kèm ({message.attachments.length}):</span>
              </div>
              <div className="flex flex-wrap gap-2.5 pt-1">
                {message.attachments.map((att) => (
                  <AttachmentBadge
                    key={att.id}
                    attachment={att}
                    onViewImage={onViewImage}
                    readOnly
                  />
                ))}
              </div>
            </div>
          )}

          {/* Assistant Demo Status Banner (Mandatory Notice) */}
          {!isUser && (
            <div className="rounded-xl border border-blue-200/80 bg-blue-50/70 p-3.5 text-xs text-blue-900 shadow-2xs space-y-2 mt-2">
              <div className="flex items-start gap-2.5">
                <Info className="h-4 w-4 text-blue-600 shrink-0 mt-0.5" />
                <div className="space-y-1 text-slate-700">
                  <p className="font-semibold text-blue-900 text-xs">
                    Tin nhắn đã được ghi nhận trong giao diện thử nghiệm.
                  </p>
                  <p className="text-[12px] leading-relaxed text-slate-600">
                    Hệ thống hiện tại chưa tích hợp LLM hoặc RAG để phân tích nội dung hay đọc hiểu tài liệu. Sau khi nhóm hoàn tất thiết kế giao diện, tính năng kết nối mô hình ngôn ngữ lớn (Gemini / OpenAI / Ollama) và kho tri thức Vector DB sẽ được bổ sung độc lập ở giai đoạn tiếp theo.
                  </p>
                </div>
              </div>

              {/* Feedback reaction buttons */}
              <div className="flex items-center gap-2 pt-1 border-t border-blue-100">
                <span className="text-[11px] text-slate-400">Phản hồi giao diện:</span>
                <button
                  type="button"
                  onClick={() => handleReactionClick('like')}
                  className={`flex items-center gap-1 rounded-md px-2 py-0.5 text-[11px] font-medium transition ${
                    reaction === 'like'
                      ? 'bg-blue-600 text-white'
                      : 'text-slate-500 hover:bg-blue-100/60 hover:text-slate-700'
                  }`}
                  title="Hữu ích"
                >
                  <ThumbsUp className="h-3 w-3" />
                  <span>Tốt</span>
                </button>
                <button
                  type="button"
                  onClick={() => handleReactionClick('dislike')}
                  className={`flex items-center gap-1 rounded-md px-2 py-0.5 text-[11px] font-medium transition ${
                    reaction === 'dislike'
                      ? 'bg-rose-600 text-white'
                      : 'text-slate-500 hover:bg-rose-100/60 hover:text-slate-700'
                  }`}
                  title="Chưa tốt"
                >
                  <ThumbsDown className="h-3 w-3" />
                  <span>Cần cải thiện</span>
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
