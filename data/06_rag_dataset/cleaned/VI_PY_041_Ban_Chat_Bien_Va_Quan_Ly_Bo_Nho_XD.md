# VI_PY_041: Bản chất biến, gán giá trị và cơ chế cấp phát bộ nhớ trong Python

**Nguồn tài liệu chính thống**: Ebook Python Kỹ Thuật - ThS. Nguyễn Đình Quý
**Chuyên mục**: Bộ nhớ | **Đối tượng học tập**: Sinh viên Công nghệ Thông tin & Kỹ sư Phần mềm
**Chuẩn ngôn ngữ**: Python 3 (CPython Standard Implementation)

---

## Nội dung Giáo trình & Kiến thức Chuyên môn

MỤC LỤC

Giới thiệu
Trong bối cảnh chuyển đổi sốmạnh mẽhiện nay, lập trình đã trởthành một công cụ
nền tảng không chỉđối với các nhà khoa học máy tính mà còn đối với kỹsư và nhà nghiên
cứu trong hầu hết các lĩnh vực khoa học – kỹthuật. Khảnăng mô hình hóa, mô phỏng, xử
lý dữliệu và tựđộng hóa bằng máy tính đóng vai trò then chốt trong việc giải quyết các
bài toán thực tiễn ngày càng phức tạp. Vì vậy, việc trang bịcho sinh viên những kiến thức
và kỹnăng lập trình ngay từgiai đoạn đào tạo đại học là một yêu cầu tất yếu.
Python là một trong những ngôn ngữlập trình phổbiến nhất hiện nay trong lĩnh vực
khoa học và kỹthuật nhờcú pháp đơn giản, dễtiếp cận, khảnăng biểu đạt cao và hệsinh
thái thư viện phong phú. Python cho phép người học tập trung vào tư duy thuật toán và
mô hình tính toán thay vì bịchi phối bởi các chi tiết cú pháp phức tạp. Đặc biệt, với các
thư viện mạnh như NumPy, SciPy và các công cụtrực quan hóa dữliệu, Python đã trở
thành ngôn ngữtiêu chuẩn trong tính toán khoa học, phân tích dữliệu và mô phỏng kỹ
thuật.
Giáo trình Lập trình Python dành cho kỹthuật được biên soạn nhằm phục vụgiảng dạy
và học tập cho sinh viên ngành Khoa học Máy tính, Trường Đại học Xây dựng Hà Nội.
Nội dung giáo trình được xây dựng theo hướng kết hợp chặt chẽgiữa lý thuyết và thực
hành, từnhững khái niệm cơ bản của lập trình Python đến các ứng dụng trong tính toán
số, xửlý dữliệu và mô hình hóa các bài toán kỹthuật. Giáo trình không chỉgiúp sinh viên
nắm vững cú pháp và cấu trúc của ngôn ngữPython mà còn hình thành tư duy lập trình
và khảnăng áp dụng Python như một công cụgiải quyết bài toán thực tế.
Bên cạnh việc trình bày các kiến thức nền tảng như kiểu dữliệu, điều khiển luồng, hàm
và module, giáo trình còn giới thiệu các thư viện quan trọng phục vụcho tính toán khoa
học và kỹthuật. Các ví dụminh họa và bài tập được thiết kếtheo hướng gần gũi với các
bài toán thực tế, giúp sinh viên từng bước làm quen với việc xây dựng mô hình tính toán,
thực hiện tính toán sốvà trực quan hóa kết quả.
Giáo trình được biên soạn với mục tiêu trởthành tài liệu học tập chính thức cho học
phần lập trình Python, đồng thời cũng có thểđược sửdụng như tài liệu tham khảo cho
sinh viên, học viên cao học và những người làm việc trong lĩnh vực khoa học – kỹthuật
có nhu cầu tiếp cận và ứng dụng Python trong công việc nghiên cứu và thực tiễn.
Tác giảxin chân thành cảm ơn các tài liệu, giáo trình và nguồn học thuật trong và
ngoài nước đã được tham khảo trong quá trình biên soạn. Mặc dù đã có nhiều cốgắng,
giáo trình khó tránh khỏi những thiếu sót, rất mong nhận được các ý kiến đóng góp của
đồng nghiệp và người học đểtài liệu ngày càng được hoàn thiện hơn.
1