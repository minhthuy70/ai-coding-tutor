'use client';

import React from 'react';
import { 
  FileText, 
  FileCode, 
  FileArchive, 
  File, 
  X, 
  Eye,
  Image as ImageIcon 
} from 'lucide-react';
import { ChatAttachment } from '@/types/chat';

interface AttachmentBadgeProps {
  attachment: ChatAttachment;
  onRemove?: (id: string) => void;
  onViewImage?: (url: string, name: string) => void;
  onViewDocument?: (attachment: ChatAttachment) => void;
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
  onViewImage,
  onViewDocument,
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
      case 'h':
      case 'java':
      case 'js':
      case 'ts':
      case 'jsx':
      case 'tsx':
      case 'html':
      case 'css':
      case 'json':
      case 'sql':
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
      <div className="group relative flex items-center gap-2.5 rounded-xl border border-slate-200/90 bg-white p-2 shadow-2xs hover:shadow-xs hover:border-blue-300 transition-all max-w-[240px]">
        {/* Thumbnail with click-to-preview */}
        <div 
          onClick={() => onViewImage && attachment.previewUrl && onViewImage(attachment.previewUrl, attachment.name)}
          className={`relative h-12 w-12 shrink-0 overflow-hidden rounded-lg bg-slate-100 border border-slate-150 ${
            onViewImage ? 'cursor-pointer' : ''
          }`}
          title="Nhấn để phóng to ảnh"
        >
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={attachment.previewUrl}
            alt={attachment.name}
            className="h-full w-full object-cover transition-transform duration-200 group-hover:scale-105"
          />
          {onViewImage && (
            <div className="absolute inset-0 bg-slate-900/30 opacity-0 group-hover:opacity-100 flex items-center justify-center text-white transition-opacity">
              <Eye className="h-3.5 w-3.5" />
            </div>
          )}
        </div>

        {/* Info */}
        <div className="flex-1 min-w-0 pr-1">
          <p className="truncate text-xs font-semibold text-slate-800" title={attachment.name}>
            {attachment.name}
          </p>
          <div className="flex items-center gap-1.5 mt-0.5">
            <span className="rounded bg-blue-50 px-1 py-0.2 text-[9px] font-medium text-blue-600">
              ẢNH
            </span>
            <span className="text-[11px] text-slate-400">
              {formatFileSize(attachment.size)}
            </span>
          </div>
        </div>

        {/* Delete action in composer stage */}
        {!readOnly && onRemove && (
          <button
            type="button"
            onClick={() => onRemove(attachment.id)}
            className="absolute -top-1.5 -right-1.5 flex h-5 w-5 items-center justify-center rounded-full bg-slate-700 text-white shadow-sm hover:bg-rose-600 focus:outline-none focus:ring-2 focus:ring-rose-500 transition scale-90 hover:scale-100"
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
    <div 
      onClick={() => onViewDocument && onViewDocument(attachment)}
      className={`group relative flex items-center gap-2.5 rounded-xl border border-slate-200/90 bg-white px-3 py-2 shadow-2xs hover:shadow-xs hover:border-blue-300 transition-all max-w-[250px] ${
        onViewDocument ? 'cursor-pointer' : ''
      }`}
      title={onViewDocument ? 'Nhấn để xem nội dung tệp' : attachment.name}
    >
      <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-slate-50 border border-slate-100 group-hover:bg-blue-50 transition">
        {getDocIcon()}
      </div>
      <div className="flex-1 min-w-0 pr-2">
        <p className="truncate text-xs font-semibold text-slate-800 group-hover:text-blue-600 transition" title={attachment.name}>
          {attachment.name}
        </p>
        <p className="text-[11px] text-slate-400 mt-0.5">
          {formatFileSize(attachment.size)}
        </p>
      </div>

      {!readOnly && onRemove && (
        <button
          type="button"
          onClick={(e) => {
            e.stopPropagation();
            onRemove(attachment.id);
          }}
          className="flex h-6 w-6 items-center justify-center rounded-lg text-slate-400 hover:bg-slate-100 hover:text-rose-600 focus:outline-none focus:ring-1 focus:ring-slate-300 transition"
          aria-label={`Xóa tệp ${attachment.name}`}
          title="Xóa tệp đính kèm này"
        >
          <X className="h-3.5 w-3.5" />
        </button>
      )}
    </div>
  );
};
