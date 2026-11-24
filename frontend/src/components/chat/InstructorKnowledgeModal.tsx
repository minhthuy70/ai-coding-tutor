'use client';

import React, { useState, useRef, useEffect } from 'react';
import { 
  X, 
  UploadCloud, 
  FileText, 
  CheckCircle2, 
  AlertCircle, 
  Loader2, 
  Database, 
  BookOpen, 
  Layers, 
  Sparkles,
  FileCode,
  FileCheck
} from 'lucide-react';

interface InstructorKnowledgeModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUploadSuccess?: (totalRecords: number) => void;
}

export const InstructorKnowledgeModal: React.FC<InstructorKnowledgeModalProps> = ({
  isOpen,
  onClose,
  onUploadSuccess,
}) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [language, setLanguage] = useState<string>('general');
  const [topic, setTopic] = useState<string>('');
  const [collectionTarget, setCollectionTarget] = useState<string>('auto');

  const [isUploading, setIsUploading] = useState<boolean>(false);
  const [uploadProgressText, setUploadProgressText] = useState<string>('');
  const [uploadResult, setUploadResult] = useState<{
    success: boolean;
    message: string;
    chunksCreated?: number;
    totalRecords?: number;
    filename?: string;
  } | null>(null);

  const [dbStats, setDbStats] = useState<{
    total: number;
    textCount: number;
    codeCount: number;
  }>({ total: 5230, textCount: 4293, codeCount: 937 });

  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isDragging, setIsDragging] = useState<boolean>(false);

  // Fetch current DB stats on open
  useEffect(() => {
    if (isOpen) {
      setUploadResult(null);
      setSelectedFile(null);
      fetchStats();
    }
  }, [isOpen]);

  const fetchStats = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/knowledge/stats');
      if (res.ok) {
        const data = await res.json();
        setDbStats({
          total: data.total_records || 5230,
          textCount: data.collections?.qwen3_text || 4293,
          codeCount: data.collections?.jina_code || 937,
        });
      }
    } catch {
      // Fallback local numbers
    }
  };

  if (!isOpen) return null;

  const handleFileDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileSelected(e.dataTransfer.files[0]);
    }
  };

  const handleFileSelected = (file: File) => {
    const ext = file.name.split('.').pop()?.toLowerCase();
    const allowed = ['pdf', 'txt', 'md', 'docx', 'py', 'cpp', 'c', 'java', 'js', 'json'];
    if (!allowed.includes(ext || '')) {
      alert(`Định dạng .${ext} chưa được hỗ trợ. Vui lòng chọn tệp .pdf, .txt, .md, .docx, .py, .cpp`);
      return;
    }
    setSelectedFile(file);
    setUploadResult(null);

    // Tự động đoán topic và language
    if (ext === 'py') setLanguage('python');
    else if (ext === 'cpp' || ext === 'c') setLanguage('cpp');
    else if (ext === 'java') setLanguage('java');
  };

  const handleStartIngest = async () => {
    if (!selectedFile) return;

    setIsUploading(true);
    setUploadProgressText('Đang gửi tệp tài liệu lên máy chủ...');

    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('language', language);
    formData.append('topic', topic.trim() || 'Giáo trình chuẩn');
    formData.append('target_collection', collectionTarget);

    try {
      setUploadProgressText('Đang bóc tách bố cục văn bản & cắt nhỏ chunks...');

      const response = await fetch('http://localhost:8000/api/knowledge/upload-curriculum', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Lỗi xử lý tài liệu trên máy chủ.');
      }

      setUploadResult({
        success: true,
        message: data.message,
        chunksCreated: data.chunks_created,
        totalRecords: data.total_records,
        filename: data.filename,
      });

      if (data.total_records) {
        setDbStats((prev) => ({
          ...prev,
          total: data.total_records,
        }));
        if (onUploadSuccess) {
          onUploadSuccess(data.total_records);
        }
      }
    } catch (err: any) {
      setUploadResult({
        success: false,
        message: err.message || 'Không thể kết nối đến máy chủ Backend FastAPI.',
      });
    } finally {
      setIsUploading(false);
      setUploadProgressText('');
    }
  };

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-200"
      onClick={onClose}
    >
      <div 
        className="w-full max-w-xl rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-2xl overflow-hidden flex flex-col"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Modal Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/50">
          <div className="flex items-center gap-2.5">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-emerald-600 to-teal-600 text-white shadow-md shadow-emerald-500/20">
              <Database className="h-5 w-5" />
            </div>
            <div>
              <h2 className="text-sm font-bold text-slate-900 dark:text-slate-100">
                Nạp Tài Liệu Giáo Trình (Dành cho Giảng Viên)
              </h2>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">
                Bóc tách tự động, sinh Vector & Lưu trữ gia tăng vào ChromaDB
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg p-1.5 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 space-y-4 max-h-[75vh] overflow-y-auto">
          {/* Database Stats Card */}
          <div className="grid grid-cols-3 gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/60">
            <div className="text-center">
              <span className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Tổng Tri Thức</span>
              <div className="text-base font-extrabold text-slate-800 dark:text-slate-100 mt-0.5">
                {dbStats.total.toLocaleString()} chunks
              </div>
            </div>
            <div className="text-center border-x border-slate-200 dark:border-slate-700">
              <span className="text-[10px] uppercase font-bold text-blue-500 tracking-wider">Lý Thuyết (Qwen3)</span>
              <div className="text-base font-extrabold text-blue-600 dark:text-blue-400 mt-0.5">
                {dbStats.textCount.toLocaleString()}
              </div>
            </div>
            <div className="text-center">
              <span className="text-[10px] uppercase font-bold text-emerald-500 tracking-wider">Mã Nguồn (Jina)</span>
              <div className="text-base font-extrabold text-emerald-600 dark:text-emerald-400 mt-0.5">
                {dbStats.codeCount.toLocaleString()}
              </div>
            </div>
          </div>

          {/* Upload Dropzone */}
          <div
            onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
            onDragLeave={() => setIsDragging(false)}
            onDrop={handleFileDrop}
            onClick={() => fileInputRef.current?.click()}
            className={`border-2 border-dashed rounded-2xl p-6 text-center cursor-pointer transition-all ${
              isDragging
                ? 'border-emerald-500 bg-emerald-50/30 dark:bg-emerald-950/20'
                : selectedFile
                ? 'border-emerald-400 bg-emerald-50/20 dark:bg-emerald-950/10'
                : 'border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:hover:border-emerald-500 hover:bg-slate-50 dark:hover:bg-slate-800/40'
            }`}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept=".pdf,.txt,.md,.docx,.py,.cpp,.c,.java,.js"
              className="hidden"
              onChange={(e) => {
                if (e.target.files && e.target.files[0]) {
                  handleFileSelected(e.target.files[0]);
                }
              }}
            />

            {selectedFile ? (
              <div className="flex items-center justify-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-100 dark:bg-emerald-900/60 text-emerald-600 dark:text-emerald-400">
                  <FileCheck className="h-6 w-6" />
                </div>
                <div className="text-left">
                  <div className="text-xs font-bold text-slate-800 dark:text-slate-100 truncate max-w-xs">
                    {selectedFile.name}
                  </div>
                  <div className="text-[11px] text-slate-400">
                    {(selectedFile.size / 1024).toFixed(1)} KB • Nhấn để chọn tệp khác
                  </div>
                </div>
              </div>
            ) : (
              <div className="flex flex-col items-center">
                <UploadCloud className="h-9 w-9 text-slate-400 mb-2" />
                <p className="text-xs font-bold text-slate-700 dark:text-slate-200">
                  Kéo thả tệp giáo trình vào đây hoặc <span className="text-emerald-600 dark:text-emerald-400">duyệt tệp</span>
                </p>
                <p className="text-[11px] text-slate-400 mt-1">
                  Hỗ trợ: PDF (.pdf), Markdown (.md), Text (.txt), Word (.docx), Mã nguồn (.py, .cpp, .java)
                </p>
              </div>
            )}
          </div>

          {/* Form Options */}
          <div className="grid grid-cols-2 gap-3 text-xs">
            <div>
              <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-300 mb-1">
                Ngôn ngữ / Danh mục
              </label>
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-2 text-xs text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              >
                <option value="general">Lý thuyết chung & Giải thuật (DSA)</option>
                <option value="python">Ngôn ngữ Python</option>
                <option value="cpp">Ngôn ngữ C / C++</option>
                <option value="java">Ngôn ngữ Java</option>
              </select>
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-300 mb-1">
                Bộ sưu tập lưu trữ
              </label>
              <select
                value={collectionTarget}
                onChange={(e) => setCollectionTarget(e.target.value)}
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-2 text-xs text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              >
                <option value="auto">Tự động nhận diện (Văn bản / Code)</option>
                <option value="qwen3_text">qwen3_text (Lý thuyết, giáo trình)</option>
                <option value="jina_code">jina_code (Mã nguồn mẫu, thuật toán)</option>
              </select>
            </div>

            <div className="col-span-2">
              <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-300 mb-1">
                Tên chương / Chủ đề bổ sung (Tùy chọn)
              </label>
              <input
                type="text"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                placeholder="Ví dụ: Chương 4 - Cây nhị phân tìm kiếm & Cân bằng AVL"
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-2 text-xs text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-1 focus:ring-emerald-500"
              />
            </div>
          </div>

          {/* Upload Status / Result */}
          {isUploading && (
            <div className="flex items-center gap-3 p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800 text-xs text-emerald-800 dark:text-emerald-300 animate-pulse">
              <Loader2 className="h-4 w-4 animate-spin text-emerald-600" />
              <span>{uploadProgressText}</span>
            </div>
          )}

          {uploadResult && (
            <div className={`p-3.5 rounded-xl border text-xs flex items-start gap-2.5 ${
              uploadResult.success 
                ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300'
                : 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-800 text-rose-800 dark:text-rose-300'
            }`}>
              {uploadResult.success ? (
                <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0 mt-0.5" />
              ) : (
                <AlertCircle className="h-4 w-4 text-rose-600 shrink-0 mt-0.5" />
              )}
              <div className="flex-1">
                <div className="font-bold">{uploadResult.success ? 'Nạp Tri Thức Thành Công!' : 'Không Thể Nạp Tài Liệu'}</div>
                <div className="text-[11px] mt-0.5">{uploadResult.message}</div>
                {uploadResult.chunksCreated && (
                  <div className="mt-1 text-[10px] text-emerald-700 dark:text-emerald-400 font-semibold">
                    Đã tạo và nhúng: {uploadResult.chunksCreated} chunks • Tổng kho dữ liệu: {uploadResult.totalRecords?.toLocaleString()} chunks
                  </div>
                )}
              </div>
            </div>
          )}
        </div>

        {/* Modal Footer */}
        <div className="flex items-center justify-between px-6 py-3.5 border-t border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/50">
          <span className="text-[11px] text-slate-400">
            Tự động tương thích với mô hình Gemini Socratic
          </span>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={onClose}
              disabled={isUploading}
              className="px-3.5 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
            >
              Đóng
            </button>

            <button
              type="button"
              onClick={handleStartIngest}
              disabled={!selectedFile || isUploading}
              className="flex items-center gap-1.5 px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-xs font-bold text-white shadow-sm hover:shadow transition"
            >
              {isUploading ? (
                <>
                  <Loader2 className="h-3.5 w-3.5 animate-spin" />
                  <span>Đang xử lý...</span>
                </>
              ) : (
                <>
                  <UploadCloud className="h-3.5 w-3.5" />
                  <span>Nạp vào ChromaDB</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
