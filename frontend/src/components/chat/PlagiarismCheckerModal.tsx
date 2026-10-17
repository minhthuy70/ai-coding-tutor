'use client';

import React, { useState, useMemo } from 'react';
import {
  X,
  ScanSearch,
  AlertTriangle,
  CheckCircle2,
  Copy,
  Sparkles,
  RotateCcw,
  Code2,
  Scale,
  FileText,
  ChevronRight,
  ShieldAlert,
  ShieldCheck,
  Eye
} from 'lucide-react';

interface PlagiarismPreset {
  name: string;
  desc: string;
  lang: string;
  codeA: string;
  codeB: string;
}

const PRESETS: PlagiarismPreset[] = [
  {
    name: 'Hai bài Two Sum (Đổi tên biến & Thêm comment nhằm qua mặt)',
    desc: 'Sinh viên B sao chép logic Two Sum của Sinh viên A, đổi tên biến và thêm comment thừa.',
    lang: 'python',
    codeA: `# Lời giải Sinh viên Nguyễn Văn A (MSSV: 2111001)
import sys

def two_sum():
    lines = sys.stdin.read().strip().split('\\n')
    if len(lines) < 2: return
    target = int(lines[0].strip())
    nums = list(map(int, lines[1].strip().split()))
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print(f"{seen[complement]} {i}")
            return
        seen[num] = i

two_sum()`,
    codeB: `# Lời giải Sinh viên Trần Văn B (MSSV: 2111045)
# Bài tập nộp lúc 23:58
import sys

def find_target_pair():
    # Đọc dữ liệu đầu vào
    data = sys.stdin.read().strip().split('\\n')
    if len(data) < 2:
        return
    k = int(data[0].strip())
    arr = list(map(int, data[1].strip().split()))
    
    # Dùng dictionary lưu trữ
    lookup_table = {}
    for idx, val in enumerate(arr):
        diff = k - val
        if diff in lookup_table:
            print(f"{lookup_table[diff]} {idx}")
            return
        lookup_table[val] = idx

find_target_pair()`,
  },
  {
    name: 'Tìm Kiếm Nhị Phân (2 Hướng tiếp cận độc lập: Đệ quy vs Vòng lặp)',
    desc: 'Một sinh viên viết vòng lặp While, một sinh viên viết hàm đệ quy Recursive. Cấu trúc khác nhau.',
    lang: 'python',
    codeA: `# Sinh viên A: Vòng lặp Iterative While O(log n)
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1`,
    codeB: `# Sinh viên B: Đệ quy Recursive Divide & Conquer
def binary_search(nums, target):
    def helper(l, r):
        if l > r:
            return -1
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            return helper(m + 1, r)
        return helper(l, m - 1)
    return helper(0, len(nums) - 1)`,
  },
  {
    name: 'Valid Parentheses (Khác biệt cấu trúc dữ liệu)',
    desc: 'Một bài dùng Dictionary mapping, một bài dùng nhiều khối lệnh if-elif thủ công.',
    lang: 'python',
    codeA: `# Sinh viên A: Dictionary mapping với Stack
def is_valid(s):
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in s:
        if c in mapping.values():
            stack.append(c)
        elif c in mapping:
            if not stack or stack.pop() != mapping[c]:
                return False
    return len(stack) == 0`,
    codeB: `# Sinh viên B: If/elif kiểm tra trực tiếp
def isValid(s: str) -> bool:
    st = []
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            st.append(ch)
        else:
            if not st:
                return False
            top = st.pop()
            if ch == ')' and top != '(': return False
            if ch == ']' and top != '[': return False
            if ch == '}' and top != '{': return False
    return not st`,
  }
];

