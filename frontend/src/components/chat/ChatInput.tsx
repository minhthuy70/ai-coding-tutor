'use client';

import React, { useState, useRef, useEffect, useCallback } from 'react';
import { 
  Paperclip, 
  Send, 
  Loader2, 
  AlertCircle, 
  X, 
  FileUp, 
  Sparkles,
  ClipboardCheck,
  CheckCircle2,
  Square,
  Mic,
  MicOff,
  Lightbulb
} from 'lucide-react';
import { ChatAttachment, FileValidationError } from '@/types/chat';
import { AttachmentBadge } from './AttachmentBadge';

interface ChatInputProps {
  onSendMessage: (text: string, attachments: ChatAttachment[]) => void;
  onViewImage?: (url: string, name: string) => void;
  onViewDocument?: (attachment: ChatAttachment) => void;
  isGenerating?: boolean;
  onStopGenerating?: () => void;
  disabled?: boolean;
  onOpenPromptTemplates?: () => void;
  externalInputText?: string;
}

const MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024; // 10MB
const MAX_DOC_SIZE_BYTES = 20 * 1024 * 1024;   // 20MB

const ALLOWED_IMAGE_EXTS = ['png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif'];
const ALLOWED_DOC_EXTS = [
  'pdf', 'txt', 'md', 'docx', 'doc', 
  'py', 'cpp', 'c', 'h', 'java', 'js', 'ts', 'jsx', 'tsx', 
  'json', 'csv', 'sql', 'xml', 'yaml', 'yml'
];

