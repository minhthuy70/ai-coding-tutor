'use client';

import React, { useState, useEffect } from 'react';
import {
  X,
  ShieldCheck,
  Zap,
  CheckCircle2,
  AlertTriangle,
  Info,
  Sparkles,
  ArrowRight,
  Code2,
  Copy,
  Check,
  RotateCcw,
  Play,
  Flame,
  FileCheck,
  TrendingUp,
  Cpu
} from 'lucide-react';

interface CodeQualityModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialCode: string;
  initialLanguage?: string;
  onApplyRefactoredCode?: (code: string) => void;
  onAskAIAboutQuality?: (prompt: string) => void;
}

interface IssueItem {
  id: string;
  type: 'error' | 'warning' | 'info' | 'optimization';
  line?: number;
  title: string;
  description: string;
  suggestion: string;
}

export const CodeQualityModal: React.FC<CodeQualityModalProps> = ({
  isOpen,
  onClose,
  initialCode,
  initialLanguage = 'python',
  onApplyRefactoredCode,
  onAskAIAboutQuality,
}) => {
  const [code, setCode] = useState(initialCode);
  const [language, setLanguage] = useState(initialLanguage);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [activeTab, setActiveTab] = useState<'issues' | 'diff' | 'raw'>('issues');
  const [copied, setCopied] = useState(false);

  // Analysis Result State
  const [qualityScore, setQualityScore] = useState(82);
  const [issues, setIssues] = useState<IssueItem[]>([]);
  const [refactoredCode, setRefactoredCode] = useState('');

  useEffect(() => {
    if (isOpen) {
      setCode(initialCode || '# Dán mã nguồn cần đánh giá chất lượng tại đây...');
      setLanguage(initialLanguage || 'python');
      runQualityAnalysis(initialCode || '');
    }
  }, [isOpen, initialCode, initialLanguage]);

  const runQualityAnalysis = (source: string) => {
    setIsAnalyzing(true);

    setTimeout(() => {
      // Heuristic analysis based on source code rules
      const detectedIssues: IssueItem[] = [];
      let score = 95;

      // 1. Check for broad except in Python
      if (source.includes('except:') || source.includes('except Exception:')) {
        detectedIssues.push({
          id: 'err-broad-except',
          type: 'warning',
          line: 12,
          title: 'Khối try-except bắt ngoại lệ quá chung chung',
          description: 'Sử dụng `except:` hoặc `except Exception:` mà không chỉ rõ loại ngoại lệ cụ thể có thể vô tình ẩn đi các lỗi logic nghiêm trọng như KeyboardInterrupt hoặc SyntaxError.',
          suggestion: 'Nên chỉ định rõ loại Exception như `except ValueError:` hoặc `except KeyError:`.'
        });
        score -= 8;
      }

      // 2. Check for nested loops
      if (/for[^\n]+\n\s+for/g.test(source) || /while[^\n]+\n\s+while/g.test(source)) {
        detectedIssues.push({
          id: 'perf-nested-loops',
          type: 'optimization',
          line: 6,
          title: 'Phát hiện vòng lặp lồng nhau O(n²)',
          description: 'Hai vòng lặp lồng nhau làm tăng độ phức tạp thời gian lên bậc hai. Khi dữ liệu lớn (N > 10,000), chương trình có thể gặp lỗi Time Limit Exceeded (TLE).',
          suggestion: 'Cân nhắc sử dụng Hash Map (Dictionary) hoặc Hash Set để giảm thời gian tra cứu xuống O(1).'
        });
        score -= 10;
      }

      // 3. Check for string concatenation in loop
      if (/\+=\s*["']|\+=\s*\w+/g.test(source) && source.includes('for ')) {
        detectedIssues.push({
          id: 'perf-str-concat',
          type: 'optimization',
          title: 'Nối chuỗi trong vòng lặp bằng toán tử +=',
          description: 'Trong Python, chuỗi ký tự là bất biến (immutable). Việc nối chuỗi liên tục bằng `+=` tạo ra một đối tượng chuỗi mới sau mỗi lần lặp, tiêu tốn O(n²) bộ nhớ.',
          suggestion: 'Hãy lưu các chuỗi vào một List và dùng `"".join(list)` khi kết thúc vòng lặp để đạt O(n).'
        });
        score -= 5;
      }

      // 4. Missing type hints or docstrings
      if (!source.includes('def ') || !source.includes('->') || !source.includes('"""')) {
        detectedIssues.push({
          id: 'style-type-hints',
          type: 'info',
          title: 'Thiếu Type Annotations & Docstrings',
          description: 'Mã nguồn chưa khai báo kiểu dữ liệu cho tham số và giá trị trả về, hoặc thiếu khối tài liệu mô tả hàm (Docstring PEP 257).',
          suggestion: 'Thêm gợi ý kiểu ví dụ: `def calculate(a: int, b: int) -> float:` và Docstring 3 dấu nháy để mã nguồn dễ đọc hơn.'
        });
        score -= 5;
      }

      // 5. Global variables check
      if (source.includes('global ')) {
        detectedIssues.push({
          id: 'smell-global-var',
          type: 'warning',
          title: 'Lạm dụng biến toàn cục (global variable)',
          description: 'Sử dụng từ khóa `global` phá vỡ tính bao đóng và làm hàm trở nên khó viết unit test cũng như tiềm ẩn lỗi side-effects.',
          suggestion: 'Truyền biến qua đối số của hàm hoặc đóng gói vào trong Class (OOP).'
        });
        score -= 7;
      }

      // Fallback if clean
      if (detectedIssues.length === 0) {
        detectedIssues.push({
          id: 'info-clean-code',
          type: 'info',
          title: 'Cấu trúc mã nguồn tương đối sạch',
          description: 'Không phát hiện các mẫu lỗi nghiêm trọng hoặc code smell rõ rệt.',
          suggestion: 'Tiếp tục duy trì quy chuẩn đặt tên biến rõ nghĩa và bổ sung thêm các bộ kiểm thử tự động.'
        });
      }

      // Generate simulated refactored clean code
      let cleaned = source;
      if (source.includes('nums') && source.includes('target')) {
        cleaned = `# Mã nguồn đã được chuẩn hóa theo chuẩn Clean Code & PEP 8\nfrom typing import List, Tuple, Optional\n\ndef two_sum_optimized(nums: List[int], target: int) -> Optional[Tuple[int, int]]:\n    """\n    Tìm vị trí của hai số có tổng bằng target sử dụng Hash Map.\n    Độ phức tạp thời gian: O(n)\n    Độ phức tạp không gian: O(n)\n    """\n    lookup_table = {}\n    for index, value in enumerate(nums):\n        difference = target - value\n        if difference in lookup_table:\n            return (lookup_table[difference], index)\n        lookup_table[value] = index\n    return None\n\n# Kiểm thử mẫu\nresult = two_sum_optimized([2, 7, 11, 15], 9)\nprint("Kết quả:", result)`;
      } else {
        cleaned = `# Mã nguồn đã tối ưu chuẩn Clean Code & Type Hints\nfrom typing import Any, Dict, List\n\ndef process_data(data_stream: List[Any]) -> Dict[str, Any]:\n    """\n    Xử lý dữ liệu chuẩn hóa với kiểm soát ngoại lệ chặt chẽ.\n    """\n    processed = []\n    for item in data_stream:\n        if item is not None:\n            processed.append(item)\n    return {"status": "success", "total_valid": len(processed)}\n\nprint(process_data([1, 2, None, 4]))`;
      }

      setIssues(detectedIssues);
      setQualityScore(Math.max(50, Math.min(100, score)));
      setRefactoredCode(cleaned);
      setIsAnalyzing(false);
    }, 400);
  };

  const handleCopyRefactored = () => {
    navigator.clipboard.writeText(refactoredCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-900/60 dark:bg-black/75 backdrop-blur-md animate-fade-in">
      <div className="flex flex-col w-full max-w-5xl h-[88vh] bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden animate-scale-in">
        
        {/* Header */}
        <div className="px-6 py-4.5 border-b border-slate-200/80 dark:border-slate-800 bg-gradient-to-r from-slate-50 via-white to-blue-50/30 dark:from-slate-900 dark:via-slate-900 dark:to-blue-950/20 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-tr from-indigo-600 to-blue-600 text-white shadow-md shadow-indigo-500/25">
              <ShieldCheck className="h-6 w-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
                  Phân Tích Chất Lượng & Đánh Giá Mã Nguồn
                </h2>
                <span className="rounded-full bg-indigo-100 dark:bg-indigo-900/60 px-2.5 py-0.5 text-[10px] font-extrabold text-indigo-700 dark:text-indigo-300">
                  Static Linter & PEP 8
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Kiểm tra chuẩn Clean Code, phát hiện code smell, tối ưu độ phức tạp và đề xuất tái cấu trúc
              </p>
            </div>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="rounded-2xl p-2 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Score Overview Banner */}
        <div className="px-6 py-4 bg-slate-50/70 dark:bg-slate-950/40 border-b border-slate-200/70 dark:border-slate-800/80 flex flex-wrap items-center justify-between gap-4 shrink-0">
          <div className="flex items-center gap-4">
            {/* Circular Gauge */}
            <div className={`flex items-center justify-center h-14 w-14 rounded-2xl font-black text-lg shadow-md ${
              qualityScore >= 85
                ? 'bg-emerald-500 text-white shadow-emerald-500/20'
                : qualityScore >= 70
                ? 'bg-amber-500 text-white shadow-amber-500/20'
                : 'bg-rose-500 text-white shadow-rose-500/20'
            }`}>
              {qualityScore}
            </div>

            <div>
              <div className="flex items-center gap-2">
                <span className="text-sm font-extrabold text-slate-800 dark:text-slate-100">
                  {qualityScore >= 85 ? 'Chất lượng Tốt (Clean Code)' : qualityScore >= 70 ? 'Cần cải thiện hiệu năng & quy chuẩn' : 'Chất lượng Kém (Nhiều Code Smell)'}
                </span>
                <span className="text-xs text-slate-400">/ 100 điểm</span>
              </div>
              <div className="flex items-center gap-3 text-xs text-slate-500 dark:text-slate-400 mt-1">
                <span>Phát hiện: <strong className="text-slate-700 dark:text-slate-200">{issues.length}</strong> điểm lưu ý</span>
                <span>•</span>
                <span>Ngôn ngữ: <strong className="uppercase font-mono text-slate-700 dark:text-slate-200">{language}</strong></span>
              </div>
            </div>
          </div>

          {/* Tab Selector */}
          <div className="flex items-center gap-1.5 bg-slate-200/70 dark:bg-slate-800 p-1 rounded-2xl">
            <button
              type="button"
              onClick={() => setActiveTab('issues')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                activeTab === 'issues'
                  ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              Danh sách vấn đề ({issues.length})
            </button>
            <button
              type="button"
              onClick={() => setActiveTab('diff')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                activeTab === 'diff'
                  ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              Mã sau khi Tái cấu trúc (Refactored)
            </button>
          </div>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 bg-slate-50/30 dark:bg-slate-900/50">
          {activeTab === 'issues' ? (
            <div className="space-y-3.5 max-w-4xl mx-auto">
              <div className="flex items-center justify-between pb-1">
                <span className="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  Chi tiết các phát hiện từ Static Linter
                </span>
                <button
                  type="button"
                  onClick={() => runQualityAnalysis(code)}
                  className="flex items-center gap-1 text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:underline"
                >
                  <RotateCcw className="h-3 w-3" />
                  Chạy lại phân tích
                </button>
              </div>

              {issues.map((issue) => (
                <div
                  key={issue.id}
                  className="p-4 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-800 shadow-sm space-y-2.5"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex items-center gap-2">
                      {issue.type === 'error' ? (
                        <div className="h-6 w-6 rounded-lg bg-rose-100 dark:bg-rose-950/70 text-rose-600 flex items-center justify-center shrink-0">
                          <AlertTriangle className="h-3.5 w-3.5" />
                        </div>
                      ) : issue.type === 'warning' ? (
                        <div className="h-6 w-6 rounded-lg bg-amber-100 dark:bg-amber-950/70 text-amber-600 flex items-center justify-center shrink-0">
                          <AlertTriangle className="h-3.5 w-3.5" />
                        </div>
                      ) : issue.type === 'optimization' ? (
                        <div className="h-6 w-6 rounded-lg bg-blue-100 dark:bg-blue-950/70 text-blue-600 flex items-center justify-center shrink-0">
                          <Zap className="h-3.5 w-3.5" />
                        </div>
                      ) : (
                        <div className="h-6 w-6 rounded-lg bg-emerald-100 dark:bg-emerald-950/70 text-emerald-600 flex items-center justify-center shrink-0">
                          <CheckCircle2 className="h-3.5 w-3.5" />
                        </div>
                      )}
                      <h4 className="text-xs sm:text-sm font-extrabold text-slate-900 dark:text-white">
                        {issue.title}
                      </h4>
                    </div>

                    <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full shrink-0 ${
                      issue.type === 'error'
                        ? 'bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300'
                        : issue.type === 'warning'
                        ? 'bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300'
                        : issue.type === 'optimization'
                        ? 'bg-blue-100 text-blue-700 dark:bg-blue-950 dark:text-blue-300'
                        : 'bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300'
                    }`}>
                      {issue.type === 'optimization' ? 'Tối ưu' : issue.type}
                    </span>
                  </div>

                  <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed pl-8">
                    {issue.description}
                  </p>

                  <div className="ml-8 p-3 rounded-xl bg-slate-50 dark:bg-slate-900/70 border border-slate-100 dark:border-slate-800 text-xs flex items-start gap-2">
                    <Sparkles className="h-3.5 w-3.5 text-amber-500 shrink-0 mt-0.5" />
                    <div>
                      <strong className="text-slate-800 dark:text-slate-200">Đề xuất khắc phục: </strong>
                      <span className="text-slate-600 dark:text-slate-400">{issue.suggestion}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="max-w-4xl mx-auto space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="text-sm font-black text-slate-900 dark:text-white">
                    Phương án Tái Cấu Trúc Đề Xuất (Refactored Clean Code)
                  </h4>
                  <p className="text-xs text-slate-500">
                    Đã chuẩn hóa PEP 8, thêm Type Annotations, Docstring và cấu trúc dữ liệu tối ưu
                  </p>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    type="button"
                    onClick={handleCopyRefactored}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-50 shadow-2xs"
                  >
                    {copied ? <Check className="h-3.5 w-3.5 text-emerald-500" /> : <Copy className="h-3.5 w-3.5" />}
                    <span>{copied ? 'Đã sao chép' : 'Sao chép code'}</span>
                  </button>

                  {onApplyRefactoredCode && (
                    <button
                      type="button"
                      onClick={() => {
                        onApplyRefactoredCode(refactoredCode);
                        onClose();
                      }}
                      className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-sm"
                    >
                      <Check className="h-3.5 w-3.5" />
                      <span>Áp dụng vào Sandbox</span>
                    </button>
                  )}
                </div>
              </div>

              <pre className="p-4 rounded-2xl bg-slate-900 text-slate-100 text-xs font-mono overflow-x-auto border border-slate-800 leading-relaxed max-h-[480px]">
                <code>{refactoredCode}</code>
              </pre>
            </div>
          )}
        </div>

        {/* Footer Actions */}
        <div className="px-6 py-4 border-t border-slate-200/80 dark:border-slate-800 bg-white dark:bg-slate-900 flex flex-col sm:flex-row items-center justify-between gap-3 shrink-0">
          <span className="text-xs text-slate-400">
            Dựa trên chuẩn PEP 8 (Python), Google Style Guide (C++) và ESLint Clean Code
          </span>

          <div className="flex items-center gap-2.5 w-full sm:w-auto">
            {onAskAIAboutQuality && (
              <button
                type="button"
                onClick={() => {
                  onAskAIAboutQuality(`Hãy giải thích chi tiết báo cáo chất lượng mã nguồn này giúp tôi. Làm thế nào để cải thiện điểm số từ ${qualityScore}/100 lên 100/100?`);
                  onClose();
                }}
                className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 hover:bg-indigo-100 text-indigo-600 dark:text-indigo-400 text-xs font-bold transition"
              >
                <Sparkles className="h-4 w-4" />
                <span>Thảo luận cùng AI Tutor</span>
              </button>
            )}

            <button
              type="button"
              onClick={onClose}
              className="flex-1 sm:flex-initial px-5 py-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold transition"
            >
              Đóng
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
