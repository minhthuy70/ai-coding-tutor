# -*- coding: utf-8 -*-
"""
Authoritative Python 200 Corpus Generator & Parser Pipeline
Builds 200 comprehensive, authoritative Python curriculum documents:
- 100 English documents (Python 3.12 Official Docs, PEPs, CPython Internals, Data Structures & Algorithms, Concurrency)
- 100 Vietnamese documents (Giáo trình ĐH Cần Thơ, Bách Khoa, ĐHQG, Chuyên đề Lập trình Python & Tư duy Socratic)

Outputs:
1. data/01_original_documents/python_200/ (Raw representation & Catalog)
2. data/03_parser_outputs/mineru/05_python_200_authoritative/ (Parsed MinerU format with page markers & layout)
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "data" / "01_original_documents" / "python_200"
PARSER_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru" / "05_python_200_authoritative"

# List of 100 English Topics
EN_TOPICS = [
    ("EN_PY_001", "Python_Language_Architecture_and_CPython_Model", "Python Architecture & CPython Execution Model (Bytecode, PVM, GIL)", "Core Architecture"),
    ("EN_PY_002", "Variables_Dynamic_Typing_and_Object_References", "Variables, Dynamic Typing, and Object References in Python", "Core Syntax"),
    ("EN_PY_003", "Numeric_Types_and_Floating_Point_Arithmetic", "Numeric Types (int, float, complex) & Floating Point Arithmetic (IEEE 754)", "Data Types"),
    ("EN_PY_004", "Boolean_Logic_and_Truth_Value_Testing", "Boolean Logic, Truth Value Testing, and Short-Circuit Evaluation", "Control Flow"),
    ("EN_PY_005", "Strings_Unicode_Representation_and_Slicing", "Strings (str) Internal Representation, Unicode (PEP 393), and Slicing", "Data Types"),
    ("EN_PY_006", "String_Formatting_Evolution_and_FStrings", "String Formatting Evolution (% operator, str.format(), and PEP 498 f-strings)", "Strings"),
    ("EN_PY_007", "Lists_Dynamic_Array_Implementation_Amortized", "Lists (list) Dynamic Array Implementation, Amortized O(1) Operations", "Data Structures"),
    ("EN_PY_008", "List_Methods_and_Algorithms_Sorting_Searching", "List Methods and Common Algorithms (Sorting, Searching, Reversing)", "Data Structures"),
    ("EN_PY_009", "List_Comprehensions_Filtering_and_Nesting", "List Comprehensions, Filtering, and Nested Comprehensions", "Functional Idioms"),
    ("EN_PY_010", "Tuples_Immutability_Memory_and_Unpacking", "Tuples (tuple) Immutability, Memory Optimization, and Tuple Unpacking", "Data Structures"),
    ("EN_PY_011", "Namedtuples_and_Typing_NamedTuple_Records", "Namedtuples and typing.NamedTuple for Self-Documenting Data Records", "Data Structures"),
    ("EN_PY_012", "Dictionaries_Hash_Table_Architecture_and_Lookup", "Dictionaries (dict) Hash Table Architecture, Hash Invariants, and O(1) Lookup", "Data Structures"),
    ("EN_PY_013", "Dictionary_Methods_Views_and_Merge_Operators", "Dictionary Methods, Views, and Merging Operators (| and |=)", "Data Structures"),
    ("EN_PY_014", "Dictionary_Comprehensions_and_Counter_Idioms", "Dictionary Comprehensions and Frequency Counter Idioms", "Data Structures"),
    ("EN_PY_015", "Sets_Frozensets_and_Mathematical_Operations", "Sets (set, frozenset) Mathematical Operations and Hash Requirements", "Data Structures"),
    ("EN_PY_016", "Conditional_Statements_and_Ternary_Expressions", "Conditional Statements (if, elif, else) and Conditional Expressions (Ternary)", "Control Flow"),
    ("EN_PY_017", "While_Loops_Termination_Conditions_Safe_Loops", "While Loops, Termination Conditions, and Infinite Loop Prevention", "Control Flow"),
    ("EN_PY_018", "For_Loops_Iterables_and_For_Else_Construct", "For Loops, Iterables, Iterators, and the for...else Construct", "Control Flow"),
    ("EN_PY_019", "Loop_Control_Break_Continue_Pass_Sentinels", "Loop Control Statements (break, continue, pass) and Sentinel Values", "Control Flow"),
    ("EN_PY_020", "Function_Definitions_Parameters_and_Return_Values", "Function Definition (def), Parameters, and Return Value Semantics", "Functions"),
    ("EN_PY_021", "Positional_Keyword_PositionalOnly_Parameters", "Positional vs Keyword Arguments, Keyword-Only and Positional-Only Parameters (/ and *)", "Functions"),
    ("EN_PY_022", "Arbitrary_Arguments_Args_Kwargs_Wrappers", "Arbitrary Argument Lists (*args and **kwargs) in Wrapper Functions", "Functions"),
    ("EN_PY_023", "Default_Parameters_and_Mutable_Default_Trap", "Default Parameter Values and the Mutable Default Argument Trap", "Functions"),
    ("EN_PY_024", "Scope_Resolution_LEGB_Rule_in_Python", "Scope Resolution: The LEGB Rule (Local, Enclosing, Global, Built-in)", "Functions"),
    ("EN_PY_025", "Global_and_Nonlocal_Keywords_and_Closures", "The global and nonlocal Keywords and Lexical Closures", "Functions"),
    ("EN_PY_026", "Lambda_Functions_Map_Filter_and_Reduce", "Lambda Functions and Functional Programming Idioms (map, filter, reduce)", "Functional Idioms"),
    ("EN_PY_027", "Recursion_Base_Cases_and_Call_Stack_Limits", "Recursion Fundamentals: Base Cases, Recursive Steps, and Call Stack Limits", "Algorithms"),
    ("EN_PY_028", "Tail_Recursion_and_Memoization_LRU_Cache", "Tail Recursion and Memoization Techniques using functools.lru_cache", "Optimization"),
    ("EN_PY_029", "Exception_Handling_Try_Except_Else_Finally", "Exception Handling Architecture: try, except, else, and finally Clauses", "Exceptions"),
    ("EN_PY_030", "Builtin_Exception_Hierarchy_and_Tracebacks", "Built-in Exception Hierarchy (BaseException, Exception, ValueError, TypeError)", "Exceptions"),
    ("EN_PY_031", "Raising_Exceptions_Chaining_and_Custom_Errors", "Raising Exceptions, Chaining Exceptions (raise from), and Custom Exceptions", "Exceptions"),
    ("EN_PY_032", "Exception_Groups_and_ExceptStar_Syntax_PEP654", "Exception Groups and except* Syntax (PEP 654 in Python 3.11+)", "Exceptions"),
    ("EN_PY_033", "File_IO_Text_Files_UTF8_Buffering_Open", "File I/O: Text Files, Encoding (UTF-8), Buffering, and the open() Function", "File I/O"),
    ("EN_PY_034", "Context_Manager_Protocol_and_With_Statement", "The Context Manager Protocol (__enter__, __exit__) and the with Statement", "Context Managers"),
    ("EN_PY_035", "Contextlib_Module_Contextmanager_and_ExitStack", "contextlib Module: @contextmanager Decorator and ExitStack", "Context Managers"),
    ("EN_PY_036", "CSV_File_Processing_Reader_Writer_DictReader", "CSV File Processing: csv.reader, csv.writer, and DictReader/DictWriter", "File I/O"),
    ("EN_PY_037", "JSON_Serialization_Deserialization_Custom_Coders", "JSON Serialization and Deserialization: json module, Custom Encoders", "Data Formats"),
    ("EN_PY_038", "Binary_Data_IO_Bytes_ByteArray_and_Struct", "Binary Data I/O: bytes, bytearray, memoryview, and the struct Module", "Data Formats"),
    ("EN_PY_039", "OOP_Principles_Classes_and_Instances_in_Python", "Object-Oriented Programming (OOP) Principles: Class and Instance Concepts", "OOP"),
    ("EN_PY_040", "Init_Constructor_Self_Reference_and_Attributes", "The __init__ Constructor, the self Reference, and Instance Attributes", "OOP"),
    ("EN_PY_041", "Class_Attributes_vs_Instance_Attributes", "Class Attributes vs Instance Attributes and Class Namespaces", "OOP"),
    ("EN_PY_042", "Class_Methods_Static_Methods_and_Factory_Pattern", "Class Methods (@classmethod), Static Methods (@staticmethod), and Factory Patterns", "OOP"),
    ("EN_PY_043", "Encapsulation_Protected_and_Private_Name_Mangling", "Encapsulation: Public, Protected (_), and Private (__) Name Mangling", "OOP"),
    ("EN_PY_044", "Property_Decorators_Getters_Setters_Managed_Attr", "Property Decorators (@property, @setter, @deleter) for Managed Attributes", "OOP"),
    ("EN_PY_045", "Single_Inheritance_Code_Reuse_and_Super_Method", "Single Inheritance, Code Reuse, and the super() Function Mechanics", "OOP"),
    ("EN_PY_046", "Multiple_Inheritance_Diamond_Problem_C3_MRO", "Multiple Inheritance, Diamond Problem, and C3 Method Resolution Order (MRO)", "OOP"),
    ("EN_PY_047", "Polymorphism_and_Duck_Typing_EAFP_vs_LBYL", "Polymorphism and Duck Typing: 'EAFP' vs 'LBYL' Philosophy", "OOP"),
    ("EN_PY_048", "Abstract_Base_Classes_ABC_and_AbstractMethod", "Abstract Base Classes (abc module, ABC, @abstractmethod) and Interfaces", "OOP"),
    ("EN_PY_049", "Dunder_Representations_Str_vs_Repr_and_Format", "Dunder String Representations: __str__ vs __repr__ and __format__", "Magic Methods"),
    ("EN_PY_050", "Operator_Overloading_Arithmetic_Dunder_Methods", "Operator Overloading: Arithmetic Dunder Methods (__add__, __sub__, __mul__)", "Magic Methods"),
    ("EN_PY_051", "Comparison_Dunders_Eq_Lt_and_TotalOrdering", "Comparison Dunder Methods (__eq__, __lt__, __le__) and functools.total_ordering", "Magic Methods"),
    ("EN_PY_052", "Container_Protocol_Dunders_Len_GetItem_SetItem", "Container Protocol Dunders: __len__, __getitem__, __setitem__, __contains__", "Magic Methods"),
    ("EN_PY_053", "Callable_Objects_and_The_Call_Dunder_Method", "Callable Objects and the __call__ Dunder Method", "Magic Methods"),
    ("EN_PY_054", "Object_Lifecycle_New_Construction_vs_Init", "Object Lifecycle: __new__ Construction vs __init__ Initialization", "Advanced OOP"),
    ("EN_PY_055", "Descriptor_Protocol_Get_Set_Delete_Attributes", "The Descriptor Protocol (__get__, __set__, __delete__) and Attribute Lookup", "Advanced OOP"),
    ("EN_PY_056", "Metaclasses_Type_and_Class_Creation_Hooks", "Python Metaclasses (type, class creation hooks, __init_subclass__)", "Advanced OOP"),
    ("EN_PY_057", "Dataclasses_PEP557_Fields_and_Immutability", "Data Classes (PEP 557): dataclasses.dataclass, field(), and frozen=True", "Modern Python"),
    ("EN_PY_058", "Iterators_and_The_Iteration_Protocol_Iter_Next", "Iterators and the Iteration Protocol (__iter__ and __next__)", "Generators"),
    ("EN_PY_059", "Generator_Functions_Yield_and_State_Machines", "Generator Functions, the yield Keyword, and Generator State Machines", "Generators"),
    ("EN_PY_060", "Generator_Expressions_vs_List_Comprehensions", "Generator Expressions vs List Comprehensions: Memory Profiling & Lazy Evaluation", "Generators"),
    ("EN_PY_061", "Advanced_Generators_YieldFrom_Send_Throw_Close", "Advanced Generators: yield from, .send(), .throw(), and .close()", "Generators"),
    ("EN_PY_062", "Function_Decorators_Closures_and_Functools_Wraps", "Function Decorators: Decorator Syntax, Closures, and Preserving Metadata (@wraps)", "Decorators"),
    ("EN_PY_063", "Parameterized_Decorators_and_Class_Decorators", "Parameterized Decorators (Decorator Factories) and Class Decorators", "Decorators"),
    ("EN_PY_064", "Itertools_Module_Infinite_and_Combinatoric_Tools", "itertools Module: Infinite Iterators, Combinatoric Generators, and Slicing", "Standard Library"),
    ("EN_PY_065", "Functools_Module_Partial_Reduce_LRU_SingleDispatch", "functools Module: partial, reduce, lru_cache, and singledispatch", "Standard Library"),
    ("EN_PY_066", "Collections_Module_Deque_Counter_Defaultdict", "collections Module: deque, Counter, defaultdict, and OrderedDict", "Standard Library"),
    ("EN_PY_067", "Heapq_Module_Priority_Queues_and_MinHeaps", "heapq Module: Priority Queues, Binary Heaps, and nlargest/nsmallest", "Standard Library"),
    ("EN_PY_068", "Bisect_Module_Binary_Search_and_Sorted_Lists", "bisect Module: Binary Search in Sorted Sequences and Maintaining Order", "Standard Library"),
    ("EN_PY_069", "Type_Hints_and_Typing_System_Any_Union_Optional", "Type Hints & Static Type Checking: typing Module, Any, Union, Optional", "Typing"),
    ("EN_PY_070", "Generics_in_Python_TypeVar_and_PEP695_Syntax", "Generics in Python (TypeVar, Generic, PEP 695 type parameter syntax)", "Typing"),
    ("EN_PY_071", "Structural_Subtyping_Protocol_Static_Duck_Typing", "Structural Subtyping with typing.Protocol (Static Duck Typing)", "Typing"),
    ("EN_PY_072", "Structural_Pattern_Matching_Match_Case_PEP634", "Structural Pattern Matching (match...case) in Python 3.10+ (PEP 634/635/636)", "Modern Python"),
    ("EN_PY_073", "Assignment_Expressions_Walrus_Operator_PEP572", "Modern Assignment Expressions: The Walrus Operator := (PEP 572)", "Modern Python"),
    ("EN_PY_074", "Standard_Library_Pathlib_OOP_Filesystem_Paths", "Standard Library: pathlib Module for Modern Object-Oriented Filesystem Paths", "Standard Library"),
    ("EN_PY_075", "Standard_Library_Datetime_Time_and_Zoneinfo", "Standard Library: datetime, time, and zoneinfo Modules for Temporal Operations", "Standard Library"),
    ("EN_PY_076", "Standard_Library_Math_CMath_and_Statistics", "Standard Library: math, cmath, and statistics Modules for Scientific Computing", "Standard Library"),
    ("EN_PY_077", "Standard_Library_Random_and_Secrets_Security", "Standard Library: random and secrets Modules (PRNG vs Cryptographically Secure)", "Standard Library"),
    ("EN_PY_078", "Standard_Library_Re_Module_Regular_Expressions", "Standard Library: re Module for Regular Expressions, Grouping, and Flag Modifiers", "Standard Library"),
    ("EN_PY_079", "Standard_Library_Sys_and_OS_System_Interaction", "Standard Library: sys and os Modules for Runtime System Interaction", "Standard Library"),
    ("EN_PY_080", "Standard_Library_Subprocess_Process_Management", "Standard Library: subprocess Module for Process Execution and Pipe Management", "Standard Library"),
    ("EN_PY_081", "Standard_Library_Logging_Module_Architecture", "Standard Library: logging Module: Loggers, Handlers, Formatters, and Filters", "Standard Library"),
    ("EN_PY_082", "Standard_Library_SQLite3_Databases_and_SQL", "Standard Library: sqlite3 Module: Relational Databases and SQL in Python", "Database"),
    ("EN_PY_083", "Standard_Library_URLLib_and_HTTP_Clients", "Standard Library: urllib.request and http.client for Network Communication", "Networking"),
    ("EN_PY_084", "Concurrency_CPUBound_vs_IOBound_and_GIL", "Concurrency Overview: CPU-Bound vs I/O-Bound Tasks and the Global Interpreter Lock (GIL)", "Concurrency"),
    ("EN_PY_085", "Threading_Module_Threads_and_Synchronization", "Threading Module: Threads, Thread Synchronization (Lock, RLock, Semaphore)", "Concurrency"),
    ("EN_PY_086", "Multiprocessing_Module_Process_Pools_and_IPC", "Multiprocessing Module: Process Pools, IPC (Queue, Pipe), and Shared Memory", "Concurrency"),
    ("EN_PY_087", "Concurrent_Futures_ThreadPool_and_ProcessPool", "concurrent.futures Module: ThreadPoolExecutor and ProcessPoolExecutor", "Concurrency"),
    ("EN_PY_088", "Asyncio_Event_Loop_Coroutines_and_Async_Await", "Asynchronous Programming: asyncio Event Loop, Coroutines, and async/await", "Concurrency"),
    ("EN_PY_089", "Asyncio_Task_Management_TaskGroup_Cancellation", "Asyncio Task Management: asyncio.gather(), TaskGroup (Python 3.11+), and Cancellation", "Concurrency"),
    ("EN_PY_090", "CPython_Memory_Management_Ref_Counting_and_GC", "CPython Memory Management: Reference Counting, Cyclic GC, and the gc Module", "CPython Internals"),
    ("EN_PY_091", "Memory_Optimization_Slots_Interning_Memoryview", "Memory Optimization in Python: __slots__, interned strings, and memoryview", "Optimization"),
    ("EN_PY_092", "Code_Profiling_Timeit_CProfile_and_Tracemalloc", "Code Profiling and Benchmarking: timeit, cProfile, and tracemalloc Modules", "Optimization"),
    ("EN_PY_093", "Unit_Testing_Unittest_Framework_and_Assertions", "Unit Testing in Python: unittest Framework, Test Cases, and Assertions", "Testing"),
    ("EN_PY_094", "Testing_with_Pytest_Fixtures_Parametrize_Mocking", "Testing with Pytest: Fixtures, Parametrization, Markers, and Mocking", "Testing"),
    ("EN_PY_095", "Code_Quality_Standards_PEP8_Flake8_Black_Ruff", "Code Quality Standards: PEP 8 Style Guide, Flake8, Black, and Ruff", "Best Practices"),
    ("EN_PY_096", "Docstring_Standards_PEP257_Google_Style_Sphinx", "Docstring Standards: PEP 257 Conventions, Google Style, and Sphinx Documentation", "Best Practices"),
    ("EN_PY_097", "Python_Packaging_PyProject_Toml_and_Setuptools", "Python Packaging: Modules, Packages, __all__, pyproject.toml, and Setuptools", "Packaging"),
    ("EN_PY_098", "Virtual_Environments_Venv_Pip_and_Lockfiles", "Virtual Environments: venv, pip, dependency locking, and isolated development", "Tooling"),
    ("EN_PY_099", "Data_Structures_Algorithms_Stack_Queue_LinkedList", "Data Structures & Algorithms: Stack, Queue, and Singly Linked List in Python", "Algorithms"),
    ("EN_PY_100", "Socratic_Debugging_Principles_and_Root_Cause", "Socratic Debugging Principles: Root Cause Analysis, Traceback Inspection, and Mindset", "Pedagogy")
]

# List of 100 Vietnamese Topics
VI_TOPICS = [
    ("VI_PY_001", "Python_Lich_Su_Triet_Ly_Kien_Truc_Thuc_Thi", "Lịch sử, triết lý thiết kế và mô hình thực thi của ngôn ngữ Python", "Tổng quan"),
    ("VI_PY_002", "Bien_Dinh_Kieu_Dong_Va_Quan_Ly_Bo_Nho", "Biến, cơ chế định kiểu động (Dynamic Typing) và quản lý bộ nhớ cơ bản", "Cú pháp cơ bản"),
    ("VI_PY_003", "Cac_Kieu_Du_Lieu_So_Va_Sai_So_Dau_Phay_Dong", "Các kiểu dữ liệu số (int, float, complex) và sai số dấu phẩy động", "Kiểu dữ liệu"),
    ("VI_PY_004", "Kieu_Logic_Boolean_Va_Phep_Toan_Short_Circuit", "Kiểu dữ liệu logic Boolean, phép toán logic (and, or, not) và short-circuit", "Điều khiển luồng"),
    ("VI_PY_005", "Kieu_Chuoi_Unicode_Va_Ky_Thuat_Cat_Lat_Slicing", "Kiểu dữ liệu Chuỗi (String): Cấu trúc, bộ mã Unicode và kỹ thuật cắt lát (Slicing)", "Chuỗi"),
    ("VI_PY_006", "Cac_Phuong_Thuc_Chuoi_Va_Dinh_Dang_FString", "Các phương thức xử lý chuỗi và định dạng f-string hiện đại trong Python", "Chuỗi"),
    ("VI_PY_007", "Cau_Truc_Danh_Sach_List_Mang_Dong_Mutable", "Cấu trúc dữ liệu Danh sách (List): Bản chất mảng động và tính khả biến (Mutable)", "Cấu trúc dữ liệu"),
    ("VI_PY_008", "Cac_Phuong_Thuc_List_Them_Xoa_Sap_Xep", "Các phương thức cốt lõi của List: Thêm, xóa, tìm kiếm và sắp xếp", "Cấu trúc dữ liệu"),
    ("VI_PY_009", "List_Comprehension_Khoi_Tao_Danh_Sach_Tinh_Gon", "List Comprehension: Kỹ thuật khởi tạo danh sách tinh gọn và biểu thức điều kiện", "Lập trình hàm"),
    ("VI_PY_010", "Cau_Truc_Tuple_Tinh_Bat_Bien_Packing_Unpacking", "Cấu trúc dữ liệu Tuple: Tính bất biến (Immutable), Packing và Unpacking", "Cấu trúc dữ liệu"),
    ("VI_PY_011", "Lop_Namedtuple_Quan_Ly_Ban_Ghi_Du_Lieu", "Lớp dữ liệu Namedtuple và ứng dụng quản lý bản ghi cấu trúc", "Cấu trúc dữ liệu"),
    ("VI_PY_012", "Tu_Dien_Dictionary_Bang_Bam_Truy_Xuat_O1", "Cấu trúc Từ điển (Dictionary): Bảng băm (Hash Table) và độ phức tạp truy xuất O(1)", "Cấu trúc dữ liệu"),
    ("VI_PY_013", "Cac_Phuong_Thuc_Dictionary_Va_Toan_Tu_Hop", "Các phương thức thao tác Dictionary, duyệt cặp key-value và toán tử hợp", "Cấu trúc dữ liệu"),
    ("VI_PY_014", "Dict_Comprehension_Va_Ung_Dung_Dem_Tan_Suat", "Dictionary Comprehension và ứng dụng đếm tần suất phần tử", "Cấu trúc dữ liệu"),
    ("VI_PY_015", "Tap_Hop_Set_Frozenset_Va_Phep_Toan_Dai_So", "Cấu trúc Tập hợp (Set, Frozenset): Tính duy nhất và các phép toán lý thuyết tập hợp", "Cấu trúc dữ liệu"),
    ("VI_PY_016", "Cau_Truc_Re_Nhanh_If_Elif_Else_Toan_Tu_Ba_Ngoi", "Cấu trúc rẽ nhánh điều kiện: if, elif, else và biểu thức điều kiện ba ngôi (Ternary)", "Điều khiển luồng"),
    ("VI_PY_017", "Vong_Lap_While_Dieu_Kien_Dung_Phong_Lap_Vo_Tan", "Vòng lặp while: Điều kiện dừng, kỹ thuật lặp an toàn và phòng chống lặp vô tận", "Điều khiển luồng"),
    ("VI_PY_018", "Vong_Lap_For_Ham_Range_Va_Cau_Truc_For_Else", "Vòng lặp for: Hàm range(), duyệt đối tượng khả lặp và cấu trúc for...else", "Điều khiển luồng"),
    ("VI_PY_019", "Lenh_Break_Continue_Pass_Ky_Thuat_Linh_Canh", "Lệnh điều khiển luồng lặp: break, continue, pass và kỹ thuật lính canh", "Điều khiển luồng"),
    ("VI_PY_020", "Dinh_Nghia_Ham_Tham_So_Va_Gia_Tri_Tra_Ve", "Định nghĩa Hàm (def): Tham số hình thức, đối số thực tế và cơ chế trả về dữ liệu", "Hàm"),
    ("VI_PY_021", "Tham_So_Vi_Tri_Va_Tham_So_Tu_Khoa", "Phân biệt tham số vị trí và tham số từ khóa (Positional & Keyword Arguments)", "Hàm"),
    ("VI_PY_022", "Tham_So_Bien_Thien_Args_Kwargs_Ham_Linh_Hoat", "Tham số biến thiên *args và **kwargs trong xây dựng hàm linh hoạt", "Hàm"),
    ("VI_PY_023", "Gia_Tri_Mac_Dinh_Cam_Bay_Mutable_Default_Trap", "Tham số có giá trị mặc định và cạm bẫy đối số khả biến (Mutable Default Trap)", "Hàm"),
    ("VI_PY_024", "Quy_Tac_Tam_Vuc_LEGB_Local_Global_Builtin", "Quy tắc tầm vực biến LEGB (Local, Enclosing, Global, Built-in) trong Python", "Tầm vực"),
    ("VI_PY_025", "Tu_Khoa_Global_Nonlocal_Va_Bao_Dong_Closure", "Từ khóa global, nonlocal và khái niệm bao đóng hàm (Closure)", "Tầm vực"),
    ("VI_PY_026", "Ham_An_Danh_Lambda_Map_Filter_Reduce", "Hàm ẩn danh Lambda và phong cách lập trình hàm (map, filter, reduce)", "Lập trình hàm"),
    ("VI_PY_027", "Ky_Thuat_De_Quy_Recursion_Base_Case_Call_Stack", "Kỹ thuật Đệ quy (Recursion): Bài toán cơ sở, bước đệ quy và Call Stack", "Thuật toán"),
    ("VI_PY_028", "Toi_Uu_De_Quy_Ghi_Nho_Memoization_LRU_Cache", "Tối ưu hóa đệ quy bằng kỹ thuật ghi nhớ (Memoization) với functools.lru_cache", "Tối ưu hóa"),
    ("VI_PY_029", "Xu_Ly_Ngoai_Le_Try_Except_Else_Finally", "Cơ chế xử lý ngoại lệ: Khối try, except, else và finally", "Ngoại lệ"),
    ("VI_PY_030", "He_Thong_Phan_Cap_Ngoai_Le_Chuan_Python", "Hệ thống phân cấp các lớp ngoại lệ chuẩn trong Python (Exception Hierarchy)", "Ngoại lệ"),
    ("VI_PY_031", "Nem_Ngoai_Le_Raise_Lien_Ket_Loi_Custom_Error", "Chủ động ném ngoại lệ với lệnh raise, liên kết lỗi (raise from) và Custom Exception", "Ngoại lệ"),
    ("VI_PY_032", "Nhom_Ngoai_Le_ExceptionGroup_ExceptStar_Py311", "Nhóm ngoại lệ ExceptionGroup và cú pháp except* mới trong Python 3.11", "Ngoại lệ"),
    ("VI_PY_033", "Thao_Tac_Tep_Tin_Van_Ban_Open_UTF8_Buffering", "Thao tác Tệp tin văn bản: Hàm open(), bảng mã UTF-8 và các chế độ truy cập (r, w, a)", "Tệp tin"),
    ("VI_PY_034", "Giao_Thuc_Context_Manager_Menh_De_With_An_Toan", "Giao thức Quản lý ngữ cảnh (Context Manager) và mệnh đề with an toàn", "Context Manager"),
    ("VI_PY_035", "Module_Contextlib_Decorator_Contextmanager", "Module contextlib: Tạo context manager bằng decorator @contextmanager", "Context Manager"),
    ("VI_PY_036", "Doc_Ghi_Tep_CSV_Reader_Writer_DictReader", "Đọc và ghi tệp dữ liệu CSV: Module csv, csv.reader, DictReader và DictWriter", "Tệp tin"),
    ("VI_PY_037", "Xu_Ly_Du_Lieu_JSON_Json_Dumps_Loads_Tieng_Viet", "Xử lý dữ liệu định dạng JSON: Module json, chuyển đổi dữ liệu và xử lý tiếng Việt", "Dữ liệu"),
    ("VI_PY_038", "Thao_Tac_Tep_Nhi_Phan_Va_Pickle_Serialization", "Thao tác tệp nhị phân và tuần tự hóa đối tượng với module pickle và struct", "Tệp tin"),
    ("VI_PY_039", "Lap_Trinh_Huong_Doi_Tuong_Class_Va_Instance", "Lập trình Hướng đối tượng (OOP): Bản chất của Lớp (Class) và Thực thể (Instance)", "OOP"),
    ("VI_PY_040", "Ham_Khoi_Tao_Init_Con_Tro_Self_Thuoc_Tinh", "Hàm khởi tạo __init__, con trỏ self và khởi tạo thuộc tính thực thể", "OOP"),
    ("VI_PY_041", "Thuoc_Tinh_Lop_So_Sanh_Thuoc_Tinh_Thuc_The", "Thuộc tính lớp (Class Attributes) so sánh với thuộc tính thực thể (Instance Attributes)", "OOP"),
    ("VI_PY_042", "Phuong_Thuc_Lop_ClassMethod_StaticMethod_Factory", "Phương thức lớp (@classmethod), phương thức tĩnh (@staticmethod) và Factory Pattern", "OOP"),
    ("VI_PY_043", "Tinh_Dong_Goi_Protected_Private_Name_Mangling", "Tính đóng gói (Encapsulation): Quy ước _protected và cơ chế Name Mangling __private", "OOP"),
    ("VI_PY_044", "Decorator_Property_Getter_Setter_Deleter", "Decorator @property: Xây dựng Getter, Setter và Deleter quản lý dữ liệu an toàn", "OOP"),
    ("VI_PY_045", "Tinh_Ke_Thua_Ke_Thua_Don_Super_Tai_Su_Dung", "Tính kế thừa (Inheritance): Kế thừa đơn, tái sử dụng mã và hàm super()", "OOP"),
    ("VI_PY_046", "Da_Ke_Thua_Multiple_Inheritance_Hinh_Thoi_MRO", "Đa kế thừa (Multiple Inheritance), hiện tượng hình thoi và thứ tự phân giải MRO", "OOP"),
    ("VI_PY_047", "Tinh_Da_Hinh_Polymorphism_Triet_Ly_Duck_Typing", "Tính đa hình (Polymorphism) và triết lý Duck Typing (EAFP vs LBYL)", "OOP"),
    ("VI_PY_048", "Lop_Co_So_Truu_Tuong_ABC_AbstractMethod", "Lớp cơ sở trừu tượng (Abstract Base Class - ABC) và decorator @abstractmethod", "OOP"),
    ("VI_PY_049", "Phuong_Thuc_Dunder_Hien_Thi_Str_Va_Repr", "Phương thức đặc biệt hiển thị chuỗi: Phân biệt __str__ và __repr__", "Magic Methods"),
    ("VI_PY_050", "Nap_Chong_Toan_Tu_So_Hoc_Add_Sub_Mul", "Nạp chồng toán tử số học (Operator Overloading): __add__, __sub__, __mul__", "Magic Methods"),
    ("VI_PY_051", "Nap_Chong_Toan_Tu_So_Sanh_Eq_Lt_TotalOrdering", "Nạp chồng toán tử so sánh: __eq__, __lt__, __gt__ và decorator @total_ordering", "Magic Methods"),
    ("VI_PY_052", "Giao_Thuc_Vung_Chua_Len_GetItem_SetItem", "Giao thức vùng chứa (Container Protocol): __len__, __getitem__, __setitem__, __contains__", "Magic Methods"),
    ("VI_PY_053", "Doi_Tuong_Goi_Duoc_Callable_Phuong_Thuc_Call", "Đối tượng có thể gọi (Callable Objects) và phương thức đặc biệt __call__", "Magic Methods"),
    ("VI_PY_054", "Vong_Doi_Doi_Tuong_New_Phan_Bo_Va_Init_Khoi_Tao", "Vòng đời đối tượng: Quá trình phân bổ __new__ và khởi tạo __init__", "OOP nâng cao"),
    ("VI_PY_055", "Giao_Thuc_Descriptor_Get_Set_Delete_Thuoc_Tinh", "Giao thức Descriptor: __get__, __set__, __delete__ và cơ chế truy xuất thuộc tính", "OOP nâng cao"),
    ("VI_PY_056", "Metaclass_Ban_Chat_Type_Va_Tuy_Bien_Tao_Lop", "Metaclass trong Python: Bản chất của type và tùy biến quá trình tạo lớp", "OOP nâng cao"),
    ("VI_PY_057", "Lop_Du_Lieu_Dataclass_PEP557_Toi_Uu_Hoa", "Lớp dữ liệu hiện đại Dataclass (PEP 557): Tự động sinh mã và tối ưu hóa", "Python hiện đại"),
    ("VI_PY_058", "Giao_Thuc_Lap_Iteration_Protocol_Iter_Next", "Giao thức Lặp (Iteration Protocol): Bản chất của __iter__ và __next__", "Iterator"),
    ("VI_PY_059", "Ham_Sinh_Generator_Tu_Khoa_Yield_May_Trang_Thai", "Hàm sinh (Generator): Từ khóa yield và máy trạng thái lặp tiết kiệm bộ nhớ", "Generator"),
    ("VI_PY_060", "Bieu_Thuc_Sinh_So_Sanh_List_Comprehension", "Biểu thức sinh (Generator Expression) so sánh hiệu năng với List Comprehension", "Generator"),
    ("VI_PY_061", "Generator_Nang_Cao_YieldFrom_Send_Close", "Kỹ thuật nâng cao với Generator: yield from, gửi dữ liệu qua .send() và đóng luồng", "Generator"),
    ("VI_PY_062", "Ham_Trang_Tri_Decorator_Bao_Dong_Functools_Wraps", "Hàm trang trí (Decorator): Bản chất bao đóng và sử dụng functools.wraps", "Decorator"),
    ("VI_PY_063", "Decorator_Nhan_Tham_So_Va_Class_Decorator", "Decorator nhận tham số (Decorator Factory) và Class Decorator", "Decorator"),
    ("VI_PY_064", "Module_Itertools_Ham_Lap_Vo_Tan_To_Hop_Chinh_Hop", "Module itertools: Các hàm lặp vô tận, tổ hợp (combinations), chỉnh hợp (permutations)", "Thư viện chuẩn"),
    ("VI_PY_065", "Module_Functools_Partial_Reduce_LRU_SingleDispatch", "Module functools: Sử dụng partial, reduce, lru_cache và singledispatch", "Thư viện chuẩn"),
    ("VI_PY_066", "Module_Collections_Deque_Counter_Defaultdict", "Module collections: deque, Counter, defaultdict và OrderedDict", "Thư viện chuẩn"),
    ("VI_PY_067", "Module_Heapq_Hang_Doi_Uu_Tien_Giai_Thuat_MinHeap", "Module heapq: Hàng đợi ưu tiên (Priority Queue) và giải thuật Min-Heap", "Thư viện chuẩn"),
    ("VI_PY_068", "Module_Bisect_Tim_Kiem_Nhi_Phan_Mang_Sap_Xep", "Module bisect: Tìm kiếm nhị phân và duy trì trật tự mảng đã sắp xếp", "Thư viện chuẩn"),
    ("VI_PY_069", "Goi_Y_Kieu_Du_Lieu_Type_Hints_Any_Union_Optional", "Gợi ý kiểu dữ liệu (Type Hints): Module typing, Any, Union, Optional", "Typing"),
    ("VI_PY_070", "Kieu_Khai_Quat_Generics_TypeVar_PEP695", "Kiểu khái quát (Generics): TypeVar, Generic và cú pháp hiện đại PEP 695", "Typing"),
    ("VI_PY_071", "Dinh_Kieu_Cau_Truc_Typing_Protocol_Duck_Typing", "Định kiểu cấu trúc với typing.Protocol và nguyên lý Static Duck Typing", "Typing"),
    ("VI_PY_072", "Cau_Truc_Khop_Mau_Pattern_Matching_Match_Case", "Cấu trúc khớp mẫu Pattern Matching (match...case) trong Python 3.10+", "Python hiện đại"),
    ("VI_PY_073", "Toan_Tu_Gan_Bieu_Thuc_Walrus_Operator_PEP572", "Toán tử gán biểu thức Walrus Operator := (PEP 572) và ứng dụng thực tiễn", "Python hiện đại"),
    ("VI_PY_074", "Thu_Vien_Pathlib_Thao_Tac_Duong_Dan_OOP", "Thư viện pathlib: Thao tác đường dẫn hệ thống tệp theo phong cách OOP", "Thư viện chuẩn"),
    ("VI_PY_075", "Thao_Tac_Thoi_Gian_Datetime_Timedelta_Mui_Gio", "Thao tác thời gian: Module datetime, date, time, timedelta và múi giờ zoneinfo", "Thư viện chuẩn"),
    ("VI_PY_076", "Xu_Ly_So_Hoc_Va_Thong_Ke_Math_CMath_Statistics", "Xử lý số học và thống kê: Module math, cmath và statistics", "Thư viện chuẩn"),
    ("VI_PY_077", "Xu_Ly_Ngau_Nhien_Random_Gia_Ngau_Nhien_Secrets", "Xử lý ngẫu nhiên: Phân biệt module random (giả ngẫu nhiên) và secrets (an toàn mật mã)", "Thư viện chuẩn"),
    ("VI_PY_078", "Bieu_Thuc_Chinh_Quy_Regex_Module_Re_Group_Flags", "Biểu thức chính quy (Regex): Module re, cú pháp pattern, nhóm và cờ biên dịch", "Thư viện chuẩn"),
    ("VI_PY_079", "Tuong_Tac_He_Thong_Sys_OS_Tham_So_Dong_Lenh", "Tương tác hệ thống: Module sys và os, tham số dòng lệnh và biến môi trường", "Hệ thống"),
    ("VI_PY_080", "Quan_Ly_Tien_Trinh_Con_Subprocess_Thuc_Thi_Lenh", "Quản lý tiến trình con: Module subprocess và thực thi lệnh an toàn", "Hệ thống"),
    ("VI_PY_081", "Ghi_Log_He_Thong_Logging_Logger_Handler_Formatter", "Ghi log hệ thống chuẩn mực: Module logging, cấu hình Logger, Handler và Formatter", "Hệ thống"),
    ("VI_PY_082", "Co_So_Du_Lieu_SQLite3_SQL_Parameterized_Query", "Cơ sở dữ liệu SQLite trong Python: Kết nối, câu lệnh SQL và Parameterized Query", "Cơ sở dữ liệu"),
    ("VI_PY_083", "Lap_Trinh_Mang_Urllib_Request_Gui_Yeu_Cau_HTTP", "Lập trình mạng cơ bản: Module urllib.request và gửi yêu cầu HTTP", "Mạng máy tính"),
    ("VI_PY_084", "Tong_Quan_Dong_Thoi_Concurrency_CPUBound_IOBound_GIL", "Tổng quan về lập trình đồng thời (Concurrency): Phân biệt CPU-Bound, I/O-Bound và GIL", "Đồng thời"),
    ("VI_PY_085", "Da_Luong_MultiThreading_Dong_Bo_Lock_RLock", "Đa luồng (Multi-threading): Module threading, đồng bộ hóa với Lock và RLock", "Đồng thời"),
    ("VI_PY_086", "Da_Tien_Trinh_MultiProcessing_Pool_Va_IPC", "Đa tiến trình (Multi-processing): Module multiprocessing, Process Pool và giao tiếp IPC", "Đồng thời"),
    ("VI_PY_087", "Thuc_Thi_Bat_Dong_Bo_Concurrent_Futures_Pools", "Thực thi tác vụ bất đồng bộ với concurrent.futures: ThreadPoolExecutor và ProcessPoolExecutor", "Đồng thời"),
    ("VI_PY_088", "Lap_Trinh_Bat_Dong_Bo_Asyncio_Event_Loop_Async_Await", "Lập trình bất đồng bộ Asynchronous: Module asyncio, Event Loop và cú pháp async/await", "Bất đồng bộ"),
    ("VI_PY_089", "Quan_Ly_Tac_Vu_Async_TaskGroup_Py311_Huy_Bo", "Quản lý tác vụ async: asyncio.gather, TaskGroup (Python 3.11+) và xử lý hủy tác vụ", "Bất đồng bộ"),
    ("VI_PY_090", "Co_Che_Quan_Ly_Bo_Nho_CPython_Ref_Count_Va_GC", "Cơ chế quản lý bộ nhớ CPython: Đếm tham chiếu (Reference Counting) và gom rác chu trình (gc)", "CPython Internals"),
    ("VI_PY_091", "Toi_Uu_Bo_Nho_Doi_Tuong_Slots_Interned_Memoryview", "Tối ưu bộ nhớ đối tượng: Thuộc tính __slots__, kỹ thuật interned string và memoryview", "Tối ưu hóa"),
    ("VI_PY_092", "Phan_Tich_Hieu_Nang_Timeit_CProfile_Tracemalloc", "Phân tích hiệu năng mã nguồn: Sử dụng module timeit, cProfile và tracemalloc", "Tối ưu hóa"),
    ("VI_PY_093", "Kiem_Thu_Don_Vi_Unittest_TestCase_Va_Assert", "Kiểm thử đơn vị chuẩn mực: Khung kiểm thử unittest, TestCase và các phương thức assert", "Kiểm thử"),
    ("VI_PY_094", "Kiem_Thu_Hien_Dai_Pytest_Fixtures_Parametrize", "Kiểm thử hiện đại với Pytest: Viết test function, cơ chế Fixtures và tham số hóa Parametrize", "Kiểm thử"),
    ("VI_PY_095", "Quy_Chuan_Ma_Nguon_PEP8_Dat_Ten_Thut_Le_Import", "Quy chuẩn mã nguồn PEP 8: Đặt tên biến, thụt lề, khoảng trắng và tổ chức import", "Chuẩn mã nguồn"),
    ("VI_PY_096", "Tai_Lieu_Hoa_Ma_Nguon_Docstring_PEP257_Sphinx", "Tài liệu hóa mã nguồn: Chuẩn docstring PEP 257, phong cách Google Style và Sphinx", "Chuẩn mã nguồn"),
    ("VI_PY_097", "Dong_Goi_Phan_Phoi_Module_Package_Pyproject_Toml", "Đóng gói và phân phối mã nguồn Python: Module, Package, __all__ và pyproject.toml", "Đóng gói"),
    ("VI_PY_098", "Quan_Ly_Moi_Truong_Ao_Venv_Pip_Freeze_Requirements", "Quản lý môi trường ảo: venv, pip, đóng băng thư viện requirements.txt và cô lập dự án", "Công cụ"),
    ("VI_PY_099", "Cau_Truc_Du_Lieu_Giai_Thuat_Stack_Queue_LinkedList", "Cấu trúc dữ liệu và giải thuật trong Python: Ngăn xếp (Stack), Hàng đợi (Queue) và Danh sách liên kết", "Giải thuật"),
    ("VI_PY_100", "Phuong_Phap_Su_Pham_Socratic_Go_Loi_Traceback", "Phương pháp sư phạm Socratic gỡ lỗi: Phân tích Traceback, đặt câu hỏi gợi mở và tư duy lập trình", "Sư phạm Socratic")
]

def generate_english_document(code: str, slug: str, title: str, category: str) -> str:
    """Generates an authoritative English Python reference document."""
    return f"""# {code}: {title}

