'use client';

import React, { useEffect } from 'react';
import { X, Download, ZoomIn } from 'lucide-react';

interface ImageLightboxProps {
  imageUrl: string | null;
  imageName: string | null;
  onClose: () => void;
}

export const ImageLightbox: React.FC<ImageLightboxProps> = ({
  imageUrl,
  imageName,
  onClose,
}) => {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    if (imageUrl) {
      window.addEventListener('keydown', handleKeyDown);
      document.body.style.overflow = 'hidden';
    }
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      document.body.style.overflow = 'auto';
    };
  }, [imageUrl, onClose]);

  if (!imageUrl) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4 animate-in fade-in duration-200"
      onClick={onClose}
    >
      <div
        className="relative max-h-[90vh] max-w-[90vw] flex flex-col items-center"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Top Control Bar */}
        <div className="absolute -top-12 left-0 right-0 flex items-center justify-between text-white px-2">
          <span className="text-sm font-medium truncate max-w-md text-slate-200" title={imageName || 'Hình ảnh'}>
            {imageName || 'Hình ảnh xem trước'}
          </span>
          <div className="flex items-center gap-2">
            <a
              href={imageUrl}
              download={imageName || 'screenshot.png'}
              className="flex h-9 w-9 items-center justify-center rounded-lg bg-white/10 hover:bg-white/20 text-white transition focus:outline-none"
              title="Tải ảnh về máy"
            >
              <Download className="h-4 w-4" />
            </a>
            <button
              type="button"
              onClick={onClose}
              className="flex h-9 w-9 items-center justify-center rounded-lg bg-white/10 hover:bg-rose-600 text-white transition focus:outline-none"
              title="Đóng (Esc)"
            >
              <X className="h-5 w-5" />
            </button>
          </div>
        </div>

        {/* The Image */}
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          src={imageUrl}
          alt={imageName || 'Xem trước'}
          className="max-h-[85vh] max-w-[88vw] rounded-xl object-contain shadow-2xl border border-white/10"
        />
      </div>
    </div>
  );
};
