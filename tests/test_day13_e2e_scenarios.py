"""
Day 13: End-to-End Multimodal Chat API & 30 Real-World Scenarios
Author: AI Coding Tutor Team
Description:
    Bộ kiểm thử tích hợp toàn diện 30 kịch bản thực tế của Ngày 13:
    - 10 kịch bản câu hỏi lý thuyết / thuật toán / cú pháp (Text Only)
    - 10 kịch bản câu hỏi kết hợp tệp mã nguồn (.py, .cpp, .sql)
    - 10 kịch bản câu hỏi kết hợp ảnh chụp màn hình lỗi Terminal (Vision OCR)
"""

import os
import sys
import io
import time
import pytest
from pathlib import Path
from PIL import Image, ImageDraw
from fastapi.testclient import TestClient

# Thêm backend vào sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")

from app.main import app

client = TestClient(app)


def create_synthetic_terminal_image(title: str, code_line: str, error_line: str) -> bytes:
    """Tạo ảnh giả lập chụp màn hình terminal lỗi sắc nét phục vụ test OCR."""
    img = Image.new('RGB', (650, 180), color=(25, 25, 30))
    d = ImageDraw.Draw(img)
    d.text((20, 20), title, fill=(255, 120, 120))
    d.text((20, 60), f"  File 'solution.py', line 12: {code_line}", fill=(210, 210, 210))
    d.text((20, 100), error_line, fill=(255, 90, 90))
    d.text((20, 140), ">>> Process finished with exit code 1", fill=(140, 140, 140))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()


