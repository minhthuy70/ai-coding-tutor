'use client';

import React, { useState } from 'react';
import { 
  X, 
  Sparkles, 
  Lightbulb, 
  Bug, 
  Zap, 
  CheckCheck, 
  ShieldAlert, 
  HelpCircle,
  Search,
  ArrowRight
} from 'lucide-react';

interface PromptTemplate {
  id: string;
  category: 'socratic' | 'debug' | 'bigo' | 'cleancode' | 'testcase';
  title: string;
  prompt: string;
  icon: 'lightbulb' | 'bug' | 'zap' | 'check' | 'shield';
  description: string;
}

const TEMPLATES: PromptTemplate[] = [
  {
    id: 'soc-1',
    category: 'socratic',
    title: 'Gợi ý giải thuật bước 1 (Không lộ code)',
    icon: 'lightbulb',
    description: 'Yêu cầu gia sư đặt câu hỏi dẫn dắt từng bước để bạn tự tư duy.',
    prompt: 'Em đang làm bài toán này nhưng chưa biết bắt đầu từ đâu. Thầy/Cô hãy cho em một gợi ý hướng tiếp cận (Hint 1) dạng câu hỏi phản biện, xin đừng đưa ngay code giải sẵn nhé!'
  },
  {
    id: 'soc-2',
    category: 'socratic',
    title: 'Chẩn đoán quan niệm sai lầm (Misconception)',
    icon: 'lightbulb',
    description: 'Hỏi AI vì sao suy luận ban đầu của bạn chưa đúng.',
    prompt: 'Em đang tư duy giải quyết vấn đề theo hướng này: [mô tả ý tưởng của bạn]. Thầy/Cô chỉ ra giúp em quan niệm sai lầm trong logic này và tại sao nó không áp dụng được cho mọi trường hợp?'
  },
  {
    id: 'bigo-1',
    category: 'bigo',
    title: 'Phân tích độ phức tạp thời gian & không gian Big-O',
    icon: 'zap',
    description: 'Ước tính Big-O chi tiết từng vòng lặp và bộ nhớ phụ trợ.',
    prompt: 'Hãy phân tích độ phức tạp thời gian (Time Complexity) và không gian bộ nhớ (Space Complexity) của đoạn mã sau theo ký hiệu Big-O. Giải thích chi tiết từng vòng lặp và đệ quy:'
  },
  {
    id: 'bigo-2',
    category: 'bigo',
    title: 'Tối ưu hóa từ O(n²) xuống O(n log n) hoặc O(n)',
    icon: 'zap',
    description: 'Đề xuất cấu trúc dữ liệu mới như Hash Map, Heap, Binary Search.',
    prompt: 'Thuật toán hiện tại của tôi đang có độ phức tạp O(n²). Hãy gợi ý cách cấu trúc lại dữ liệu (ví dụ: dùng Hash Map, Hai con trỏ Two Pointers, hoặc Quy hoạch động) để tối ưu xuống O(n) hoặc O(n log n).'
  },
  {
    id: 'debug-1',
    category: 'debug',
    title: 'Giải thích mã lỗi & Tìm dòng gây Crash',
    icon: 'bug',
    description: 'Dịch thông báo lỗi compiler/runtime sang tiếng Việt dễ hiểu.',
    prompt: 'Đoạn mã của tôi gặp lỗi thông báo sau: [dán thông báo lỗi]. Hãy giải thích nguyên nhân gốc rễ (Root Cause) bằng tiếng Việt và chỉ ra dòng nào cần chỉnh sửa.'
  },
  {
    id: 'debug-2',
    category: 'debug',
    title: 'Bắt lỗi Segmentation Fault & Dangling Pointer C++',
    icon: 'shield',
    description: 'Rà soát lỗi con trỏ, mảng vượt chỉ số và cấp phát động.',
    prompt: 'Tôi đang viết code C/C++ và bị lỗi Segmentation Fault (Core Dumped). Hãy kiểm tra giúp tôi các lỗi truy cập mảng ngoài phạm vi (Out of bounds), con trỏ rác (Dangling pointer) hoặc vùng nhớ chưa malloc/new.'
  },
  {
    id: 'test-1',
    category: 'testcase',
    title: 'Sinh 5 bộ Test Cases hiểm & Edge Cases',
    icon: 'check',
    description: 'Kiểm thử mảng rỗng, giá trị âm, số cực đại, dãy đối xứng.',
    prompt: 'Hãy tạo cho tôi 5 bộ test cases (gồm Input và Expected Output) bao gồm cả trường hợp thông thường và các trường hợp biên hiểm hóc (Edge cases: n = 0, mảng rỗng, số nguyên âm, số cực đại INT_MAX) cho bài toán sau:'
  },
  {
    id: 'clean-1',
    category: 'cleancode',
    title: 'Rà soát chuẩn Clean Code & PEP 8 / Google Style',
    icon: 'check',
    description: 'Chuẩn hóa đặt tên biến, tách hàm con và loại bỏ code smells.',
    prompt: 'Hãy review đoạn code này theo nguyên tắc Clean Code và chuẩn phong cách (PEP 8 cho Python / Google Style cho C++). Gợi ý cách đặt tên biến rõ nghĩa và tách hàm con nhỏ gọn hơn.'
  }
];

