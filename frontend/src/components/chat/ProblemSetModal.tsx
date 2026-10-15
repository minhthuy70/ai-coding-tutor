'use client';

import React, { useState, useMemo } from 'react';
import {
  X,
  Code2,
  Trophy,
  Search,
  Filter,
  CheckCircle2,
  Play,
  Sparkles,
  ArrowRight,
  Clock,
  Tag,
  AlertCircle,
  HelpCircle,
  Cpu,
  Flame,
  ChevronRight
} from 'lucide-react';

export interface CodingProblem {
  id: string;
  number: number;
  title: string;
  difficulty: 'Dễ' | 'Trung bình' | 'Khó';
  category: 'Array' | 'String' | 'LinkedList' | 'Stack' | 'Tree' | 'DP' | 'BinarySearch' | 'SQL';
  acceptanceRate: string;
  description: string;
  inputDesc: string;
  outputDesc: string;
  constraints: string[];
  examples: {
    input: string;
    output: string;
    explanation?: string;
  }[];
  starterCode: {
    python: string;
    javascript?: string;
    cpp?: string;
  };
  testCases: {
    id: number;
    name: string;
    input: string;
    expectedOutput: string;
  }[];
  hintPrompt: string;
}

interface ProblemSetModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSolveInSandbox: (problem: CodingProblem, language: string) => void;
  onAskAIHint: (prompt: string) => void;
}