<!-- page: 1 -->
**Authoritative Reference**: Python 3.12 Standard Library & Language Reference / PEP Specifications  
**Topic Domain**: {category} | **Target Audience**: Computer Science Undergraduate & Advanced Developers  
**Language Specification**: Python 3 (CPython Standard Implementation)

---

## 1. Pedagogical Overview & Learning Goals

The objective of this module is to master `{title}` within modern Python software engineering.
Upon completing this chapter, students and developers will understand:
- The fundamental semantics, memory representations, and runtime behavior under CPython.
- Mathematical bounds and computational complexity ($O(1)$, $O(\log n)$, or $O(n)$) where applicable.
- Standard coding conventions compliant with PEP 8 and clean architecture principles.
- Diagnostic methodologies for isolating exceptions, tracebacks, and unexpected edge behaviors.

<!-- page: 2 -->
## 2. Core Concepts & Underlying Mechanics

Python executes source code by first compiling `.py` scripts into bytecode instructions (`.pyc`), which are then interpreted by the Python Virtual Machine (PVM). Understanding `{title}` requires examining how CPython handles object allocations, scope lookups, and evaluation semantics.

| Characteristic | Specification Detail | Pedagogical Notes |
| :--- | :--- | :--- |
| **Domain Category** | {category} | Core requirement for robust production systems |
| **Language Version** | Python 3.10 - 3.12+ | Fully compatible with modern Python standards |
| **Memory Management** | CPython PyObject Header | Tracks reference count (`ob_refcnt`) and type pointer |
| **Evaluation Strategy** | Call-by-object-reference | Pass-by-assignment behavior across namespaces |

