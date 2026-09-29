# HƯỚNG DẪN RÀ SOÁT VÀ CHỈNH SỬA SƠ ĐỒ USE CASE (CHI TIẾT THEO DOAN4.MD)

Sau khi rà soát sơ đồ use case mới nhất của bạn đối chiếu với đặc tả chi tiết 48 Use Case trong file [DOAN4.md](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/DOAN4.md), bạn đã khắc phục được một số điểm (đã thêm Actor Giáo vụ, sửa tên Xem bài nộp, bỏ Chạy thử chương trình). 

Tuy nhiên, **sơ đồ hiện tại vẫn còn 4 nhóm lỗi quan trọng (đặc biệt là lỗi ngữ nghĩa UML và sai lệch quyền actor)** cần phải sửa để không bị thầy cô trừ điểm:

---

## 🔴 NHÓM 1: CÁC MŨI TÊN «INCLUDE» VÀ «EXTEND» SAI NGHIÊM TRỌNG (Bắt buộc phải bỏ)

Trong UML:
- `«include»` nghĩa là: Khi thực hiện UC gốc thì **BẮT BUỘC** phải thực hiện UC được include 100% số lần.
- `«extend»` nghĩa là: UC mở rộng chỉ diễn ra trong một số điều kiện đặc biệt để bổ sung cho UC gốc.

Trong sơ đồ của bạn đang có các mũi tên sau bị sai bản chất hoàn toàn:

1. **BỎ mũi tên `Phân quyền người dùng` --«include»--> `Giám sát Docker Sandbox`**:
   - *Lý do sai:* Việc phân quyền tài khoản (UC-35) hoàn toàn không liên quan gì đến việc giám sát Docker Sandbox (UC-46).
   - *Cách sửa:* **Xóa bỏ hoàn toàn mũi tên này**.

2. **BỎ mũi tên `Quản lý cấu hình AI` --«include»--> `Cấu hình Docker Sandbox`**:
   - *Lý do sai:* UC-44 (cấu hình API key, model LLM) và UC-45 (cấu hình tài nguyên, bộ nhớ, CPU của Docker sandbox) là 2 chức năng quản trị hoàn toàn độc lập.
   - *Cách sửa:* **Xóa bỏ hoàn toàn mũi tên này**. Cả 2 UC này đều do Superadmin nối trực tiếp.

3. **BỎ mũi tên `Xem chi tiết bài tập` --«include»--> `Tương tác với AI Tutor`**:
   - *Lý do sai:* Sinh viên bấm xem chi tiết bài tập thì KHÔNG BẮT BUỘC phải chat với AI Tutor. AI Tutor là tính năng tùy chọn.
   - *Cách sửa:* **Xóa bỏ mũi tên này**. Sinh viên đã có đường nối trực tiếp tới `Tương tác với AI Tutor` rồi.

4. **BỎ mũi tên `Xem chi tiết bài tập` --«include»--> `Viết code`**:
   - *Lý do sai:* Xem đề bài không bắt buộc phải viết code ngay (sinh viên có thể chỉ vào đọc đề rồi thoát ra). 
   - *Cách sửa:* **Xóa bỏ mũi tên này**.

5. **BỎ mũi tên `Xem bài nộp` --«include»--> `Đánh giá/chấm bài thủ công`**:
   - *Lý do sai:* Giáo viên vào xem bài nộp của sinh viên (UC-28) không bắt buộc phải chấm bài thủ công (UC-31) mỗi lần xem, vì hệ thống đã Auto-Grade rồi.
   - *Cách sửa:* **Xóa bỏ mũi tên này**. Giáo viên nối trực tiếp vào cả `Xem bài nộp` và `Đánh giá/chấm bài thủ công`.

6. **BỎ mũi tên `Giao bài tập cho lớp` --«include»--> `Tạo bài tập`**:
   - *Lý do sai:* Theo UC-27, Giáo viên giao bài tập **đã có sẵn** trong ngân hàng đề cho lớp học, không phải mỗi lần giao bài là bắt buộc phải tạo mới bài tập.
   - *Cách sửa:* **Xóa bỏ mũi tên này**.

7. **BỎ mũi tên `Đăng xuất` --«extend»--> `Đăng nhập`**:
   - *Lý do sai:* Đây là lỗi kinh điển trong UML. Đăng xuất không phải là phần mở rộng của Đăng nhập. Cả hai là hai hành vi độc lập trong phiên làm việc.
   - *Cách sửa:* Bỏ mũi tên nối giữa Đăng xuất và Đăng nhập.

