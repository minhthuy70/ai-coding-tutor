/**
 * Socratic Pedagogical AI Engine
 * Hỗ trợ:
 * 1. Gọi trực tiếp Google Gemini API (khi người dùng nhập API Key trong Settings)
 * 2. Gọi máy chủ Ollama cục bộ (http://localhost:11434)
 * 3. Bộ máy tri thức sư phạm Socratic ngoại tuyến (Built-in Knowledge Engine)
 */

import { ChatAttachment, ModelSettings } from '@/types/chat';

export interface SocraticEngineResult {
  content: string;
  followUps: string[];
  modelBadge: string;
}

// System Prompts for Different Pedagogical Personas
const PERSONA_SYSTEM_PROMPTS = {
  socratic: `Bạn là Trợ giảng Lập trình Socratic (AI Coding Tutor) tại một trường Đại học Công nghệ hàng đầu.
Phương pháp sư phạm của bạn tuân thủ nguyên tắc Socratic:
1. Đặt câu hỏi gợi mở để người học tự tư duy, không đưa ngay toàn bộ lời giải sẵn nếu sinh viên mới bắt đầu.
2. Chia nhỏ gợi ý theo cấp độ: Cấp 1 (Ý tưởng cốt lõi) -> Cấp 2 (Mã giả / Thuật toán) -> Cấp 3 (Mã nguồn minh họa).
3. Luôn phân tích độ phức tạp thời gian và không gian Big-O (Time & Space Complexity).
4. Khuyến khích sinh viên tự sửa lỗi và cảnh báo các trường hợp biên (edge cases).
5. Trả lời bằng tiếng Việt thân thiện, rõ ràng, định dạng Markdown chuẩn với code block syntax.`,

  algorithm_expert: `Bạn là Chuyên gia Thuật toán & Cấu trúc Dữ liệu (Algorithm & Big-O Expert).
Phong cách của bạn:
1. Tập trung phân tích chuyên sâu về độ phức tạp thời gian (Time Complexity) và không gian (Space Complexity) Big-O.
2. So sánh các hướng tiếp cận: Brute Force O(n²) vs Tối ưu O(n) hoặc O(n log n).
3. Phân tích Call Stack, cây đệ quy và quản lý bộ nhớ.
4. Nêu rõ các trường hợp biên đặc thù: mảng rỗng, n = 0, số âm, số nguyên cực đại.
5. Định dạng Markdown trực quan, có khối mã nguồn hoàn chỉnh chuẩn chỉnh.`,

  strict_reviewer: `Bạn là Chuyên gia Rà soát Mã nguồn Chuẩn mực (Clean Code & Security Reviewer).
Phong cách của bạn:
1. Đánh giá nghiêm ngặt theo chuẩn PEP 8 (với Python), Google C++ Style Guide hoặc chuẩn ECMAScript.
2. Phát hiện Code Smells: hàm quá dài, biến toàn cục, magic numbers, catch Exception quá rộng.
3. Rà soát bảo mật: SQL Injection, tràn bộ đệm, rò rỉ bộ nhớ, hardcoded secrets.
4. Đưa ra phiên bản Refactored Code rõ ràng kèm giải thích lý do cải tiến.`,

  casual: `Bạn là Bạn đồng hành Lập trình (Coding Study Buddy) vui tính, nhiệt tình, giải thích dễ hiểu từ cơ bản đến nâng cao.`
};

/**
 * Gọi Google Gemini 1.5 API trực tiếp từ Client-side (với API Key người dùng cấu hình)
 */
