'use client';

import React, { useState } from 'react';
import {
  X,
  Compass,
  CheckCircle2,
  Circle,
  Clock,
  Sparkles,
  ChevronRight,
  Code2,
  BookOpen,
  Award,
  Layers,
  ArrowRight,
  Flame,
  Zap,
  GraduationCap,
  Play
} from 'lucide-react';

interface LearningRoadmapModalProps {
  isOpen: boolean;
  onClose: () => void;
  onStartLesson: (prompt: string) => void;
  onOpenPracticeInSandbox?: (code: string, language: string) => void;
}

interface TrackModule {
  id: string;
  title: string;
  summary: string;
  duration: string;
  difficulty: 'Cơ bản' | 'Trung bình' | 'Nâng cao';
  status: 'completed' | 'in_progress' | 'available';
  topics: string[];
  lessonPrompt: string;
  starterCode?: string;
  codeLang?: string;
}

interface LearningTrack {
  id: string;
  title: string;
  icon: string;
  color: string;
  description: string;
  progressPercent: number;
  modules: TrackModule[];
}

export const LearningRoadmapModal: React.FC<LearningRoadmapModalProps> = ({
  isOpen,
  onClose,
  onStartLesson,
  onOpenPracticeInSandbox,
}) => {
  const [selectedTrackId, setSelectedTrackId] = useState<string>('python');
  const [selectedModuleId, setSelectedModuleId] = useState<string>('py-1');

  if (!isOpen) return null;

  const tracks: LearningTrack[] = [
    {
      id: 'python',
      title: 'Python Toàn Diện: Zero to Hero',
      icon: '🐍',
      color: 'from-blue-500 to-indigo-600',
      description: 'Chinh phục ngôn ngữ lập trình phổ biến nhất thế giới từ biến, hàm, OOP đến cấu trúc dữ liệu nâng cao.',
      progressPercent: 60,
      modules: [
        {
          id: 'py-1',
          title: '1. Nền tảng Cú pháp & Kiểu dữ liệu',
          summary: 'Làm quen với biến số, chuỗi ký tự, toán tử số học, ép kiểu và cú pháp căn bản của Python 3.',
          duration: '3 giờ',
          difficulty: 'Cơ bản',
          status: 'completed',
          topics: ['Biến & Kiểu dữ liệu (int, float, str, bool)', 'Toán tử số học & Logic', 'Nhập xuất dữ liệu với input() & print()', 'Format chuỗi f-string'],
          lessonPrompt: 'Hãy hướng dẫn tôi bằng phương pháp Socratic về "Kiểu dữ liệu và Biến trong Python 3". Đưa ra ví dụ minh họa trực quan và cho tôi 1 câu hỏi tương tác để tôi trả lời trước khi chuyển sang phần tiếp theo.',
          starterCode: '# Nền tảng Python: Biến & F-string\nname = "Sinh viên"\nage = 20\ngpa = 3.85\n\nprint(f"Xin chào {name}, {age} tuổi, GPA: {gpa}")\nprint(f"Kiểu dữ liệu name: {type(name).__name__}")',
          codeLang: 'python'
        },
        {
          id: 'py-2',
          title: '2. Cấu trúc Điều khiển & Vòng lặp',
          summary: 'Nắm vững rẽ nhánh if-elif-else, vòng lặp for với range(), vòng lặp while và các lệnh break, continue.',
          duration: '4 giờ',
          difficulty: 'Cơ bản',
          status: 'completed',
          topics: ['Câu lệnh điều kiện if - elif - else', 'Vòng lặp for & hàm range()', 'Vòng lặp while & điều kiện dừng', 'Lệnh break & continue'],
          lessonPrompt: 'Hãy đóng vai Gia sư Socratic, giải thích cho tôi cơ chế hoạt động của vòng lặp `for` và `while` trong Python. Khi nào nên dùng `for`, khi nào nên dùng `while`? Đặt cho tôi 1 bài toán nhỏ về vòng lặp để kiểm tra hiểu biết.',
          starterCode: '# Cấu trúc vòng lặp for và while trong Python\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nevens = []\n\nfor n in numbers:\n    if n % 2 == 0:\n        evens.append(n)\n\nprint("Các số chẵn:", evens)\nprint("Tổng các số chẵn:", sum(evens))',
          codeLang: 'python'
        },
        {
          id: 'py-3',
          title: '3. Bộ sưu tập Dữ liệu (List, Dict, Tuple, Set)',
          summary: 'Sử dụng thành thạo 4 cấu trúc dữ liệu nền tảng, List Comprehension và các phương thức xử lý mạnh mẽ.',
          duration: '5 giờ',
          difficulty: 'Trung bình',
          status: 'in_progress',
          topics: ['Danh sách (List) & List Comprehension', 'Từ điển (Dictionary) key-value lookup', 'Tập hợp (Set) & phép toán giao, hợp', 'Bộ giá trị (Tuple) bất biến'],
          lessonPrompt: 'Tôi muốn học về 4 cấu trúc dữ liệu cơ bản của Python: List, Tuple, Set và Dict. Hãy so sánh sự khác nhau về tính năng, tốc độ tra cứu $O(1)$ vs $O(n)$ và tính có thể thay đổi (mutable vs immutable). Hãy hỏi tôi 1 câu hỏi phản biện để kiểm tra kiến thức.',
          starterCode: '# Thao tác với List Comprehension và Dictionary trong Python\nwords = ["apple", "banana", "cherry", "date", "elderberry"]\n\n# List comprehension: Lọc từ có độ dài > 5\nlong_words = [w.upper() for w in words if len(w) > 5]\n\n# Dict đếm độ dài\nword_lengths = {w: len(w) for w in words}\n\nprint("Từ dài > 5:", long_words)\nprint("Độ dài từng từ:", word_lengths)',
          codeLang: 'python'
        },
        {
          id: 'py-4',
          title: '4. Hàm, Phạm vi Biến & Lambda Expression',
          summary: 'Xây dựng hàm tái sử dụng, tham số mặc định, *args, **kwargs, biến toàn cục và hàm vô danh lambda.',
          duration: '4 giờ',
          difficulty: 'Trung bình',
          status: 'available',
          topics: ['Định nghĩa hàm def & giá trị trả về return', 'Tham số *args và **kwargs linh hoạt', 'Phạm vi biến (Scope: Local, Enclosing, Global, Built-in)', 'Hàm ẩn danh lambda & map/filter'],
          lessonPrompt: 'Hãy hướng dẫn tôi chi tiết về *args và **kwargs trong hàm Python. Cho ví dụ thực tế trong các thư viện lớn như Flask hoặc FastAPI, và đặt cho tôi 1 bài tập viết hàm decorator hoặc wrapper đơn giản.',
          starterCode: '# Hàm nâng cao với *args và **kwargs\ndef summarize_student(name: str, *scores: float, **metadata):\n    avg = sum(scores) / len(scores) if scores else 0.0\n    return {\n        "name": name,\n        "average": round(avg, 2),\n        "scores_count": len(scores),\n        "details": metadata\n    }\n\ninfo = summarize_student("Minh Thùy", 8.5, 9.0, 9.5, major="CNTT", year=4)\nprint(info)',
          codeLang: 'python'
        },
        {
          id: 'py-5',
          title: '5. Lập trình Hướng đối tượng (OOP Python)',
          summary: 'Làm chủ Class, Object, Encapsulation, Kế thừa Inheritance, Đa hình Polymorphism và các Magic Methods.',
          duration: '6 giờ',
          difficulty: 'Nâng cao',
          status: 'available',
          topics: ['Class & Instance, hàm khởi tạo __init__', 'Thuộc tính Private & Decorator @property', 'Kế thừa đơn & Kế thừa bội (MRO)', 'Magic Methods (__str__, __repr__, __eq__)'],
          lessonPrompt: 'Hãy dạy tôi về Lập trình hướng đối tượng (OOP) trong Python theo phong cách Socratic. Hãy dẫn dắt từ việc tại sao chúng ta cần Class thay vì chỉ dùng Dictionary, sau đó giải thích 4 tính chất OOP bằng một ví dụ hệ thống quản lý sinh viên.',
          starterCode: '# Lập trình Hướng đối tượng OOP trong Python\nclass BankAccount:\n    def __init__(self, owner: str, balance: float = 0.0):\n        self.owner = owner\n        self._balance = balance  # Protected attribute\n\n    def deposit(self, amount: float):\n        if amount <= 0:\n            raise ValueError("Số tiền nạp phải lớn hơn 0")\n        self._balance += amount\n        return self._balance\n\n    def withdraw(self, amount: float):\n        if amount > self._balance:\n            return False\n        self._balance -= amount\n        return True\n\n    def __str__(self):\n        return f"Tài khoản của {self.owner}: {self._balance:,.0f} VNĐ"\n\nacc = BankAccount("Nguyễn Văn A", 500000)\nacc.deposit(250000)\nprint(acc)',
          codeLang: 'python'
        }
      ]
    },
    {
      id: 'dsa',
      title: 'Cấu Trúc Dữ Liệu & Giải Thuật (DSA)',
      icon: '⚡',
      color: 'from-amber-500 to-rose-600',
      description: 'Nắm vững tư duy giải thuật từ phân tích Big-O đến các cấu trúc dữ liệu phỏng vấn Big Tech.',
      progressPercent: 40,
      modules: [
        {
          id: 'dsa-1',
          title: '1. Phân tích Độ phức tạp Thời gian & Không gian (Big-O)',
          summary: 'Đọc hiểu O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n). Đánh giá thuật toán trong trường hợp tốt nhất và xấu nhất.',
          duration: '3 giờ',
          difficulty: 'Cơ bản',
          status: 'completed',
          topics: ['Định nghĩa Big-O, Big-Omega, Big-Theta', 'Quy tắc bỏ hằng số & bậc thấp hơn', 'Phân tích vòng lặp lồng nhau', 'Độ phức tạp bộ nhớ phụ trợ (Auxiliary Space)'],
          lessonPrompt: 'Hãy hướng dẫn tôi cách phân tích độ phức tạp thời gian Big-O của một đoạn mã. Hãy đưa ra 3 đoạn code mẫu khác nhau (1 vòng lặp, 2 vòng lặp lồng, và tìm kiếm nhị phân) và hỏi tôi độ phức tạp của từng đoạn code.',
          starterCode: '# Phân tích độ phức tạp Big-O\ndef linear_search(arr, target):\n    # Độ phức tạp O(n) thời gian, O(1) bộ nhớ\n    for i, val in enumerate(arr):\n        if val == target:\n            return i\n    return -1\n\ndef nested_pairs(arr):\n    # Độ phức tạp O(n^2) thời gian\n    pairs = []\n    for i in range(len(arr)):\n        for j in range(i + 1, len(arr)):\n            pairs.append((arr[i], arr[j]))\n    return len(pairs)\n\nprint("Pairs count:", nested_pairs([1, 2, 3, 4]))',
          codeLang: 'python'
        },
        {
          id: 'dsa-2',
          title: '2. Mảng Kỹ thuật & Kỹ thuật Hai Con Trỏ (Two Pointers)',
          summary: 'Áp dụng Two Pointers và Cửa sổ Trượt (Sliding Window) để giải quyết các bài toán tối ưu từ O(n^2) về O(n).',
          duration: '5 giờ',
          difficulty: 'Trung bình',
          status: 'in_progress',
          topics: ['Two Pointers cùng hướng & ngược hướng', 'Cửa sổ trượt kích thước cố định & biến thiên', 'Prefix Sum mảng cộng dồn', 'Tối ưu hóa bài toán Two Sum'],
          lessonPrompt: 'Hãy hướng dẫn tôi kỹ thuật Two Pointers (Hai con trỏ) trong cấu trúc dữ liệu mảng. Dẫn dắt tôi từng bước cách biến thuật toán $O(n^2)$ vét cạn thành thuật toán $O(n)$ thông qua bài toán kiểm tra chuỗi đối xứng (Palindrome) hoặc Two Sum mảng đã sắp xếp.',
          starterCode: '# Kỹ thuật Two Pointers: Kiểm tra chuỗi Palindrome O(n) thời gian, O(1) không gian\ndef is_palindrome(s: str) -> bool:\n    left = 0\n    right = len(s) - 1\n    while left < right:\n        if s[left] != s[right]:\n            return False\n        left += 1\n        right -= 1\n    return True\n\nprint("radar ->", is_palindrome("radar"))\nprint("hello ->", is_palindrome("hello"))',
          codeLang: 'python'
        },
        {
          id: 'dsa-3',
          title: '3. Ngăn Xếp & Hàng Đợi (Stack & Queue)',
          summary: 'Nguyên lý LIFO và FIFO, ứng dụng vào kiểm tra dấu ngoặc hợp lệ, Monotonic Stack và Breadth-First Search.',
          duration: '4 giờ',
          difficulty: 'Trung bình',
          status: 'available',
          topics: ['Cài đặt Stack với List/Deque', 'Bài toán Valid Parentheses', 'Queue hàng đợi & Double-ended Queue (Deque)', 'Monotonic Stack tìm phần tử lớn hơn tiếp theo'],
          lessonPrompt: 'Hãy hướng dẫn tôi cấu trúc dữ liệu Stack (Ngăn xếp - LIFO). Tại sao Stack lại phù hợp nhất để giải bài toán "Kiểm tra tính hợp lệ của các cặp dấu ngoặc () [] {}"? Hãy đưa ra câu hỏi gợi ý để tôi tự code giải pháp.',
          starterCode: '# Ứng dụng Stack: Kiểm tra dấu ngoặc hợp lệ O(n)\ndef is_valid_parentheses(s: str) -> bool:\n    mapping = {")": "(", "}": "{", "]": "["}\n    stack = []\n    for char in s:\n        if char in mapping.values():\n            stack.append(char)\n        elif char in mapping:\n            if not stack or stack.pop() != mapping[char]:\n                return False\n    return len(stack) == 0\n\nprint("({[]}) ->", is_valid_parentheses("({[]})"))\nprint("([)] ->", is_valid_parentheses("([)]"))',
          codeLang: 'python'
        },
        {
          id: 'dsa-4',
          title: '4. Cây Nhị Phân & Cây Tìm Kiếm Nhị Phân (BST)',
          summary: 'Duyệt cây Preorder, Inorder, Postorder, duyệt theo tầng Level-order, tìm kiếm và chèn trong BST.',
          duration: '6 giờ',
          difficulty: 'Nâng cao',
          status: 'available',
          topics: ['Node & Cấu trúc Cây nhị phân', '3 phép duyệt DFS (Pre, In, Post-order)', 'Cây tìm kiếm nhị phân (Binary Search Tree)', 'Tính chiều cao & Độ sâu tối đa của Cây'],
          lessonPrompt: 'Hãy giải thích cho tôi cấu trúc dữ liệu Cây tìm kiếm nhị phân (Binary Search Tree - BST). Tính chất quan trọng nhất của BST là gì? Tại sao duyệt Inorder trên BST lại cho ra danh sách đã sắp xếp tăng dần?',
          starterCode: '# Cây Nhị Phân Tìm Kiếm (BST)\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef inorder_traversal(root):\n    res = []\n    def dfs(node):\n        if not node: return\n        dfs(node.left)\n        res.append(node.val)\n        dfs(node.right)\n    dfs(root)\n    return res\n\nroot = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))\nprint("Inorder BST:", inorder_traversal(root))',
          codeLang: 'python'
        },
        {
          id: 'dsa-5',
          title: '5. Quy Hoạch Động (Dynamic Programming)',
          summary: 'Chuyển hóa bài toán đệ quy trùng lặp sang Memoization (Top-down) và Tabulation (Bottom-up).',
          duration: '8 giờ',
          difficulty: 'Nâng cao',
          status: 'available',
          topics: ['Tính chất Gối chồng bài toán con & Cấu trúc tối ưu', 'Fibonacci từ O(2^n) về O(n)', 'Bài toán Leo cầu thang (Climbing Stairs)', 'Bài toán Cái túi (0/1 Knapsack)'],
          lessonPrompt: 'Hãy hướng dẫn tôi phương pháp Quy hoạch động (Dynamic Programming). Hãy bắt đầu từ một bài toán đơn giản như "Leo cầu thang (Climbing Stairs)" hoặc dãy Fibonacci, chỉ ra tại sao đệ quy ngây thơ bị $O(2^n)$ và cách bảng phương án giải quyết nó với $O(n)$.',
          starterCode: '# Quy hoạch động: Fibonacci với Bottom-up Tabulation O(n) thời gian, O(1) không gian\ndef fibonacci_dp(n: int) -> int:\n    if n <= 1:\n        return n\n    prev, curr = 0, 1\n    for _ in range(2, n + 1):\n        prev, curr = curr, prev + curr\n    return curr\n\nfor i in range(10):\n    print(f"F({i}) = {fibonacci_dp(i)}")',
          codeLang: 'python'
        }
      ]
    },
    {
      id: 'web',
      title: 'Lập Trình Web Hiện Đại (Full-Stack)',
      icon: '🌐',
      color: 'from-emerald-500 to-teal-600',
      description: 'Từ cấu trúc HTML5/CSS3 chuẩn SEO, JavaScript ES6+ đến Next.js App Router và kết nối API.',
      progressPercent: 50,
      modules: [
        {
          id: 'web-1',
          title: '1. HTML5 Semantics & CSS3 Flexbox/Grid',
          summary: 'Xây dựng cấu trúc trang web chuẩn SEO với thẻ ngữ nghĩa và bố cục dàn trang hiện đại thích ứng đa màn hình.',
          duration: '4 giờ',
          difficulty: 'Cơ bản',
          status: 'completed',
          topics: ['Semantic Tags (header, nav, main, article, section)', 'Bố cục Flexbox 1 chiều (justify, align)', 'Bố cục CSS Grid 2 chiều (grid-template-columns)', 'Responsive Media Queries'],
          lessonPrompt: 'Hãy giải thích sự khác biệt giữa CSS Flexbox và CSS Grid. Khi nào nên dùng Flexbox, khi nào nên dùng Grid? Cho tôi ví dụ mã HTML/CSS xây dựng thanh Navbar và khu vực hiển thị Card sản phẩm.',
          starterCode: '<!DOCTYPE html>\n<html>\n<head>\n  <style>\n    .container { display: flex; gap: 16px; padding: 20px; font-family: sans-serif; }\n    .card { flex: 1; padding: 20px; border-radius: 12px; background: #f1f5f9; border: 1px solid #cbd5e1; }\n    .card h3 { margin-top: 0; color: #0284c7; }\n  </style>\n</head>\n<body>\n  <div class="container">\n    <div class="card"><h3>Flex Card 1</h3><p>Nội dung thẻ responsive 1</p></div>\n    <div class="card"><h3>Flex Card 2</h3><p>Nội dung thẻ responsive 2</p></div>\n  </div>\n</body>\n</html>',
          codeLang: 'html'
        },
        {
          id: 'web-2',
          title: '2. JavaScript ES6+ & Bất Đồng Bộ (Async/Await)',
          summary: 'Arrow functions, Destructuring, Spread/Rest, Promise, Async/Await và tương tác Fetch API.',
          duration: '5 giờ',
          difficulty: 'Trung bình',
          status: 'in_progress',
          topics: ['Let/Const & Lexical Scoping', 'Destructuring & Spread Operator', 'Promises & Event Loop microtasks', 'Async / Await & Fetch API'],
          lessonPrompt: 'Hãy giải thích cơ chế Bất đồng bộ trong JavaScript: Event Loop, Call Stack, Microtask Queue hoạt động thế nào với Promise và async/await? Cho ví dụ thực tế về việc gọi một API lấy dữ liệu người dùng.',
          starterCode: '// JavaScript Bất Đồng Bộ với Async / Await\nasync function fetchUserData(userId) {\n  try {\n    console.log(`Đang tải dữ liệu cho User ID: ${userId}...`);\n    // Giả lập delay mạng 500ms\n    await new Promise(res => setTimeout(res, 500));\n    const mockUser = {\n      id: userId,\n      name: "Nguyễn Văn IT",\n      email: "user@example.com",\n      skills: ["React", "TypeScript", "Node.js"]\n    };\n    return mockUser;\n  } catch (err) {\n    console.error("Lỗi khi tải dữ liệu:", err);\n  }\n}\n\nfetchUserData(101).then(data => console.log("Kết quả:", data));',
          codeLang: 'javascript'
        },
        {
          id: 'web-3',
          title: '3. React Fundamentals & State Hooks',
          summary: 'Tư duy Component hóa, Props, State với useState, Vòng đời với useEffect và tối ưu re-render.',
          duration: '6 giờ',
          difficulty: 'Trung bình',
          status: 'available',
          topics: ['JSX Syntax & Virtual DOM', 'State Management với useState', 'Side Effects với useEffect', 'Custom Hooks tái sử dụng logic'],
          lessonPrompt: 'Hãy đóng vai Gia sư Socratic, giải thích cho tôi quy tắc hoạt động của `useState` và `useEffect` trong React. Tại sao không được gọi Hook bên trong câu lệnh điều kiện `if`? Đặt cho tôi 1 câu hỏi tương tác để tôi trả lời.',
          starterCode: '// React Component Đơn Giản (Demo logic)\nfunction Counter() {\n  let count = 0;\n  const increment = () => { count += 1; console.log("Count is now:", count); };\n  return { count, increment };\n}\n\nconst myCounter = Counter();\nmyCounter.increment();\nmyCounter.increment();',
          codeLang: 'javascript'
        }
      ]
    },
    {
      id: 'sql',
      title: 'Cơ Sở Dữ Liệu & SQL Thực Chiến',
      icon: '🗄️',
      color: 'from-purple-500 to-pink-600',
      description: 'Thiết kế cơ sở dữ liệu quan hệ, viết câu truy vấn phức tạp, tối ưu Indexing và phân tích dữ liệu.',
      progressPercent: 30,
      modules: [
        {
          id: 'sql-1',
          title: '1. Truy Vấn Dữ Liệu Căn Bản (SELECT & Filtering)',
          summary: 'Cú pháp SELECT, WHERE, LIKE, IN, BETWEEN, ORDER BY và giới hạn bản ghi LIMIT.',
          duration: '3 giờ',
          difficulty: 'Cơ bản',
          status: 'completed',
          topics: ['SELECT cột dữ liệu & đặt alias AS', 'Điều kiện lọc WHERE với toán tử AND, OR, NOT', 'Tìm kiếm mẫu ký tự với LIKE & ILIKE', 'Sắp xếp ORDER BY ASC/DESC'],
          lessonPrompt: 'Hãy hướng dẫn tôi cách viết câu truy vấn SQL SELECT cơ bản. Hãy cho 1 bảng dữ liệu mẫu `employees` (id, name, department, salary) và đặt cho tôi 2 bài tập truy vấn từ dễ đến vừa để tôi tự viết câu lệnh SQL.',
          starterCode: '-- SQL: Lọc dữ liệu nhân viên có mức lương trên 15,000,000 VNĐ\nSELECT id, full_name, department, salary\nFROM employees\nWHERE salary >= 15000000 AND status = \'ACTIVE\'\nORDER BY salary DESC\nLIMIT 5;',
          codeLang: 'sql'
        },
        {
          id: 'sql-2',
          title: '2. Gom Nhóm Dữ Liệu (GROUP BY & HAVING)',
          summary: 'Tính toán tổng hợp với COUNT, SUM, AVG, MIN, MAX và phân biệt điều kiện WHERE vs HAVING.',
          duration: '4 giờ',
          difficulty: 'Trung bình',
          status: 'in_progress',
          topics: ['Các hàm tổng hợp Aggregate Functions', 'Mệnh đề GROUP BY gom nhóm', 'Phân biệt WHERE (trước gom nhóm) và HAVING (sau gom nhóm)', 'Thống kê doanh thu và số lượng'],
          lessonPrompt: 'Hãy giải thích cho tôi sự khác biệt then chốt giữa mệnh đề `WHERE` và `HAVING` trong SQL. Khi nào bắt buộc phải dùng `HAVING`? Hãy đưa ra 1 ví dụ thực tế kèm câu lệnh SQL minh họa.',
          starterCode: '-- SQL: Thống kê số lượng nhân viên và mức lương trung bình theo từng phòng ban\nSELECT \n    department,\n    COUNT(id) AS total_employees,\n    ROUND(AVG(salary), 0) AS avg_salary\nFROM employees\nGROUP BY department\nHAVING COUNT(id) >= 3\nORDER BY avg_salary DESC;',
          codeLang: 'sql'
        },
        {
          id: 'sql-3',
          title: '3. Kết Nối Bảng Đa Chiều (JOIN Master)',
          summary: 'Nắm vững INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN và tự kết nối SELF JOIN.',
          duration: '5 giờ',
          difficulty: 'Nâng cao',
          status: 'available',
          topics: ['Khóa chính (PK) & Khóa ngoại (FK)', 'INNER JOIN giao tập dữ liệu', 'LEFT JOIN bảo toàn dữ liệu bảng trái', 'Subqueries & CTE (WITH clause)'],
          lessonPrompt: 'Hãy dạy tôi các loại JOIN trong SQL (INNER, LEFT, RIGHT, FULL) bằng mô hình tập hợp Venn trực quan. Hãy cho ví dụ bảng `orders` và bảng `customers` để giải thích trường hợp nào nên dùng LEFT JOIN.',
          starterCode: '-- SQL: Kết nối đơn hàng và khách hàng bằng LEFT JOIN\nSELECT \n    c.customer_id,\n    c.customer_name,\n    COUNT(o.order_id) AS total_orders,\n    COALESCE(SUM(o.total_amount), 0) AS total_spent\nFROM customers c\nLEFT JOIN orders o ON c.customer_id = o.customer_id\nGROUP BY c.customer_id, c.customer_name\nORDER BY total_spent DESC;',
          codeLang: 'sql'
        }
      ]
    }
  ];

  const currentTrack = tracks.find(t => t.id === selectedTrackId) || tracks[0];
  const currentModule = currentTrack.modules.find(m => m.id === selectedModuleId) || currentTrack.modules[0];

  const handleSelectTrack = (trackId: string) => {
    setSelectedTrackId(trackId);
    const targetTrack = tracks.find(t => t.id === trackId);
    if (targetTrack && targetTrack.modules.length > 0) {
      setSelectedModuleId(targetTrack.modules[0].id);
    }
  };

  const handleStartLessonAction = (module: TrackModule) => {
    onStartLesson(module.lessonPrompt);
    onClose();
  };

  const handlePracticeAction = (module: TrackModule) => {
    if (onOpenPracticeInSandbox && module.starterCode) {
      onOpenPracticeInSandbox(module.starterCode, module.codeLang || 'python');
      onClose();
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-900/60 dark:bg-black/75 backdrop-blur-md animate-fade-in">
      <div className="flex flex-col w-full max-w-5xl h-[88vh] bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden animate-scale-in">
        
        {/* Modal Header */}
        <div className="px-6 py-4.5 border-b border-slate-200/80 dark:border-slate-800 bg-gradient-to-r from-slate-50 via-white to-blue-50/30 dark:from-slate-900 dark:via-slate-900 dark:to-blue-950/20 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white shadow-md shadow-blue-500/25">
              <Compass className="h-6 w-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
                  Lộ Trình Học Tập & Cây Kỹ Năng
                </h2>
                <span className="rounded-full bg-blue-100 dark:bg-blue-900/60 px-2.5 py-0.5 text-[10px] font-extrabold text-blue-700 dark:text-blue-300">
                  Curriculum AI v2.5
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Các bài học được chuẩn hóa theo phương pháp sư phạm Socratic có bài tập thực hành kèm theo
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

        {/* Track Selector Tabs */}
        <div className="flex items-center gap-2 px-6 py-2.5 bg-slate-50/70 dark:bg-slate-950/40 border-b border-slate-200/70 dark:border-slate-800/80 overflow-x-auto no-scrollbar shrink-0">
          {tracks.map((track) => {
            const isSelected = track.id === selectedTrackId;
            return (
              <button
                key={track.id}
                type="button"
                onClick={() => handleSelectTrack(track.id)}
                className={`flex items-center gap-2.5 px-4 py-2 rounded-2xl text-xs font-bold transition-all whitespace-nowrap shrink-0 ${
                  isSelected
                    ? 'bg-white dark:bg-slate-800 text-blue-600 dark:text-blue-400 shadow-sm border border-slate-200 dark:border-slate-700'
                    : 'text-slate-600 dark:text-slate-400 hover:bg-white/60 dark:hover:bg-slate-800/60'
                }`}
              >
                <span className="text-base">{track.icon}</span>
                <span>{track.title}</span>
                <span className="ml-1 rounded-full bg-slate-100 dark:bg-slate-700 px-2 py-0.5 text-[10px] text-slate-500 dark:text-slate-400 font-extrabold">
                  {track.progressPercent}%
                </span>
              </button>
            );
          })}
        </div>

        {/* Main Content Area: Split 2 columns */}
        <div className="flex-1 flex flex-col md:flex-row min-h-0 overflow-hidden">
          
          {/* Left Column: Modules List */}
          <div className="w-full md:w-5/12 border-r border-slate-200/80 dark:border-slate-800 overflow-y-auto p-4 space-y-2.5 bg-slate-50/30 dark:bg-slate-900/50">
            <div className="flex items-center justify-between px-2 pb-1">
              <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                Các chuyên đề ({currentTrack.modules.length})
              </span>
              <span className="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400 flex items-center gap-1">
                <CheckCircle2 className="h-3.5 w-3.5" />
                Tiến độ: {currentTrack.progressPercent}%
              </span>
            </div>

            {/* Track Progress Bar */}
            <div className="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden mb-3">
              <div 
                className="bg-gradient-to-r from-blue-500 to-indigo-600 h-full rounded-full transition-all duration-500"
                style={{ width: `${currentTrack.progressPercent}%` }}
              />
            </div>

            {currentTrack.modules.map((mod, idx) => {
              const isSelected = mod.id === selectedModuleId;
              return (
                <div
                  key={mod.id}
                  onClick={() => setSelectedModuleId(mod.id)}
                  className={`group relative p-3.5 rounded-2xl border transition-all cursor-pointer ${
                    isSelected
                      ? 'bg-white dark:bg-slate-800 border-blue-500 dark:border-blue-500 shadow-md shadow-blue-500/10'
                      : 'bg-white/80 dark:bg-slate-800/60 border-slate-200/70 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                  }`}
                >
                  <div className="flex items-start gap-3">
                    {/* Status Icon */}
                    <div className="mt-0.5">
                      {mod.status === 'completed' ? (
                        <div className="h-6 w-6 rounded-full bg-emerald-100 dark:bg-emerald-950/70 flex items-center justify-center text-emerald-600 dark:text-emerald-400">
                          <CheckCircle2 className="h-4 w-4" />
                        </div>
                      ) : mod.status === 'in_progress' ? (
                        <div className="h-6 w-6 rounded-full bg-blue-100 dark:bg-blue-950/70 flex items-center justify-center text-blue-600 dark:text-blue-400">
                          <Flame className="h-4 w-4 animate-pulse" />
                        </div>
                      ) : (
                        <div className="h-6 w-6 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-400">
                          <Circle className="h-3.5 w-3.5" />
                        </div>
                      )}
                    </div>

                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-1 mb-1">
                        <h4 className={`text-xs font-extrabold truncate ${
                          isSelected ? 'text-blue-600 dark:text-blue-400' : 'text-slate-800 dark:text-slate-200'
                        }`}>
                          {mod.title}
                        </h4>
                        <span className={`text-[10px] font-bold px-1.5 py-0.5 rounded-full shrink-0 ${
                          mod.difficulty === 'Cơ bản'
                            ? 'bg-emerald-100 dark:bg-emerald-950 text-emerald-600 dark:text-emerald-300'
                            : mod.difficulty === 'Trung bình'
                            ? 'bg-amber-100 dark:bg-amber-950 text-amber-600 dark:text-amber-300'
                            : 'bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-300'
                        }`}>
                          {mod.difficulty}
                        </span>
                      </div>

                      <p className="text-[11px] text-slate-500 dark:text-slate-400 line-clamp-2 leading-relaxed">
                        {mod.summary}
                      </p>

                      <div className="flex items-center gap-3 mt-2 text-[10px] text-slate-400">
                        <span className="flex items-center gap-1">
                          <Clock className="h-3 w-3" />
                          {mod.duration}
                        </span>
                        <span className="flex items-center gap-1">
                          <Layers className="h-3 w-3" />
                          {mod.topics.length} khái niệm
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Right Column: Module Details & Lesson Launcher */}
          <div className="w-full md:w-7/12 flex flex-col justify-between p-6 overflow-y-auto bg-white dark:bg-slate-900">
            <div>
              {/* Badge & Title */}
              <div className="flex flex-wrap items-center gap-2 mb-3">
                <span className="rounded-full bg-blue-100 dark:bg-blue-900/60 px-2.5 py-0.5 text-xs font-extrabold text-blue-700 dark:text-blue-300">
                  {currentTrack.title}
                </span>
                <span className={`rounded-full px-2.5 py-0.5 text-xs font-bold ${
                  currentModule.status === 'completed'
                    ? 'bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300'
                    : currentModule.status === 'in_progress'
                    ? 'bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-300'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                }`}>
                  {currentModule.status === 'completed' ? '✓ Đã hoàn thành' : currentModule.status === 'in_progress' ? '🔥 Đang học' : '⏳ Sẵn sàng học'}
                </span>
                <span className="text-xs text-slate-400 flex items-center gap-1 ml-auto">
                  <Clock className="h-3.5 w-3.5" />
                  Thời lượng: {currentModule.duration}
                </span>
              </div>

              <h3 className="text-xl font-black text-slate-900 dark:text-white tracking-tight mb-2">
                {currentModule.title}
              </h3>

              <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-6">
                {currentModule.summary}
              </p>

              {/* Topics Breakdown */}
              <div className="mb-6">
                <h5 className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3 flex items-center gap-1.5">
                  <GraduationCap className="h-4 w-4 text-blue-500" />
                  Mục tiêu kiến thức cốt lõi
                </h5>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {currentModule.topics.map((topic, i) => (
                    <div
                      key={i}
                      className="flex items-start gap-2.5 p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-100 dark:border-slate-800"
                    >
                      <span className="h-5 w-5 rounded-full bg-blue-50 dark:bg-blue-950 text-blue-600 dark:text-blue-400 flex items-center justify-center text-[10px] font-bold shrink-0 mt-0.5">
                        {i + 1}
                      </span>
                      <span className="text-xs text-slate-700 dark:text-slate-300 font-medium leading-snug">
                        {topic}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Starter Code Preview if present */}
              {currentModule.starterCode && (
                <div className="mb-6">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                      <Code2 className="h-4 w-4 text-emerald-500" />
                      Mã nguồn thực hành đính kèm
                    </span>
                    <span className="text-[10px] font-mono uppercase bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 px-2 py-0.5 rounded">
                      {currentModule.codeLang || 'python'}
                    </span>
                  </div>
                  <pre className="p-3.5 rounded-2xl bg-slate-900 text-slate-100 text-xs font-mono overflow-x-auto border border-slate-800 max-h-40">
                    <code>{currentModule.starterCode}</code>
                  </pre>
                </div>
              )}
            </div>

            {/* Action Buttons */}
            <div className="pt-4 border-t border-slate-200/80 dark:border-slate-800 flex flex-col sm:flex-row items-center gap-3">
              <button
                type="button"
                onClick={() => handleStartLessonAction(currentModule)}
                className="w-full sm:flex-1 flex items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white px-5 py-3 text-xs sm:text-sm font-extrabold shadow-lg shadow-blue-500/25 transition-all active:scale-[0.98]"
              >
                <Sparkles className="h-4 w-4 text-amber-300" />
                <span>Bắt đầu học cùng AI Tutor (Socratic)</span>
                <ArrowRight className="h-4 w-4" />
              </button>

              {currentModule.starterCode && onOpenPracticeInSandbox && (
                <button
                  type="button"
                  onClick={() => handlePracticeAction(currentModule)}
                  className="w-full sm:w-auto flex items-center justify-center gap-2 rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 px-4 py-3 text-xs sm:text-sm font-bold transition-all"
                  title="Mở mã nguồn này trong Sandbox để chạy thử"
                >
                  <Play className="h-4 w-4 text-emerald-500 fill-emerald-500" />
                  <span>Mở trong Sandbox</span>
                </button>
              )}
            </div>

          </div>
        </div>

      </div>
    </div>
  );
};