8. **XÓA oval `Chỉnh sửa code` và mũi tên `«extend»` từ `Viết code`**:
   - *Lý do sai:* Trong [DOAN4.md](file:///d:/CNTT2311/HK9/DOAN4/ai-coding-tutor/DOAN4.md), UC-09 tên là "Viết code" (đã bao gồm cả việc viết mới và chỉnh sửa code trên Monaco Editor). Không có use case riêng tên là "Chỉnh sửa code".
   - *Cách sửa:* **Xóa hẳn oval "Chỉnh sửa code"**.

---

## 🟠 NHÓM 2: LỖI GÁN NHẦM ACTOR VỚI USE CASE AI (Rất dễ bị soi)

1. **Oval `Xem nhận xét AI` (UC-13):**
   - Hiện tại: Trong hình có đường nối từ **Teacher** sang `Xem nhận xét AI`.
   - Đặc tả DOAN4.md: UC-13 là chức năng riêng của **Sinh viên** (xem nhận xét sư phạm để sửa code).
   - *Cách sửa:* **Xóa đường nối từ Teacher sang `Xem nhận xét AI`**.

2. **Oval `Xem AI đánh giá` (UC-30):**
   - Hiện tại: Đang nằm lơ lửng dưới góc phải, bị biến thành `«extend»` của "Đánh giá/chấm bài thủ công" và Teacher không nối trực tiếp.
   - Đặc tả DOAN4.md: UC-30 là chức năng độc lập của **Teacher** (Giáo viên xem phân tích code chất lượng, complexity và điểm số mà AI gợi ý cho cả lớp/từng bài nộp).
   - *Cách sửa:* Nối một đường thẳng trực tiếp từ **Teacher** sang `Xem AI đánh giá`. Bỏ mũi tên extend từ "Đánh giá/chấm bài thủ công".

---

## 🟡 NHÓM 3: THIẾU KẾT NỐI ACTOR VÀ PHÂN QUYỀN QUẢN LÝ LỚP

1. **Các Use Case Quản lý Lớp (Tạo lớp, Chỉnh sửa lớp, Đóng lớp, Xóa lớp, Quản lý sinh viên trong lớp):**
   - Hiện tại trên hình: Chỉ có duy nhất **Giáo vụ** nối vào các UC này.
   - Theo đặc tả DOAN4.md:
     + **Admin (Quản trị viên):** Có quyền quản trị lớp học trên phạm vi toàn trường (UC-38, 39, 40, 41, 42). Vì vậy **Admin bắt buộc phải nối tới**: `Tạo lớp`, `Chỉnh sửa lớp`, `Đóng/mở lớp`, `Xóa lớp`, `Quản lý sinh viên trong lớp`.
     + **Teacher (Giáo viên):** Quản lý lớp do mình phụ trách:
       * UC-17: Tạo lớp học do mình phụ trách
       * UC-18: Chỉnh sửa lớp học do mình phụ trách
       * UC-40: Đóng/Mở lại lớp học do mình phụ trách
       * UC-20: Quản lý sinh viên trong lớp mình phụ trách
       *(Teacher cũng cần được nối tới các chức năng này).*
   - **Lưu ý quan trọng về đường nối giữa Giáo vụ và Admin:** Nếu trên hình đang vẽ mũi tên kế thừa (mũi tên tam giác rỗng) từ Giáo vụ lên Admin là **SAI NGHIỆP VỤ**. Giáo vụ không phải là Admin (Giáo vụ không được quản lý tài khoản, không được phân quyền, không quản lý cấu hình hệ thống). Hãy dùng đường liên kết association bình thường.

2. **Actor bị mất kết nối với Use Case `Đăng nhập`:**
   - Oval `Đăng nhập` đang nằm cô lập ở giữa, không có actor nào nối vào!
   - Cả 5 Actor đều phải có khả năng Đăng nhập vào hệ thống.

---

## 🟢 NHÓM 4: TRÙNG LẶP USE CASE (ANTI-PATTERN CẦN XỬ LÝ)

Hiện trên sơ đồ đang có:
- **2 oval `Quên mật khẩu`** (1 cái góc trên bên trái, 1 cái ở giữa bên trái).
- **2 oval `Xem thông tin cá nhân`** (1 cái góc trên, 1 cái ở giữa).
- **2 oval `Cập nhật thông tin cá nhân`** (1 cái góc trên, 1 cái ở giữa).

Trong chuẩn UML, mỗi Use Case chỉ là một hình oval duy nhất đại diện cho 1 chức năng hệ thống, không được nhân bản.

### 👉 GIẢI PHÁP TỐI ƯU NHẤT (Khuyên dùng để biểu đồ cực kỳ sạch và chuẩn điểm 10):
Tạo 1 Actor trừu tượng ở phía trên tên là **`Người dùng`** (hoặc `User`).
- Cả 5 Actor (`Sinh viên`, `Giáo viên`, `Giáo vụ`, `Admin`, `Superadmin`) đều có mũi tên hình tam giác rỗng (Generalization `—▷`) trỏ về `Người dùng`.
- Nối `Người dùng` tới 6 Use Case chung:
  1. `Đăng nhập` (UC-01)
  2. `Đăng xuất` (UC-02)
  3. `Quên mật khẩu` (UC-03)
  4. `Xem thông tin cá nhân` (UC-04)
  5. `Cập nhật thông tin cá nhân` (UC-05)
  6. `Đổi mật khẩu` (UC-06)
- **Lợi ích:** 
  + Triệt tiêu toàn bộ 3 oval bị trùng lặp.
  + Biểu đồ không còn cảnh hàng chục sợi dây kéo chằng chịt qua lại giữa màn hình.
  + Thầy cô chấm biểu đồ sẽ đánh giá rất cao vì nắm vững nguyên lý kế thừa trong UML.

---

## 🔵 NHÓM 5: CHUẨN HÓA LẠI TÊN USE CASE CHO TRÙNG KHỚP VỚI ĐẶC TẢ

| Tên hiện tại trên sơ đồ | Tên chuẩn theo DOAN4.md | Mã UC | Lý do điều chỉnh |
| :--- | :--- | :--- | :--- |
| `Tạo tài khoản Student/Teacher` | **Tạo tài khoản người dùng** | UC-32 | Admin tạo cả tài khoản Giáo vụ, không chỉ mỗi Student/Teacher. |
| Tách làm 2: `Khóa tài khoản` & `Mở tài khoản` | **Khóa/mở tài khoản** | UC-33 | Trong đặc tả là 1 use case duy nhất thực hiện việc chuyển đổi trạng thái. |
| `Đóng lớp` | **Đóng/mở lại lớp** | UC-40 | Bao gồm cả đóng lớp và mở lại lớp học. |
| `Xóa lớp` | **Quản lý lưu trữ & xóa lớp** | UC-41 | Tên đầy đủ theo nghiệp vụ bao gồm Lưu trữ (Archive) và Xóa. |
| `Thiết lập deadline` | **Thiết lập hạn nộp bài** | UC-24 | Chuẩn hóa thuật ngữ tiếng Việt đồng bộ với tài liệu. |
| `Reset mật khẩu` | **Đặt lại mật khẩu** | UC-36 | Đồng bộ thuật ngữ tiếng Việt với tài liệu. |
| `Import danh sách Excel/CSV` | **Nhập danh sách từ Excel/CSV** | UC-37 | Đồng bộ thuật ngữ tiếng Việt. |
| `Tạo bài tập` | **Quản lý/cấu hình bài tập** | UC-21 | Bao gồm tạo mới và cấu hình các chính sách bài tập. |

---

## BẢNG TỔNG KẾT CHECKLIST THAO TÁC CẦN LÀM:

- [ ] **Xóa mũi tên include sai 1:** `Phân quyền người dùng` -> `Giám sát Docker Sandbox`
- [ ] **Xóa mũi tên include sai 2:** `Quản lý cấu hình AI` -> `Cấu hình Docker Sandbox`
- [ ] **Xóa mũi tên include sai 3:** `Xem chi tiết bài tập` -> `Tương tác với AI Tutor`
- [ ] **Xóa mũi tên include sai 4:** `Xem chi tiết bài tập` -> `Viết code`
- [ ] **Xóa mũi tên include sai 5:** `Xem bài nộp` -> `Đánh giá/chấm bài thủ công`
- [ ] **Xóa mũi tên include sai 6:** `Giao bài tập cho lớp` -> `Tạo bài tập`
- [ ] **Xóa mũi tên extend sai:** `Đăng xuất` -> `Đăng nhập`
- [ ] **Xóa oval thừa:** `Chỉnh sửa code`
- [ ] **Sửa nối AI:** Bỏ dây Teacher -> `Xem nhận xét AI`. Nối Teacher -> `Xem AI đánh giá`.
- [ ] **Thêm quyền Quản lý lớp:** Nối Admin vào `Tạo lớp`, `Chỉnh sửa lớp`, `Đóng/mở lớp`, `Xóa lớp`, `Quản lý SV trong lớp`.
- [ ] **Gộp oval trùng lặp:** Xóa các oval nhân bản của `Quên mật khẩu`, `Xem TT cá nhân`, `Cập nhật TT cá nhân` (dùng actor tổng quát `Người dùng` để kế thừa).
- [ ] **Đổi tên các use case:** Cho khớp chính xác với bảng chuẩn hóa ở Nhóm 5.