export const ChatInput: React.FC<ChatInputProps> = ({
  onSendMessage,
  onViewImage,
  onViewDocument,
  isGenerating = false,
  onStopGenerating,
  disabled = false,
  onOpenPromptTemplates,
  externalInputText,
}) => {
  const [inputText, setInputText] = useState('');
  const [isListening, setIsListening] = useState(false);
  const recognitionRef = useRef<any>(null);
  const [stagedAttachments, setStagedAttachments] = useState<ChatAttachment[]>([]);
  const [validationErrors, setValidationErrors] = useState<FileValidationError[]>([]);
  const [isDragging, setIsDragging] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [pasteNotification, setPasteNotification] = useState<string | null>(null);

  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Auto-resize textarea
  const adjustTextareaHeight = useCallback(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      const scrollHeight = textarea.scrollHeight;
      textarea.style.height = `${Math.min(Math.max(scrollHeight, 46), 180)}px`;
    }
  }, []);

  useEffect(() => {
    adjustTextareaHeight();
  }, [inputText, adjustTextareaHeight]);

  // Handle external text injection (from prompt templates or suggestions)
  useEffect(() => {
    if (externalInputText) {
      setInputText(externalInputText);
      if (textareaRef.current) {
        textareaRef.current.focus();
      }
    }
  }, [externalInputText]);

  // Handle Speech-to-Text Recognition (Web Speech API)
  const handleToggleListening = useCallback(() => {
    if (typeof window === 'undefined') return;
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;

    if (!SpeechRecognition) {
      setValidationErrors((prev) => [
        ...prev,
        {
          fileName: 'Trình nhận diện giọng nói',
          reason: 'Trình duyệt hiện tại chưa hỗ trợ Web Speech API. Vui lòng sử dụng Google Chrome hoặc Microsoft Edge để nói trực tiếp.',
        },
      ]);
      return;
    }

    if (isListening) {
      if (recognitionRef.current) {
        try {
          recognitionRef.current.stop();
        } catch {}
      }
      setIsListening(false);
      return;
    }

    try {
      const recognition = new SpeechRecognition();
      recognition.lang = 'vi-VN';
      recognition.continuous = true;
      recognition.interimResults = true;

      recognition.onstart = () => {
        setIsListening(true);
      };

      recognition.onresult = (event: any) => {
        let currentTranscript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
          currentTranscript += event.results[i][0].transcript;
        }
        if (currentTranscript.trim()) {
          setInputText((prev) => (prev ? `${prev} ${currentTranscript.trim()}` : currentTranscript.trim()));
        }
      };

      recognition.onerror = (event: any) => {
        console.warn('Speech Recognition error:', event);
        setIsListening(false);
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognition.start();
      recognitionRef.current = recognition;
    } catch (e) {
      setIsListening(false);
    }
  }, [isListening]);

  // Clean up speech recognition on unmount
  useEffect(() => {
    return () => {
      if (recognitionRef.current) {
        try {
          recognitionRef.current.stop();
        } catch {}
      }
    };
  }, []);

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

  const processFiles = useCallback((files: FileList | File[]) => {
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

      const previewUrl = isImg ? URL.createObjectURL(file) : undefined;
      const attId = `att-${Date.now()}-${Math.random().toString(36).substring(2, 9)}`;

      const newAtt: ChatAttachment = {
        id: attId,
        name: file.name,
        size: file.size,
        type: file.type || `application/${ext}`,
        category: isImg ? 'image' : 'document',
        previewUrl,
      };

      // Read text/code content for preview if it's a code/text document
      if (!isImg && file.size < 2 * 1024 * 1024 && ['py', 'cpp', 'c', 'h', 'java', 'js', 'ts', 'jsx', 'tsx', 'txt', 'md', 'json', 'sql', 'xml', 'yaml', 'yml'].includes(ext)) {
        const reader = new FileReader();
        reader.onload = () => {
          if (typeof reader.result === 'string') {
            setStagedAttachments((prev) =>
              prev.map((a) => (a.id === attId ? { ...a, fileContent: reader.result as string } : a))
            );
          }
        };
        reader.readAsText(file);
      }

      validAttachments.push(newAtt);
    });

    if (errors.length > 0) {
      setValidationErrors((prev) => [...prev, ...errors]);
    }

    if (validAttachments.length > 0) {
      setStagedAttachments((prev) => [...prev, ...validAttachments]);
    }

    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  }, []);

  // Handle Clipboard Paste (Ctrl + V)
  const handlePaste = useCallback((e: React.ClipboardEvent<HTMLTextAreaElement>) => {
    const items = e.clipboardData?.items;
    if (!items) return;

    const filesFromClipboard: File[] = [];

    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      if (item.type.startsWith('image/')) {
        const file = item.getAsFile();
        if (file) {
          const now = new Date();
          const pad = (n: number) => n.toString().padStart(2, '0');
          const timeStr = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}_${pad(now.getHours())}${pad(now.getMinutes())}${pad(now.getSeconds())}`;
          const ext = file.type.split('/')[1]?.replace('jpeg', 'jpg') || 'png';
          const namedFile = new File([file], `screenshot_${timeStr}.${ext}`, { type: file.type });
          filesFromClipboard.push(namedFile);
        }
      }
    }

    if (filesFromClipboard.length > 0) {
      processFiles(filesFromClipboard);
      setPasteNotification(`📸 Đã dán ${filesFromClipboard.length} ảnh chụp màn hình từ Clipboard!`);
      setTimeout(() => setPasteNotification(null), 3500);
    }
  }, [processFiles]);

  // Window-level paste listener
  useEffect(() => {
    const handleGlobalPaste = (e: ClipboardEvent) => {
      if (document.activeElement === textareaRef.current) return;

      const items = e.clipboardData?.items;
      if (!items) return;

      const filesFromClipboard: File[] = [];
      for (let i = 0; i < items.length; i++) {
        const item = items[i];
        if (item.type.startsWith('image/')) {
          const file = item.getAsFile();
          if (file) {
            const now = new Date();
            const pad = (n: number) => n.toString().padStart(2, '0');
            const timeStr = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}_${pad(now.getHours())}${pad(now.getMinutes())}${pad(now.getSeconds())}`;
            const ext = file.type.split('/')[1]?.replace('jpeg', 'jpg') || 'png';
            const namedFile = new File([file], `screenshot_${timeStr}.${ext}`, { type: file.type });
            filesFromClipboard.push(namedFile);
          }
        }
      }

      if (filesFromClipboard.length > 0) {
        processFiles(filesFromClipboard);
        setPasteNotification(`📸 Đã dán ${filesFromClipboard.length} ảnh chụp màn hình từ Clipboard!`);
        setTimeout(() => setPasteNotification(null), 3500);
      }
    };

    window.addEventListener('paste', handleGlobalPaste);
    return () => window.removeEventListener('paste', handleGlobalPaste);
  }, [processFiles]);

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

    if (isListening && recognitionRef.current) {
      try {
        recognitionRef.current.stop();
      } catch {}
      setIsListening(false);
    }

    setIsSubmitting(true);
    onSendMessage(trimmed, stagedAttachments);

    setInputText('');
    setStagedAttachments([]);
    setValidationErrors([]);
    setIsSubmitting(false);

    if (textareaRef.current) {
      textareaRef.current.style.height = '46px';
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

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
  const wordCount = inputText.trim() ? inputText.trim().split(/\s+/).length : 0;
  const charCount = inputText.length;
  const estimatedTokens = Math.ceil(charCount / 4);

  return (
    <div className="w-full max-w-4xl mx-auto px-4 pb-4">
      {/* Clipboard Paste Toast Banner */}
      {pasteNotification && (
        <div className="mb-3 flex items-center justify-between rounded-xl border border-emerald-200 bg-emerald-50 px-3.5 py-2 text-xs font-semibold text-emerald-800 shadow-sm animate-in fade-in slide-in-from-bottom-2 duration-200">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
            <span>{pasteNotification}</span>
          </div>
          <button
            type="button"
            onClick={() => setPasteNotification(null)}
            className="rounded p-0.5 text-emerald-600 hover:bg-emerald-100 transition"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        </div>
      )}

      {/* Validation Errors Alert */}
      {validationErrors.length > 0 && (
        <div className="mb-3 rounded-xl border border-amber-200 dark:border-amber-800 bg-amber-50 dark:bg-amber-950/60 p-3 text-xs text-amber-800 dark:text-amber-200 shadow-sm animate-in fade-in duration-200">
          <div className="flex items-center justify-between pb-1 font-semibold">
            <div className="flex items-center gap-1.5">
              <AlertCircle className="h-4 w-4 text-amber-600 dark:text-amber-400 shrink-0" />
              <span>Một số tệp không thể đính kèm:</span>
            </div>
            <button
              type="button"
              onClick={() => setValidationErrors([])}
              className="rounded p-0.5 text-amber-600 dark:text-amber-400 hover:bg-amber-100 dark:hover:bg-amber-900 transition"
              aria-label="Đóng thông báo lỗi tệp"
            >
              <X className="h-3.5 w-3.5" />
            </button>
          </div>
          <ul className="list-disc pl-5 space-y-0.5 mt-1 text-slate-700 dark:text-slate-300">
            {validationErrors.map((err, idx) => (
              <li key={idx}>
                <span className="font-medium text-slate-900 dark:text-slate-100">{err.fileName}:</span> {err.reason}
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
        className={`relative flex flex-col rounded-2xl border bg-white dark:bg-slate-900 shadow-sm transition-all duration-200 ${
          isDragging 
            ? 'border-blue-500 bg-blue-50/40 dark:bg-blue-950/40 ring-4 ring-blue-500/15 scale-[1.005]' 
            : 'border-slate-300 dark:border-slate-700 focus-within:border-blue-600 focus-within:ring-3 focus-within:ring-blue-600/15 focus-within:shadow-md'
        }`}
      >
        {isDragging && (
          <div className="absolute inset-0 z-10 flex items-center justify-center rounded-2xl bg-blue-50/95 dark:bg-slate-900/95 text-blue-700 dark:text-blue-400 text-sm font-semibold backdrop-blur-xs">
            <FileUp className="h-6 w-6 mr-2 animate-bounce" />
            Thả hình ảnh hoặc tài liệu vào đây...
          </div>
        )}

        {/* Staged Attachments Preview Strip */}
        {stagedAttachments.length > 0 && (
          <div className="flex flex-wrap gap-2.5 p-3 border-b border-slate-100 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-950/60 rounded-t-2xl max-h-48 overflow-y-auto">
            {stagedAttachments.map((att) => (
              <AttachmentBadge
                key={att.id}
                attachment={att}
                onRemove={handleRemoveAttachment}
                onViewImage={onViewImage}
                onViewDocument={onViewDocument}
              />
            ))}
          </div>
        )}

        {/* Listening Indicator overlay */}
        {isListening && (
          <div className="absolute top-3 right-14 z-20 flex items-center gap-2 rounded-full bg-rose-600 text-white px-3 py-1 text-xs font-semibold shadow-lg animate-pulse">
            <span className="h-2 w-2 rounded-full bg-white animate-ping" />
            <span>Đang nghe tiếng Việt...</span>
            <div className="flex items-center gap-0.5 h-3">
              <span className="w-0.5 h-2 bg-white animate-bounce" style={{ animationDelay: '0ms' }} />
              <span className="w-0.5 h-3 bg-white animate-bounce" style={{ animationDelay: '150ms' }} />
              <span className="w-0.5 h-1.5 bg-white animate-bounce" style={{ animationDelay: '300ms' }} />
            </div>
          </div>
        )}

        {/* Textarea & Actions Row */}
        <div className="flex items-end gap-1.5 sm:gap-2 p-3">
          {/* File Picker Trigger */}
          <button
            type="button"
            onClick={() => fileInputRef.current?.click()}
            disabled={disabled}
            className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-800 dark:hover:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500/30 transition disabled:opacity-50"
            aria-label="Đính kèm hình ảnh hoặc tài liệu"
            title="Đính kèm tệp hoặc chụp ảnh màn hình rồi nhấn Ctrl + V"
          >
            <Paperclip className="h-5 w-5" />
          </button>

          {/* Voice Speech-to-Text Button */}
          {isListening ? (
            <button
              type="button"
              onClick={handleToggleListening}
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-rose-600 text-white shadow-md shadow-rose-600/30 ring-4 ring-rose-500/20 animate-pulse transition"
              title="Dừng ghi âm giọng nói"
            >
              <MicOff className="h-5 w-5" />
            </button>
          ) : (
            <button
              type="button"
              onClick={handleToggleListening}
              disabled={disabled}
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-rose-600 dark:hover:text-rose-400 focus:outline-none focus:ring-2 focus:ring-rose-500/30 transition disabled:opacity-50"
              title="Nhập bằng giọng nói (Microphone - Web Speech API Tiếng Việt)"
            >
              <Mic className="h-5 w-5" />
            </button>
          )}

          {/* Socratic Prompt Templates Button */}
          {onOpenPromptTemplates && (
            <button
              type="button"
              onClick={onOpenPromptTemplates}
              disabled={disabled}
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-amber-500 dark:hover:text-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-500/30 transition disabled:opacity-50"
              title="Kho mẫu câu hỏi Socratic & Thuật toán"
            >
              <Sparkles className="h-5 w-5 text-amber-500" />
            </button>
          )}

          <input
            ref={fileInputRef}
            type="file"
            multiple
            accept=".png,.jpg,.jpeg,.webp,.pdf,.txt,.md,.docx,.doc,.py,.cpp,.c,.h,.java,.js,.ts,.jsx,.tsx,.json,.csv,.sql"
            onChange={handleFileInputChange}
            className="hidden"
          />

          {/* Text input with Ctrl+V support */}
          <textarea
            ref={textareaRef}
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={handleKeyDown}
            onPaste={handlePaste}
            disabled={disabled}
            placeholder="Hỏi về code, dán ảnh màn hình (Ctrl + V), hoặc kéo thả tệp... (Enter để gửi, Shift + Enter xuống dòng)"
            rows={1}
            className="flex-1 resize-none bg-transparent py-2.5 px-1 text-sm text-[#202123] dark:text-slate-100 placeholder-slate-400 dark:placeholder-slate-500 focus:outline-none leading-relaxed max-h-[180px]"
          />

          {/* Stop Generating Button or Send Button */}
          {isGenerating ? (
            <button
              type="button"
              onClick={onStopGenerating}
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-rose-600 text-white hover:bg-rose-700 shadow-md transition active:scale-95"
              title="Dừng tạo phản hồi"
            >
              <Square className="h-4 w-4 fill-white" />
            </button>
          ) : (
            <button
              type="button"
              onClick={handleSubmit}
              disabled={!hasContent || disabled || isSubmitting}
              className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl transition duration-150 ${
                hasContent && !disabled && !isSubmitting
                  ? 'bg-blue-600 text-white hover:bg-blue-700 shadow-md hover:shadow-lg active:scale-95 focus:outline-none focus:ring-2 focus:ring-blue-500/40'
                  : 'bg-slate-100 dark:bg-slate-800 text-slate-300 dark:text-slate-600 cursor-not-allowed'
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
          )}
        </div>
      </div>

      {/* Helper & Word/Token Stats Row */}
      <div className="mt-2 flex items-center justify-between px-1 text-[11px] text-slate-400 select-none">
        <span className="flex items-center gap-1 text-slate-500 dark:text-slate-400">
          <ClipboardCheck className="h-3.5 w-3.5 text-blue-500" />
          <span>Mẹo: Chụp màn hình rồi nhấn <b className="font-bold text-slate-700 dark:text-slate-300">Ctrl + V</b> để tải ảnh lên tức thì</span>
        </span>

        {charCount > 0 ? (
          <span className="font-mono text-slate-500 dark:text-slate-400 text-[10px]">
            {wordCount} từ • {charCount} ký tự • ~{estimatedTokens} tokens
          </span>
        ) : (
          <span className="text-slate-400 dark:text-slate-500">Phiên bản thử nghiệm UI</span>
        )}
      </div>
    </div>
  );
};
