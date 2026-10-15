'use client';

import React, { useEffect, useRef, useState } from 'react';
import { 
  Sparkles, 
  HelpCircle, 
  FileText, 
  Image as ImageIcon, 
  Code2,
  Bot,
  ArrowRight,
  Zap
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

const suggestions = [
  {
    icon: Code2,
    title: 'Phân tích thuật toán & Đệ quy',
    desc: 'Đo độ phức tạp Big-O, phát hiện vòng lặp vô hạn và tối ưu mảng',
    query: 'Hãy phân tích độ phức tạp thời gian và không gian của thuật toán QuickSort.',
    gradient: 'from-blue-500 via-blue-600 to-indigo-600',
    glow: 'rgba(59,130,246,0.25)',
    badge: 'Thuật toán',
    delay: 'delay-100',
  },
  {
    icon: FileText,
    title: 'Đính kèm tài liệu đề bài & code',
    desc: 'Tải tệp .pdf, .docx, .py, .cpp để làm cơ sở tri thức cho RAG',
    query: 'Tôi chuẩn bị tải lên tài liệu đề bài thực hành môn Cấu trúc dữ liệu để làm bối cảnh.',
    gradient: 'from-emerald-500 via-teal-500 to-cyan-600',
    glow: 'rgba(16,185,129,0.25)',
    badge: 'Đa phương thức',
    delay: 'delay-200',
  },
  {
    icon: ImageIcon,
    title: 'Dán ảnh màn hình (Ctrl + V)',
    desc: 'Chụp màn hình lỗi Terminal rồi nhấn Ctrl + V để tải lên ngay',
    query: 'Tôi vừa chụp ảnh màn hình lỗi Segmentation Fault (core dumped), hãy xem ảnh đính kèm giúp tôi.',
    gradient: 'from-amber-500 via-orange-500 to-rose-500',
    glow: 'rgba(245,158,11,0.25)',
    badge: 'Vision AI',
    delay: 'delay-300',
  },
  {
    icon: HelpCircle,
    title: 'Phương pháp sư phạm Socratic',
    desc: 'Hỏi gợi mở từng bước, không đưa trực tiếp mã nguồn giải sẵn',
    query: 'Làm thế nào để phát hiện rò rỉ bộ nhớ (memory leak) khi dùng malloc/free trong C?',
    gradient: 'from-purple-500 via-violet-500 to-pink-600',
    glow: 'rgba(139,92,246,0.25)',
    badge: 'Socratic',
    delay: 'delay-400',
  },
];

const TYPING_PHRASES = [
  'Hỏi bất kỳ điều gì về lập trình...',
  'Phân tích code của bạn với AI...',
  'Giải thích thuật toán từng bước...',
  'Debug lỗi thông minh với Socratic...',
  'Tối ưu Big-O complexity ngay...',
];

function WelcomeScreen({ onSelectSuggestion }: { onSelectSuggestion?: (q: string) => void }) {
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [displayText, setDisplayText] = useState('');
  const [isDeleting, setIsDeleting] = useState(false);
  const [charIndex, setCharIndex] = useState(0);

  // Typewriter effect
  useEffect(() => {
    const phrase = TYPING_PHRASES[phraseIndex];
    let timeout: ReturnType<typeof setTimeout>;

    if (!isDeleting && charIndex <= phrase.length) {
      timeout = setTimeout(() => {
        setDisplayText(phrase.slice(0, charIndex));
        setCharIndex(c => c + 1);
      }, 55);
    } else if (!isDeleting && charIndex > phrase.length) {
      timeout = setTimeout(() => setIsDeleting(true), 2000);
    } else if (isDeleting && charIndex >= 0) {
      timeout = setTimeout(() => {
        setDisplayText(phrase.slice(0, charIndex));
        setCharIndex(c => c - 1);
      }, 28);
    } else if (isDeleting && charIndex < 0) {
      setIsDeleting(false);
      setCharIndex(0);
      setPhraseIndex(i => (i + 1) % TYPING_PHRASES.length);
    }

    return () => clearTimeout(timeout);
  }, [charIndex, isDeleting, phraseIndex]);

  return (
    <div className="flex-1 flex flex-col items-center justify-center px-4 py-10 select-none overflow-hidden">
      {/* Ambient Background Orbs */}
      <div className="pointer-events-none fixed inset-0 overflow-hidden" aria-hidden>
        <div className="absolute top-1/4 left-1/4 w-80 h-80 bg-blue-500/5 dark:bg-blue-500/8 rounded-full blur-3xl animate-float" style={{ animationDelay: '0s' }} />
        <div className="absolute top-1/3 right-1/4 w-64 h-64 bg-indigo-500/5 dark:bg-indigo-500/8 rounded-full blur-3xl animate-float" style={{ animationDelay: '1.5s' }} />
        <div className="absolute bottom-1/3 left-1/3 w-72 h-72 bg-violet-500/4 dark:bg-violet-500/6 rounded-full blur-3xl animate-float" style={{ animationDelay: '3s' }} />
      </div>

      {/* Hero Section */}
      <div className="relative flex flex-col items-center text-center max-w-2xl w-full">
        {/* Animated Logo */}
        <div className="welcome-orb mb-6 animate-fade-in">
          <div className="welcome-orb-inner relative flex h-20 w-20 items-center justify-center rounded-3xl bg-gradient-to-br from-blue-600 via-indigo-600 to-violet-600 text-white shadow-2xl glow-indigo">
            {/* Rotating ring */}
            <div className="absolute inset-0 rounded-3xl border-2 border-white/20 animate-spin-slow" style={{ borderTopColor: 'rgba(255,255,255,0.6)' }} />
            <Sparkles className="h-9 w-9 relative z-10 drop-shadow-lg" />
          </div>
        </div>

        {/* Title */}
        <div className="animate-fade-in delay-75 space-y-2">
          <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight">
            <span className="gradient-text">AI Coding Tutor</span>
          </h1>
          <p className="text-slate-500 dark:text-slate-400 text-sm font-medium">
            Trợ lý lập trình thế hệ mới · Phương pháp Socratic
          </p>
        </div>

        {/* Typewriter subtitle */}
        <div className="mt-4 animate-fade-in delay-150 h-8 flex items-center justify-center">
          <p className="text-sm text-slate-600 dark:text-slate-300 font-medium">
            {displayText}
            <span className="inline-block w-0.5 h-4 bg-blue-500 ml-0.5 animate-pulse rounded-full" />
          </p>
        </div>

        {/* Stats pills */}
        <div className="mt-5 animate-fade-in delay-200 flex flex-wrap items-center justify-center gap-2">
          {[
            { icon: Zap, label: 'Multimodal AI', color: 'text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/50 border-amber-200 dark:border-amber-800/60' },
            { icon: Code2, label: 'Code Sandbox', color: 'text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/50 border-blue-200 dark:border-blue-800/60' },
            { icon: Bot, label: 'Socratic Hints', color: 'text-violet-600 dark:text-violet-400 bg-violet-50 dark:bg-violet-950/50 border-violet-200 dark:border-violet-800/60' },
          ].map(({ icon: Icon, label, color }) => (
            <span key={label} className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-semibold ${color}`}>
              <Icon className="h-3.5 w-3.5" />
              {label}
            </span>
          ))}
        </div>
      </div>

      {/* Suggestion Cards Grid */}
      <div className="mt-10 grid grid-cols-1 sm:grid-cols-2 gap-3 w-full max-w-2xl">
        {suggestions.map((item, idx) => {
          const Icon = item.icon;
          return (
            <button
              key={idx}
              type="button"
              onClick={() => onSelectSuggestion && onSelectSuggestion(item.query)}
              className={`suggestion-card group relative flex flex-col justify-between rounded-2xl border border-slate-200/80 dark:border-slate-700/60 bg-white/90 dark:bg-slate-800/80 p-4 text-left focus:outline-none focus-ring animate-fade-in-up ${item.delay}`}
              style={{ 
                boxShadow: '0 1px 3px 0 rgb(0 0 0 / 0.06)',
              }}
              onMouseEnter={e => {
                (e.currentTarget as HTMLElement).style.boxShadow = `0 12px 32px -6px ${item.glow}, 0 4px 10px -4px rgb(0 0 0 / 0.08)`;
              }}
              onMouseLeave={e => {
                (e.currentTarget as HTMLElement).style.boxShadow = '0 1px 3px 0 rgb(0 0 0 / 0.06)';
              }}
            >
              {/* Badge */}
              <div className="flex items-center justify-between mb-3">
                <div className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br ${item.gradient} text-white shadow-md`}>
                  <Icon className="h-4.5 w-4.5" />
                </div>
                <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400 dark:text-slate-500 bg-slate-100 dark:bg-slate-900 px-2 py-0.5 rounded-full">
                  {item.badge}
                </span>
              </div>

              <div className="flex-1">
                <p className="text-xs font-bold text-slate-800 dark:text-slate-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors leading-snug mb-1.5">
                  {item.title}
                </p>
                <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed line-clamp-2">
                  {item.desc}
                </p>
              </div>

              {/* Hover arrow */}
              <div className="mt-3 flex items-center gap-1 text-[11px] font-semibold text-blue-600 dark:text-blue-400 opacity-0 group-hover:opacity-100 transition-all -translate-x-1 group-hover:translate-x-0">
                <span>Thử ngay</span>
                <ArrowRight className="h-3 w-3" />
              </div>
            </button>
          );
        })}
      </div>

      {/* Bottom hint */}
      <p className="mt-8 animate-fade-in delay-500 text-[11px] text-slate-400 dark:text-slate-600 text-center">
        💡 Nhấn <kbd className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-[10px]">Ctrl+/</kbd> để xem phím tắt • Kéo thả file để đính kèm
      </p>
    </div>
  );
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
    return <WelcomeScreen onSelectSuggestion={onSelectSuggestion} />;
  }

  return (
    <div className="flex-1 overflow-y-auto scroll-smooth">
      <div className="flex flex-col">
        {messages.map((msg, idx) => (
          <div 
            key={msg.id} 
            className="animate-message-in"
            style={{ animationDelay: `${Math.min(idx * 30, 200)}ms` }}
          >
            <ChatMessageItem
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
          </div>
        ))}

        {/* Typing Indicator */}
        {isGenerating && (
          <div className="w-full py-5 px-4 md:px-6 animate-fade-in">
            <div className="max-w-4xl mx-auto flex items-start gap-4">
              {/* Avatar */}
              <div className="relative h-9 w-9 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white shrink-0 shadow-md glow-blue">
                <Bot className="h-4.5 w-4.5" />
                {/* Pulsing ring */}
                <span className="absolute inset-0 rounded-full bg-blue-500/30 animate-ping" style={{ animationDuration: '1.5s' }} />
              </div>

              {/* Bubble */}
              <div className="flex items-center gap-2 px-4 py-3 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm">
                <span className="typing-dot text-blue-500" />
                <span className="typing-dot text-blue-500" />
                <span className="typing-dot text-blue-500" />
                <span className="text-xs text-slate-400 dark:text-slate-500 ml-1.5 font-medium">Đang tạo câu trả lời...</span>
              </div>
            </div>
          </div>
        )}

        <div ref={bottomRef} className="h-6" />
      </div>
    </div>
  );
};
