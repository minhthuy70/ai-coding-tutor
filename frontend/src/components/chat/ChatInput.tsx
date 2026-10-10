'use client';

import React, { useState, useRef, useEffect, useCallback } from 'react';
import { 
  Paperclip, 
  Send, 
  Loader2, 
  AlertCircle, 
  X, 
  FileUp, 
  Image as ImageIcon 
} from 'lucide-react';
import { ChatAttachment, FileValidationError } from '@/types/chat';
import { AttachmentBadge } from './AttachmentBadge';

interface ChatInputProps {
  onSendMessage: (text: string, attachments: ChatAttachment[]) => void;
  disabled?: boolean;
}

const MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024; // 10MB
const MAX_DOC_SIZE_BYTES = 20 * 1024 * 1024;   // 20MB

const ALLOWED_IMAGE_EXTS = ['png', 'jpg', 'jpeg', 'webp'];
const ALLOWED_DOC_EXTS = [
  'pdf', 'txt', 'md', 'docx', 'doc', 
  'py', 'cpp', 'c', 'h', 'java', 'js', 'ts', 'jsx', 'tsx', 
  'json', 'csv', 'sql', 'xml', 'yaml', 'yml'
];

export const ChatInput: React.FC<ChatInputProps> = ({
  onSendMessage,
  disabled = false,
}) => {
  const [inputText, setInputText] = useState('');
  const [stagedAttachments, setStagedAttachments] = useState<ChatAttachment[]>([]);
  const [validationErrors, setValidationErrors] = useState<FileValidationError[]>([]);
  const [isDragging, setIsDragging] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Auto-resize textarea
  const adjustTextareaHeight = useCallback(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      const scrollHeight = textarea.scrollHeight;
      // Cap height between 44px and 180px
      textarea.style.height = `${Math.min(Math.max(scrollHeight, 44), 180)}px`;
    }
  }, []);

  useEffect(() => {
    adjustTextareaHeight();
  }, [inputText, adjustTextareaHeight]);

  // Clean up object URLs on unmount
  useEffect(() => {
    return () => {
      stagedAttachments.forEach((att) => {
        if (att.previewUrl) {
          URL.revokeObjectURL(att.previewUrl);
        }
      });
    };
  }, [stagedAttachments]);

  const processFiles = (files: FileList | File[]) => {
    const errors: FileValidationError[] = [];
    const validAttachments: ChatAttachment[] = [];

    Array.from(files).forEach((file) => {
      const ext = file.name.split('.').pop()?.toLowerCase() || '';
      const isImg = ALLOWED_IMAGE_EXTS.includes(ext) || file.type.startsWith('image/');
      const isDoc = ALLOWED_DOC_EXTS.includes(ext);

      if (!isImg && !isDoc) {
        errors.push({
          fileName: file.name,
          reason: `Định dạng tệp .${ext || 'unknown'} không được hỗ trợ. Chỉ nhận ảnh (.png, .jpg, .webp) và tài liệu (.pdf, .docx, .txt, .py, v.v.).`,
        });
        return;
      }

      if (isImg && file.size > MAX_IMAGE_SIZE_BYTES) {
        errors.push({
          fileName: file.name,
          reason: `Ảnh vượt quá dung lượng tối đa cho phép (10MB).`,
        });
        return;
      }

      if (isDoc && file.size > MAX_DOC_SIZE_BYTES) {
        errors.push({
          fileName: file.name,
          reason: `Tài liệu vượt quá dung lượng tối đa cho phép (20MB).`,
        });
        return;
      }

      // Valid file
      const previewUrl = isImg ? URL.createObjectURL(file) : undefined;
      validAttachments.push({
        id: `att-${Date.now()}-${Math.random().toString(36).substring(2, 9)}`,
        name: file.name,
        size: file.size,
        type: file.type || `application/${ext}`,
        category: isImg ? 'image' : 'document',
        previewUrl,
      });
    });

    if (errors.length > 0) {
      setValidationErrors((prev) => [...prev, ...errors]);
    }

    if (validAttachments.length > 0) {
      setStagedAttachments((prev) => [...prev, ...validAttachments]);
    }

    // Reset native input to allow selecting same file again if desired
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      processFiles(e.target.files);
    }
  };

  const handleRemoveAttachment = (id: string) => {
    setStagedAttachments((prev) => {
      const target = prev.find((att) => att.id === id);
      if (target?.previewUrl) {
        URL.revokeObjectURL(target.previewUrl);
      }
      return prev.filter((att) => att.id !== id);
    });
  };

  const handleSubmit = () => {
    const trimmed = inputText.trim();
    if ((!trimmed && stagedAttachments.length === 0) || disabled || isSubmitting) {
      return;
    }

    setIsSubmitting(true);
    onSendMessage(trimmed, stagedAttachments);

    // Reset input state
    setInputText('');
    setStagedAttachments([]);
    setValidationErrors([]);
    setIsSubmitting(false);

    // Reset textarea height
    if (textareaRef.current) {
      textareaRef.current.style.height = '44px';
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  // Drag and drop handlers
  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      processFiles(e.dataTransfer.files);
    }
  };

  const hasContent = inputText.trim().length > 0 || stagedAttachments.length > 0;

  return (
    <div className="w-full max-w-4xl mx-auto px-4 pb-4">
      {/* Validation Errors Alert Banner */}
      {validationErrors.length > 0 && (
        <div className="mb-3 rounded-lg border border-amber-200 bg-amber-50 p-3 text-xs text-amber-800">
          <div className="flex items-center justify-between pb-1 font-semibold">
            <div className="flex items-center gap-1.5">
              <AlertCircle className="h-4 w-4 text-amber-600 shrink-0" />
              <span>Một số tệp không thể đính kèm:</span>
            </div>
            <button
              type="button"
              onClick={() => setValidationErrors([])}
              className="rounded p-0.5 text-amber-600 hover:bg-amber-100 transition"
              aria-label="Đóng thông báo lỗi tệp"
            >
              <X className="h-3.5 w-3.5" />
            </button>
          </div>
          <ul className="list-disc pl-5 space-y-0.5 mt-1 text-slate-700">
            {validationErrors.map((err, idx) => (
              <li key={idx}>
                <span className="font-medium text-slate-900">{err.fileName}:</span> {err.reason}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Main Composer Box */}
      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        className={`relative flex flex-col rounded-2xl border bg-white shadow-sm transition-all ${
          isDragging 
            ? 'border-blue-500 bg-blue-50/30 ring-2 ring-blue-500/20' 
            : 'border-slate-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-500/20'
        }`}
      >
        {/* Drag overlay notice */}
        {isDragging && (
          <div className="absolute inset-0 z-10 flex items-center justify-center rounded-2xl bg-blue-50/90 text-blue-700 text-sm font-medium backdrop-blur-xs">
            <FileUp className="h-6 w-6 mr-2 animate-bounce" />
            Thả hình ảnh hoặc tài liệu vào đây...
          </div>
        )}

        {/* Staged Attachments Preview Strip */}
        {stagedAttachments.length > 0 && (
          <div className="flex flex-wrap gap-2 p-3 border-b border-slate-100 bg-slate-50/50 rounded-t-2xl max-h-48 overflow-y-auto">
            {stagedAttachments.map((att) => (
              <AttachmentBadge
                key={att.id}
                attachment={att}
                onRemove={handleRemoveAttachment}
              />
            ))}
          </div>
        )}

        {/* Textarea & Actions Row */}
        <div className="flex items-end gap-2 p-3">
          {/* File Picker Trigger Button */}
          <button
            type="button"
            onClick={() => fileInputRef.current?.click()}
            disabled={disabled}
            className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-slate-500 hover:bg-slate-100 hover:text-slate-700 focus:outline-none focus:ring-2 focus:ring-blue-500/30 transition disabled:opacity-50"
            aria-label="Đính kèm hình ảnh hoặc tài liệu"
            title="Đính kèm ảnh (.png, .jpg, .webp) hoặc tài liệu (.pdf, .docx, .txt, .py,...)"
          >
            <Paperclip className="h-5 w-5" />
          </button>

          {/* Hidden file input */}
          <input
            ref={fileInputRef}
            type="file"
            multiple
            accept=".png,.jpg,.jpeg,.webp,.pdf,.txt,.md,.docx,.doc,.py,.cpp,.c,.h,.java,.js,.ts,.jsx,.tsx,.json,.csv,.sql"
            onChange={handleFileInputChange}
            className="hidden"
          />

          {/* Text input */}
          <textarea
            ref={textareaRef}
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={disabled}
            placeholder="Gửi tin nhắn, câu hỏi lập trình, hoặc đính kèm ảnh/tài liệu... (Nhấn Enter để gửi, Shift + Enter để xuống dòng)"
            rows={1}
            className="flex-1 resize-none bg-transparent py-2 px-1 text-sm text-[#202123] placeholder-slate-400 focus:outline-none leading-relaxed max-h-[180px]"
          />

          {/* Send Button */}
          <button
            type="button"
            onClick={handleSubmit}
            disabled={!hasContent || disabled || isSubmitting}
            className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl transition ${
              hasContent && !disabled && !isSubmitting
                ? 'bg-blue-600 text-white hover:bg-blue-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500/40'
                : 'bg-slate-100 text-slate-300 cursor-not-allowed'
            }`}
            aria-label="Gửi tin nhắn"
            title="Gửi tin nhắn"
          >
            {isSubmitting ? (
              <Loader2 className="h-4 w-4 animate-spin text-white" />
            ) : (
              <Send className="h-4 w-4" />
            )}
          </button>
        </div>
      </div>

      {/* Mandatory Disclaimer Note */}
      <p className="mt-2 text-center text-[11px] text-slate-400 select-none">
        Phiên bản thử nghiệm — chức năng AI và phân tích tài liệu chưa được tích hợp.
      </p>
    </div>
  );
};