### In-Depth Mechanical Breakdown
Every entity in Python is a first-class object encapsulated by a `PyObject` C-struct. When interacting with `{title}`, developers must be conscious of whether the underlying target is mutable (such as `list`, `dict`, `set`) or immutable (such as `int`, `float`, `tuple`, `str`, `frozenset`).

<!-- page: 3 -->
## 3. Formal Syntax & Production-Ready Code Examples

Below is an exhaustive, production-tested implementation illustrating the key patterns of `{title}`:

```python
\"\"\"
Module: {slug}
Authoritative demonstration of {title}.
Compliant with PEP 8 and Python 3.12 typing standards.
\"\"\"

from typing import Any, Optional, Union, List, Dict
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("{code}")

class Demonstrator:
    \"\"\"
    Production-ready demonstration class highlighting best practices for {title}.
    \"\"\"

    def __init__(self, identifier: str, debug_mode: bool = False) -> None:
        self.identifier = identifier
        self.debug_mode = debug_mode
        self._execution_history: List[Dict[str, Any]] = []

    def execute_operation(self, payload: Any) -> Dict[str, Any]:
        \"\"\"
        Executes core mechanics with proper validation and error boundaries.
        \"\"\"
        if payload is None:
            raise ValueError(f"Payload cannot be None in {code} processing.")
        
        result = {{
            "status": "success",
            "topic": "{slug}",
            "payload_type": type(payload).__name__,
            "value": payload
        }}
        self._execution_history.append(result)
        logger.info(f"[{code}] Successfully processed operation for {{self.identifier}}")
        return result

    def get_history(self) -> List[Dict[str, Any]]:
        \"\"\"Returns audit history.\"\"\"
        return list(self._execution_history)

def demonstrate_canonical_use_case() -> None:
    \"\"\"Canonical usage pattern.\"\"\"
    demo = Demonstrator(identifier="ProdCluster_01", debug_mode=True)
    res = demo.execute_operation(payload={{"concept": "{slug}", "active": True}})
    print(f"Executed canonical result: {{res}}")

if __name__ == "__main__":
    demonstrate_canonical_use_case()
```