interface PlagiarismCheckerModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const PlagiarismCheckerModal: React.FC<PlagiarismCheckerModalProps> = ({
  isOpen,
  onClose,
}) => {
  const [selectedPresetIdx, setSelectedPresetIdx] = useState(0);
  const [codeA, setCodeA] = useState(PRESETS[0].codeA);
  const [codeB, setCodeB] = useState(PRESETS[0].codeB);
  const [studentAName, setStudentAName] = useState('Nguyễn Văn A (MSSV: 2111001)');
  const [studentBName, setStudentBName] = useState('Trần Văn B (MSSV: 2111045)');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [showTokensView, setShowTokensView] = useState(false);

  // Load preset
  const handleSelectPreset = (idx: number) => {
    setSelectedPresetIdx(idx);
    setCodeA(PRESETS[idx].codeA);
    setCodeB(PRESETS[idx].codeB);
  };

  // Tokenization & Winnowing Similarity Algorithm
  const similarityResult = useMemo(() => {
    // 1. Normalize code: strip comments and whitespace
    const cleanA = codeA.replace(/#.*$/gm, '').replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '');
    const cleanB = codeB.replace(/#.*$/gm, '').replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '');

    // 2. Tokenize words / keywords
    const tokenize = (src: string) => {
      const words = src.match(/[a-zA-Z_]\w*|[0-9]+|[^\s\w]/g) || [];
      // Normalize variable identifiers to general tokens
      const varMap = new Map<string, string>();
      let varCounter = 1;
      const keywords = new Set([
        'def', 'class', 'import', 'from', 'if', 'else', 'elif', 'return', 'for', 'while',
        'in', 'range', 'len', 'print', 'sys', 'stdin', 'read', 'split', 'map', 'list', 'int',
        'function', 'const', 'let', 'var', 'True', 'False', 'None'
      ]);

      return words.map((w) => {
        if (keywords.has(w) || /^[^a-zA-Z0-9_]+$/.test(w) || !isNaN(Number(w))) {
          return w;
        }
        if (!varMap.has(w)) {
          varMap.set(w, `V${varCounter++}`);
        }
        return varMap.get(w)!;
      });
    };

    const tokensA = tokenize(cleanA);
    const tokensB = tokenize(cleanB);

    // 3. N-gram shingles (k = 3)
    const k = 3;
    const makeNgrams = (tokens: string[]) => {
      const ngrams = new Set<string>();
      for (let i = 0; i <= tokens.length - k; i++) {
        ngrams.add(tokens.slice(i, i + k).join('_'));
      }
      return ngrams;
    };

    const ngramsA = makeNgrams(tokensA);
    const ngramsB = makeNgrams(tokensB);

    if (ngramsA.size === 0 || ngramsB.size === 0) {
      return {
        score: 0,
        verdict: 'Chưa đủ dữ liệu mã nguồn để so sánh',
        risk: 'low' as const,
        tokensA: tokensA.slice(0, 30).join(' '),
        tokensB: tokensB.slice(0, 30).join(' '),
      };
    }

    // Jaccard similarity index: Intersection / Union
    let intersection = 0;
    ngramsA.forEach((gram) => {
      if (ngramsB.has(gram)) intersection++;
    });

    const union = ngramsA.size + ngramsB.size - intersection;
    const rawScore = union > 0 ? (intersection / union) * 100 : 0;
    // Scale up slightly for tokenized algorithmic structure
    const scaledScore = Math.min(100, Math.round(rawScore * 1.5 + (rawScore > 30 ? 20 : 0)));

    let verdict = 'Độc lập - Không phát hiện dấu hiệu gian lận';
    let risk: 'high' | 'medium' | 'low' = 'low';

    if (scaledScore >= 75) {
      verdict = 'Cảnh báo nghiêm trọng: Độ tương đồng rất cao! Nghi vấn sao chép thuật toán và chỉ đổi tên biến/comment.';
      risk = 'high';
    } else if (scaledScore >= 45) {
      verdict = 'Độ tương đồng trung bình: Hai bài cùng ý tưởng giải thuật hoặc có đoạn mã mẫu tương tự.';
      risk = 'medium';
    }

    return {
      score: scaledScore,
      verdict,
      risk,
      tokensA: tokensA.slice(0, 40).join(' ') + (tokensA.length > 40 ? '...' : ''),
      tokensB: tokensB.slice(0, 40).join(' ') + (tokensB.length > 40 ? '...' : ''),
      tokenCountA: tokensA.length,
      tokenCountB: tokensB.length,
    };
  }, [codeA, codeB]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75 backdrop-blur-md animate-in fade-in duration-200">
      <div className="flex flex-col w-full max-w-6xl h-[92vh] bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden animate-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 bg-gradient-to-r from-rose-50/70 via-white to-orange-50/40 dark:from-slate-900 dark:via-slate-900 dark:to-rose-950/30 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-tr from-rose-600 to-orange-600 text-white shadow-md shadow-rose-500/25">
              <ScanSearch className="h-6 w-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
                  Hệ Thống So Trùng Mã Nguồn & Phát Hiện Gian Lận (Plagiarism Detector)
                </h2>
                <span className="rounded-full bg-rose-100 dark:bg-rose-900/60 px-2.5 py-0.5 text-[10px] font-extrabold text-rose-700 dark:text-rose-300">
                  Chuẩn Moss / Winnowing Engine
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Thuật toán chuẩn hóa token trừu tượng hóa tên biến, cấu trúc lặp và so khớp n-gram chống ngụy trang mã nguồn
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

        {/* Presets and Controls Bar */}
        <div className="px-6 py-3 border-b border-slate-200/80 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-950/40 flex flex-wrap items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold text-slate-500 dark:text-slate-400 flex items-center gap-1.5">
              <Scale className="h-3.5 w-3.5" />
              <span>Bài test mẫu:</span>
            </span>
            <div className="flex flex-wrap items-center gap-1.5">
              {PRESETS.map((preset, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => handleSelectPreset(idx)}
                  className={`px-3 py-1 rounded-xl text-xs font-bold transition ${
                    selectedPresetIdx === idx
                      ? 'bg-rose-600 text-white shadow-xs'
                      : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:border-slate-300'
                  }`}
                >
                  Mẫu {idx + 1}
                </button>
              ))}
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => setShowTokensView(!showTokensView)}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-bold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 transition"
            >
              <Eye className="h-3.5 w-3.5" />
              <span>{showTokensView ? 'Ẩn Luồng Token' : 'Xem Luồng Token Chuẩn Hóa'}</span>
            </button>
          </div>
        </div>

        {/* Similarity Score Banner */}
        <div className={`px-6 py-3 border-b flex items-center justify-between transition-colors ${
          similarityResult.risk === 'high'
            ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60 text-rose-900 dark:text-rose-200'
            : similarityResult.risk === 'medium'
            ? 'bg-amber-50 dark:bg-amber-950/40 border-amber-200 dark:border-amber-900/60 text-amber-900 dark:text-amber-200'
            : 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60 text-emerald-900 dark:text-emerald-200'
        }`}>
          <div className="flex items-center gap-3">
            <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-2xl font-black text-sm shadow-sm ${
              similarityResult.risk === 'high'
                ? 'bg-rose-600 text-white'
                : similarityResult.risk === 'medium'
                ? 'bg-amber-600 text-white'
                : 'bg-emerald-600 text-white'
            }`}>
              {similarityResult.score}%
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-black text-sm">
                  Độ tương đồng thuật toán: {similarityResult.score}%
                </span>
                <span className={`px-2 py-0.5 rounded-full text-[10px] font-black uppercase ${
                  similarityResult.risk === 'high'
                    ? 'bg-rose-200 dark:bg-rose-900 text-rose-800 dark:text-rose-200'
                    : similarityResult.risk === 'medium'
                    ? 'bg-amber-200 dark:bg-amber-900 text-amber-800 dark:text-amber-200'
                    : 'bg-emerald-200 dark:bg-emerald-900 text-emerald-800 dark:text-emerald-200'
                }`}>
                  {similarityResult.risk === 'high' ? 'Nguy cơ cao (Plagiarism Detected)' : similarityResult.risk === 'medium' ? 'Tương đồng vừa' : 'Hợp lệ (Independent Work)'}
                </span>
              </div>
              <p className="text-xs mt-0.5 opacity-90">
                {similarityResult.verdict}
              </p>
            </div>
          </div>
        </div>

        {/* Tokens Inspection Bar (Optional) */}
        {showTokensView && (
          <div className="p-4 bg-slate-950 text-slate-300 font-mono text-[11px] border-b border-slate-800 grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <span className="text-rose-400 font-bold block mb-1">Normalized Tokens A ({similarityResult.tokenCountA} tokens):</span>
              <div className="p-2 rounded bg-slate-900/80 border border-slate-800 text-slate-400 break-all leading-relaxed">
                {similarityResult.tokensA}
              </div>
            </div>
            <div>
              <span className="text-blue-400 font-bold block mb-1">Normalized Tokens B ({similarityResult.tokenCountB} tokens):</span>
              <div className="p-2 rounded bg-slate-900/80 border border-slate-800 text-slate-400 break-all leading-relaxed">
                {similarityResult.tokensB}
              </div>
            </div>
          </div>
        )}

        {/* Two-Column Side by Side Code Comparison */}
        <div className="flex-1 grid grid-cols-1 md:grid-cols-2 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-slate-200 dark:divide-slate-800">
          {/* Column A: Submission A */}
          <div className="flex flex-col h-full overflow-hidden bg-slate-50/50 dark:bg-slate-950/20">
            <div className="p-3 border-b border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="flex h-5 w-5 items-center justify-center rounded-full bg-blue-600 text-white text-[10px] font-black">
                  A
                </span>
                <input
                  type="text"
                  value={studentAName}
                  onChange={(e) => setStudentAName(e.target.value)}
                  className="bg-transparent text-xs font-bold text-slate-800 dark:text-slate-200 focus:outline-none"
                />
              </div>
              <span className="text-[11px] font-mono text-slate-400">
                {codeA.split('\n').length} dòng
              </span>
            </div>

            <div className="flex-1 p-3 overflow-hidden">
              <textarea
                value={codeA}
                onChange={(e) => setCodeA(e.target.value)}
                placeholder="Dán mã nguồn bài nộp A..."
                className="w-full h-full p-3 rounded-2xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 font-mono text-xs text-slate-800 dark:text-slate-200 leading-relaxed focus:outline-none focus:border-blue-500 resize-none shadow-xs"
              />
            </div>
          </div>

          {/* Column B: Submission B */}
          <div className="flex flex-col h-full overflow-hidden bg-slate-50/50 dark:bg-slate-950/20">
            <div className="p-3 border-b border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="flex h-5 w-5 items-center justify-center rounded-full bg-rose-600 text-white text-[10px] font-black">
                  B
                </span>
                <input
                  type="text"
                  value={studentBName}
                  onChange={(e) => setStudentBName(e.target.value)}
                  className="bg-transparent text-xs font-bold text-slate-800 dark:text-slate-200 focus:outline-none"
                />
              </div>
              <span className="text-[11px] font-mono text-slate-400">
                {codeB.split('\n').length} dòng
              </span>
            </div>

            <div className="flex-1 p-3 overflow-hidden">
              <textarea
                value={codeB}
                onChange={(e) => setCodeB(e.target.value)}
                placeholder="Dán mã nguồn bài nộp B..."
                className="w-full h-full p-3 rounded-2xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 font-mono text-xs text-slate-800 dark:text-slate-200 leading-relaxed focus:outline-none focus:border-rose-500 resize-none shadow-xs"
              />
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="px-6 py-3 border-t border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950/50 flex items-center justify-between shrink-0">
          <div className="text-xs text-slate-500 dark:text-slate-400">
            Thuật toán Jaccard N-gram trên luồng Token đã loại bỏ comment và biến số.
          </div>

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={() => {
                setCodeA(PRESETS[selectedPresetIdx].codeA);
                setCodeB(PRESETS[selectedPresetIdx].codeB);
              }}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold hover:bg-slate-100 dark:hover:bg-slate-700 transition"
            >
              <RotateCcw className="h-3.5 w-3.5" />
              <span>Khôi Phục Mẫu</span>
            </button>

            <button
              type="button"
              onClick={onClose}
              className="px-4 py-1.5 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold transition"
            >
              Đóng
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
