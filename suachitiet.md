# Hướng dẫn sửa sơ đồ Use Case

---

## SỬA 1 — Thêm actor "Giáo vụ"

**Vị trí đặt:** Bên phải sơ đồ, giữa Admin và Teacher (hoặc dưới Admin).

**Cách làm trong draw.io / StarUML / PlantUML:**
- Thêm 1 stick figure mới, đặt nhãn là **"Giáo vụ"**
- Đặt bên phải, thẳng hàng với Admin và Teacher

---

## SỬA 2 — Nối Giáo vụ vào các Use Case

Sau khi thêm actor Giáo vụ, kéo đường nối (association) từ **Giáo vụ** đến các oval sau:

| UC | Tên oval trong sơ đồ |
|----|----------------------|
| UC-38 | Tạo lớp (oval bên phía Admin, KHÔNG phải oval của Teacher) |
| UC-39 | Chỉnh sửa lớp (oval bên phía Admin) |
| UC-40 | Đóng lớp (oval hiện chỉ nối Admin) |
| UC-41 | Xóa lớp (oval hiện chỉ nối Admin) |
| UC-42 | Quản lý sinh viên trong lớp (oval bên phía Admin) |
| UC-43 | Phân công giảng viên vào lớp |

> Lưu ý: Oval "Tạo lớp" và "Chỉnh sửa lớp" xuất hiện 2 lần trong sơ đồ:
> - Oval bên phía **Teacher** → giữ nguyên (UC-17, UC-18 của Teacher)
> - Oval bên phía **Admin** → thêm nối Giáo vụ vào oval này

---

## SỬA 3 — Nối Admin vào "Quản lý tổ chức"

Hiện tại oval **"Quản lý tổ chức"** chỉ nối với **Superadmin**.

**Sửa:** Kéo thêm đường nối từ **Admin** → oval "Quản lý tổ chức"

> Căn cứ: UC-47 — Tác nhân: Quản trị viên hệ thống (Superadmin), Quản trị viên (Admin)

---

## SỬA 4 — Xóa oval "Chạy thử chương trình"

Oval **"Chạy thử chương trình"** hiện đang có trong sơ đồ nhưng **không tồn tại** trong tài liệu UC (DOAN4.md).

**Chọn 1 trong 2 cách:**

**Cách A — Xóa hoàn toàn (khuyến nghị):**
- Xóa oval "Chạy thử chương trình"
- Xóa các đường «extend» nối đến nó từ "Viết code" và "Nộp bài"
- Giữ lại "Viết code", "Nộp bài", "Upload file bài làm"

**Cách B — Đổi tên (nếu muốn giữ chức năng):**
- Đổi tên oval thành "Chạy thử (Run)" và bổ sung UC tương ứng vào tài liệu DOAN4.md

---

## SỬA 5 — Đổi tên "Xem submission" → "Xem bài nộp"

Oval hiện tại tên **"Xem submission"** cần đổi thành **"Xem bài nộp"** cho đồng nhất với UC-28 trong tài liệu.

**Cách làm:** Double-click vào oval → sửa text thành "Xem bài nộp"

---

## SỬA 6 — Tách rõ "Xem nhận xét AI" (Student) và "Xem AI đánh giá" (Teacher)

| UC | Tên chính xác | Actor đúng |
|----|--------------|------------|
| UC-13 | Xem nhận xét AI | Student |
| UC-30 | Xem AI đánh giá | Teacher |

**Sửa:**
- Oval **"Xem nhận xét AI"** → chỉ nối với **Student**
- Oval **"Xem AI đánh giá"** → chỉ nối với **Teacher**
- Nếu hiện tại dùng chung 1 oval thì tách ra thành 2 oval riêng

---

## SỬA 7 — Kiểm tra quan hệ «include»/«extend» nhóm Student

| Quan hệ hiện tại | Đúng/Sai | Ghi chú |
|-----------------|----------|---------|
| Nộp bài «include» Upload file bài làm | Đúng | UC-10 |
| Nộp bài «extend» Chạy thử chương trình | Sai | Xóa nếu xóa UC "Chạy thử" |
| Xem chi tiết bài tập «include» Xem AI đánh giá | Sai | "Xem AI đánh giá" là của Teacher, không phải Student |
| Xem điểm «extend» Xem submission | Cần đổi tên | Đổi "Xem submission" → "Xem bài nộp" |

---

## SỬA 8 — Kiểm tra "Đóng lớp" — thiếu Giáo vụ

UC-40 "Đóng/Mở lại lớp": Tác nhân là **Giáo viên, Quản trị viên, Giáo vụ**.

- Oval **"Đóng lớp"** → cần nối: Admin ✅, Teacher ✅ (kiểm tra), **Giáo vụ ❌ còn thiếu**
- Thêm đường nối Giáo vụ → Đóng lớp

---

## SỬA 9 — Kiểm tra "Xóa lớp" — actor sai

UC-41 "Quản lý Lưu trữ & Xóa lớp": Tác nhân là **Quản trị viên, Giáo vụ** (KHÔNG có Teacher).

- Nếu Teacher đang nối vào "Xóa lớp" → **xóa đường nối đó**
- Thêm Giáo vụ → "Xóa lớp"

---

## SỬA 10 — "Chỉnh sửa code" — xem xét xóa

Sơ đồ có oval **"Chỉnh sửa code"** với quan hệ «extend» từ "Viết code". Tuy nhiên trong UC-09 (Viết code) đã bao gồm cả chỉnh sửa code. Oval này không có UC riêng trong tài liệu.

**Gợi ý:** Xóa oval "Chỉnh sửa code" để tránh dư thừa, hoặc giữ và coi như một bước con hiển thị cho rõ flow.

---

## Checklist tổng kết

- [ ] Thêm actor **Giáo vụ** (stick figure)
- [ ] Nối Giáo vụ → Tạo lớp (Admin side)
- [ ] Nối Giáo vụ → Chỉnh sửa lớp (Admin side)
- [ ] Nối Giáo vụ → Đóng lớp
- [ ] Nối Giáo vụ → Xóa lớp
- [ ] Nối Giáo vụ → Quản lý sinh viên trong lớp (Admin side)
- [ ] Nối Giáo vụ → Phân công giảng viên vào lớp
- [ ] Nối Admin → Quản lý tổ chức
- [ ] Xóa oval "Chạy thử chương trình" (hoặc bổ sung UC vào tài liệu)
- [ ] Đổi "Xem submission" → "Xem bài nộp"
- [ ] Tách "Xem nhận xét AI" (Student) và "Xem AI đánh giá" (Teacher) thành 2 oval riêng
- [ ] Xóa đường nối sai: Student ↔ "Xem AI đánh giá"
- [ ] Kiểm tra + xóa đường nối Teacher → Xóa lớp (nếu có)