class TestDay13EndToEndScenarios:

    # =========================================================================
    # NHÓM 1: 10 KỊCH BẢN CHỈ TEXT (THEORY, SYNTAX, ALGORITHMS)
    # =========================================================================

    def test_t01_quicksort_complexity(self):
        """Kịch bản T01: Phân tích độ phức tạp QuickSort."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Phân tích độ phức tạp thời gian Big-O của QuickSort trong trường hợp xấu nhất và tốt nhất."})
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "success"
        assert len(data["reply"]) > 50

    def test_t02_cpp_pointer_memory(self):
        """Kịch bản T02: Quản lý bộ nhớ con trỏ C++."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Làm sao để tránh dangling pointer và memory leak khi quản lý con trỏ trong C++?", "language": "cpp"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t03_pep8_indentation(self):
        """Kịch bản T03: Quy chuẩn PEP 8 Python."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "PEP 8 quy định thụt lề bao nhiêu khoảng trắng và cách đặt tên hàm như thế nào trong Python?", "language": "python"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t04_list_vs_tuple_mutability(self):
        """Kịch bản T04: Khác biệt List vs Tuple."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Phân biệt List và Tuple trong Python về tính biến đổi và hiệu năng bộ nhớ."})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t05_binary_search_prerequisite(self):
        """Kịch bản T05: Điều kiện Binary Search."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Tại sao thuật toán Binary Search bắt buộc mảng đầu vào phải được sắp xếp trước?"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t06_recursion_base_case(self):
        """Kịch bản T06: Đệ quy và Base Case."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Giải thích khái niệm Đệ quy và điều gì sẽ xảy ra nếu hàm đệ quy thiếu điều kiện dừng?"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t07_hash_table_collision(self):
        """Kịch bản T07: Bảng băm và xung đột."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Bảng băm (Hash Table) xử lý xung đột va chạm bằng phương pháp Separate Chaining như thế nào?"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t08_stack_vs_queue(self):
        """Kịch bản T08: Stack (LIFO) vs Queue (FIFO)."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "So sánh cơ chế LIFO của Stack và FIFO của Queue cùng ví dụ ứng dụng thực tế."})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t09_try_except_finally(self):
        """Kịch bản T09: Xử lý ngoại lệ try-except-finally."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Khối finally trong try-except-finally có chắc chắn luôn chạy không, kể cả khi có lệnh return?"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_t10_oop_inheritance_polymorphism(self):
        """Kịch bản T10: Tính kế thừa và đa hình trong OOP."""
        resp = client.post("/api/tutor/multimodal-chat", data={"prompt": "Giải thích tính kế thừa và tính đa hình trong Lập trình hướng đối tượng OOP."})
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    # =========================================================================
    # NHÓM 2: 10 KỊCH BẢN TEXT + FILE CODE (LOGIC, PERFORMANCE, SYNTAX BUGS)
    # =========================================================================

    def test_f01_inefficient_bubble_sort(self):
        """Kịch bản F01: Thuật toán sắp xếp chạy chậm O(n^2)."""
        code = b"def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(n):\n            if arr[i] < arr[j]:\n                arr[i], arr[j] = arr[j], arr[i]\n    return arr\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Tại sao code sắp xếp này chạy rất chậm khi mảng có 50.000 phần tử?"},
            files=[("code_files", ("bubble.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["filesCount"] == 1

    def test_f02_infinite_recursion_fibonacci(self):
        """Kịch bản F02: Đệ quy Fibonacci tràn stack."""
        code = b"def fib(n):\n    return fib(n - 1) + fib(n - 2)\nprint(fib(5))\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Hàm Fibonacci của em bị lỗi RecursionError: maximum recursion depth exceeded, sửa sao ạ?"},
            files=[("code_files", ("fib.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f03_cpp_memory_leak(self):
        """Kịch bản F03: Rò rỉ bộ nhớ C++ trong vòng lặp."""
        code = b"#include <iostream>\nint main() {\n    for (int i = 0; i < 1000; i++) {\n        int* arr = new int[500];\n        // do something\n    }\n    return 0;\n}\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Chương trình C++ này có nguy cơ rò rỉ bộ nhớ (memory leak) ở đâu?", "language": "cpp"},
            files=[("code_files", ("leak.cpp", code, "text/x-c++"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f04_mutable_default_argument(self):
        """Kịch bản F04: Lỗi mutable default argument."""
        code = b"def append_to_list(val, my_list=[]):\n    my_list.append(val)\n    return my_list\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Tại sao mỗi lần gọi hàm này thì list lại tích lũy kết quả của các lần gọi trước?"},
            files=[("code_files", ("default_arg.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f05_off_by_one_index(self):
        """Kịch bản F05: Lỗi duyệt mảng vượt biên (Off-by-one)."""
        code = b"arr = [10, 20, 30]\nfor i in range(len(arr) + 1):\n    print(arr[i])\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Đoạn mã này báo lỗi IndexError ở dòng nào và vì sao?"},
            files=[("code_files", ("index_bug.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f06_unclosed_file_resource(self):
        """Kịch bản F06: Quên đóng file, không dùng context manager with."""
        code = "f = open('data.txt', 'r')\ncontent = f.read()\n# quen dong file\n".encode('utf-8')
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Tại sao dùng with open() lại tốt hơn cách mở file truyền thống này?"},
            files=[("code_files", ("file_io.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f07_string_concatenation_inefficiency(self):
        """Kịch bản F07: Cộng chuỗi không tối ưu trong vòng lặp."""
        code = b"s = ''\nfor i in range(10000):\n    s += str(i)\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Tại sao việc cộng chuỗi trong vòng lặp này lại ngốn nhiều bộ nhớ và chậm?"},
            files=[("code_files", ("str_concat.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f08_builtin_shadowing(self):
        """Kịch bản F08: Đặt tên biến trùng với built-in keyword."""
        code = b"list = [1, 2, 3]\nnew_list = list('abc')\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Tại sao dòng thứ 2 lại báo lỗi TypeError: 'list' object is not callable?"},
            files=[("code_files", ("shadowing.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f09_deadlock_threads(self):
        """Kịch bản F09: Khóa tài nguyên gây Deadlock."""
        code = b"import threading\nlock1 = threading.Lock()\nlock2 = threading.Lock()\n# Thread 1: lock1 then lock2\n# Thread 2: lock2 then lock1\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Nguyên nhân gây ra hiện tượng Deadlock trong đoạn code đa luồng này là gì?"},
            files=[("code_files", ("deadlock.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_f10_sql_injection_concatenation(self):
        """Kịch bản F10: Format chuỗi SQL trực tiếp nguy cơ Injection."""
        code = b"def get_user(user_id):\n    query = f'SELECT * FROM users WHERE id = {user_id}'\n    return db.execute(query)\n"
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Hàm SQL này có lỗ hổng bảo mật gì và cách dùng Parameterized Query để phòng tránh?"},
            files=[("code_files", ("query.py", code, "text/x-python"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    # =========================================================================
    # NHÓM 3: 10 KỊCH BẢN TEXT + ẢNH CHỤP LỖI MÀN HÌNH TERMINAL (VISION OCR)
    # =========================================================================

    def test_i01_terminal_index_error(self):
        """Kịch bản I01: Ảnh chụp terminal lỗi IndexError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "print(students[50])", "IndexError: list index out of range")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Em chạy code thì terminal báo lỗi như trong ảnh, thầy xem giúp em với ạ"},
            files=[("image_files", ("terminal_err01.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["imagesCount"] == 1

    def test_i02_terminal_zerodivision_error(self):
        """Kịch bản I02: Ảnh chụp terminal lỗi ZeroDivisionError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "avg = total / count", "ZeroDivisionError: division by zero")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Ảnh terminal báo lỗi gì vậy thầy?"},
            files=[("image_files", ("terminal_err02.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i03_terminal_recursion_error(self):
        """Kịch bản I03: Ảnh chụp terminal lỗi RecursionError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "return calculate(n)", "RecursionError: maximum recursion depth exceeded")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Màn hình của em bị lỗi tràn đệ quy như ảnh"},
            files=[("image_files", ("terminal_err03.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i04_terminal_type_error(self):
        """Kịch bản I04: Ảnh chụp terminal lỗi TypeError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "res = 'Tuoi: ' + 20", "TypeError: can only concatenate str (not 'int') to str")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Tại sao cộng chuỗi với số trong ảnh lại bị lỗi?"},
            files=[("image_files", ("terminal_err04.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i05_terminal_key_error(self):
        """Kịch bản I05: Ảnh chụp terminal lỗi KeyError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "val = config['database_url']", "KeyError: 'database_url'")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Em tra cứu dictionary thì bị lỗi như ảnh"},
            files=[("image_files", ("terminal_err05.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i06_terminal_attribute_error(self):
        """Kịch bản I06: Ảnh chụp terminal lỗi AttributeError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "res.append(10)", "AttributeError: 'NoneType' object has no attribute 'append'")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Thầy cho em hỏi lỗi AttributeError trong ảnh nghĩa là sao?"},
            files=[("image_files", ("terminal_err06.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i07_terminal_segmentation_fault(self):
        """Kịch bản I07: Ảnh chụp terminal lỗi Segmentation fault C++."""
        img_bytes = create_synthetic_terminal_image("Runtime Crash Detected:", "./my_program", "Segmentation fault (core dumped)")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Chương trình C++ của em bị crash như hình", "language": "cpp"},
            files=[("image_files", ("terminal_err07.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i08_terminal_syntax_error(self):
        """Kịch bản I08: Ảnh chụp terminal lỗi SyntaxError."""
        img_bytes = create_synthetic_terminal_image("  File 'script.py', line 5", "if x > 10", "SyntaxError: expected ':'")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Terminal báo lỗi SyntaxError như ảnh, chỉ giúp em với"},
            files=[("image_files", ("terminal_err08.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i09_terminal_indentation_error(self):
        """Kịch bản I09: Ảnh chụp terminal lỗi IndentationError."""
        img_bytes = create_synthetic_terminal_image("  File 'main.py', line 8", "    print(x)", "IndentationError: unexpected indent")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Lỗi thụt lề trong ảnh giải quyết thế nào?"},
            files=[("image_files", ("terminal_err09.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"

    def test_i10_terminal_name_error(self):
        """Kịch bản I10: Ảnh chụp terminal lỗi NameError."""
        img_bytes = create_synthetic_terminal_image("Traceback (most recent call last):", "print(result_counter)", "NameError: name 'result_counter' is not defined")
        resp = client.post(
            "/api/tutor/multimodal-chat",
            data={"prompt": "Ảnh terminal báo lỗi NameError này xử lý ra sao ạ?"},
            files=[("image_files", ("terminal_err10.png", img_bytes, "image/png"))]
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "success"
