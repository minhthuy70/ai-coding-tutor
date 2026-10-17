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
  hints?: {
    level1: string; // Tư duy cốt lõi (Socratic Conceptual)
    level2: string; // Chiến lược thuật toán & Mã giả (Pseudocode)
    level3: string; // Tối ưu Big-O & Edge Cases
  };
}

interface ProblemSetModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSolveInSandbox: (problem: CodingProblem, language: string) => void;
  onAskAIHint: (prompt: string) => void;
  solvedProblemIds?: string[];
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
      { input: '6\n3 2 4', output: '1 2', explanation: 'nums[1] + nums[2] == 2 + 4 == 6, trả về 1 2.' },
      { input: '6\n3 3', output: '0 1', explanation: 'Hai số giống nhau nhưng khác vị trí index.' }
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
    hintPrompt: 'Tôi đang làm bài toán Two Sum. Thay vì dùng 2 vòng lặp lồng O(n^2), hãy dùng phương pháp Socratic gợi ý cho tôi cách dùng cấu trúc dữ liệu Hash Table để giảm độ phức tạp thời gian xuống O(n) mà không đưa ra code hoàn chỉnh ngay.',
    hints: {
      level1: 'Thay vì duyệt hai vòng lặp lồng nhau O(n²), hãy đặt câu hỏi: Khi duyệt đến một phần tử x, ta đang tìm một phần tử y thỏa mãn y = target - x. Liệu có cấu trúc dữ liệu nào cho phép tra cứu xem y đã từng xuất hiện hay chưa trong thời gian O(1)?',
      level2: 'Sử dụng Bảng băm (Hash Map / Dictionary). Khởi tạo `seen = {}`:\n- Lặp qua từng số `num` tại chỉ số `i`.\n- Tính phần bù `complement = target - num`.\n- Nếu `complement in seen`: in ra `seen[complement]` và `i`.\n- Ngược lại: gán `seen[num] = i` để phục vụ các số xét sau.',
      level3: 'Độ phức tạp thời gian: O(n) với một lượt duyệt duy nhất. Độ phức tạp không gian: O(n) cho bảng băm. Chú ý: Đề bài yêu cầu không dùng cùng 1 phần tử hai lần, kỹ thuật kiểm tra trước khi ghi vào `seen` đã tự động đảm bảo điều này.'
    }
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
      { input: '(]', output: 'false', explanation: 'Ngoặc tròn mở nhưng lại đóng bằng ngoặc vuông.' },
      { input: '([)]', output: 'false', explanation: 'Ngoặc đóng sai thứ tự lồng nhau.' }
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
    hintPrompt: 'Tôi đang làm bài kiểm tra chuỗi ngoặc hợp lệ (Valid Parentheses). Hãy đóng vai gia sư Socratic, giải thích tại sao Stack (Ngăn xếp) với tính chất LIFO lại là cấu trúc dữ liệu tối ưu nhất cho bài toán này và đặt câu hỏi gợi ý cho tôi.',
    hints: {
      level1: 'Một cặp ngoặc mở xuất hiện sau cùng luôn phải được đóng đầu tiên trước khi các ngoặc mở bên ngoài được đóng. Cấu trúc dữ liệu nào hoạt động theo nguyên lý Last In, First Out (LIFO)?',
      level2: 'Dùng Ngăn xếp (Stack):\n- Duyệt qua từng ký tự của chuỗi `s`.\n- Nếu gặp ngoặc mở `(`, `{`, `[`: đẩy vào Stack (`stack.append(char)`).\n- Nếu gặp ngoặc đóng: kiểm tra xem Stack có rỗng không hoặc phần tử đỉnh lấy ra (`pop()`) có khớp với ngoặc đóng tương ứng hay không.',
      level3: 'Sau khi duyệt hết chuỗi, chuỗi chỉ hợp lệ khi Stack rỗng hoàn toàn (`len(stack) == 0`). Độ phức tạp: O(n) thời gian, O(n) không gian. Cẩn thận các edge cases: chuỗi chỉ toàn ngoặc mở `((((` hoặc chuỗi mở đầu bằng ngoặc đóng `)]}`.'
    }
  },
  {
    id: 'prob-03',
    number: 3,
    title: 'Tìm Kiếm Nhị Phân (Binary Search)',
    difficulty: 'Dễ',
    category: 'BinarySearch',
    acceptanceRate: '92.1%',
    description: 'Cho một mảng số nguyên `nums` đã được sắp xếp theo thứ tự tăng dần và một số nguyên `target`.\nHãy viết hàm tìm kiếm `target` trong mảng `nums`. Nếu `target` tồn tại, trả về chỉ số của nó, ngược lại trả về `-1`.\nThuật toán bắt buộc phải có độ phức tạp thời gian chạy O(log n).',
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
    hintPrompt: 'Hãy hướng dẫn tôi tư duy Binary Search (Chia để trị). Tại sao mỗi lần so sánh ta lại có thể loại bỏ được một nửa không gian tìm kiếm? Cách tính mid = (left + right) // 2 có nguy cơ tràn số trong C++ không?',
    hints: {
      level1: 'Mảng đã được sắp xếp tăng dần! Nếu ta so sánh phần tử cần tìm `target` với phần tử nằm chính giữa `nums[mid]`, ta có thể chắc chắn loại bỏ 50% số phần tử còn lại mà không cần kiểm tra từng số.',
      level2: 'Dùng hai con trỏ `left = 0, right = len(nums) - 1`:\n- Trong khi `left <= right`: tính `mid = (left + right) // 2`.\n- Nếu `nums[mid] == target`: in ra `mid` và kết thúc.\n- Nếu `nums[mid] < target`: thu hẹp tìm kiếm sang nửa phải `left = mid + 1`.\n- Ngược lại: thu hẹp sang nửa trái `right = mid - 1`.',
      level3: 'Độ phức tạp: O(log n) thời gian, O(1) bộ nhớ. Lưu ý cho C++/Java: phép cộng `(left + right)` có nguy cơ Integer Overflow nếu giá trị lớn; giải pháp chuẩn là `mid = left + (right - left) / 2`.'
    }
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
      { input: '4\n1 3\n2 6\n8 10\n15 18', output: '1 6\n8 10\n15 18', explanation: 'Khoảng [1,3] và [2,6] gối lên nhau, được hợp nhất thành [1,6].' },
      { input: '2\n1 4\n2 3', output: '1 4', explanation: 'Khoảng [1,4] bao trọn khoảng [2,3].' }
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
    hintPrompt: 'Tôi đang giải bài toán Merge Intervals. Tại sao bước sắp xếp các khoảng theo thời điểm bắt đầu `start` lại là mấu chốt quyết định giúp ta giải bài toán trong 1 lượt duyệt duy nhất?',
    hints: {
      level1: 'Nếu các khoảng thời gian nằm lộn xộn, làm sao biết hai khoảng có giao nhau? Tiêu chí sắp xếp nào sẽ giúp ta chỉ cần xét các khoảng liền kề theo thứ tự thời gian?',
      level2: 'Sắp xếp danh sách `intervals` theo thời điểm bắt đầu `start` tăng dần. Khởi tạo `merged = []`:\n- Duyệt qua từng khoảng `curr`.\n- Nếu `merged` rỗng hoặc `merged[-1].end < curr.start`: thêm `curr` vào `merged`.\n- Ngược lại: khoảng hiện tại bị gối đầu, cập nhật `merged[-1].end = max(merged[-1].end, curr.end)`.',
      level3: 'Độ phức tạp: O(n log n) do sắp xếp, O(n) không gian lưu kết quả. Chú ý trường hợp một khoảng bao trọn khoảng kia (ví dụ `[1, 10]` và `[2, 5]`), lúc này giá trị kết thúc phải là `max(10, 5) = 10`.'
    }
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
    hintPrompt: 'Hãy hướng dẫn tôi xây dựng công thức chuyển trạng thái Quy hoạch động cho bài toán Dãy con tăng dài nhất (LIS). Định nghĩa mảng `dp[i]` ở đây đại diện cho ý nghĩa gì?',
    hints: {
      level1: 'Dãy con tăng không nhất thiết phải liên tiếp nhau! Tại mỗi vị trí i, độ dài dãy con tăng kết thúc tại `nums[i]` có thể kế thừa từ bất kỳ vị trí j nào đứng trước nó (j < i) nếu `nums[i] > nums[j]`.',
      level2: 'Quy hoạch động (DP):\n- Gọi `dp[i]` là độ dài dãy con tăng dài nhất kết thúc tại chỉ số `i`. Khởi tạo `dp = [1] * n`.\n- Hai vòng lặp lồng: với mỗi `i` từ 0 đến n-1, duyệt mọi `j` từ 0 đến i-1.\n- Nếu `nums[i] > nums[j]`: `dp[i] = max(dp[i], dp[j] + 1)`.\n- Kết quả cuối cùng là `max(dp)`.',
      level3: 'Độ phức tạp thời gian: O(n²) với DP truyền thống, O(n) không gian. Để tối ưu lên O(n log n), có thể kết hợp Binary Search với mảng `tails` (thuật toán Patience Sorting).'
    }
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
    hintPrompt: 'Hãy dùng phương pháp gợi mở Socratic giải thích bài toán Number of Islands. Tại sao kỹ thuật "làm chìm đảo" (sink the island - đánh dấu ô 1 thành 0 sau khi thăm) lại giúp chúng ta không cần dùng thêm mảng phụ `visited`?',
    hints: {
      level1: 'Một hòn đảo là một thành phần liên thông gồm các ô "1" kề nhau 4 hướng. Khi duyệt gặp một ô đất "1", làm sao ta đi thăm toàn bộ các ô thuộc cùng đảo đó để không bao giờ đếm lại nó nữa?',
      level2: 'Duyệt đồ thị bằng DFS (hoặc BFS):\n- Lặp qua từng ô `(r, c)` trong ma trận. Nếu `grid[r][c] == "1"`, tăng biến `islands += 1` và gọi `dfs(r, c)`.\n- Hàm `dfs(r, c)` kiểm tra biên, nếu gặp ô "1" thì đổi thành "0" (làm chìm đảo) và đệ quy sang 4 ô lân cận (trên, dưới, trái, phải).',
      level3: 'Kỹ thuật "làm chìm đảo" (ghi đè trực tiếp `grid[r][c] = "0"`) giúp giảm độ phức tạp không gian phụ xuống O(1) ngoài stack đệ quy (thay vì cần ma trận `visited` O(m*n)). Độ phức tạp thời gian: O(m*n).'
    }
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
    hintPrompt: 'Làm thế nào để tìm mức lương cao thứ 2 trong SQL? Tại sao dùng LIMIT 1 OFFSET 1 đơn thuần có thể bị lỗi khi bảng không có mức lương thứ 2? Hãy hướng dẫn tôi cách dùng MAX() hoặc Subquery.',
    hints: {
      level1: 'Mức lương cao thứ nhì thực chất là mức lương lớn nhất trong số tất cả các mức lương còn lại sau khi đã loại bỏ mức lương cao nhất tuyệt đối!',
      level2: 'Dùng Subquery lồng nhau:\n```sql\nSELECT MAX(salary) AS SecondHighestSalary\nFROM Employee\nWHERE salary < (\n  SELECT MAX(salary) FROM Employee\n);\n```',
      level3: 'Hàm `MAX()` trong SQL có đặc tính rất hay: Nếu tập dữ liệu truyền vào rỗng (ví dụ bảng chỉ có 1 nhân viên), `MAX()` tự động trả về `NULL` đúng theo yêu cầu của đề bài mà không làm phát sinh lỗi.'
    }
  },
  {
    id: 'prob-08',
    number: 8,
    title: 'Đảo Ngược Danh Sách Liên Kết Đơn (Reverse Linked List)',
    difficulty: 'Dễ',
    category: 'LinkedList',
    acceptanceRate: '82.4%',
    description: 'Cho con trỏ đầu `head` của một danh sách liên kết đơn. Hãy đảo ngược thứ tự các nút trong danh sách liên kết và trả về danh sách đã đảo ngược.\n\nThuật toán cần thực hiện lặp (Iterative) hoặc đệ quy (Recursive) trong thời gian O(n) và O(1) không gian phụ.',
    inputDesc: 'Dãy các số nguyên cách nhau bởi dấu cách biểu diễn danh sách liên kết ban đầu',
    outputDesc: 'Dãy các số nguyên sau khi đảo ngược cách nhau bởi dấu cách',
    constraints: ['0 <= Số lượng node <= 5000', '-5000 <= Node.val <= 5000'],
    examples: [
      { input: '1 2 3 4 5', output: '5 4 3 2 1', explanation: 'Danh sách 1 -> 2 -> 3 -> 4 -> 5 đảo ngược thành 5 -> 4 -> 3 -> 2 -> 1.' },
      { input: '1 2', output: '2 1', explanation: 'Danh sách 1 -> 2 đảo ngược thành 2 -> 1.' }
    ],
    starterCode: {
      python: `# Đảo ngược danh sách liên kết đơn O(n) thời gian, O(1) không gian
import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list():
    raw = sys.stdin.read().strip()
    if not raw:
        return
    vals = list(map(int, raw.split()))
    if not vals:
        return
        
    # Xây dựng danh sách liên kết
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
        
    # Thuật toán đảo ngược 3 con trỏ: prev, curr, next_node
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    # In ra danh sách sau khi đảo ngược
    res = []
    curr = prev
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" ".join(res))

reverse_linked_list()`,
      javascript: `const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim();
if (input) {
  const nums = input.split(/\\s+/);
  console.log(nums.reverse().join(' '));
}`
    },
    testCases: [
      { id: 1, name: 'Test 1 (5 phần tử)', input: '1 2 3 4 5', expectedOutput: '5 4 3 2 1' },
      { id: 2, name: 'Test 2 (2 phần tử)', input: '1 2', expectedOutput: '2 1' },
      { id: 3, name: 'Test 3 (1 phần tử)', input: '42', expectedOutput: '42' }
    ],
    hintPrompt: 'Làm thế nào để đảo ngược chiều các liên kết `curr.next` trong danh sách liên kết đơn mà không bị mất dấu nút tiếp theo? Hãy dùng phương pháp gợi ý Socratic phân tích kỹ thuật 3 con trỏ.',
    hints: {
      level1: 'Khi bạn thay đổi liên kết `curr.next = prev`, bạn sẽ lập tức mất đi địa chỉ của nút kế tiếp ban đầu! Bạn cần làm gì trước khi bẻ ngoặt chiều mũi tên liên kết?',
      level2: 'Kỹ thuật 3 con trỏ (`prev`, `curr`, `next_node`):\n1. Lưu tạm `next_node = curr.next`.\n2. Bẻ chiều: `curr.next = prev`.\n3. Dịch `prev` tiến lên: `prev = curr`.\n4. Dịch `curr` tiến lên: `curr = next_node`.\nLặp lại cho đến khi `curr` trở thành `None`.',
      level3: 'Khi vòng lặp kết thúc, `prev` chính là con trỏ đầu mới (`new head`) của danh sách đảo ngược. Độ phức tạp: O(n) thời gian, O(1) bộ nhớ phụ. Trường hợp biên: Danh sách rỗng (`head = None`) hoặc chỉ có 1 nút duy nhất.'
    }
  }
];