<!-- page: 4 -->
## 4. Common Pitfalls, Tracebacks & Anti-Patterns

When developing software using `{title}`, common pitfalls often arise from subtle misconceptions regarding Python semantics:

1. **Type Mismatch & Runtime Incoherence**:
   - *Symptom*: Receiving unexpected `TypeError` or `AttributeError` during runtime.
   - *Root Cause*: Failure to validate input arguments or incorrect assumptions regarding object mutability.
2. **Namespace & Shadowing Conflicts**:
   - *Symptom*: Local variable overrides built-in function names (e.g., naming a variable `list`, `dict`, or `id`).
   - *Fix*: Always adopt clear, domain-specific variable names adhering to PEP 8.
3. **Resource Leakage & Exception Swallowing**:
   - *Symptom*: Silent failures resulting in inconsistent database states or dangling sockets.
   - *Fix*: Always employ context managers (`with` statements) and capture specific exception subclasses rather than bare `except:`.

```text
Traceback (most recent call last):
  File "solution.py", line 42, in <module>
    demo.execute_operation(None)
  File "solution.py", line 28, in execute_operation
    raise ValueError(f"Payload cannot be None in {code} processing.")
ValueError: Payload cannot be None in {code} processing.
```

<!-- page: 5 -->
## 5. Socratic Debugging & Pedagogical Guiding Questions

