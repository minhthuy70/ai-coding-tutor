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
  Zap,
  BookOpen
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
    icon: HelpCircle,
    title: 'Phương pháp sư phạm Socratic',
    desc: 'Hỏi gợi mở từng bước, suy luận thuật toán mà không tiết lộ mã giải ngay lập tức',
    query: 'Tôi đang bị lỗi Segmentation Fault khi thao tác với con trỏ trong C++, bạn có thể gợi ý nguyên nhân giúp tôi không?',
    gradient: 'from-blue-500 to-indigo-600',
    badge: 'Socratic Tutor',
  },
  {
    icon: ImageIcon,
    title: 'Chụp / Dán ảnh màn hình Terminal',
    desc: 'Nhấn Ctrl + V để dán ảnh chụp màn hình lỗi Terminal biên dịch và chạy thử',
    query: 'Tôi vừa chụp màn hình thông báo lỗi Terminal, hãy phân tích ảnh đính kèm giúp tôi.',
    gradient: 'from-amber-500 to-rose-500',
    badge: 'Vision OCR',
  },
  {
    icon: FileText,
    title: 'Đính kèm tệp mã nguồn (.py, .cpp)',
    desc: 'Kéo thả hoặc tải lên tệp mã nguồn đầy đủ để trợ giảng phân tích bối cảnh',
    query: 'Tôi chuẩn bị gửi tệp mã nguồn để nhờ bạn xem giúp phần thuật toán.',
    gradient: 'from-emerald-500 to-teal-600',
    badge: 'Đa phương thức',
  },
  {
    icon: BookOpen,
    title: 'Tra cứu kiến thức chuẩn (RAG)',
    desc: 'Hỏi đáp các khái niệm CTDL & Giải thuật, tham chiếu từ 5,200+ chunks tài liệu',
    query: 'So sánh độ phức tạp thời gian và không gian giữa QuickSort và MergeSort trong trường hợp xấu nhất.',
    gradient: 'from-purple-500 to-violet-600',
    badge: 'RAG Knowledge',
  },
];

const TYPING_PHRASES = [
  'Hỏi bất kỳ điều gì về lập trình & giải thuật...',
  'Dán ảnh chụp màn hình terminal lỗi để phân tích...',
  'Kéo thả file code (.py, .cpp, .java) để trao đổi...',
  'Khám phá gợi mở theo phương pháp Socratic...',
];

interface WelcomeScreenProps {
  onSelectSuggestion?: (q: string) => void;
}