export const PROBLEMS_DATA: CodingProblem[] = [
  {
    id: 'prob-01',
    number: 1,
    title: 'Hai Con Số Có Tổng Bằng Target (Two Sum)',
    difficulty: 'Dễ',
    category: 'Array',
    acceptanceRate: '89.4%',
    description: 'Cho một mảng số nguyên `nums` và một số nguyên `target`. Hãy tìm vị trí (chỉ số index) của hai số trong mảng sao cho tổng của chúng đúng bằng `target`.\n\nGiả định rằng mỗi bộ dữ liệu đầu vào luôn có chính xác một phương án giải quyết và bạn không được sử dụng cùng một phần tử hai lần.',
    inputDesc: 'Dòng 1: Target\nDòng 2: Mảng số nguyên cách nhau bởi dấu cách',
    outputDesc: 'In ra 2 chỉ số [i, j] cách nhau bởi dấu cách (theo thứ tự tăng dần)',
    constraints: ['2 <= nums.length <= 10^4', '-10^9 <= nums[i] <= 10^9', '-10^9 <= target <= 10^9', 'Chỉ tồn tại duy nhất một nghiệm đúng'],
    examples: [
      { input: '9\n2 7 11 15', output: '0 1', explanation: 'nums[0] + nums[1] == 2 + 7 == 9, trả về 0 1.' },
      { input: '6\n3 2 4', output: '1 2', explanation: 'nums[1] + nums[2] == 2 + 4 == 6, trả về 1 2.' }
    ],
    starterCode: {
      python: `# Bài toán Two Sum: O(n) thời gian dùng Hash Map
import sys

def two_sum():
    lines = sys.stdin.read().strip().split('\\n')
    if len(lines) < 2:
        return
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
      javascript: `const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\\n');
if (input.length >= 2) {
  const target = parseInt(input[0].trim());
  const nums = input[1].trim().split(/\\s+/).map(Number);
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (seen.has(diff)) {
      console.log(\`\${seen.get(diff)} \${i}\`);
      process.exit(0);
    }
    seen.set(nums[i], i);
  }
}`
    },
    testCases: [
      { id: 1, name: 'Test 1 (Cơ bản)', input: '9\n2 7 11 15', expectedOutput: '0 1' },
      { id: 2, name: 'Test 2 (Chỉ số cuối)', input: '6\n3 2 4', expectedOutput: '1 2' },
      { id: 3, name: 'Test 3 (Hai số giống nhau)', input: '6\n3 3', expectedOutput: '0 1' }
    ],
    hintPrompt: 'Tôi đang làm bài toán Two Sum. Thay vì dùng 2 vòng lặp lồng $O(n^2)$, hãy dùng phương pháp Socratic gợi ý cho tôi cách dùng cấu trúc dữ liệu Hash Table (Dictionary trong Python) để giảm độ phức tạp thời gian xuống $O(n)$ mà không đưa ra code hoàn chỉnh ngay.'
  },
  {
    id: 'prob-02',
    number: 2,
    title: 'Kiểm Tra Chuỗi Ngoặc Hợp Lệ (Valid Parentheses)',
    difficulty: 'Dễ',
    category: 'Stack',
    acceptanceRate: '78.5%',
    description: 'Cho một chuỗi `s` chỉ chứa các ký tự ngoặc `(`, `)`, `{`, `}`, `[` và `]`.\nHãy xác định xem chuỗi đầu vào có hợp lệ hay không.\n\nMột chuỗi hợp lệ nếu:\n1. Các ngoặc mở phải được đóng bằng ngoặc cùng loại.\n2. Các ngoặc mở phải được đóng theo đúng thứ tự (LIFO).',
    inputDesc: 'Một dòng duy nhất chứa chuỗi các ký tự ngoặc',
    outputDesc: 'In ra "true" nếu chuỗi hợp lệ, ngược lại in ra "false"',
    constraints: ['1 <= s.length <= 10^4', 's chỉ chứa các ký tự ()[]{}'],
    examples: [
      { input: '()[]{}', output: 'true', explanation: 'Các cặp ngoặc đóng mở đúng thứ tự.' },
      { input: '(]', output: 'false', explanation: 'Ngoặc tròn mở nhưng lại đóng bằng ngoặc vuông.' }
    ],
    starterCode: {
      python: `# Kiểm tra tính hợp lệ của chuỗi ngoặc dùng Stack
import sys

def is_valid_parentheses():
    s = sys.stdin.read().strip()
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                print("false")
                return
    print("true" if len(stack) == 0 else "false")

is_valid_parentheses()`,
    },
    testCases: [
      { id: 1, name: 'Test 1 (Đơn giản)', input: '()[]{}', expectedOutput: 'true' },
      { id: 2, name: 'Test 2 (Lồng nhau)', input: '{[()]}', expectedOutput: 'true' },
      { id: 3, name: 'Test 3 (Sai thứ tự)', input: '([)]', expectedOutput: 'false' }
    ],
    hintPrompt: 'Tôi đang làm bài kiểm tra chuỗi ngoặc hợp lệ (Valid Parentheses). Hãy đóng vai gia sư Socratic, giải thích tại sao Stack (Ngăn xếp) với tính chất LIFO lại là cấu trúc dữ liệu tối ưu nhất cho bài toán này và đặt câu hỏi gợi ý cho tôi.'
  },
  {
    id: 'prob-03',
    number: 3,
    title: 'Tìm Kiếm Nhị Phân (Binary Search)',
    difficulty: 'Dễ',
    category: 'BinarySearch',
    acceptanceRate: '92.1%',
    description: 'Cho một mảng số nguyên `nums` đã được sắp xếp theo thứ tự tăng dần và một số nguyên `target`.\nHãy viết hàm tìm kiếm `target` trong mảng `nums`. Nếu `target` tồn tại, trả về chỉ số của nó, ngược lại trả về `-1`.\nThuật toán bắt buộc phải có độ phức tạp thời gian chạy $O(\\log n)$.',
    inputDesc: 'Dòng 1: Target\nDòng 2: Mảng số nguyên đã sắp xếp tăng dần',
    outputDesc: 'In ra chỉ số tìm thấy hoặc -1',
    constraints: ['1 <= nums.length <= 10^4', '-10^4 < nums[i], target < 10^4', 'Tất cả các số trong nums là duy nhất và đã sắp xếp'],
    examples: [
      { input: '9\n-1 0 3 5 9 12', output: '4', explanation: '9 tồn tại tại chỉ số 4.' },
      { input: '2\n-1 0 3 5 9 12', output: '-1', explanation: '2 không tồn tại trong mảng, in ra -1.' }
    ],
    starterCode: {
      python: `# Tìm kiếm nhị phân Binary Search O(log n)
import sys

def binary_search():
    lines = sys.stdin.read().strip().split('\\n')
    if len(lines) < 2: return
    target = int(lines[0].strip())
    nums = list(map(int, lines[1].strip().split()))
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print(mid)
            return
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(-1)

binary_search()`,
    },
    testCases: [
      { id: 1, name: 'Test 1 (Tìm thấy giữa)', input: '9\n-1 0 3 5 9 12', expectedOutput: '4' },
      { id: 2, name: 'Test 2 (Không tìm thấy)', input: '2\n-1 0 3 5 9 12', expectedOutput: '-1' },
      { id: 3, name: 'Test 3 (Phần tử đầu tiên)', input: '-1\n-1 0 3 5 9 12', expectedOutput: '0' }
    ],
    hintPrompt: 'Hãy hướng dẫn tôi tư duy Binary Search (Chia để trị). Tại sao mỗi lần so sánh ta lại có thể loại bỏ được một nửa không gian tìm kiếm? Cách tính `mid = (left + right) // 2` có nguy cơ tràn số (integer overflow) trong C++ không?'
  },
  {
    id: 'prob-04',
    number: 4,
    title: 'Hợp Nhất Các Khoảng Thời Gian (Merge Intervals)',
    difficulty: 'Trung bình',
    category: 'Array',
    acceptanceRate: '64.2%',
    description: 'Cho một danh sách các khoảng thời gian `intervals`, trong đó mỗi khoảng là `[start, end]`. Hãy hợp nhất tất cả các khoảng thời gian bị gối đầu/chồng chéo lên nhau và trả về danh sách các khoảng độc lập phủ kín tất cả các khoảng ban đầu.',
    inputDesc: 'Dòng 1: Số lượng khoảng N\nN dòng tiếp theo: Mỗi dòng gồm 2 số start end',
    outputDesc: 'In ra các khoảng sau khi hợp nhất theo định dạng "start end" trên mỗi dòng',
    constraints: ['1 <= intervals.length <= 10^4', '0 <= start <= end <= 10^4'],
    examples: [
      { input: '4\n1 3\n2 6\n8 10\n15 18', output: '1 6\n8 10\n15 18', explanation: 'Khoảng [1,3] và [2,6] gối lên nhau, được hợp nhất thành [1,6].' }
    ],
    starterCode: {
      python: `# Hợp nhất các khoảng thời gian Merge Intervals O(n log n)
import sys

def merge_intervals():
    lines = sys.stdin.read().strip().split('\\n')
    if not lines or not lines[0].strip(): return
    n = int(lines[0].strip())
    intervals = []
    for i in range(1, n + 1):
        if i < len(lines) and lines[i].strip():
            start, end = map(int, lines[i].strip().split())
            intervals.append([start, end])
            
    # Bắt đầu bằng việc sắp xếp theo điểm bắt đầu
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    for item in merged:
        print(f"{item[0]} {item[1]}")

merge_intervals()`,
    },
    testCases: [
      { id: 1, name: 'Test 1 (Gối đầu mẫu)', input: '4\n1 3\n2 6\n8 10\n15 18', expectedOutput: '1 6\n8 10\n15 18' },
      { id: 2, name: 'Test 2 (Chứa trọn)', input: '2\n1 4\n2 3', expectedOutput: '1 4' }
    ],
    hintPrompt: 'Tôi đang giải bài toán Merge Intervals. Tại sao bước sắp xếp các khoảng theo thời điểm bắt đầu `start` lại là mấu chốt quyết định giúp ta giải bài toán trong 1 lượt duyệt duy nhất?'
  },
  {
    id: 'prob-05',
    number: 5,
    title: 'Dãy Con Tăng Dài Nhất (Longest Increasing Subsequence)',
    difficulty: 'Trung bình',
    category: 'DP',
    acceptanceRate: '56.8%',
    description: 'Cho một mảng số nguyên `nums`. Hãy tìm độ dài của dãy con tăng nghiêm ngặt dài nhất (Longest Increasing Subsequence - LIS).\nMột dãy con được tạo ra bằng cách xóa đi 0 hoặc nhiều phần tử mà vẫn giữ nguyên thứ tự tương đối của các phần tử còn lại.',
    inputDesc: 'Mảng số nguyên phân tách bởi dấu cách',
    outputDesc: 'In ra 1 số nguyên là độ dài của dãy con tăng dài nhất',
    constraints: ['1 <= nums.length <= 2500', '-10^4 <= nums[i] <= 10^4'],
    examples: [
      { input: '10 9 2 5 3 7 101 18', output: '4', explanation: 'Dãy con tăng dài nhất là [2, 3, 7, 101], có độ dài 4.' },
      { input: '0 1 0 3 2 3', output: '4', explanation: 'Dãy con tăng dài nhất là [0, 1, 2, 3], độ dài 4.' }
    ],
    starterCode: {
      python: `# Dãy con tăng dài nhất LIS bằng Quy hoạch động O(n^2)
import sys

def longest_increasing_subsequence():
    raw = sys.stdin.read().strip()
    if not raw: return
    nums = list(map(int, raw.split()))
    if not nums:
        print(0)
        return
        
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    print(max(dp))

longest_increasing_subsequence()`,
    },
    testCases: [
      { id: 1, name: 'Test 1 (Mẫu LeetCode)', input: '10 9 2 5 3 7 101 18', expectedOutput: '4' },
      { id: 2, name: 'Test 2 (Mảng tăng sẵn)', input: '1 2 3 4 5', expectedOutput: '5' },
      { id: 3, name: 'Test 3 (Mảng bằng nhau)', input: '7 7 7 7 7', expectedOutput: '1' }
    ],
    hintPrompt: 'Hãy hướng dẫn tôi xây dựng công thức chuyển trạng thái Quy hoạch động cho bài toán Dãy con tăng dài nhất (LIS). Định nghĩa mảng `dp[i]` ở đây đại diện cho ý nghĩa gì?'
  },
  {
    id: 'prob-06',
    number: 6,
    title: 'Đếm Số Lượng Đảo Trong Ma Trận (Number of Islands)',
    difficulty: 'Trung bình',
    category: 'Tree',
    acceptanceRate: '58.3%',
    description: 'Cho một lưới ma trận nhị phân `grid` kích thước `m x n` đại diện cho bản đồ gồm nước biển ("0") và đất liền ("1").\nMột hòn đảo được bao quanh bởi nước và được hình thành bằng cách liên kết các ô đất liền kề nhau theo chiều ngang hoặc chiều dọc.\nHãy đếm tổng số lượng hòn đảo độc lập.',
    inputDesc: 'Dòng 1: Kích thước m n\nm dòng tiếp theo: Mỗi dòng gồm n ký tự 0 hoặc 1 cách nhau bởi khoảng trắng',
    outputDesc: 'In ra số lượng đảo',
    constraints: ['1 <= m, n <= 300', 'grid[i][j] chỉ nhận giá trị "0" hoặc "1"'],
    examples: [
      { input: '4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0', output: '1', explanation: 'Tất cả các ô 1 đều nối liền với nhau tạo thành 1 đảo duy nhất.' },
      { input: '4 5\n1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1', output: '3', explanation: 'Có 3 cụm đất liền biệt lập.' }
    ],
    starterCode: {
      python: `# Đếm số lượng đảo bằng thuật toán duyệt đồ thị DFS O(m * n)
import sys

def num_islands():
    lines = sys.stdin.read().strip().split('\\n')
    if not lines: return
    m, n = map(int, lines[0].strip().split())
    grid = []
    for i in range(1, m + 1):
        if i < len(lines):
            grid.append(lines[i].strip().split())
            
    islands = 0
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '0' # Đánh dấu đã thăm (chìm ô đất)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
                
    print(islands)

num_islands()`,
    },
    testCases: [
      { id: 1, name: 'Test 1 (1 đảo lớn)', input: '4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0', expectedOutput: '1' },
      { id: 2, name: 'Test 2 (3 đảo riêng biệt)', input: '4 5\n1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1', expectedOutput: '3' }
    ],
    hintPrompt: 'Hãy dùng phương pháp gợi mở Socratic giải thích bài toán Number of Islands. Tại sao kỹ thuật "làm chìm đảo" (sink the island - đánh dấu ô 1 thành 0 sau khi thăm) lại giúp chúng ta không cần dùng thêm mảng phụ `visited`?'
  },
  {
    id: 'prob-07',
    number: 7,
    title: 'SQL: Nhân Viên Lương Cao Thứ Hai (Second Highest Salary)',
    difficulty: 'Dễ',
    category: 'SQL',
    acceptanceRate: '72.3%',
    description: 'Viết câu lệnh SQL để tìm mức lương cao thứ hai trong bảng `Employee`. Nếu không có mức lương cao thứ hai (ví dụ bảng chỉ có 1 nhân viên hoặc tất cả cùng lương), kết quả trả về phải là `NULL`.\n\nCấu trúc bảng `Employee`:\n- `id` (INT, Primary Key)\n- `salary` (INT)',
    inputDesc: 'Bảng dữ liệu Employee có sẵn trong database',
    outputDesc: 'Một cột có tên SecondHighestSalary',
    constraints: ['1 <= số bản ghi <= 10^5'],
    examples: [
      { input: 'id | salary\n 1 | 100\n 2 | 200\n 3 | 300', output: '200', explanation: 'Mức lương cao nhất là 300, cao thứ 2 là 200.' }
    ],
    starterCode: {
      python: `-- SQL: Tìm mức lương cao thứ 2 xử lý trường hợp NULL
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);`,
    },
    testCases: [
      { id: 1, name: 'Test 1 (Đầy đủ 3 lương)', input: '1 100\n2 200\n3 300', expectedOutput: '200' }
    ],
    hintPrompt: 'Làm thế nào để tìm mức lương cao thứ 2 trong SQL? Tại sao dùng `LIMIT 1 OFFSET 1` đơn thuần có thể bị lỗi khi bảng không có mức lương thứ 2? Hãy hướng dẫn tôi cách dùng `MAX()` hoặc Subquery.'
  }
];

export const ProblemSetModal: React.FC<ProblemSetModalProps> = ({
  isOpen,
  onClose,
  onSolveInSandbox,
  onAskAIHint,
}) => {
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('all');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [activeProblemId, setActiveProblemId] = useState<string>(PROBLEMS_DATA[0].id);

  const filteredProblems = useMemo(() => {
    return PROBLEMS_DATA.filter((p) => {
      const matchDiff = selectedDifficulty === 'all' || p.difficulty === selectedDifficulty;
      const matchCat = selectedCategory === 'all' || p.category === selectedCategory;
      const matchQuery = 
        searchQuery.trim() === '' ||
        p.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        p.description.toLowerCase().includes(searchQuery.toLowerCase());
      return matchDiff && matchCat && matchQuery;
    });
  }, [selectedDifficulty, selectedCategory, searchQuery]);

  const activeProblem = useMemo(() => {
    return PROBLEMS_DATA.find((p) => p.id === activeProblemId) || PROBLEMS_DATA[0];
  }, [activeProblemId]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-900/60 dark:bg-black/75 backdrop-blur-md animate-fade-in">
      <div className="flex flex-col w-full max-w-6xl h-[90vh] bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden animate-scale-in">
        
        {/* Header */}
        <div className="px-6 py-4.5 border-b border-slate-200/80 dark:border-slate-800 bg-gradient-to-r from-slate-50 via-white to-amber-50/30 dark:from-slate-900 dark:via-slate-900 dark:to-amber-950/20 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-tr from-amber-500 to-rose-600 text-white shadow-md shadow-amber-500/25">
              <Trophy className="h-6 w-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
                  Đấu Trường Lập Trình & Kho Bài Tập Thực Hành
                </h2>
                <span className="rounded-full bg-amber-100 dark:bg-amber-900/60 px-2.5 py-0.5 text-[10px] font-extrabold text-amber-700 dark:text-amber-300">
                  Auto-Grader Ready
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Các bài toán thuật toán chuẩn LeetCode tích hợp bộ test case chấm điểm tức thì
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

        {/* Filter & Search Bar */}
        <div className="px-6 py-3 border-b border-slate-200/70 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/30 flex flex-wrap items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-2 flex-1 min-w-[240px] max-w-md bg-white dark:bg-slate-800 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700">
            <Search className="h-4 w-4 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm kiếm bài tập theo tên hoặc từ khóa..."
              className="w-full bg-transparent text-xs text-slate-800 dark:text-slate-100 placeholder-slate-400 focus:outline-none"
            />
            {searchQuery && (
              <button onClick={() => setSearchQuery('')} className="text-slate-400 hover:text-slate-600">
                <X className="h-3.5 w-3.5" />
              </button>
            )}
          </div>

          {/* Difficulty Filter */}
          <div className="flex items-center gap-1.5">
            <span className="text-[11px] font-bold text-slate-400 mr-1 hidden sm:inline">Độ khó:</span>
            {['all', 'Dễ', 'Trung bình', 'Khó'].map((diff) => (
              <button
                key={diff}
                type="button"
                onClick={() => setSelectedDifficulty(diff)}
                className={`px-2.5 py-1 rounded-xl text-xs font-bold transition-all ${
                  selectedDifficulty === diff
                    ? 'bg-blue-600 text-white shadow-sm'
                    : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700 hover:bg-slate-50'
                }`}
              >
                {diff === 'all' ? 'Tất cả' : diff}
              </button>
            ))}
          </div>
        </div>

        {/* Content Body: Split Left (List) & Right (Details) */}
        <div className="flex-1 flex flex-col md:flex-row min-h-0 overflow-hidden">
          
          {/* Left Column: Problem List */}
          <div className="w-full md:w-5/12 border-r border-slate-200/80 dark:border-slate-800 overflow-y-auto p-4 space-y-2 bg-slate-50/40 dark:bg-slate-900/40">
            <div className="flex items-center justify-between px-2 pb-1 text-[11px] font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
              <span>Danh sách ({filteredProblems.length} bài)</span>
              <span>Tỉ lệ đỗ</span>
            </div>

            {filteredProblems.map((prob) => {
              const isSelected = prob.id === activeProblemId;
              return (
                <div
                  key={prob.id}
                  onClick={() => setActiveProblemId(prob.id)}
                  className={`group p-3 rounded-2xl border transition-all cursor-pointer ${
                    isSelected
                      ? 'bg-white dark:bg-slate-800 border-amber-500 dark:border-amber-500 shadow-md shadow-amber-500/10'
                      : 'bg-white/80 dark:bg-slate-800/60 border-slate-200/70 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                  }`}
                >
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex items-center gap-2 min-w-0">
                      <span className="text-xs font-mono font-bold text-slate-400">
                        #{prob.number}
                      </span>
                      <h4 className={`text-xs font-extrabold truncate ${
                        isSelected ? 'text-amber-600 dark:text-amber-400' : 'text-slate-800 dark:text-slate-200'
                      }`}>
                        {prob.title}
                      </h4>
                    </div>

                    <span className="text-[10px] font-bold text-slate-400 shrink-0">
                      {prob.acceptanceRate}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 mt-2">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      prob.difficulty === 'Dễ'
                        ? 'bg-emerald-100 dark:bg-emerald-950 text-emerald-600 dark:text-emerald-300'
                        : prob.difficulty === 'Trung bình'
                        ? 'bg-amber-100 dark:bg-amber-950 text-amber-600 dark:text-amber-300'
                        : 'bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-300'
                    }`}>
                      {prob.difficulty}
                    </span>
                    <span className="text-[10px] bg-slate-100 dark:bg-slate-700 px-2 py-0.5 rounded-full text-slate-600 dark:text-slate-300 font-semibold">
                      {prob.category}
                    </span>
                    <span className="text-[10px] text-slate-400 ml-auto">
                      {prob.testCases.length} test cases
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Right Column: Problem Detail & Actions */}
          <div className="w-full md:w-7/12 flex flex-col justify-between p-6 overflow-y-auto bg-white dark:bg-slate-900">
            <div>
              {/* Header Title & Badges */}
              <div className="flex items-center gap-2 mb-2">
                <span className="text-sm font-mono font-black text-slate-400">
                  Bài tập #{activeProblem.number}
                </span>
                <span className={`text-xs font-extrabold px-2.5 py-0.5 rounded-full ${
                  activeProblem.difficulty === 'Dễ'
                    ? 'bg-emerald-100 dark:bg-emerald-950 text-emerald-600 dark:text-emerald-300'
                    : activeProblem.difficulty === 'Trung bình'
                    ? 'bg-amber-100 dark:bg-amber-950 text-amber-600 dark:text-amber-300'
                    : 'bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-300'
                }`}>
                  {activeProblem.difficulty}
                </span>
                <span className="text-xs bg-slate-100 dark:bg-slate-800 px-2.5 py-0.5 rounded-full text-slate-600 dark:text-slate-300 font-semibold">
                  Chủ đề: {activeProblem.category}
                </span>
              </div>

              <h3 className="text-xl font-black text-slate-900 dark:text-white tracking-tight mb-4">
                {activeProblem.title}
              </h3>

              {/* Description */}
              <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800 text-xs sm:text-sm text-slate-700 dark:text-slate-200 whitespace-pre-line leading-relaxed mb-4">
                {activeProblem.description}
              </div>

              {/* Input / Output Format */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                <div className="p-3 rounded-xl bg-slate-50/70 dark:bg-slate-800/40 border border-slate-100 dark:border-slate-800">
                  <div className="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 mb-1">
                    Định dạng đầu vào (Input)
                  </div>
                  <div className="text-xs text-slate-700 dark:text-slate-300 font-mono whitespace-pre-line">
                    {activeProblem.inputDesc}
                  </div>
                </div>

                <div className="p-3 rounded-xl bg-slate-50/70 dark:bg-slate-800/40 border border-slate-100 dark:border-slate-800">
                  <div className="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 mb-1">
                    Định dạng đầu ra (Output)
                  </div>
                  <div className="text-xs text-slate-700 dark:text-slate-300 font-mono whitespace-pre-line">
                    {activeProblem.outputDesc}
                  </div>
                </div>
              </div>

              {/* Examples */}
              <div className="mb-4">
                <div className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-2">
                  Ví dụ minh họa
                </div>
                <div className="space-y-2">
                  {activeProblem.examples.map((ex, i) => (
                    <div key={i} className="p-3 rounded-xl bg-slate-900 text-slate-100 text-xs font-mono">
                      <div className="text-amber-400 font-semibold mb-1">Ví dụ {i + 1}:</div>
                      <div className="text-slate-400"><span className="text-slate-300 font-bold">Input:</span> {ex.input.replace(/\n/g, ' ')}</div>
                      <div className="text-emerald-400"><span className="text-slate-300 font-bold">Output:</span> {ex.output.replace(/\n/g, ' ')}</div>
                      {ex.explanation && (
                        <div className="text-slate-400 text-[11px] font-sans mt-1 italic">
                          Giải thích: {ex.explanation}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              {/* Constraints */}
              <div className="mb-4">
                <div className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-2">
                  Ràng buộc (Constraints)
                </div>
                <ul className="list-disc list-inside text-xs text-slate-600 dark:text-slate-400 space-y-1 font-mono">
                  {activeProblem.constraints.map((c, i) => (
                    <li key={i}>{c}</li>
                  ))}
                </ul>
              </div>

            </div>

            {/* Action Buttons */}
            <div className="pt-4 border-t border-slate-200/80 dark:border-slate-800 flex flex-col sm:flex-row items-center gap-3">
              <button
                type="button"
                onClick={() => {
                  onSolveInSandbox(activeProblem, activeProblem.category === 'SQL' ? 'sql' : 'python');
                  onClose();
                }}
                className="w-full sm:flex-1 flex items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-amber-500 to-rose-600 hover:from-amber-600 hover:to-rose-700 text-white px-5 py-3 text-xs sm:text-sm font-extrabold shadow-lg shadow-amber-500/25 transition-all active:scale-[0.98]"
              >
                <Play className="h-4 w-4 fill-white" />
                <span>Giải bài trong Sandbox & Chấm Test Cases</span>
                <ArrowRight className="h-4 w-4" />
              </button>

              <button
                type="button"
                onClick={() => {
                  onAskAIHint(activeProblem.hintPrompt);
                  onClose();
                }}
                className="w-full sm:w-auto flex items-center justify-center gap-2 rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 px-4 py-3 text-xs sm:text-sm font-bold transition-all"
                title="Yêu cầu AI Tutor gợi ý giải pháp theo phương pháp Socratic"
              >
                <Sparkles className="h-4 w-4 text-amber-500" />
                <span>Nhờ AI Gợi ý (Socratic)</span>
              </button>
            </div>

          </div>

        </div>

      </div>
    </div>
  );
};
