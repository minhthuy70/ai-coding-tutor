'use client';

import React, { useState, useEffect, useRef } from 'react';
import { 
  User, 
  Bot, 
  Check, 
  Copy, 
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
  Sparkles,
  Play,
  AlertTriangle,
  ShieldCheck
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
  onRunCode?: (code: string, language: string) => void;
  onOpenCodeQuality?: (code: string, language: string) => void;
}

// Map language names to accent colors
const LANG_COLORS: Record<string, { bg: string; text: string; border: string }> = {
  python:     { bg: 'bg-blue-950',   text: 'text-blue-300',   border: 'border-blue-800' },
  javascript: { bg: 'bg-yellow-950', text: 'text-yellow-300', border: 'border-yellow-800' },
  typescript: { bg: 'bg-blue-950',   text: 'text-blue-300',   border: 'border-blue-800' },
  cpp:        { bg: 'bg-purple-950', text: 'text-purple-300', border: 'border-purple-800' },
  c:          { bg: 'bg-purple-950', text: 'text-purple-300', border: 'border-purple-800' },
  java:       { bg: 'bg-orange-950', text: 'text-orange-300', border: 'border-orange-800' },
  html:       { bg: 'bg-rose-950',   text: 'text-rose-300',   border: 'border-rose-800' },
  css:        { bg: 'bg-cyan-950',   text: 'text-cyan-300',   border: 'border-cyan-800' },
  sql:        { bg: 'bg-green-950',  text: 'text-green-300',  border: 'border-green-800' },
  bash:       { bg: 'bg-gray-900',   text: 'text-gray-300',   border: 'border-gray-700' },
  default:    { bg: 'bg-slate-900',  text: 'text-emerald-300', border: 'border-slate-700' },
};

