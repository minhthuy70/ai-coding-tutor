'use client';

import React from 'react';
import { 
  FileText, 
  FileCode, 
  FileArchive, 
  File, 
  X, 
  Image as ImageIcon 
} from 'lucide-react';
import { ChatAttachment } from '@/types/chat';

interface AttachmentBadgeProps {
  attachment: ChatAttachment;
  onRemove?: (id: string) => void;
  readOnly?: boolean;
}

export function formatFileSize(bytes: number): string {
  if (bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(1))} ${sizes[i]}`;
}

export const AttachmentBadge: React.FC<AttachmentBadgeProps> = ({
  attachment,
  onRemove,
  readOnly = false,
}) => {
  const isImage = attachment.category === 'image' && attachment.previewUrl;

  const getDocIcon = () => {
    const ext = attachment.name.split('.').pop()?.toLowerCase();
    switch (ext) {
      case 'pdf':
        return <FileText className="h-5 w-5 text-rose-500" />;
      case 'py':
      case 'cpp':
      case 'c':
      case 'js':
      case 'ts':
      case 'html':
      case 'css':
      case 'json':
        return <FileCode className="h-5 w-5 text-indigo-500" />;
      case 'zip':
      case 'rar':
      case 'tar':
      case 'gz':
        return <FileArchive className="h-5 w-5 text-amber-500" />;
      default:
        return <File className="h-5 w-5 text-slate-500" />;
    }
  };

  if (isImage) {
    return (
      <div className="group relative flex items-center gap-2 rounded-lg border border-slate-200 bg-white p-1.5 shadow-sm transition hover:border-slate-300 max-w-[220px]">
        <div className="relative h-12 w-12 shrink-0 overflow-hidden rounded-md bg-slate-100 border border-slate-100">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={attachment.previewUrl}
            alt={attachment.name}
            className="h-full w-full object-cover"
          />
        </div>
        <div className="flex-1 min-w-0 pr-1">
          <p className="truncate text-xs font-medium text-slate-800" title={attachment.name}>
            {attachment.name}
          </p>
          <p className="text-[11px] text-slate-400">
            {formatFileSize(attachment.size)}
          </p>
        </div>
        {!readOnly && onRemove && (
          <button
            type="button"
            onClick={() => onRemove(attachment.id)}
            className="absolute -top-1.5 -right-1.5 flex h-5 w-5 items-center justify-center rounded-full bg-slate-700 text-white shadow hover:bg-rose-600 focus:outline-none focus:ring-2 focus:ring-rose-500 transition"
            aria-label={`Xóa tệp ${attachment.name}`}
            title="Xóa tệp đính kèm này"
          >
            <X className="h-3 w-3" />
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="group relative flex items-center gap-2.5 rounded-lg border border-slate-200 bg-white px-3 py-2 shadow-sm transition hover:border-slate-300 max-w-[240px]">
      <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md bg-slate-50 border border-slate-100">
        {getDocIcon()}
      </div>
      <div className="flex-1 min-w-0">
        <p className="truncate text-xs font-medium text-slate-800" title={attachment.name}>
          {attachment.name}
        </p>
        <p className="text-[11px] text-slate-400">
          {formatFileSize(attachment.size)}
        </p>
      </div>
      {!readOnly && onRemove && (
        <button
          type="button"
          onClick={() => onRemove(attachment.id)}
          className="flex h-6 w-6 items-center justify-center rounded-md text-slate-400 hover:bg-slate-100 hover:text-rose-600 focus:outline-none focus:ring-1 focus:ring-slate-300 transition"
          aria-label={`Xóa tệp ${attachment.name}`}
          title="Xóa tệp đính kèm này"
        >
          <X className="h-3.5 w-3.5" />
        </button>
      )}
    </div>
  );
};
