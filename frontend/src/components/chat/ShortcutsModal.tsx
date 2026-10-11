'use client';

import React, { useEffect } from 'react';
import { X, Keyboard } from 'lucide-react';

interface ShortcutsModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const ShortcutsModal: React.FC<ShortcutsModalProps> = ({ isOpen, onClose }) => {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (isOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const shortcuts = [
    { key: 'Enter', desc: 'Gửi tin nhắn trong ô soạn thảo' },
    { key: 'Shift + Enter', desc: 'Xuống dòng trong ô soạn thảo' },
    { key: 'Ctrl + V', desc: 'Dán ảnh chụp màn hình trực tiếp từ clipboard' },
    { key: 'Ctrl + F', desc: 'Tìm kiếm tin nhắn trong cuộc hội thoại' },
    { key: 'Ctrl + Shift + O', desc: 'Tạo cuộc trò chuyện mới' },
    { key: 'Ctrl + B', desc: 'Thu gọn hoặc mở rộng thanh bên' },
    { key: 'Ctrl + /', desc: 'Mở trang phím tắt này' },
    { key: 'Esc', desc: 'Đóng modal xem ảnh, xem tệp hoặc hủy sửa' },
  ];

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/70 backdrop-blur-xs p-4 animate-in fade-in duration-150"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-md rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
          <div className="flex items-center gap-2 text-slate-900 dark:text-slate-100 font-bold text-sm">
            <Keyboard className="h-4.5 w-4.5 text-blue-600 dark:text-blue-400" />
            <span>Phím tắt thao tác nhanh</span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 transition"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        <div className="mt-4 space-y-2.5">
          {shortcuts.map((sc, i) => (
            <div key={i} className="flex items-center justify-between text-xs py-1">
              <span className="text-slate-600 dark:text-slate-300">{sc.desc}</span>
              <kbd className="rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 px-2 py-1 font-mono text-[11px] font-semibold text-slate-800 dark:text-slate-200 shadow-2xs">
                {sc.key}
              </kbd>
            </div>
          ))}
        </div>

        <div className="mt-5 pt-3 border-t border-slate-100 dark:border-slate-800 text-center">
          <button
            type="button"
            onClick={onClose}
            className="rounded-xl bg-blue-600 px-4 py-2 text-xs font-semibold text-white hover:bg-blue-700 transition shadow-xs"
          >
            Đã hiểu
          </button>
        </div>
      </div>
    </div>
  );
};