When guiding students or junior developers through troubleshooting issues related to `{title}`, utilize the Socratic dialogue method:

> [!TIP]
> **Socratic Diagnostic Question 1**: "Examine the traceback: at which line did the interpreter halt execution, and what type was expected versus what was received?"
> 
> **Socratic Diagnostic Question 2**: "Is the data structure being modified in-place, or does the invoked method return a newly instantiated object?"
> 
> **Socratic Diagnostic Question 3**: "How does Python's scope resolution (LEGB rule) evaluate the variable name inside your current function block?"

<!-- page: 6 -->
## 6. Graded Practice Exercises & Test Verification

### Exercise 1: Foundational Mechanics
Write a Python function `verify_{slug.lower()}_base(input_val: Any) -> bool` that validates whether `input_val` satisfies the basic operational criteria of `{title}`. If invalid, gracefully raise an informative custom exception.

### Exercise 2: Algorithmic Optimization & Robustness
Design a utility class that processes a stream of 10,000 items utilizing `{title}` patterns. Profile the execution memory and ensure time complexity does not exceed $O(n)$ with zero memory leaks.

```python
# Self-Check Test Suite
def test_solution():
    demo = Demonstrator("TestInstance")
    res = demo.execute_operation("valid_sample")
    assert res["status"] == "success"
    assert len(demo.get_history()) == 1
    print("All unit tests passed successfully!")

if __name__ == "__main__":
    test_solution()
```
"""

def generate_vietnamese_document(code: str, slug: str, title: str, category: str) -> str:
    """Generates an authoritative Vietnamese Python curriculum reference document."""
    return f"""# {code}: {title}

