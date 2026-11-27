import os
from pathlib import Path
from PIL import Image, ImageDraw

demo_dir = Path('demo_samples')
code_dir = demo_dir / 'code_files'
img_dir = demo_dir / 'terminal_images'

code_dir.mkdir(parents=True, exist_ok=True)
img_dir.mkdir(parents=True, exist_ok=True)

# 1. Tạo các file code mẫu
samples = {
    '01_bubble_sort_inefficient.py': '''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Test với mảng lớn
import random
large_array = [random.randint(1, 1000) for _ in range(20000)]
print('Bắt đầu sắp xếp...')
sorted_arr = bubble_sort(large_array)
print('Hoàn thành!')
''',

    '02_infinite_recursion_fibonacci.py': '''def fib(n):
    # Lỗi: Thiếu điều kiện cơ sở (base case) khi n <= 1
    return fib(n - 1) + fib(n - 2)

print('Tính số Fibonacci thứ 5:')
print(fib(5))
''',

    '03_mutable_default_argument.py': '''def append_item(val, target_list=[]):
    # Lỗi kinh điển trong Python: Default argument là một mutable object (list)
    target_list.append(val)
    return target_list

print('Lần gọi 1:', append_item('Apple'))
print('Lần gọi 2:', append_item('Banana'))
print('Lần gọi 3:', append_item('Cherry'))
# Kết quả bất ngờ: ['Apple', 'Banana', 'Cherry'] thay vì ['Cherry']
''',

    '04_off_by_one_index.py': '''students = ['An', 'Binh', 'Cuong', 'Dung']

# Lỗi: Duyệt vượt biên len(students) + 1
for i in range(len(students) + 1):
    print(f'Học sinh {i + 1}: {students[i]}')
''',

    '05_cpp_memory_leak.cpp': '''#include <iostream>

void process_data() {
    for (int i = 0; i < 10000; i++) {
        // Lỗi: Cấp phát động bằng new nhưng không dùng delete[] để giải phóng
        int* buffer = new int[500];
        buffer[0] = i;
    }
}

int main() {
    std::cout << "Dang xu ly du lieu..." << std::endl;
    process_data();
    std::cout << "Xu ly xong!" << std::endl;
    return 0;
}
''',

    '06_sql_injection_concatenation.py': '''import sqlite3

def find_user_by_username(user_input):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Lỗi bảo mật nghiêm trọng: Nối chuỗi trực tiếp vào câu lệnh SQL
    query = f"SELECT * FROM accounts WHERE username = '{user_input}'"
    print('Executing query:', query)
    cursor.execute(query)
    return cursor.fetchall()

# Input hiểm độc: admin' OR '1'='1
result = find_user_by_username("admin' OR '1'='1")
'''
}

for name, content in samples.items():
    file_path = code_dir / name
    file_path.write_text(content.strip(), encoding='utf-8')
    print('Created code file:', file_path)

# 2. Tạo các ảnh terminal lỗi chân thực
def create_terminal_image(filename, header, code_snippet, error_msg, exit_code='1'):
    width = 750
    height = 220
    img = Image.new('RGB', (width, height), color=(20, 24, 33))
    d = ImageDraw.Draw(img)
    
    # Title bar
    d.rectangle([0, 0, width, 32], fill=(30, 36, 48))
    d.ellipse([14, 11, 24, 21], fill=(239, 68, 68)) # red
    d.ellipse([32, 11, 42, 21], fill=(245, 158, 11)) # yellow
    d.ellipse([50, 11, 60, 21], fill=(16, 185, 129)) # green
    d.text((width // 2 - 80, 9), 'Terminal - bash (python)', fill=(156, 163, 175))
    
    # Body text
    y = 48
    d.text((25, y), '$ python main.py', fill=(229, 231, 235))
    y += 28
    d.text((25, y), header, fill=(248, 113, 113))
    y += 24
    d.text((45, y), code_snippet, fill=(209, 213, 219))
    y += 28
    d.text((25, y), error_msg, fill=(239, 68, 68))
    y += 34
    d.text((25, y), f'Process finished with exit code {exit_code}', fill=(107, 114, 128))
    
    out_path = img_dir / filename
    img.save(out_path)
    print('Created terminal image:', out_path)

create_terminal_image(
    '01_terminal_index_error.png',
    'Traceback (most recent call last): File "solution.py", line 5, in <module>',
    'print(students[i])',
    'IndexError: list index out of range'
)

create_terminal_image(
    '02_terminal_recursion_error.png',
    'Traceback (most recent call last): [Previous line repeated 996 more times]',
    'return fib(n - 1) + fib(n - 2)',
    'RecursionError: maximum recursion depth exceeded in comparison'
)

create_terminal_image(
    '03_terminal_type_error.png',
    'Traceback (most recent call last): File "calc.py", line 12, in <module>',
    'total = "Tong diem: " + 85',
    'TypeError: can only concatenate str (not "int") to str'
)

create_terminal_image(
    '04_terminal_zerodivision_error.png',
    'Traceback (most recent call last): File "average.py", line 7, in compute_avg',
    'avg = total_sum / count',
    'ZeroDivisionError: division by zero'
)

create_terminal_image(
    '05_terminal_cpp_segfault.png',
    'Segmentation fault (core dumped) in ./binary_tree_search',
    'Thread 1 "app" received signal SIGSEGV, Segmentation fault.',
    '0x0000555555555189 in TreeNode::insert(int) () at tree.cpp:34',
    exit_code='139'
)

print('All demo assets generated successfully in demo_samples/')