interface PromptTemplatesModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectPrompt: (promptText: string) => void;
}

export const PromptTemplatesModal: React.FC<PromptTemplatesModalProps> = ({
  isOpen,
  onClose,
  onSelectPrompt,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeCategory, setActiveCategory] = useState<string>('all');

  if (!isOpen) return null;

  const filteredTemplates = TEMPLATES.filter((tpl) => {
    const matchesCategory = activeCategory === 'all' || tpl.category === activeCategory;
    const matchesSearch = 
      tpl.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tpl.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tpl.prompt.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const getCategoryIcon = (iconName: string) => {
    switch (iconName) {
      case 'lightbulb': return <Lightbulb className="h-4 w-4 text-amber-500" />;
      case 'bug': return <Bug className="h-4 w-4 text-rose-500" />;
      case 'zap': return <Zap className="h-4 w-4 text-amber-400" />;
      case 'shield': return <ShieldAlert className="h-4 w-4 text-purple-500" />;
      default: return <Sparkles className="h-4 w-4 text-blue-500" />;
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs animate-in fade-in duration-200">
      <div 
        className="relative flex flex-col w-full max-w-2xl max-h-[85vh] bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-slate-100 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-950">
          <div className="flex items-center gap-2.5">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-tr from-amber-500 to-orange-500 text-white shadow-xs">
              <Sparkles className="h-5 w-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-slate-900 dark:text-slate-100">
                Kho Mẫu Câu Hỏi & Gợi Ý Sư Phạm
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                Chọn câu hỏi mẫu chuẩn phong cách gia sư Socratic để AI hỗ trợ học tập hiệu quả nhất
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Search & Categories Bar */}
        <div className="p-4 border-b border-slate-100 dark:border-slate-800 space-y-3 bg-white dark:bg-slate-900">
          <div className="relative flex items-center">
            <Search className="absolute left-3 h-4 w-4 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm kiếm mẫu câu hỏi theo từ khóa..."
              className="w-full rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 pl-9 pr-3 py-2 text-xs text-slate-800 dark:text-slate-200 placeholder-slate-400 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500/20"
            />
          </div>

          <div className="flex flex-wrap gap-1.5 text-xs">
            {[
              { id: 'all', label: 'Tất cả' },
              { id: 'socratic', label: '💡 Gia sư Socratic' },
              { id: 'bigo', label: '⚡ Big-O & Tối ưu' },
              { id: 'debug', label: '🐛 Debug & Bắt lỗi' },
              { id: 'testcase', label: '🧪 Test Cases' },
              { id: 'cleancode', label: '🧼 Clean Code' },
            ].map((cat) => (
              <button
                key={cat.id}
                type="button"
                onClick={() => setActiveCategory(cat.id)}
                className={`px-3 py-1 rounded-lg font-medium transition ${
                  activeCategory === cat.id
                    ? 'bg-blue-600 text-white shadow-xs'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>

        {/* Templates List */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2.5">
          {filteredTemplates.length === 0 ? (
            <div className="text-center py-8 text-xs text-slate-400">
              Không tìm thấy mẫu câu hỏi phù hợp.
            </div>
          ) : (
            filteredTemplates.map((item) => (
              <button
                key={item.id}
                type="button"
                onClick={() => {
                  onSelectPrompt(item.prompt);
                  onClose();
                }}
                className="w-full text-left p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950/60 hover:bg-blue-50/50 dark:hover:bg-blue-950/30 hover:border-blue-300 dark:hover:border-blue-700 transition group flex items-start justify-between gap-3 shadow-2xs"
              >
                <div className="flex items-start gap-3">
                  <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-100 dark:bg-slate-800 shrink-0 mt-0.5">
                    {getCategoryIcon(item.icon)}
                  </div>
                  <div>
                    <h4 className="font-bold text-xs sm:text-sm text-slate-900 dark:text-slate-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">
                      {item.title}
                    </h4>
                    <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                      {item.description}
                    </p>
                    <p className="text-[11px] font-mono text-slate-400 dark:text-slate-500 line-clamp-1 mt-1 bg-slate-50 dark:bg-slate-900 px-2 py-0.5 rounded border border-slate-100 dark:border-slate-800">
                      &quot;{item.prompt}&quot;
                    </p>
                  </div>
                </div>

                <div className="flex h-7 w-7 items-center justify-center rounded-lg text-slate-400 group-hover:text-blue-600 group-hover:bg-blue-100 dark:group-hover:bg-blue-900/40 shrink-0 transition">
                  <ArrowRight className="h-4 w-4" />
                </div>
              </button>
            ))
          )}
        </div>

        {/* Footer */}
        <div className="px-5 py-3 border-t border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 flex items-center justify-between text-xs text-slate-500">
          <span>Nhấp vào bất kỳ mẫu nào để chèn vào ô nhập câu hỏi.</span>
          <button
            type="button"
            onClick={onClose}
            className="px-3 py-1.5 rounded-lg border border-slate-300 dark:border-slate-700 font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            Đóng
          </button>
        </div>
      </div>
    </div>
  );
};