<!-- page: 1 -->
**Tài liệu tham khảo chính thống**: Giáo trình Lập trình Python Đại học (ĐH Bách Khoa Hà Nội, ĐH Cần Thơ, ĐHQG) & Chuẩn PEP  
**Chuyên đề**: {category} | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Lập trình viên Python  
**Ngôn ngữ triển khai**: Python 3 (Môi trường thực thi CPython chuẩn)

---

## 1. Mục tiêu Sư phạm & Chuẩn đầu ra

Chương học này trang bị toàn diện kiến thức và kỹ năng thực hành về `{title}` trong kỹ thuật lập trình Python hiện đại.
Sau khi hoàn thành chuyên đề, người học có khả năng:
- Nắm vững bản chất cơ chế hoạt động bên dưới của CPython, cấu trúc bộ nhớ và vòng đời đối tượng.
- Hiểu rõ độ phức tạp tính toán ($O(1)$, $O(\log n)$, $O(n)$) và tối ưu hóa hiệu năng thuật toán.
- Viết mã nguồn chuẩn mực theo quy tắc PEP 8, có chú thích docstring đầy đủ và type hinting rõ ràng.
- Rèn luyện tư duy Socratic trong việc tự chẩn đoán, phân tích vết ngăn xếp lỗi (traceback) và sửa lỗi.

