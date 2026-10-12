'use client';

import React from 'react';
import { 
  X, 
  BarChart3, 
  MessageSquare, 
  Coins, 
  Zap, 
  Code2, 
  Clock, 
  CheckCircle2, 
  Sparkles,
  Flame,
  ShieldCheck
} from 'lucide-react';
import { ChatConversation } from '@/types/chat';

interface AnalyticsModalProps {
  isOpen: boolean;
  onClose: () => void;
  conversations: ChatConversation[];
}

export const AnalyticsModal: React.FC<AnalyticsModalProps> = ({
  isOpen,
  onClose,
  conversations,
}) => {
  if (!isOpen) return null;

  // Aggregate stats from all conversations
  let totalMessages = 0;
  let userMessages = 0;
  let assistantMessages = 0;
  let totalCharacters = 0;
  let totalCodeBlocks = 0;

  conversations.forEach((conv) => {
    totalMessages += conv.messages.length;
    conv.messages.forEach((m) => {
      if (m.role === 'user') userMessages++;
      if (m.role === 'assistant') assistantMessages++;
      totalCharacters += m.content.length;
      
      const codeMatches = m.content.match(/```[\s\S]*?```/g);
      if (codeMatches) {
        totalCodeBlocks += codeMatches.length;
      }
    });
  });

  const estimatedTokens = Math.ceil(totalCharacters / 4);
  const promptTokens = Math.ceil(estimatedTokens * 0.4);
  const completionTokens = Math.ceil(estimatedTokens * 0.6);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-200">
      <div 
        className="relative flex flex-col w-full max-w-xl bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-slate-100 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-950">
          <div className="flex items-center gap-2.5">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-600 text-white shadow-xs">
              <BarChart3 className="h-5 w-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-slate-900 dark:text-slate-100">
                Thống Kê Hoạt Động & Ước Lượng Token
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                Dữ liệu phiên làm việc hiện tại và tài nguyên AI đã sử dụng
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Body Stats */}
        <div className="p-5 space-y-4 overflow-y-auto max-h-[75vh]">
          {/* Top 4 Metric Cards */}
          <div className="grid grid-cols-2 gap-3">
            <div className="p-3.5 rounded-xl border border-blue-100 dark:border-blue-900/60 bg-blue-50/50 dark:bg-blue-950/30">
              <div className="flex items-center justify-between text-blue-600 dark:text-blue-400 mb-1">
                <span className="text-xs font-semibold">Tổng cuộc trò chuyện</span>
                <MessageSquare className="h-4 w-4" />
              </div>
              <div className="text-2xl font-extrabold text-slate-900 dark:text-slate-100 font-mono">
                {conversations.length}
              </div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                {totalMessages} tin nhắn đã trao đổi
              </div>
            </div>

            <div className="p-3.5 rounded-xl border border-emerald-100 dark:border-emerald-900/60 bg-emerald-50/50 dark:bg-emerald-950/30">
              <div className="flex items-center justify-between text-emerald-600 dark:text-emerald-400 mb-1">
                <span className="text-xs font-semibold">Ước lượng Tokens</span>
                <Coins className="h-4 w-4" />
              </div>
              <div className="text-2xl font-extrabold text-slate-900 dark:text-slate-100 font-mono">
                {estimatedTokens.toLocaleString()}
              </div>
              <div className="text-[11px] text-emerald-600 dark:text-emerald-400 font-semibold mt-0.5">
                Chi phí: $0.00 (Miễn phí)
              </div>
            </div>

            <div className="p-3.5 rounded-xl border border-purple-100 dark:border-purple-900/60 bg-purple-50/50 dark:bg-purple-950/30">
              <div className="flex items-center justify-between text-purple-600 dark:text-purple-400 mb-1">
                <span className="text-xs font-semibold">Khối Code đã tạo</span>
                <Code2 className="h-4 w-4" />
              </div>
              <div className="text-2xl font-extrabold text-slate-900 dark:text-slate-100 font-mono">
                {totalCodeBlocks}
              </div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                Python, C++, JS, SQL
              </div>
            </div>

            <div className="p-3.5 rounded-xl border border-amber-100 dark:border-amber-900/60 bg-amber-50/50 dark:bg-amber-950/30">
              <div className="flex items-center justify-between text-amber-600 dark:text-amber-400 mb-1">
                <span className="text-xs font-semibold">Chuỗi học tập</span>
                <Flame className="h-4 w-4 text-amber-500" />
              </div>
              <div className="text-2xl font-extrabold text-slate-900 dark:text-slate-100 font-mono">
                3 Ngày 🔥
              </div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                Coding Streak hoạt động
              </div>
            </div>
          </div>

          {/* Token Breakdown Details */}
          <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-950/60 space-y-2.5">
            <h4 className="font-bold text-xs uppercase tracking-wider text-slate-700 dark:text-slate-300">
              Phân Bổ Token & Mô Hình
            </h4>
            
            <div className="space-y-1.5 text-xs">
              <div className="flex justify-between text-slate-600 dark:text-slate-400">
                <span>Prompt Input Tokens (Câu hỏi):</span>
                <span className="font-mono font-bold text-slate-800 dark:text-slate-200">~{promptTokens.toLocaleString()} tokens</span>
              </div>
              <div className="flex justify-between text-slate-600 dark:text-slate-400">
                <span>Completion Output Tokens (Phản hồi AI):</span>
                <span className="font-mono font-bold text-slate-800 dark:text-slate-200">~{completionTokens.toLocaleString()} tokens</span>
              </div>
              <div className="flex justify-between text-slate-600 dark:text-slate-400 border-t border-slate-200 dark:border-slate-800 pt-1.5">
                <span className="font-semibold text-slate-800 dark:text-slate-200">Mô hình AI mặc định:</span>
                <span className="font-bold text-blue-600 dark:text-blue-400">Google Gemini 1.5 Flash</span>
              </div>
            </div>

            {/* Visual Token Bar */}
            <div className="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-800 overflow-hidden flex mt-2">
              <div className="h-full bg-blue-500" style={{ width: '40%' }} title="Prompt: 40%" />
              <div className="h-full bg-emerald-500" style={{ width: '60%' }} title="Completion: 60%" />
            </div>
            <div className="flex justify-between text-[10px] text-slate-400">
              <span>● Prompt (40%)</span>
              <span>● Completion (60%)</span>
            </div>
          </div>

          {/* Socratic Pedagogy Badge */}
          <div className="flex items-center gap-3 p-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <ShieldCheck className="h-5 w-5 text-emerald-500 shrink-0" />
            <div className="text-xs">
              <span className="font-bold text-slate-800 dark:text-slate-200">Nguyên tắc Socratic được kích hoạt: </span>
              <span className="text-slate-500 dark:text-slate-400">
                Hệ thống ưu tiên đặt câu hỏi gợi mở, giúp bạn rèn luyện kỹ năng tự giải quyết vấn đề và tư duy thuật toán độc lập.
              </span>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-5 py-3 border-t border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 flex justify-end">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold transition"
          >
            Xong
          </button>
        </div>
      </div>
    </div>
  );
};