function getLangStyle(lang: string) {
  return LANG_COLORS[lang.toLowerCase()] || LANG_COLORS.default;
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
  onRunCode,
  onOpenCodeQuality,
}) => {
  const [copied, setCopied] = useState(false);
  const [copiedCodeBlockIdx, setCopiedCodeBlockIdx] = useState<number | null>(null);
  const [reaction, setReaction] = useState<'like' | 'dislike' | null>(message.reaction || null);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isEditingUser, setIsEditingUser] = useState(false);
  const [editUserText, setEditUserText] = useState(message.content);
  const [hoveredCodeBlock, setHoveredCodeBlock] = useState<number | null>(null);

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
    const cleanText = message.content
      .replace(/```[\s\S]*?```/g, 'Đoạn mã lập trình.')
      .replace(/[*_#`]/g, '')
      .replace(/\n+/g, ' ');
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = 'vi-VN';
    utterance.rate = 1.05;
    utterance.pitch = 1.0;

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
  const formattedFullDate = new Date(message.timestamp).toLocaleString('vi-VN', {
    weekday: 'short',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });

  // Inline formatting: bold **text**, inline code `code`, italic _text_
  const formatInlineMarkdown = (text: string): React.ReactNode => {
    const parts = text.split(/(`[^`]+`|\*\*[^*]+\*\*|_[^_]+_)/g);
    return parts.map((part, idx) => {
      if (part.startsWith('`') && part.endsWith('`') && part.length > 2) {
        return (
          <code key={idx} className="rounded-md bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 px-1.5 py-0.5 font-mono text-[11.5px] text-blue-700 dark:text-blue-300 leading-none">
            {part.slice(1, -1)}
          </code>
        );
      }
      if (part.startsWith('**') && part.endsWith('**') && part.length > 4) {
        return (
          <strong key={idx} className="font-semibold text-slate-900 dark:text-slate-100">
            {part.slice(2, -2)}
          </strong>
        );
      }
      if (part.startsWith('_') && part.endsWith('_') && part.length > 2) {
        return (
          <em key={idx} className="italic text-slate-700 dark:text-slate-300">
            {part.slice(1, -1)}
          </em>
        );
      }
      return part;
    });
  };

  // Rich markdown parser for assistant and user text
  const renderFormattedContent = (content: string) => {
    const codeBlocks = content.split(/(```[\s\S]*?```)/g);

    return codeBlocks.map((block, bIdx) => {
      if (block.startsWith('```') && block.endsWith('```')) {
        const lines = block.slice(3, -3).trim().split('\n');
        const firstLine = lines[0].trim();
        const hasLang = /^[a-zA-Z0-9_+-]+$/.test(firstLine) && firstLine.length < 20;
        const language = hasLang ? firstLine : 'code';
        const codeText = hasLang ? lines.slice(1).join('\n') : lines.join('\n');
        const langStyle = getLangStyle(language);
        const isHovered = hoveredCodeBlock === bIdx;

        return (
          <div 
            key={bIdx} 
            className={`my-3.5 rounded-xl overflow-hidden border transition-all duration-200 ${langStyle.border} ${isHovered ? 'shadow-lg shadow-black/20' : 'shadow-md shadow-black/10'}`}
            onMouseEnter={() => setHoveredCodeBlock(bIdx)}
            onMouseLeave={() => setHoveredCodeBlock(null)}
          >
            {/* Code Header */}
            <div className={`flex items-center justify-between px-4 py-2 ${langStyle.bg} border-b ${langStyle.border}`}>
              <div className="flex items-center gap-2">
                {/* Traffic light dots */}
                <div className="flex items-center gap-1.5">
                  <div className="h-2.5 w-2.5 rounded-full bg-rose-500/70" />
                  <div className="h-2.5 w-2.5 rounded-full bg-amber-500/70" />
                  <div className="h-2.5 w-2.5 rounded-full bg-emerald-500/70" />
                </div>
                <div className="h-3.5 w-px bg-white/10 mx-1" />
                <Terminal className="h-3.5 w-3.5 text-blue-400" />
                <span className={`text-[11px] font-bold uppercase tracking-widest ${langStyle.text}`}>{language}</span>
              </div>
              <div className="flex items-center gap-1.5">
                {/* Run button */}
                <button
                  type="button"
                  onClick={() => onRunCode?.(codeText, language)}
                  className="flex items-center gap-1 rounded-md bg-emerald-500/15 hover:bg-emerald-500/25 border border-emerald-500/30 px-2.5 py-1 text-[11px] text-emerald-400 hover:text-emerald-300 transition-all font-semibold"
                  title="Mở Interactive Code Sandbox & Chạy thử mã nguồn này"
                >
                  <Play className="h-3 w-3 fill-emerald-400" />
                  <span>Chạy</span>
                </button>
                {/* Code Quality button */}
                {onOpenCodeQuality && (
                  <button
                    type="button"
                    onClick={() => onOpenCodeQuality(codeText, language)}
                    className="flex items-center gap-1 rounded-md bg-indigo-500/15 hover:bg-indigo-500/25 border border-indigo-500/30 px-2.5 py-1 text-[11px] text-indigo-400 hover:text-indigo-300 transition-all font-semibold"
                    title="Đánh giá chất lượng mã nguồn, lỗi PEP 8, Big-O và gợi ý tối ưu"
                  >
                    <ShieldCheck className="h-3 w-3 text-indigo-400" />
                    <span>Soát lỗi</span>
                  </button>
                )}
                {/* Copy code */}
                <button
                  type="button"
                  onClick={() => handleCopyCode(codeText, bIdx)}
                  className="flex items-center gap-1 rounded-md px-2.5 py-1 text-[11px] text-slate-400 hover:text-white hover:bg-white/10 transition-all"
                >
                  {copiedCodeBlockIdx === bIdx ? (
                    <>
                      <Check className="h-3 w-3 text-emerald-400" />
                      <span className="text-emerald-400">Đã chép!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="h-3 w-3" />
                      <span>Sao chép</span>
                    </>
                  )}
                </button>
              </div>
            </div>
            {/* Code Body */}
            <pre className={`p-4 overflow-x-auto text-[12.5px] leading-relaxed bg-slate-950 ${langStyle.text}`}>
              <code className="font-mono">{codeText}</code>
            </pre>
          </div>
        );
      }

      // Parse lines for headers, bullet lists, blockquotes, numbered lists
      const lines = block.split('\n');
      return (
        <div key={bIdx} className="space-y-1.5">
          {lines.map((line, lIdx) => {
            // Header 3
            if (line.startsWith('### ')) {
              return <h3 key={lIdx} className="text-sm font-bold text-slate-900 dark:text-slate-100 mt-3 mb-1">{formatInlineMarkdown(line.slice(4))}</h3>;
            }
            // Header 2
            if (line.startsWith('## ')) {
              return <h2 key={lIdx} className="text-base font-bold text-slate-900 dark:text-slate-100 mt-4 mb-1 pb-1 border-b border-slate-200 dark:border-slate-800">{formatInlineMarkdown(line.slice(3))}</h2>;
            }
            // Header 1
            if (line.startsWith('# ')) {
              return <h1 key={lIdx} className="text-lg font-extrabold text-slate-900 dark:text-slate-100 mt-4 mb-1.5">{formatInlineMarkdown(line.slice(2))}</h1>;
            }
            // Numbered list
            const numberedMatch = line.match(/^(\d+)\. (.+)/);
            if (numberedMatch) {
              return (
                <div key={lIdx} className="flex items-start gap-2.5 pl-1">
                  <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-blue-100 dark:bg-blue-950/60 text-blue-700 dark:text-blue-400 font-bold text-[10px] mt-0.5">
                    {numberedMatch[1]}
                  </span>
                  <span className="leading-relaxed">{formatInlineMarkdown(numberedMatch[2])}</span>
                </div>
              );
            }
            // Bullet list item
            if (line.startsWith('- ') || line.startsWith('* ')) {
              return (
                <div key={lIdx} className="flex items-start gap-2 pl-1">
                  <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-blue-500 dark:bg-blue-400" />
                  <span className="leading-relaxed">{formatInlineMarkdown(line.slice(2))}</span>
                </div>
              );
            }
            // Blockquote
            if (line.startsWith('> ')) {
              return (
                <blockquote key={lIdx} className="border-l-[3px] border-blue-500 pl-3.5 py-1 text-slate-600 dark:text-slate-300 italic bg-blue-50/40 dark:bg-blue-950/30 rounded-r-xl">
                  {formatInlineMarkdown(line.slice(2))}
                </blockquote>
              );
            }
            // Horizontal rule
            if (line.trim() === '---' || line.trim() === '***') {
              return <hr key={lIdx} className="my-3 border-t border-slate-200 dark:border-slate-800" />;
            }
            // Empty line becomes spacer
            if (line.trim() === '') {
              return <div key={lIdx} className="h-1.5" />;
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

  return (
    <div
      className={`group w-full py-5 px-4 md:px-8 transition-all duration-150 ${
        isUser 
          ? 'bg-white dark:bg-slate-950 hover:bg-slate-50/50 dark:hover:bg-slate-950/80' 
          : 'bg-slate-50/80 dark:bg-slate-900/50 border-y border-slate-100 dark:border-slate-800/60'
      }`}
    >
      <div className="max-w-4xl mx-auto flex gap-4 items-start">
        {/* Avatar */}
        <div
          className={`relative h-9 w-9 rounded-full flex items-center justify-center shrink-0 text-white font-medium shadow-md transition-transform duration-150 group-hover:scale-105 ${
            isUser 
              ? 'bg-gradient-to-br from-slate-600 to-slate-800 dark:from-slate-500 dark:to-slate-700 ring-2 ring-slate-200 dark:ring-slate-700' 
              : 'bg-gradient-to-br from-blue-500 to-indigo-600 ring-2 ring-blue-100 dark:ring-blue-900/50'
          }`}
          aria-hidden="true"
        >
          {isUser ? <User className="h-4.5 w-4.5" /> : <Bot className="h-4.5 w-4.5" />}
          {/* Online indicator for AI */}
          {!isUser && !message.isStreaming && (
            <span className="absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-emerald-400 border-2 border-white dark:border-slate-950" />
          )}
          {!isUser && message.isStreaming && (
            <span className="absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-blue-400 border-2 border-white dark:border-slate-950 animate-pulse" />
          )}
        </div>

        {/* Content Body */}
        <div className="flex-1 min-w-0 space-y-2.5">
          {/* Header Row */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-900 dark:text-slate-100">
                {isUser ? 'Bạn' : 'Trợ lý AI'}
              </span>
              {!isUser && (
                <span className="inline-flex items-center gap-1 rounded-full bg-blue-50 dark:bg-blue-950/50 border border-blue-200/80 dark:border-blue-800/60 px-2 py-0.5 text-[10px] font-semibold text-blue-600 dark:text-blue-400">
                  <Sparkles className="h-2.5 w-2.5" />
                  AI
                </span>
              )}
              <span 
                className="text-[11px] text-slate-400 dark:text-slate-500 flex items-center gap-1 cursor-default" 
                title={formattedFullDate}
              >
                <Clock className="h-3 w-3" />
                {formattedTime}
              </span>
            </div>

            {/* Top Right Quick Actions */}
            <div className="flex items-center gap-0.5 opacity-0 group-hover:opacity-100 transition-all duration-150">
              {isUser && onEditUserMessage && !isEditingUser && (
                <button
                  type="button"
                  onClick={() => { setEditUserText(message.content); setIsEditingUser(true); }}
                  className="rounded-lg p-1.5 text-slate-400 hover:bg-blue-50 dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 transition-all"
                  title="Chỉnh sửa câu hỏi này"
                >
                  <Edit2 className="h-3.5 w-3.5" />
                </button>
              )}
              {onDeleteMessage && (
                <button
                  type="button"
                  onClick={() => onDeleteMessage(message.id)}
                  className="rounded-lg p-1.5 text-slate-400 hover:bg-rose-50 dark:hover:bg-slate-800 hover:text-rose-500 dark:hover:text-rose-400 transition-all"
                  title="Xóa tin nhắn này"
                >
                  <Trash2 className="h-3.5 w-3.5" />
                </button>
              )}
              <button
                type="button"
                onClick={handleCopyMessage}
                className="rounded-lg p-1.5 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 transition-all"
                title="Sao chép nội dung"
              >
                {copied ? <Check className="h-3.5 w-3.5 text-emerald-500" /> : <Copy className="h-3.5 w-3.5" />}
              </button>
            </div>
          </div>

          {/* User Message Editing Mode */}
          {isUser && isEditingUser ? (
            <div className="space-y-2.5 pt-1">
              <textarea
                value={editUserText}
                onChange={(e) => setEditUserText(e.target.value)}
                rows={3}
                className="w-full rounded-xl border border-blue-400 bg-white dark:bg-slate-800 p-3 text-sm text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-blue-500/20 resize-none transition-all"
                autoFocus
              />
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={handleSaveUserEdit}
                  className="btn-primary text-xs py-1.5 px-3"
                >
                  Cập nhật & Gửi lại
                </button>
                <button
                  type="button"
                  onClick={() => setIsEditingUser(false)}
                  className="rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-1.5 text-xs font-medium text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition-all"
                >
                  Hủy
                </button>
              </div>
            </div>
          ) : (
            /* Regular Message Text */
            message.content && (
              <div className="text-sm text-slate-800 dark:text-slate-200 break-words leading-relaxed">
                {renderFormattedContent(message.content)}
                {message.isStreaming && (
                  <span className="inline-block w-[3px] h-4 ml-1 bg-blue-500 animate-pulse rounded-sm align-middle" />
                )}
              </div>
            )
          )}

          {/* Attachments Section */}
          {message.attachments && message.attachments.length > 0 && (
            <div className="space-y-1.5 pt-1">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-600 dark:text-slate-400">
                <FileCheck className="h-3.5 w-3.5 text-blue-500" />
                <span>Tệp đính kèm ({message.attachments.length}):</span>
              </div>
              <div className="flex flex-wrap gap-2 pt-0.5">
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

          {/* Assistant Action Bar */}
          {!isUser && !message.isStreaming && (
            <div className="mt-3 rounded-2xl border border-slate-200/80 dark:border-slate-700/60 bg-gradient-to-br from-slate-50 to-white dark:from-slate-800/60 dark:to-slate-800/40 p-3.5 shadow-sm">
              {/* Demo notice */}
              <div className="flex items-start gap-2.5 mb-3">
                <div className="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg bg-amber-100 dark:bg-amber-950/50">
                  <AlertTriangle className="h-3.5 w-3.5 text-amber-600 dark:text-amber-400" />
                </div>
                <div>
                  <p className="text-xs font-semibold text-slate-700 dark:text-slate-300 leading-snug">
                    Giao diện thử nghiệm
                  </p>
                  <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed mt-0.5">
                    Chưa kết nối LLM/RAG. Sau khi hoàn thiện UI, sẽ tích hợp Gemini, OpenAI và Vector DB.
                  </p>
                </div>
              </div>

              {/* Action Toolbar */}
              <div className="flex flex-wrap items-center justify-between gap-2 pt-2.5 border-t border-slate-200 dark:border-slate-700/60">
                <div className="flex items-center gap-1">
                  {/* Copy Button */}
                  <button
                    type="button"
                    onClick={handleCopyMessage}
                    className="flex items-center gap-1.5 rounded-xl border border-blue-200 dark:border-blue-800/60 bg-white dark:bg-slate-800 px-3 py-1.5 text-xs font-semibold text-blue-700 dark:text-blue-300 hover:bg-blue-50 dark:hover:bg-blue-950/30 shadow-sm transition-all active:scale-95"
                    title="Sao chép toàn bộ câu trả lời"
                  >
                    {copied ? (
                      <>
                        <Check className="h-3.5 w-3.5 text-emerald-500" />
                        <span className="text-emerald-600 dark:text-emerald-400">Đã sao chép!</span>
                      </>
                    ) : (
                      <>
                        <Copy className="h-3.5 w-3.5" />
                        <span>Sao chép</span>
                      </>
                    )}
                  </button>

                  {/* TTS Button */}
                  <button
                    type="button"
                    onClick={handleToggleSpeak}
                    className={`flex items-center gap-1.5 rounded-xl px-3 py-1.5 text-xs font-medium transition-all ${
                      isSpeaking
                        ? 'bg-blue-600 text-white shadow-md shadow-blue-500/25'
                        : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-700 hover:text-slate-900 dark:hover:text-slate-200'
                    }`}
                    title={isSpeaking ? 'Dừng đọc' : 'Đọc to câu trả lời'}
                  >
                    {isSpeaking ? (
                      <>
                        <VolumeX className="h-3.5 w-3.5 animate-pulse" />
                        <span>Dừng</span>
                      </>
                    ) : (
                      <>
                        <Volume2 className="h-3.5 w-3.5" />
                        <span className="hidden sm:inline">Đọc to</span>
                      </>
                    )}
                  </button>

                  {/* Regenerate Button */}
                  {isLastAssistantMessage && onRegenerate && (
                    <button
                      type="button"
                      onClick={onRegenerate}
                      className="flex items-center gap-1.5 rounded-xl px-3 py-1.5 text-xs font-medium text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-700 hover:text-slate-900 dark:hover:text-slate-200 transition-all"
                      title="Tạo lại câu trả lời mới"
                    >
                      <RotateCcw className="h-3.5 w-3.5" />
                      <span className="hidden sm:inline">Thử lại</span>
                    </button>
                  )}
                </div>

                {/* Reaction buttons */}
                <div className="flex items-center gap-1.5">
                  <span className="text-[11px] text-slate-400 dark:text-slate-500 hidden sm:inline">Đánh giá:</span>
                  <button
                    type="button"
                    onClick={() => handleReactionClick('like')}
                    className={`reaction-btn flex items-center gap-1 rounded-xl px-2.5 py-1.5 text-xs font-medium transition-all ${
                      reaction === 'like'
                        ? 'bg-blue-600 text-white shadow-sm shadow-blue-500/30'
                        : 'text-slate-500 dark:text-slate-400 hover:bg-blue-50 dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400'
                    }`}
                    title="Hữu ích"
                  >
                    <ThumbsUp className="h-3.5 w-3.5" />
                  </button>
                  <button
                    type="button"
                    onClick={() => handleReactionClick('dislike')}
                    className={`reaction-btn flex items-center gap-1 rounded-xl px-2.5 py-1.5 text-xs font-medium transition-all ${
                      reaction === 'dislike'
                        ? 'bg-rose-600 text-white shadow-sm shadow-rose-500/30'
                        : 'text-slate-500 dark:text-slate-400 hover:bg-rose-50 dark:hover:bg-slate-800 hover:text-rose-500 dark:hover:text-rose-400'
                    }`}
                    title="Cần cải thiện"
                  >
                    <ThumbsDown className="h-3.5 w-3.5" />
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Follow-up Suggestion Chips */}
          {!isUser && message.suggestedFollowUps && message.suggestedFollowUps.length > 0 && onSelectFollowUp && (
            <div className="pt-2">
              <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-400 dark:text-slate-500 mb-2">
                <CornerDownRight className="h-3 w-3 text-blue-500" />
                <span>Gợi ý câu hỏi tiếp theo:</span>
              </div>
              <div className="flex flex-wrap gap-2">
                {message.suggestedFollowUps.map((chip, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => onSelectFollowUp(chip)}
                    className="flex items-center gap-1.5 rounded-2xl border border-blue-200 dark:border-blue-800/60 bg-white dark:bg-slate-800 hover:bg-blue-50 dark:hover:bg-blue-950/30 hover:border-blue-400 dark:hover:border-blue-500 px-3 py-1.5 text-xs font-medium text-blue-700 dark:text-blue-300 shadow-sm transition-all active:scale-95 hover:-translate-y-0.5 text-left"
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