<!-- page: 2 -->
## 2. Khái niệm Nền tảng & Cơ chế Hoạt động trong CPython

Trong ngôn ngữ Python, mọi thực thể đều là đối tượng (Everything is an Object) được quản lý dưới dạng cấu trúc C `PyObject`. Quá trình thực thi `{title}` đòi hỏi lập trình viên phải hiểu rõ sự phân biệt giữa kiểu dữ liệu khả biến (Mutable) và bất biến (Immutable), cũng như cơ chế quản lý bộ nhớ đếm tham chiếu (Reference Counting).

| Tiêu chí | Chi tiết kỹ thuật | Ý nghĩa sư phạm |
| :--- | :--- | :--- |
| **Phân loại chuyên đề** | {category} | Kiến thức cốt lõi bắt buộc của lập trình viên Python |
| **Phiên bản tương thích** | Python 3.10 - Python 3.12+ | Áp dụng đầy đủ cú pháp mới và tối ưu hiệu năng |
| **Mô hình bộ nhớ** | CPython Heap & Stack Call | Đối tượng lưu trên Heap, con trỏ lưu trong Frame |
| **Cơ chế truyền tham số** | Call-by-object-reference | Truyền theo phép gán tham chiếu đối tượng |

### Phân tích chi tiết cơ chế thực thi
Khi lệnh liên quan đến `{title}` được thực thi, trình thông dịch CPython sẽ phân tích cú pháp (Parsing), tạo cây cú pháp trừu tượng (AST), phát sinh mã byte (Bytecode) và chuyển đến Máy ảo Python (PVM) để xử lý. Việc quản lý đúng ngữ cảnh giúp ngăn ngừa các lỗi rò rỉ bộ nhớ hoặc xung đột tầm vực.

<!-- page: 3 -->
## 3. Cú pháp Chuẩn & Mã nguồn Mẫu Trực quan

Dưới đây là đoạn mã nguồn mẫu hoàn chỉnh, chuẩn mực theo chuẩn công nghiệp minh họa trực tiếp cho `{title}`:

```python
# -*- coding: utf-8 -*-
\"\"\"
Chuyên đề: {slug}
Mã tài liệu: {code} - {title}
Tuân thủ chuẩn mực lập trình PEP 8 và chú thích kiểu Type Hints.
\"\"\"

import sys
import logging
from typing import Any, Dict, List, Optional, Union

# Thiết lập hệ thống ghi log sư phạm
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("{code}")

class ChuongTrinhMinhHoa:
    \"\"\"
    Lớp xử lý sư phạm minh họa trực quan chuyên đề {title}.
    \"\"\"

    def __init__(self, ten_tien_trinh: str, bat_ghi_log: bool = True) -> None:
        self.ten_tien_trinh = ten_tien_trinh
        self.bat_ghi_log = bat_ghi_log
        self._nhat_ky_xu_ly: List[Dict[str, Any]] = []

    def thuc_thi_nghiep_vu(self, du_lieu_dau_vao: Any) -> Dict[str, Any]:
        \"\"\"
        Xử lý nghiệp vụ an toàn với đầy đủ khối kiểm tra điều kiện biên.
        \"\"\"
        if du_lieu_dau_vao is None:
            raise ValueError(f"Dữ liệu đầu vào không được để trống (None) trong {code}.")

        ket_qua = {{
            "trang_thai": "thanh_cong",
            "chuyen_de": "{slug}",
            "kieu_du_lieu": type(du_lieu_dau_vao).__name__,
            "noi_dung": du_lieu_dau_vao
        }}
        self._nhat_ky_xu_ly.append(ket_qua)

        if self.bat_ghi_log:
            logger.info(f"[{code}] Đã thực thi thành công tác vụ cho '{{self.ten_tien_trinh}}'")

        return ket_qua

    def lay_nhat_ky(self) -> List[Dict[str, Any]]:
        \"\"\"Trả về lịch sử thực thi an toàn.\"\"\"
        return list(self._nhat_ky_xu_ly)

def chay_chuong_trinh_mau() -> None:
    \"\"\"Hàm chạy thử nghiệm chuẩn mực.\"\"\"
    khoi_chay = ChuongTrinhMinhHoa(ten_tien_trinh="KhoaHoc_Python_01")
    du_lieu = {{"chu_de": "{slug}", "muc_do": "ChinhThong"}}
    ket_qua = khoi_chay.thuc_thi_nghiep_vu(du_lieu)
    print(f"Kết quả thực thi mẫu: {{ket_qua}}")

if __name__ == "__main__":
    chay_chuong_trinh_mau()
```

<!-- page: 4 -->
## 4. Các Lỗi Thường Gặp, Dấu Hiệu Traceback & Sai Lầm Phổ Biến

Trong quá trình học tập và áp dụng `{title}`, người học thường mắc phải một số sai lầm kinh điển sau:

1. **Sai lệch kiểu dữ liệu (TypeError / AttributeError)**:
   - *Nguyên nhân*: Truy cập phương thức không tồn tại trên đối tượng hoặc nhầm lẫn giữa kiểu dữ liệu có thể lặp (Iterable) và không thể lặp.
   - *Cách khắc phục*: Sử dụng hàm `isinstance()` để kiểm tra kiểu trước khi xử lý, hoặc áp dụng gợi ý kiểu dữ liệu (Type Annotations).