async function callGeminiAPI(
  prompt: string,
  attachments: ChatAttachment[],
  settings: ModelSettings
): Promise<string> {
  const apiKey = settings.geminiApiKey?.trim();
  if (!apiKey) {
    throw new Error('Chưa cấu hình Gemini API Key.');
  }

  const personaPrompt = PERSONA_SYSTEM_PROMPTS[settings.persona] || PERSONA_SYSTEM_PROMPTS.socratic;
  
  // Format parts
  const parts: any[] = [
    { text: `${personaPrompt}\n\n---\nCâu hỏi của sinh viên:\n${prompt}` }
  ];

  // Attach images if any (convert previewUrl / base64)
  for (const att of attachments) {
    if (att.category === 'image' && att.previewUrl) {
      try {
        const base64Data = att.previewUrl.split(',')[1] || '';
        if (base64Data) {
          parts.push({
            inline_data: {
              mime_type: att.type || 'image/png',
              data: base64Data
            }
          });
        }
      } catch (e) {
        console.warn('Lỗi xử lý ảnh đính kèm:', e);
      }
    } else if (att.fileContent) {
      parts.push({
        text: `\n[Tệp mã nguồn đính kèm: ${att.name}]\n\`\`\`\n${att.fileContent}\n\`\`\``
      });
    }
  }

  const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ parts }],
      generationConfig: {
        temperature: settings.temperature,
        maxOutputTokens: settings.maxTokens,
      }
    })
  });

  if (!response.ok) {
    const errData = await response.json().catch(() => ({}));
    throw new Error(errData?.error?.message || `Lỗi Gemini API (HTTP ${response.status})`);
  }

  const data = await response.json();
  const candidate = data?.candidates?.[0]?.content?.parts?.[0]?.text;
  if (!candidate) {
    throw new Error('Mô hình Gemini không trả về nội dung hợp lệ.');
  }
  return candidate;
}

/**
 * Gọi máy chủ Ollama cục bộ (offline)
 */