function WelcomeScreen({ onSelectSuggestion }: WelcomeScreenProps) {
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
      }, 50);
    } else if (!isDeleting && charIndex > phrase.length) {
      timeout = setTimeout(() => setIsDeleting(true), 2500);
    } else if (isDeleting && charIndex >= 0) {
      timeout = setTimeout(() => {
        setDisplayText(phrase.slice(0, charIndex));
        setCharIndex(c => c - 1);
      }, 25);
    } else if (isDeleting && charIndex < 0) {
      setIsDeleting(false);
      setCharIndex(0);
      setPhraseIndex(i => (i + 1) % TYPING_PHRASES.length);
    }

    return () => clearTimeout(timeout);
  }, [charIndex, isDeleting, phraseIndex]);

  return (
    <div className="flex-1 flex flex-col items-center justify-center px-4 py-8 select-none overflow-hidden max-w-3xl mx-auto w-full">
      {/* Hero Section */}
      <div className="flex flex-col items-center text-center w-full">
        {/* Logo */}
        <div className="mb-4">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-600 via-indigo-600 to-violet-600 text-white shadow-xl shadow-blue-500/20">
            <Sparkles className="h-7 w-7 drop-shadow-md" />
          </div>
        </div>

        {/* Title */}
        <div className="space-y-1">
          <h1 className="text-2xl md:text-3xl font-extrabold tracking-tight text-slate-900 dark:text-slate-100">
            Trợ giảng Lập trình <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">AI Socratic</span>
          </h1>
          <p className="text-xs md:text-sm text-slate-500 dark:text-slate-400 font-medium">
            Hướng dẫn tư duy từng bước · Đa phương thức Code, Văn bản & Ảnh lỗi Terminal
          </p>
        </div>

        {/* Typewriter subtitle */}
        <div className="mt-2.5 h-6 flex items-center justify-center">
          <p className="text-xs md:text-sm text-slate-600 dark:text-slate-300 font-medium">
            {displayText}
            <span className="inline-block w-0.5 h-3.5 bg-blue-500 ml-0.5 animate-pulse rounded-full" />
          </p>
        </div>

        {/* Badges */}
        <div className="mt-3.5 flex flex-wrap items-center justify-center gap-2">
          <span className="inline-flex items-center gap-1.5 rounded-full border border-blue-200/80 dark:border-blue-800/60 bg-blue-50/70 dark:bg-blue-950/40 px-2.5 py-0.5 text-[11px] font-semibold text-blue-700 dark:text-blue-300">
            <Bot className="h-3 w-3" />
            Socratic Method
          </span>
          <span className="inline-flex items-center gap-1.5 rounded-full border border-amber-200/80 dark:border-amber-800/60 bg-amber-50/70 dark:bg-amber-950/40 px-2.5 py-0.5 text-[11px] font-semibold text-amber-700 dark:text-amber-300">
            <Zap className="h-3 w-3" />
            Gemini 3 Flash & Vision OCR
          </span>
          <span className="inline-flex items-center gap-1.5 rounded-full border border-emerald-200/80 dark:border-emerald-800/60 bg-emerald-50/70 dark:bg-emerald-950/40 px-2.5 py-0.5 text-[11px] font-semibold text-emerald-700 dark:text-emerald-300">
            <BookOpen className="h-3 w-3" />
            ChromaDB RAG (5,230 chunks)
          </span>
        </div>
      </div>

      {/* Suggestion Cards Grid */}
      <div className="mt-7 grid grid-cols-1 sm:grid-cols-2 gap-3 w-full">
        {suggestions.map((item, idx) => {
          const Icon = item.icon;
          return (
            <button
              key={idx}
              type="button"
              onClick={() => onSelectSuggestion && onSelectSuggestion(item.query)}
              className="group relative flex flex-col justify-between rounded-xl border border-slate-200/80 dark:border-slate-800/80 bg-white/80 dark:bg-slate-800/60 hover:bg-slate-50 dark:hover:bg-slate-800 p-3.5 text-left transition-all hover:border-blue-400 dark:hover:border-blue-500 shadow-2xs hover:shadow-xs"
            >
              <div className="flex items-center justify-between mb-2">
                <div className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-gradient-to-br ${item.gradient} text-white shadow-xs`}>
                  <Icon className="h-4 w-4" />
                </div>
                <span className="text-[10px] font-bold text-slate-400 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded-full">
                  {item.badge}
                </span>
              </div>

              <div className="flex-1">
                <p className="text-xs font-bold text-slate-800 dark:text-slate-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors mb-1">
                  {item.title}
                </p>
                <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed line-clamp-2">
                  {item.desc}
                </p>
              </div>

              <div className="mt-2.5 flex items-center gap-1 text-[11px] font-semibold text-blue-600 dark:text-blue-400 opacity-0 group-hover:opacity-100 transition-opacity">
                <span>Bắt đầu ngay</span>
                <ArrowRight className="h-3 w-3" />
              </div>
            </button>
          );
        })}
      </div>

      {/* Bottom hint */}
      <p className="mt-6 text-[11px] text-slate-400 dark:text-slate-500 text-center">
        💡 Nhấn <kbd className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-[10px]">Ctrl + /</kbd> để xem phím tắt • Kéo thả tệp code hoặc nhấn <kbd className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-[10px]">Ctrl + V</kbd> để dán ảnh lỗi Terminal
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
    return (
      <WelcomeScreen 
        onSelectSuggestion={onSelectSuggestion} 
      />
    );
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
          <div className="w-full py-4 px-4 md:px-6">
            <div className="max-w-4xl mx-auto flex items-start gap-3">
              {/* Avatar */}
              <div className="relative h-8 w-8 rounded-full bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center text-white shrink-0 shadow-sm">
                <Bot className="h-4 w-4" />
                <span className="absolute inset-0 rounded-full bg-blue-500/20 animate-ping" />
              </div>

              {/* Bubble */}
              <div className="flex items-center gap-2 px-3.5 py-2.5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs">
                <span className="typing-dot text-blue-500" />
                <span className="typing-dot text-blue-500" />
                <span className="typing-dot text-blue-500" />
                <span className="text-xs text-slate-400 dark:text-slate-500 ml-1 font-medium">Trợ giảng đang suy nghĩ câu hỏi gợi ý...</span>
              </div>
            </div>
          </div>
        )}

        <div ref={bottomRef} className="h-6" />
      </div>
    </div>
  );
};