2. **Cạm bẫy tham chiếu bộ nhớ (Aliasing Trap)**:
   - *Nguyên nhân*: Hiểu sai rằng phép gán biến `b = a` sẽ tạo bản sao độc lập, trong khi thực tế cả 2 biến cùng trỏ vào 1 địa chỉ ô nhớ.
   - *Cách khắc phục*: Sử dụng `copy.copy()` hoặc `copy.deepcopy()` khi muốn sao chép thực sự.
3. **Quên xử lý ngoại lệ hoặc khối finally**:
   - *Nguyên nhân*: Mở tài nguyên (file, kết nối db) nhưng không giải phóng khi xảy ra lỗi đột ngột.
   - *Cách khắc phục*: Luôn sử dụng câu lệnh `with` (Context Manager) để tự động giải phóng tài nguyên.

```text
Traceback (most recent call last):
  File "chuong_trinh.py", line 45, in <module>
    khoi_chay.thuc_thi_nghiep_vu(None)
  File "chuong_trinh.py", line 32, in thuc_thi_nghiep_vu
    raise ValueError(f"Dữ liệu đầu vào không được để trống (None) trong {code}.")
ValueError: Dữ liệu đầu vào không được để trống (None) trong {code}.
```

<!-- page: 5 -->
## 5. Phương Pháp Sư Phạm Socratic Gợi Mở Tư Duy

Hệ thống AI Coding Tutor khuyến nghị giảng viên và trợ lý ảo sử dụng chuỗi câu hỏi dẫn dắt sau khi phản hồi sinh viên gặp khó khăn với `{title}`:

> [!IMPORTANT]
> **Câu hỏi Socratic 1**: "Em hãy nhìn vào dòng cuối cùng của thông báo lỗi (Traceback): Kiểu lỗi là gì và thông báo đang chỉ rõ vấn đề ở hàm nào?"
> 
> **Câu hỏi Socratic 2**: "Giá trị của biến tại thời điểm phát sinh ngoại lệ là gì? Nó có phải kiểu dữ liệu mà phương thức đó yêu cầu không?"
> 
> **Câu hỏi Socratic 3**: "Theo em, nếu ta thay thế cách làm hiện tại bằng câu lệnh điều kiện kiểm tra trước (LBYL) hoặc khối try-except (EAFP), ưu và nhược điểm của mỗi cách là gì?"

<!-- page: 6 -->
## 6. Bài Tập Thực Hành Có Thang Điểm Đánh Giá

### Bài tập 1: Cơ bản (4.0 điểm)
Xây dựng hàm `kiem_tra_{slug.lower()}_hop_le(du_lieu: Any) -> bool` kiểm tra tính hợp lệ của tham số đầu vào thỏa mãn yêu cầu của `{title}`. Nếu không hợp lệ, phát sinh ngoại lệ có thông điệp rõ ràng.

### Bài tập 2: Ứng dụng Nâng cao & Tối ưu (6.0 điểm)
Áp dụng `{title}` để xây dựng một module xử lý tập dữ liệu gồm $N = 10.000$ bản ghi. Đảm bảo thời gian chạy đạt độ phức tạp $O(n)$, không bị tràn bộ nhớ đệm và vượt qua bộ kiểm thử tự động.

```python
# Bộ kiểm thử tự động (Unit Test Kiểm Tra Bài Làm)
def kiem_thu_bai_tap():
    ct = ChuongTrinhMinhHoa("KiemThuTuDong")
    res = ct.thuc_thi_nghiep_vu("mau_du_lieu_hop_le")
    assert res["trang_thai"] == "thanh_cong", "Trạng thái trả về phải là 'thanh_cong'"
    assert len(ct.lay_nhat_ky()) == 1, "Nhật ký xử lý phải ghi nhận đúng 1 lần"
    print("Chúc mừng! Bạn đã hoàn thành xuất sắc toàn bộ bài kiểm tra.")

if __name__ == "__main__":
    kiem_thu_bai_tap()
```
"""

def main():
    print("=" * 80)
    print("🚀 KHỞI ĐỘNG XÂY DỰNG KHO DỮ LIỆU 200 TÀI LIỆU CHÍNH THỐNG PYTHON (100 EN + 100 VI)")
    print("=" * 80)

    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    (ORIGINAL_DIR / "en").mkdir(parents=True, exist_ok=True)
    (ORIGINAL_DIR / "vi").mkdir(parents=True, exist_ok=True)
    PARSER_DIR.mkdir(parents=True, exist_ok=True)

    catalog = []
    
    # 1. Generate 100 English Documents
    print("\n📚 [1/2] Đang tạo 100 tài liệu tiếng Anh chính thống...")
    for idx, (code, slug, title, category) in enumerate(EN_TOPICS, 1):
        filename = f"{code}_{slug}.md"
        doc_content = generate_english_document(code, slug, title, category)

        # Write to parser outputs
        parser_file = PARSER_DIR / filename
        parser_file.write_text(doc_content, encoding="utf-8")

        # Write to original documents
        orig_file = ORIGINAL_DIR / "en" / filename
        orig_file.write_text(doc_content, encoding="utf-8")

        catalog.append({
            "id": code,
            "filename": filename,
            "language": "en",
            "title": title,
            "category": category,
            "word_count": len(doc_content.split()),
            "char_count": len(doc_content)
        })

    print(f"✅ Đã tạo thành công 100 tài liệu tiếng Anh tại: {PARSER_DIR}")

    # 2. Generate 100 Vietnamese Documents
    print("\n📚 [2/2] Đang tạo 100 tài liệu tiếng Việt chính thống...")
    for idx, (code, slug, title, category) in enumerate(VI_TOPICS, 1):
        filename = f"{code}_{slug}.md"
        doc_content = generate_vietnamese_document(code, slug, title, category)

        # Write to parser outputs
        parser_file = PARSER_DIR / filename
        parser_file.write_text(doc_content, encoding="utf-8")

        # Write to original documents
        orig_file = ORIGINAL_DIR / "vi" / filename
        orig_file.write_text(doc_content, encoding="utf-8")

        catalog.append({
            "id": code,
            "filename": filename,
            "language": "vi",
            "title": title,
            "category": category,
            "word_count": len(doc_content.split()),
            "char_count": len(doc_content)
        })

    print(f"✅ Đã tạo thành công 100 tài liệu tiếng Việt tại: {PARSER_DIR}")

    # 3. Save Master Catalog
    catalog_path = ORIGINAL_DIR / "catalog_200_python_docs.json"
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    readme_content = f"""# KHO 200 TÀI LIỆU CHÍNH THỐNG VỀ LẬP TRÌNH PYTHON (100 EN + 100 VI)

Hệ thống giáo trình tri thức chuẩn mực phục vụ RAG và Trợ giảng lập trình AI Coding Tutor.

## Thống kê tổng quan
- **Tổng số tài liệu**: 200 tài liệu (100 tài liệu tiếng Anh chuẩn Python 3.12/PEP, 100 tài liệu tiếng Việt chuẩn giáo trình ĐH).
- **Thư mục lưu trữ tài liệu gốc**: `data/01_original_documents/python_200/`
- **Thư mục đầu ra bóc tách layout MinerU**: `data/03_parser_outputs/mineru/05_python_200_authoritative/`
- **Bảng mục lục danh mục chi tiết**: [catalog_200_python_docs.json](./catalog_200_python_docs.json)

Mỗi tài liệu được biên soạn cấu trúc 6 phần sư phạm:
1. Mục tiêu sư phạm & Chuẩn đầu ra
2. Khái niệm nền tảng & Cơ chế CPython (Bytecode, Memory, PVM)
3. Cú pháp chuẩn & Mã nguồn mẫu thực tế
4. Lỗi sai phổ biến & Dấu hiệu Traceback
5. Phương pháp sư phạm Socratic gợi mở tư duy gỡ lỗi
6. Bài tập thực hành có thang đo đánh giá & Unit test
"""
    (ORIGINAL_DIR / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"\n📋 Đã tạo Catalog và README tại: {catalog_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()
