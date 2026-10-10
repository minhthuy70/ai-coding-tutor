'use client';

import React, { useState, useEffect } from 'react';
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
  Terminal, 
  Volume2, 
  VolumeX, 
  RotateCcw,
  Edit2,
  Trash2,
  CornerDownRight,
  Sparkles
} from 'lucide-react';
import { ChatMessage, ChatAttachment } from '@/types/chat';
import { AttachmentBadge } from './AttachmentBadge';

interface ChatMessageItemProps {
  message: ChatMessage;
  isLastAssistantMessage?: boolean;
  onViewImage?: (url: string, name: string) => void;
  onViewDocument?: (attachment: ChatAttachment) => void;
  onReaction?: (messageId: string, reaction: 'like' | 'dislike') => void;
  onRegenerate?: () => void;
  onDeleteMessage?: (id: string) => void;
  onEditUserMessage?: (id: string, newContent: string) => void;
  onSelectFollowUp?: (query: string) => void;
}

export const ChatMessageItem: React.FC<ChatMessageItemProps> = ({ 
  message, 
  isLastAssistantMessage = false,
  onViewImage,
  onViewDocument,
  onReaction,
  onRegenerate,
  onDeleteMessage,
  onEditUserMessage,
  onSelectFollowUp,
}) => {
  const [copied, setCopied] = useState(false);
  const [copiedCodeBlockIdx, setCopiedCodeBlockIdx] = useState<number | null>(null);
  const [reaction, setReaction] = useState<'like' | 'dislike' | null>(message.reaction || null);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isEditingUser, setIsEditingUser] = useState(false);
  const [editUserText, setEditUserText] = useState(message.content);

  const isUser = message.role === 'user';

  // Cleanup speech synthesis on unmount
  useEffect(() => {
    return () => {
      if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

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

  // Text-to-Speech (Web Speech API)
  const handleToggleSpeak = () => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) return;

    if (isSpeaking) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
      return;
    }

    window.speechSynthesis.cancel();
    const cleanText = message.content.replace(/```[\s\S]*?```/g, 'Đoạn mã lập trình.').replace(/[*_#]/g, '');
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = 'vi-VN';
    utterance.rate = 1.0;

    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);

    window.speechSynthesis.speak(utterance);
    setIsSpeaking(true);
  };

  const handleSaveUserEdit = () => {
    if (editUserText.trim() && onEditUserMessage) {
      onEditUserMessage(message.id, editUserText.trim());
      setIsEditingUser(false);
    }
  };

  const formattedTime = new Date(message.timestamp).toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
  });

  // Rich markdown parser for assistant and user text
  const renderFormattedContent = (content: string) => {
    const codeBlocks = content.split(/(```[\s\S]*?```)/g);

    return codeBlocks.map((block, bIdx) => {
      if (block.startsWith('```') && block.endsWith('```')) {
        const lines = block.slice(3, -3).trim().split('\n');
        const firstLine = lines[0].trim();
        const hasLang = /^[a-zA-Z0-9_-]+$/.test(firstLine);
        const language = hasLang ? firstLine : 'code';
        const codeText = hasLang ? lines.slice(1).join('\n') : lines.join('\n');

        return (
          <div key={bIdx} className="my-3 rounded-xl overflow-hidden border border-slate-800 bg-slate-900 shadow-md">
            <div className="flex items-center justify-between px-3.5 py-1.5 bg-slate-950 text-slate-400 text-xs font-mono border-b border-slate-800">
              <div className="flex items-center gap-1.5">
                <Terminal className="h-3.5 w-3.5 text-blue-400" />
                <span className="uppercase font-semibold tracking-wider text-[11px] text-slate-300">{language}</span>
              </div>
              <button
                type="button"
                onClick={() => handleCopyCode(codeText, bIdx)}
                className="flex items-center gap-1 rounded px-2 py-0.5 text-[11px] text-slate-400 hover:text-white hover:bg-slate-800 transition"
              >
                {copiedCodeBlockIdx === bIdx ? (
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

      // Parse lines for headers, bullet lists, blockquotes
      const lines = block.split('\n');
      return (
        <div key={bIdx} className="space-y-1.5">
          {lines.map((line, lIdx) => {
            // Header 3
            if (line.startsWith('### ')) {
              return <h3 key={lIdx} className="text-sm font-bold text-slate-900 mt-2">{line.slice(4)}</h3>;
            }
            // Header 2
            if (line.startsWith('## ')) {
              return <h2 key={lIdx} className="text-base font-bold text-slate-900 mt-2.5">{line.slice(3)}</h2>;
            }
            // Header 1
            if (line.startsWith('# ')) {
              return <h1 key={lIdx} className="text-lg font-extrabold text-slate-900 mt-3">{line.slice(2)}</h1>;
            }
            // Bullet list item
            if (line.startsWith('- ') || line.startsWith('* ')) {
              return (
                <div key={lIdx} className="flex items-start gap-2 pl-2">
                  <span className="text-blue-500 font-bold">•</span>
                  <span>{formatInlineMarkdown(line.slice(2))}</span>
                </div>
              );
            }
            // Blockquote
            if (line.startsWith('> ')) {
              return (
                <blockquote key={lIdx} className="border-l-3 border-blue-500 pl-3 py-0.5 text-slate-600 italic bg-blue-50/30 rounded-r-lg">
                  {formatInlineMarkdown(line.slice(2))}
                </blockquote>
              );
            }
            // Normal paragraph
            return (
              <p key={lIdx} className="leading-relaxed">
                {formatInlineMarkdown(line)}
              </p>
            );
          })}
        </div>
      );
    });
  };

  // Inline formatting: bold **text**, inline code `code`
  const formatInlineMarkdown = (text: string) => {
    const parts = text.split(/(`[^`]+`|\*\*[^*]+\*\*)/g);
    return parts.map((part, idx) => {
      if (part.startsWith('`') && part.endsWith('`')) {
        return (
          <code key={idx} className="rounded bg-slate-100 border border-slate-250 px-1 py-0.2 font-mono text-[12px] text-blue-700">
            {part.slice(1, -1)}
          </code>
        );
      }
      if (part.startsWith('**') && part.endsWith('**')) {
        return (
          <strong key={idx} className="font-semibold text-slate-900">
            {part.slice(2, -2)}
          </strong>
        );
      }
      return part;
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

            {/* Top Right Quick Actions (Copy, Edit, Delete) */}
            <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition">
              {isUser && onEditUserMessage && !isEditingUser && (
                <button
                  type="button"
                  onClick={() => {
                    setEditUserText(message.content);
                    setIsEditingUser(true);
                  }}
                  className="rounded-md p-1.5 text-slate-400 hover:bg-slate-100 hover:text-blue-600 transition"
                  title="Chỉnh sửa câu hỏi này"
                >
                  <Edit2 className="h-3.5 w-3.5" />
                </button>
              )}

              {onDeleteMessage && (
                <button
                  type="button"
                  onClick={() => onDeleteMessage(message.id)}
                  className="rounded-md p-1.5 text-slate-400 hover:bg-slate-100 hover:text-rose-600 transition"
                  title="Xóa tin nhắn này"
                >
                  <Trash2 className="h-3.5 w-3.5" />
                </button>
              )}

              <button
                type="button"
                onClick={handleCopyMessage}
                className="rounded-md p-1.5 text-slate-400 hover:bg-slate-100 hover:text-slate-700 transition"
                title="Sao chép nội dung"
              >
                {copied ? <Check className="h-3.5 w-3.5 text-emerald-600" /> : <Copy className="h-3.5 w-3.5" />}
              </button>
            </div>
          </div>

          {/* User Message Editing Mode */}
          {isUser && isEditingUser ? (
            <div className="space-y-2 pt-1">
              <textarea
                value={editUserText}
                onChange={(e) => setEditUserText(e.target.value)}
                rows={3}
                className="w-full rounded-xl border border-blue-400 bg-white p-3 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
              />
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={handleSaveUserEdit}
                  className="rounded-lg bg-blue-600 px-3 py-1.5 text-xs font-semibold text-white hover:bg-blue-700 transition"
                >
                  Cập nhật &amp; Gửi lại
                </button>
                <button
                  type="button"
                  onClick={() => setIsEditingUser(false)}
                  className="rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-medium text-slate-600 hover:bg-slate-50 transition"
                >
                  Hủy
                </button>
              </div>
            </div>
          ) : (
            /* Regular Message Text */
            message.content && (
              <div className="text-sm text-[#202123] break-words font-normal">
                {renderFormattedContent(message.content)}
              </div>
            )
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
                    onViewDocument={onViewDocument}
                    readOnly
                  />
                ))}
              </div>
            </div>
          )}

          {/* Assistant Action Bar & Demo Banner */}
          {!isUser && (
            <div className="rounded-xl border border-blue-200/80 bg-blue-50/70 p-3.5 text-xs text-blue-900 shadow-2xs space-y-2.5 mt-2">
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

              {/* Action Toolbar for AI Answer */}
              <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-blue-100">
                <div className="flex items-center gap-1.5">
                  {/* Copy Button */}
                  <button
                    type="button"
                    onClick={handleCopyMessage}
                    className="flex items-center gap-1.5 rounded-lg border border-blue-200 bg-white px-2.5 py-1 text-xs font-semibold text-blue-700 hover:bg-blue-50 hover:border-blue-300 shadow-2xs transition active:scale-95"
                    title="Sao chép toàn bộ câu trả lời của AI"
                  >
                    {copied ? (
                      <>
                        <Check className="h-3.5 w-3.5 text-emerald-600" />
                        <span className="text-emerald-700 font-bold">Đã sao chép!</span>
                      </>
                    ) : (
                      <>
                        <Copy className="h-3.5 w-3.5 text-blue-600" />
                        <span>Sao chép câu trả lời</span>
                      </>
                    )}
                  </button>

                  {/* Text-to-Speech Button */}
                  <button
                    type="button"
                    onClick={handleToggleSpeak}
                    className={`flex items-center gap-1 rounded-lg px-2 py-1 text-xs font-medium transition ${
                      isSpeaking
                        ? 'bg-blue-600 text-white font-semibold'
                        : 'text-slate-600 hover:bg-blue-100/60'
                    }`}
                    title={isSpeaking ? 'Dừng đọc' : 'Đọc to câu trả lời'}
                  >
                    {isSpeaking ? (
                      <>
                        <VolumeX className="h-3.5 w-3.5 animate-pulse" />
                        <span>Đang đọc...</span>
                      </>
                    ) : (
                      <>
                        <Volume2 className="h-3.5 w-3.5 text-slate-500" />
                        <span className="hidden sm:inline">Đọc to</span>
                      </>
                    )}
                  </button>

                  {/* Regenerate Button */}
                  {isLastAssistantMessage && onRegenerate && (
                    <button
                      type="button"
                      onClick={onRegenerate}
                      className="flex items-center gap-1 rounded-lg px-2 py-1 text-xs font-medium text-slate-600 hover:bg-blue-100/60 transition"
                      title="Tạo lại câu trả lời mới"
                    >
                      <RotateCcw className="h-3.5 w-3.5 text-slate-500" />
                      <span className="hidden sm:inline">Thử lại</span>
                    </button>
                  )}
                </div>

                {/* Reaction buttons */}
                <div className="flex items-center gap-1.5">
                  <span className="text-[11px] text-slate-400 hidden sm:inline">Đánh giá:</span>
                  <button
                    type="button"
                    onClick={() => handleReactionClick('like')}
                    className={`flex items-center gap-1 rounded-md px-2 py-1 text-xs font-medium transition ${
                      reaction === 'like'
                        ? 'bg-blue-600 text-white shadow-2xs'
                        : 'text-slate-500 hover:bg-blue-100/60 hover:text-slate-700'
                    }`}
                    title="Hữu ích"
                  >
                    <ThumbsUp className="h-3 w-3" />
                  </button>
                  <button
                    type="button"
                    onClick={() => handleReactionClick('dislike')}
                    className={`flex items-center gap-1 rounded-md px-2 py-1 text-xs font-medium transition ${
                      reaction === 'dislike'
                        ? 'bg-rose-600 text-white shadow-2xs'
                        : 'text-slate-500 hover:bg-rose-100/60 hover:text-slate-700'
                    }`}
                    title="Cần cải thiện"
                  >
                    <ThumbsDown className="h-3 w-3" />
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Follow-up Suggestion Prompt Chips */}
          {!isUser && message.suggestedFollowUps && message.suggestedFollowUps.length > 0 && onSelectFollowUp && (
            <div className="pt-2">
              <div className="flex items-center gap-1 text-[11px] font-semibold text-slate-400 mb-1.5">
                <CornerDownRight className="h-3 w-3 text-blue-500" />
                <span>Gợi ý câu hỏi tiếp theo:</span>
              </div>
              <div className="flex flex-wrap gap-1.5">
                {message.suggestedFollowUps.map((chip, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => onSelectFollowUp(chip)}
                    className="flex items-center gap-1 rounded-xl border border-blue-200 bg-white hover:bg-blue-50 hover:border-blue-400 px-3 py-1.5 text-xs font-medium text-blue-700 shadow-2xs transition active:scale-95 text-left"
                  >
                    <Sparkles className="h-3 w-3 text-blue-500 shrink-0" />
                    <span>{chip}</span>
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