export const ProblemSetModal: React.FC<ProblemSetModalProps> = ({
  isOpen,
  onClose,
  onSolveInSandbox,
  onAskAIHint,
  solvedProblemIds,
}) => {
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('all');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [activeProblemId, setActiveProblemId] = useState<string>(PROBLEMS_DATA[0].id);
  const [selectedHintLevel, setSelectedHintLevel] = useState<1 | 2 | 3>(1);

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

  const solvedCount = useMemo(() => {
    if (!solvedProblemIds || solvedProblemIds.length === 0) return 0;
    return PROBLEMS_DATA.filter((p) =>
      solvedProblemIds.some(
        (idOrTitle) =>
          idOrTitle.includes(p.title) ||
          idOrTitle.includes(p.id) ||
          idOrTitle.includes(String(p.number))
      )
    ).length;
  }, [solvedProblemIds]);

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

          <div className="flex items-center gap-3">
            <div className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-amber-700 dark:text-amber-300 text-xs font-bold">
              <CheckCircle2 className="h-4 w-4 text-emerald-500" />
              <span>Đã giải: {solvedCount} / {PROBLEMS_DATA.length} bài</span>
              <span className="text-amber-600 dark:text-amber-400 font-black">• {solvedCount * 50} XP</span>
            </div>

            <button
              type="button"
              onClick={onClose}
              className="rounded-2xl p-2 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
            >
              <X className="h-5 w-5" />
            </button>
          </div>
        </div>

        {/* Filter & Search Bar */}
        <div className="px-6 py-3 border-b border-slate-200/70 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/30 flex flex-wrap items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-2 flex-1 min-w-[240px] max-w-md bg-white dark:bg-slate-800 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700">
            <Search className="h-4 w-4 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm kiếm theo tên thuật toán hoặc chủ đề..."
              className="w-full bg-transparent text-xs text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none font-medium"
            />
          </div>

          <div className="flex items-center gap-2 overflow-x-auto">
            {/* Difficulty Filter */}
            <div className="flex items-center rounded-xl bg-slate-200/60 dark:bg-slate-800 p-0.5 text-xs font-bold text-slate-600 dark:text-slate-400">
              {['all', 'Dễ', 'Trung bình', 'Khó'].map((diff) => (
                <button
                  key={diff}
                  type="button"
                  onClick={() => setSelectedDifficulty(diff)}
                  className={`px-3 py-1 rounded-lg transition ${
                    selectedDifficulty === diff
                      ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs'
                      : 'hover:text-slate-900 dark:hover:text-white'
                  }`}
                >
                  {diff === 'all' ? 'Tất cả độ khó' : diff}
                </button>
              ))}
            </div>

            {/* Category Filter */}
            <div className="flex items-center rounded-xl bg-slate-200/60 dark:bg-slate-800 p-0.5 text-xs font-bold text-slate-600 dark:text-slate-400">
              {['all', 'Array', 'Stack', 'DP', 'LinkedList', 'SQL'].map((cat) => (
                <button
                  key={cat}
                  type="button"
                  onClick={() => setSelectedCategory(cat)}
                  className={`px-2.5 py-1 rounded-lg transition ${
                    selectedCategory === cat
                      ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs'
                      : 'hover:text-slate-900 dark:hover:text-white'
                  }`}
                >
                  {cat === 'all' ? 'Tất cả dạng' : cat}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Modal Body: Two Columns */}
        <div className="flex-1 flex flex-col md:flex-row overflow-hidden">
          
          {/* Left Column: Problem List */}
          <div className="w-full md:w-5/12 border-r border-slate-200/70 dark:border-slate-800 overflow-y-auto p-4 space-y-2.5 bg-slate-50/30 dark:bg-slate-950/20">
            <div className="flex items-center justify-between px-1 mb-1 text-xs font-bold text-slate-400">
              <span>Danh sách ({filteredProblems.length} bài)</span>
              <span>Tỉ lệ chấp nhận</span>
            </div>

            {filteredProblems.map((prob) => {
              const isSelected = prob.id === activeProblem.id;
              const isSolved = (solvedProblemIds || []).some(
                (idOrTitle) =>
                  idOrTitle.includes(prob.title) ||
                  idOrTitle.includes(prob.id) ||
                  idOrTitle.includes(String(prob.number))
              );

              return (
                <div
                  key={prob.id}
                  onClick={() => setActiveProblemId(prob.id)}
                  className={`p-3.5 rounded-2xl border transition-all cursor-pointer ${
                    isSelected
                      ? 'bg-amber-50/60 dark:bg-amber-950/20 border-amber-300 dark:border-amber-700 shadow-sm'
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

                    <div className="flex items-center gap-1 shrink-0">
                      {isSolved && (
                        <span className="flex items-center gap-0.5 text-[10px] font-extrabold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/80 border border-emerald-500/30 px-1.5 py-0.5 rounded-md">
                          <CheckCircle2 className="h-3 w-3" />
                          <span>Đã giải</span>
                        </span>
                      )}
                      <span className="text-[10px] font-bold text-slate-400">
                        {prob.acceptanceRate}
                      </span>
                    </div>
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

              {/* 3-Tier Socratic Progressive Hint System */}
              <div className="mb-4 rounded-2xl border border-amber-200/80 dark:border-amber-900/40 bg-gradient-to-br from-amber-50/60 via-orange-50/30 to-amber-50/20 dark:from-amber-950/20 dark:via-orange-950/10 dark:to-slate-900 p-4">
                <div className="flex items-center justify-between mb-2.5">
                  <div className="flex items-center gap-2">
                    <div className="flex h-6 w-6 items-center justify-center rounded-lg bg-amber-500/20 text-amber-600 dark:text-amber-400">
                      <Sparkles className="h-3.5 w-3.5" />
                    </div>
                    <span className="text-xs font-black uppercase tracking-wider text-amber-900 dark:text-amber-300">
                      Hệ thống gợi ý Socratic 3 Cấp độ
                    </span>
                  </div>
                  <span className="text-[10px] font-bold text-amber-700/80 dark:text-amber-300 bg-amber-100 dark:bg-amber-900/50 px-2 py-0.5 rounded-full">
                    Mở khóa từng bước
                  </span>
                </div>

                {/* Level Tabs */}
                <div className="flex items-center gap-1 mb-3 bg-white/80 dark:bg-slate-900/80 p-1 rounded-xl border border-amber-200/60 dark:border-amber-900/40">
                  <button
                    type="button"
                    onClick={() => setSelectedHintLevel(1)}
                    className={`flex-1 py-1.5 px-2 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1 ${
                      selectedHintLevel === 1
                        ? 'bg-amber-500 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <HelpCircle className="h-3 w-3" />
                    <span>Cấp 1: Tư duy</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => setSelectedHintLevel(2)}
                    className={`flex-1 py-1.5 px-2 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1 ${
                      selectedHintLevel === 2
                        ? 'bg-blue-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <Cpu className="h-3 w-3" />
                    <span>Cấp 2: Thuật toán</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => setSelectedHintLevel(3)}
                    className={`flex-1 py-1.5 px-2 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1 ${
                      selectedHintLevel === 3
                        ? 'bg-emerald-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <Flame className="h-3 w-3" />
                    <span>Cấp 3: Tối ưu & Edge Cases</span>
                  </button>
                </div>

                {/* Hint Content Card */}
                <div className="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 text-xs leading-relaxed text-slate-700 dark:text-slate-200">
                  {selectedHintLevel === 1 && (
                    <div>
                      <div className="font-extrabold text-amber-600 dark:text-amber-400 mb-1 flex items-center gap-1.5 text-xs">
                        <Sparkles className="h-3.5 w-3.5" />
                        <span>Gợi mở tư duy Socratic (Không tiết lộ code giải):</span>
                      </div>
                      <p className="whitespace-pre-line text-slate-700 dark:text-slate-300">
                        {activeProblem.hints?.level1 || activeProblem.hintPrompt}
                      </p>
                    </div>
                  )}
                  {selectedHintLevel === 2 && (
                    <div>
                      <div className="font-extrabold text-blue-600 dark:text-blue-400 mb-1 flex items-center gap-1.5 text-xs">
                        <Cpu className="h-3.5 w-3.5" />
                        <span>Chiến lược thuật toán & Cấu trúc dữ liệu:</span>
                      </div>
                      <p className="whitespace-pre-line text-slate-700 dark:text-slate-300 font-mono text-[11px] sm:text-xs">
                        {activeProblem.hints?.level2 || 'Sử dụng cấu trúc dữ liệu tối ưu để giảm thời gian xử lý.'}
                      </p>
                    </div>
                  )}
                  {selectedHintLevel === 3 && (
                    <div>
                      <div className="font-extrabold text-emerald-600 dark:text-emerald-400 mb-1 flex items-center gap-1.5 text-xs">
                        <Flame className="h-3.5 w-3.5" />
                        <span>Độ phức tạp Big-O & Xử lý trường hợp biên (Edge Cases):</span>
                      </div>
                      <p className="whitespace-pre-line text-slate-700 dark:text-slate-300">
                        {activeProblem.hints?.level3 || 'Chú ý các trường hợp mảng rỗng hoặc giá trị trùng lặp.'}
                      </p>
                    </div>
                  )}
                </div>
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