async function callOllamaAPI(
  prompt: string,
  settings: ModelSettings
): Promise<string> {
  const baseUrl = settings.ollamaBaseUrl?.trim() || 'http://localhost:11434';
  const personaPrompt = PERSONA_SYSTEM_PROMPTS[settings.persona] || PERSONA_SYSTEM_PROMPTS.socratic;

  const response = await fetch(`${baseUrl}/api/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'qwen2.5-coder',
      prompt: `${personaPrompt}\n\nSinh viên hỏi: ${prompt}`,
      stream: false,
      options: {
        temperature: settings.temperature,
        num_predict: settings.maxTokens
      }
    })
  });

  if (!response.ok) {
    throw new Error(`Không thể kết nối đến Ollama tại ${baseUrl}. Vui lòng kiểm tra lệnh 'ollama serve'.`);
  }

  const data = await response.json();
  return data.response;
}

/**
 * Bộ Máy Tri Thức Sư Phạm Socratic Cục Bộ (Built-In Pedagogical Knowledge Engine)
 * Hoạt động 100% độc lập, không phụ thuộc API ngoài, cung cấp câu trả lời sư phạm sâu sắc
 */
function generateBuiltInSocraticResponse(
  prompt: string,
  attachments: ChatAttachment[],
  settings: ModelSettings,
  selectedModelName: string
): SocraticEngineResult {
  const p = prompt.toLowerCase();
  const persona = settings.persona;

  // 1. Two Sum
  if (p.includes('two sum') || (p.includes('tổng') && p.includes('target')) || (p.includes('mảng') && p.includes('hai số'))) {
    return {
      modelBadge: `${selectedModelName} · Socratic Engine`,
      content: `### 🎯 Phân tích bài toán: Hai Con Số Có Tổng Bằng Target (Two Sum)

Chào bạn! Đây là bài toán kinh điển kiểm tra tư duy tối ưu cấu trúc dữ liệu từ $O(n^2)$ về $O(n)$.

---

#### 1. 💡 Câu hỏi gợi mở tư duy (Socratic Question)
* Nếu duyệt 2 vòng lặp lồng nhau (\`for i\` và \`for j\`), độ phức tạp sẽ là bao nhiêu?
* Khi ta đang đứng tại một phần tử $x$, số còn lại ta **cần tìm** (complement) là gì?
* Có cấu trúc dữ liệu nào cho phép ta **tra cứu xem một số đã từng xuất hiện hay chưa** chỉ với thời gian trung bình $O(1)$ không?

---

#### 2. 🔍 Gợi ý thuật toán (Two Sum với Hash Map)
Thay vì tìm kiếm tuyến tính, ta sử dụng một bảng băm (Dictionary trong Python hoặc \`unordered_map\` trong C++):
* **Key**: Giá trị của phần tử \`num\`.
* **Value**: Chỉ số \`index\` của phần tử đó trong mảng.
* Khi duyệt qua từng số, ta tính \`complement = target - num\`:
  * Nếu \`complement\` đã nằm trong bảng băm $\\rightarrow$ **Tìm thấy cặp nghiệm!**
  * Nếu chưa có $\\rightarrow$ Lưu số hiện tại vào bảng băm và tiếp tục duyệt.

---

#### 3. 💻 Mã nguồn tham khảo tối ưu:
\`\`\`python
def two_sum(nums, target):
    """
    Tìm vị trí 2 số có tổng bằng target
    Độ phức tạp: O(n) thời gian, O(n) không gian
    """
    seen = {} # map giá trị -> chỉ số
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Ví dụ kiểm thử:
print("Kết quả:", two_sum([2, 7, 11, 15], 9)) # Output: [0, 1]
\`\`\`

---

#### 4. ⏱️ Phân tích Độ phức tạp (Big-O):
* **Thời gian (Time Complexity)**: $O(n)$ vì chỉ cần duyệt qua mảng đúng 1 lần; thao tác tìm kiếm và chèn vào Hash Table mất trung bình $O(1)$.
* **Không gian (Space Complexity)**: $O(n)$ do lưu trữ tối đa $n$ phần tử trong bảng băm \`seen\`.

> ❓ **Thử thách tiếp theo:** Nếu mảng đầu vào **đã được sắp xếp tăng dần**, bạn có thể giải bài này với bộ nhớ phụ $O(1)$ bằng kỹ thuật **Hai con trỏ (Two Pointers)** không?`,
      followUps: [
        'Hướng dẫn giải Two Sum bằng kỹ thuật Two Pointers O(1) bộ nhớ',
        'Cách viết bài toán này bằng ngôn ngữ C++ với std::unordered_map',
        'Phân tích trường hợp xấu nhất Worst-Case của Hash Table khi bị xung đột hash'
      ]
    };
  }

  // 2. Valid Parentheses (Dấu ngoặc hợp lệ)
  if (p.includes('parentheses') || p.includes('ngoặc') || p.includes('valid bracket')) {
    return {
      modelBadge: `${selectedModelName} · Socratic Engine`,
      content: `### 🎯 Phân tích bài toán: Kiểm tra Dấu Ngoặc Hợp Lệ (Valid Parentheses)

Bài toán này rèn luyện việc lựa chọn cấu trúc dữ liệu **Ngăn xếp (Stack - LIFO: Last In, First Out)**.

---

#### 1. 💡 Tư duy giải quyết:
Một chuỗi ngoặc hợp lệ phải thỏa mãn:
1. Mọi dấu mở ngoặc (\`(\`, \`[\`, \`{\`) phải được đóng bởi dấu ngoặc cùng loại.
2. Dấu ngoặc mở sau cùng thì phải được đóng trước tiên $\\rightarrow$ Tính chất chuẩn của **Stack**!

---

#### 2. 🔍 Các bước thực hiện:
* Duyệt từng ký tự trong chuỗi:
  * Nếu gặp **dấu mở**: Đẩy vào Stack.
  * Nếu gặp **dấu đóng**:
    * Kiểm tra xem Stack có rỗng không? (Nếu rỗng $\\rightarrow$ Thừa dấu đóng $\\rightarrow$ Sai).
    * Lấy phần tử đỉnh của Stack ra so khớp. Nếu không cùng loại $\\rightarrow$ Sai.
* Kết thúc chuỗi: Nếu Stack còn phần tử $\\rightarrow$ Thừa dấu mở $\\rightarrow$ Sai. Chỉ đúng khi Stack hoàn toàn rỗng.

---

#### 3. 💻 Mã nguồn tham khảo (Python):
\`\`\`python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Lấy phần tử đỉnh nếu stack không rỗng, ngược lại gán ký tự rác '#'
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # Gặp dấu mở ngoặc
            stack.append(char)
            
    return len(stack) == 0

# Kiểm thử:
print(is_valid_parentheses("()[]{}")) # True
print(is_valid_parentheses("([)]"))   # False
print(is_valid_parentheses("((("))    # False
\`\`\`

---

#### 4. ⏱️ Đánh giá Big-O:
* **Thời gian (Time)**: $O(n)$ với $n$ là độ dài chuỗi ký tự.
* **Bộ nhớ (Space)**: $O(n)$ trong trường hợp xấu nhất toàn dấu mở ngoặc (ví dụ \`"(((((("\`).`,
      followUps: [
        'Cần xử lý thế nào nếu chuỗi có thêm ký tự chữ cái và toán tử?',
        'Cách cài đặt bài toán này bằng Stack trong C++ (std::stack)',
        'Gợi ý cách mở rộng cho bài toán tìm chuỗi ngoặc hợp lệ dài nhất (Longest Valid Parentheses)'
      ]
    };
  }

  // 3. QuickSort / MergeSort / Thuật toán sắp xếp
  if (p.includes('quicksort') || p.includes('quick sort') || p.includes('mergesort') || p.includes('sắp xếp') || p.includes('sort')) {
    return {
      modelBadge: `${selectedModelName} · Socratic Engine`,
      content: `### 🎯 Chuyên đề: Thuật toán Sắp xếp Chia để trị (Divide & Conquer)

Sắp xếp là nền tảng cốt lõi của khoa học máy tính. Ta thường so sánh giữa **QuickSort** và **MergeSort**.

---

#### 1. ⚖️ So sánh tổng quan giữa QuickSort và MergeSort:
| Tiêu chí | QuickSort | MergeSort |
| :--- | :--- | :--- |
| **Chiến lược** | Phân hoạch quanh phần tử chốt (Pivot) | Chia đôi mảng rồi trộn đệ quy (Merge) |
| **Thời gian trung bình** | $O(n \\log n)$ (Rất nhanh trong thực tế) | $O(n \\log n)$ (Ổn định mọi trường hợp) |
| **Thời gian xấu nhất** | $O(n^2)$ (Khi pivot chọn kém trên mảng đã xếp) | $O(n \\log n)$ |
| **Bộ nhớ phụ (Space)** | $O(\\log n)$ (Call stack) | $O(n)$ (Mảng phụ để trộn) |
| **Tính ổn định (Stable)** | Không ổn định | Ổn định (Stable) |

---

#### 2. 💻 Mã nguồn QuickSort phân hoạch Lomuto chuẩn mực:
\`\`\`python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Thử nghiệm với mảng mẫu:
sample_array = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(sample_array)
print("Mảng sau sắp xếp:", sorted_arr)
\`\`\`

---

#### 3. 💡 Lời khuyên tối ưu thực tế:
* **Chọn Pivot thông minh**: Dùng kỹ thuật *Median-of-three* (trung vị của phần tử đầu, giữa và cuối) để tránh rơi vào $O(n^2)$.
* **Sắp xếp mảng nhỏ**: Khi kích thước mảng con $\\le 16$, chuyển sang **Insertion Sort** để giảm chi phí gọi hàm đệ quy.`,
      followUps: [
        'Phân tích chi tiết trường hợp xấu nhất O(n²) của QuickSort',
        'Cách cài đặt MergeSort với mảng phụ trong C++',
        'Tại sao Python sử dụng thuật toán Timsort thay vì QuickSort thuần túy?'
      ]
    };
  }

  // 4. Segmentation Fault / Memory Leak / C++ Pointers
  if (p.includes('segmentation fault') || p.includes('segfault') || p.includes('memory leak') || p.includes('con trỏ') || p.includes('pointer')) {
    return {
      modelBadge: `${selectedModelName} · Debug & Security`,
      content: `### 🚨 Chẩn đoán Lỗi: Segmentation Fault & Quản lý Bộ nhớ C/C++

Lỗi **Segmentation Fault (core dumped)** xảy ra khi chương trình cố gắng truy cập vào vùng bộ nhớ mà hệ điều hành không cho phép.

---

#### 1. 🔍 4 Nguyên nhân phổ biến nhất:
1. **Giải tham chiếu con trỏ NULL (Null Pointer Dereference)**:
   \`\`\`cpp
   int* ptr = nullptr;
   *ptr = 10; // 💥 CRASH ngay lập tức!
   \`\`\`
2. **Truy cập mảng vượt chỉ số (Out-of-bounds Array Access)**:
   \`\`\`cpp
   int arr[5];
   arr[100] = 42; // Ghi đè vào vùng nhớ khác!
   \`\`\`
3. **Con trỏ lơ lửng (Dangling Pointer)**: Sử dụng vùng nhớ sau khi đã gọi \`free()\` hoặc \`delete\`.
4. **Tràn ngăn xếp (Stack Overflow)**: Đệ quy vô hạn hoặc khai báo mảng cục bộ quá lớn trên Stack (\`int arr[10000000];\`).

---

#### 2. 🛠️ Quy trình Debug từng bước:
1. **Biên dịch kèm cờ Debug & AddressSanitizer**:
   \`\`\`bash
   g++ -g -fsanitize=address main.cpp -o main
   ./main
   \`\`\`
   *(Trình biên dịch sẽ in ra chính xác dòng code gây ra lỗi cùng biểu đồ bộ nhớ)*
2. **Sử dụng GDB để xác định vị trí Crash**:
   \`\`\`bash
   gdb ./main
   (gdb) run
   (gdb) backtrace # Lệnh bt để xem call stack tại điểm crash
   \`\`\`

---

#### 3. 🛡️ Cách phòng ngừa hiện đại (Modern C++):
* Thay vì con trỏ thô (\`raw pointer\`) và \`malloc/free\`, luôn ưu tiên:
  * \`std::vector\` thay cho mảng tĩnh C.
  * \`std::unique_ptr\` hoặc \`std::shared_ptr\` để bộ nhớ tự giải phóng theo nguyên lý **RAII**.`,
      followUps: [
        'Hướng dẫn cài đặt và sử dụng công cụ kiểm tra rò rỉ Valgrind',
        'Cách chuyển đổi con trỏ thô C sang std::unique_ptr trong C++11',
        'Khác nhau giữa cấp phát trên Stack và Heap'
      ]
    };
  }

  // 5. Binary Search (Tìm kiếm nhị phân)
  if (p.includes('binary search') || p.includes('tìm kiếm nhị phân')) {
    return {
      modelBadge: `${selectedModelName} · Socratic Engine`,
      content: `### 🎯 Phân tích Thuật toán: Tìm kiếm Nhị phân (Binary Search)

Tìm kiếm nhị phân là thuật toán kinh điển giúp giảm số phép so sánh từ $O(n)$ xuống $O(\\log n)$.

---

#### 1. 💡 Điều kiện tiên quyết:
* Mảng đầu vào **BẮT BUỘC phải được sắp xếp** theo thứ tự tăng dần (hoặc giảm dần).

---

#### 2. ⚠️ Lỗi tràn số nguyên kinh điển (Integer Overflow Bug):
Nhiều lập trình viên viết:
\`\`\`cpp
int mid = (left + right) / 2; // ❌ CÓ THỂ TRÀN SỐ NGUYÊN nếu left + right > 2^31 - 1
\`\`\`
Công thức chuẩn mực an toàn:
\`\`\`cpp
int mid = left + (right - left) / 2; // ✅ Luôn an toàn!
\`\`\`

---

#### 3. 💻 Mã nguồn chuẩn (Python):
\`\`\`python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid # Tìm thấy tại vị trí mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 # Không tìm thấy

# Thử nghiệm:
data = [-1, 0, 3, 5, 9, 12]
print("Vị trí số 9:", binary_search(data, 9)) # Output: 4
print("Vị trí số 2:", binary_search(data, 2)) # Output: -1
\`\`\`

---

#### 4. ⏱️ Độ phức tạp:
* **Thời gian (Time)**: $O(\\log n)$ vì sau mỗi lần so sánh, không gian tìm kiếm giảm đi một nửa ($n \\rightarrow n/2 \\rightarrow n/4 \\rightarrow \\dots \\rightarrow 1$).
* **Không gian (Space)**: $O(1)$ với phiên bản lặp (Iterative).`,
      followUps: [
        'Cách tìm vị trí biên trái (Lower Bound) và biên phải (Upper Bound)',
        'Ứng dụng Binary Search trên không gian nghiệm (Binary Search on Answer)',
        'Viết phiên bản đệ quy của Binary Search và phân tích Call Stack'
      ]
    };
  }

  // 6. Python OOP / Clean Code
  if (p.includes('oop') || p.includes('hướng đối tượng') || p.includes('class') || p.includes('kế thừa') || p.includes('đa hình')) {
    return {
      modelBadge: `${selectedModelName} · OOP & Clean Code`,
      content: `### 🧱 Lập trình Hướng đối tượng (OOP) & 4 Trụ cột Cốt lõi

Lập trình hướng đối tượng giúp đóng gói dữ liệu và hành vi thành các thực thể mô phỏng thế giới thực.

---

#### 1. 🏛️ 4 Trụ cột cốt lõi của OOP:
1. **Tính Đóng gói (Encapsulation)**: Che giấu chi tiết cài đặt nội bộ, chỉ cung cấp giao diện công khai an toàn (dùng dấu \`_\` hoặc \`__\` trong Python).
2. **Tính Kế thừa (Inheritance)**: Lớp con tái sử dụng và mở rộng các thuộc tính, phương thức của lớp cha.
3. **Tính Đa hình (Polymorphism)**: Cùng một tên phương thức nhưng có cách thực thi khác nhau tùy thuộc vào đối tượng đang gọi.
4. **Tính Trừu tượng (Abstraction)**: Chỉ thể hiện những tính năng cần thiết của đối tượng mà bỏ qua các chi tiết phức tạp.

---

#### 2. 💻 Minh họa bằng Python chuẩn Clean Code:
\`\`\`python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Lớp cơ sở trừu tượng đại diện cho hình học"""
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
        
    def calculate_area(self) -> float:
        return self._width * self._height

class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius
        
    def calculate_area(self) -> float:
        import math
        return math.pi * (self._radius ** 2)

# Đa hình trong thực tế:
shapes = [Rectangle(4, 5), Circle(3)]
for s in shapes:
    print(f"Diện tích {s.__class__.__name__}: {s.calculate_area():.2f}")
\`\`\`

---

#### 3. 💡 Lời khuyên Clean Code:
* Ưu tiên **Composition over Inheritance** (kết hợp thay vì lạm dụng kế thừa sâu).
* Tuân thủ nguyên lý **SOLID**, đặc biệt là **Single Responsibility Principle** (mỗi lớp chỉ đảm nhận một trách nhiệm duy nhất).`,
      followUps: [
        'Giải thích chi tiết 5 nguyên lý SOLID qua ví dụ code',
        'Cách sử dụng Dataclasses trong Python 3.7+ để tối giản boilerplate code',
        'Phân biệt Abstract Class và Interface trong Java / C++'
      ]
    };
  }

  // 7. General Pedagogical Socratic Fallback
  const personaIntro = 
    persona === 'algorithm_expert'
      ? 'Chuyên gia Thuật toán & Tối ưu Big-O'
      : persona === 'strict_reviewer'
      ? 'Chuyên gia Đánh giá Chuẩn Mã nguồn & Bảo mật'
      : 'Trợ giảng Socratic AI';

  return {
    modelBadge: `${selectedModelName} · ${personaIntro}`,
    content: `### 🤖 [${personaIntro}] Hướng dẫn Giải đáp & Phân tích

Cảm ơn bạn đã đặt câu hỏi: *"**${prompt.slice(0, 80)}${prompt.length > 80 ? '...' : ''}**"*

---

#### 1. 💡 Nhận diện Vấn đề & Định hướng Tiếp cận
* Để giải quyết bài toán này một cách tối ưu, ta cần xác định rõ:
  1. **Đầu vào (Input)** và kiểu dữ liệu tương ứng.
  2. **Đầu ra mong đợi (Expected Output)** và các ràng buộc về kích thước dữ liệu.
  3. Cấu trúc dữ liệu nào (Mảng, Ngăn xếp, Hàng đợi, Bảng băm, Cây) phù hợp nhất với tần suất truy xuất?

---

#### 2. 🎯 Gợi ý Từng bước (Socratic Step-by-Step):
* **Bước 1**: Bắt đầu bằng giải thuật trực quan (Brute Force) để hiểu rõ luồng chạy và đảm bảo tính đúng đắn.
* **Bước 2**: Nhận diện các phép tính hoặc vòng lặp bị lặp lại vô ích để tìm cách lưu trữ kết quả trung gian (Caching / Memoization / Hash Map).
* **Bước 3**: Kiểm tra các trường hợp biên đặc biệt (mảng rỗng, dữ liệu cực đại, giá trị âm hoặc trùng lặp).

---

#### 3. 💻 Đoạn mã tham khảo khung thuật toán:
\`\`\`python
def solve_problem(data):
    """
    Khung giải thuật chuẩn hóa
    Độ phức tạp: O(n) thời gian, O(1) bộ nhớ phụ
    """
    if not data:
        return None
        
    result = []
    # Xử lý tuần tự theo logic thuật toán
    for item in data:
        # TODO: Áp dụng điều kiện xử lý của bài toán
        result.append(item)
        
    return result

# Chạy thử nghiệm:
sample = [1, 2, 3, 4, 5]
print("Kết quả:", solve_problem(sample))
\`\`\`

---

#### 4. ⏱️ Đánh giá Độ phức tạp (Big-O):
* **Thời gian (Time)**: Đạt $O(n)$ tuyến tính.
* **Không gian (Space)**: Tối ưu với $O(1)$ bộ nhớ phụ trợ.

> 💡 *Bạn có thể nhấn nút **[▶ Chạy]** ở góc khối code để mở ngay **Interactive Code Sandbox**, hoặc nhấn **[🛡️ Soát lỗi]** để kiểm tra chuẩn PEP 8.*`,
    followUps: [
      'Gợi ý cách tối ưu thuật toán này với bộ nhớ O(1)',
      'Phân tích các trường hợp biên (Edge Cases) dễ gây lỗi',
      'Hướng dẫn viết bộ Test Cases tự động kiểm thử'
    ]
  };
}

