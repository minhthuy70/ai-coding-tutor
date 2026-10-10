'use client';

import React, { useEffect } from 'react';
import { X, Copy, Check, FileText, Download } from 'lucide-react';
import { ChatAttachment } from '@/types/chat';

interface DocumentViewerModalProps {
  attachment: ChatAttachment | null;
  onClose: () => void;
}

export const DocumentViewerModal: React.FC<DocumentViewerModalProps> = ({
  attachment,
  onClose,
}) => {
  const [copied, setCopied] = React.useState(false);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (attachment) {
      window.addEventListener('keydown', handleKeyDown);
      document.body.style.overflow = 'hidden';
    }
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      document.body.style.overflow = 'auto';
    };
  }, [attachment, onClose]);

  if (!attachment) return null;

  const content = attachment.fileContent || '// Tệp này không có bản xem trước văn bản dạng thô.';
  const lines = content.split('\n');

  const handleCopy = () => {
    navigator.clipboard.writeText(content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = attachment.name;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4 animate-in fade-in duration-200"
      onClick={onClose}
    >
      <div
        className="relative flex flex-col h-[85vh] w-[90vw] max-w-4xl rounded-2xl border border-slate-700 bg-slate-900 shadow-2xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header Bar */}
        <div className="flex items-center justify-between border-b border-slate-800 bg-slate-950 px-4 py-3 text-slate-200">
          <div className="flex items-center gap-2.5 truncate">
            <div className="flex h-7 w-7 items-center justify-center rounded-lg bg-blue-600/20 text-blue-400 border border-blue-500/30">
              <FileText className="h-4 w-4" />
            </div>
            <span className="font-semibold text-sm truncate text-white">{attachment.name}</span>
            <span className="rounded bg-slate-800 px-2 py-0.5 text-[10px] text-slate-400">
              {lines.length} dòng
            </span>
          </div>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={handleCopy}
              className="flex items-center gap-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 px-2.5 py-1.5 text-xs text-slate-300 transition"
              title="Sao chép nội dung tệp"
            >
              {copied ? (
                <>
                  <Check className="h-3.5 w-3.5 text-emerald-400" />
                  <span className="text-emerald-400 font-semibold">Đã chép</span>
                </>
              ) : (
                <>
                  <Copy className="h-3.5 w-3.5" />
                  <span>Sao chép</span>
                </>
              )}
            </button>

            <button
              type="button"
              onClick={handleDownload}
              className="flex items-center gap-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 px-2.5 py-1.5 text-xs text-slate-300 transition"
              title="Tải tệp về máy"
            >
              <Download className="h-3.5 w-3.5" />
              <span className="hidden sm:inline">Tải về</span>
            </button>

            <button
              type="button"
              onClick={onClose}
              className="rounded-lg p-1.5 text-slate-400 hover:bg-rose-600 hover:text-white transition"
              title="Đóng (Esc)"
            >
              <X className="h-5 w-5" />
            </button>
          </div>
        </div>

        {/* Code Content with Line Numbers */}
        <div className="flex-1 overflow-auto p-4 font-mono text-xs text-emerald-300 leading-relaxed bg-slate-900/90 select-text">
          <div className="flex">
            {/* Line numbers column */}
            <div className="select-none pr-4 text-right text-slate-600 border-r border-slate-800 space-y-0.5">
              {lines.map((_, i) => (
                <div key={i}>{i + 1}</div>
              ))}
            </div>

            {/* Code lines */}
            <div className="pl-4 flex-1 whitespace-pre overflow-x-auto space-y-0.5">
              {lines.map((line, i) => (
                <div key={i} className="hover:bg-slate-800/40 px-1 rounded">
                  {line || ' '}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