/**
 * Hàm điều phối chính để sinh phản hồi cho Trợ giảng AI
 */
export async function getSocraticAssistantResponse(
  userText: string,
  attachments: ChatAttachment[],
  settings: ModelSettings,
  selectedModelName: string
): Promise<SocraticEngineResult> {
  // 1. Nếu người dùng chọn dùng Gemini và đã cung cấp API key
  if (settings.aiProvider === 'gemini' && settings.geminiApiKey?.trim()) {
    try {
      const liveContent = await callGeminiAPI(userText, attachments, settings);
      return {
        modelBadge: `Gemini 1.5 Flash (Cloud Live)`,
        content: liveContent,
        followUps: [
          'Giải thích chi tiết hơn về đoạn code trên',
          'Đưa ra các test case biên để kiểm thử',
          'Tối ưu độ phức tạp thời gian và không gian'
        ]
      };
    } catch (err: any) {
      console.warn('Gemini API call failed, falling back to built-in Socratic engine:', err);
      const fallback = generateBuiltInSocraticResponse(userText, attachments, settings, selectedModelName);
      return {
        ...fallback,
        content: `> ⚠️ **Thông báo kết nối API:** Không thể kết nối tới Gemini API (${err?.message || 'Lỗi mạng hoặc API key chưa đúng'}). Hệ thống đã tự động chuyển sang **Bộ máy Socratic Cục bộ** để phục vụ bạn ngay lập tức.\n\n---\n\n${fallback.content}`
      };
    }
  }

  // 2. Nếu người dùng chọn dùng Ollama
  if (settings.aiProvider === 'ollama') {
    try {
      const ollamaContent = await callOllamaAPI(userText, settings);
      return {
        modelBadge: `Ollama Local (Offline)`,
        content: ollamaContent,
        followUps: [
          'Phân tích chi tiết độ phức tạp thuật toán này',
          'Viết lại bằng một ngôn ngữ lập trình khác',
          'Kiểm tra lỗi tiềm ẩn trong đoạn mã'
        ]
      };
    } catch (err: any) {
      console.warn('Ollama API call failed, falling back to built-in Socratic engine:', err);
      const fallback = generateBuiltInSocraticResponse(userText, attachments, settings, selectedModelName);
      return {
        ...fallback,
        content: `> ⚠️ **Thông báo kết nối Ollama:** ${err?.message || 'Không thể kết nối máy chủ Ollama cục bộ'}. Hệ thống đã tự động chuyển sang **Bộ máy Socratic Cục bộ**.\n\n---\n\n${fallback.content}`
      };
    }
  }

  // 3. Mặc định: Dùng Bộ máy Socratic Tri thức Cục bộ (Free, Nhanh, Đầy đủ)
  return generateBuiltInSocraticResponse(userText, attachments, settings, selectedModelName);
}
