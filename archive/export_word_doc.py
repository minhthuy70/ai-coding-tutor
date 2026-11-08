# -*- coding: utf-8 -*-
"""
Full generator for the Word (.docx) document:
BÁO CÁO PHÂN TÍCH YÊU CẦU & ĐẶC TẢ GIAO DIỆN HỆ THỐNG (PHIÊN BẢN 1.0)
ĐỀ TÀI: NỀN TẢNG ĐÁNH GIÁ MÃ NGUỒN TỰ ĐỘNG VÀ TRỢ GIẢNG LẬP TRÌNH THÔNG MINH TÍCH HỢP AI
"""

import sys
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_document():
    doc = docx.Document()

    # Page setup: A4, Margins: Top 2cm, Bottom 2cm, Left 2.5cm, Right 2cm
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(0.98)
        section.right_margin = Inches(0.79)
        
        # Add page number in footer
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("Báo cáo Phân tích Yêu cầu & Đặc tả Giao diện v1.0 | AI Coding Tutor")
        f_run.font.name = "Times New Roman"
        f_run.font.size = Pt(9)
        f_run.font.italic = True
        f_run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.2
    normal_style.paragraph_format.space_after = Pt(4)

    # Helper functions
    def set_cell_background(cell, fill_hex):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                          f'<w:top w:w="{top}" w:type="dxa"/>'
                          f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                          f'<w:left w:w="{left}" w:type="dxa"/>'
                          f'<w:right w:w="{right}" w:type="dxa"/>'
                          f'</w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D3D3D3", sz="4"):
        tblPr = table._element.xpath('w:tblPr')
        if tblPr:
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:left w:val="none"/>'
                f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:right w:val="none"/>'
                f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:insideV w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr[0].append(borders)

    def add_p(text="", bold=False, italic=False, font_size=11, color=RGBColor(0x22, 0x22, 0x22), 
              align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=4, line_spacing=1.2):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            run = p.add_run(text)
            run.bold = bold
            run.italic = italic
            run.font.name = "Times New Roman"
            run.font.size = Pt(font_size)
            run.font.color.rgb = color
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79) # Navy
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(12.5)
        run.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6) # Steel Blue
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(11.5)
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_text = p.add_run(text)
        r_text.font.name = "Times New Roman"
        r_text.font.size = Pt(11)

    def add_callout_box(text, title="LƯU Ý QUAN TRỌNG", border_color="1F4E79", bg_color="F2F4F8"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
        
        tcPr = cell._element.get_or_add_tcPr()
        borders_elm = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                                f'<w:top w:val="none"/>'
                                f'<w:bottom w:val="none"/>'
                                f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
                                f'<w:right w:val="none"/>'
                                f'</w:tcBorders>')
        tcPr.append(borders_elm)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        run_title = p.add_run(f"📌 {title}: ")
        run_title.bold = True
        run_title.font.name = "Times New Roman"
        run_title.font.size = Pt(11)
        run_title.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        
        run_text = p.add_run(text)
        run_text.font.name = "Times New Roman"
        run_text.font.size = Pt(10.5)
        run_text.font.color.rgb = RGBColor(0x26, 0x26, 0x26)
        
        add_p("", space_after=4)

    def format_row(row, heights=None, bg_color=None, bold=False, font_size=10, text_color=RGBColor(0x22, 0x22, 0x22)):
        for cell in row.cells:
            if bg_color:
                set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.15
                for r in p.runs:
                    r.bold = bold
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(font_size)
                    r.font.color.rgb = text_color

    # ==========================================================
    # 0. COVER / TITLE PAGE
    # ==========================================================
    add_p("BỘ GIÁO DỤC VÀ ĐÀO TẠO - TRƯỜNG ĐẠI HỌC", bold=True, font_size=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p("KHOA CÔNG NGHỆ THÔNG TIN", bold=True, font_size=13, color=RGBColor(0x1F, 0x4E, 0x79), align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p("----------------------------------***", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=30)

    add_p("ĐỒ ÁN TỐT NGHIỆP ĐẠI HỌC", bold=True, font_size=18, color=RGBColor(0x1F, 0x4E, 0x79), align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    add_p("NỀN TẢNG ĐÁNH GIÁ MÃ NGUỒN TỰ ĐỘNG VÀ TRỢ GIẢNG LẬP TRÌNH THÔNG MINH TÍCH HỢP AI",
          bold=True, font_size=16, color=RGBColor(0xC0, 0x00, 0x00), align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)
    add_p("TÀI LIỆU BÁO CÁO PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG,\nTHIẾT KẾ USER FLOW & BẢN ĐẶC TẢ GIAO DIỆN HỆ THỐNG (PHIÊN BẢN 1.0)",
          bold=True, italic=True, font_size=13, color=RGBColor(0x2E, 0x75, 0xB6), align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)

    # Info Box Table
    info_tbl = doc.add_table(rows=4, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w = [Inches(2.5), Inches(4.0)]
    info_data = [
        ("Đơn vị thực hiện:", "Khoa Công nghệ Thông tin"),
        ("Chuyên ngành:", "Kỹ thuật Phần mềm / Hệ thống Thông tin"),
        ("Mã học phần:", "Đồ án Tốt nghiệp (44 Use Cases)"),
        ("Phiên bản tài liệu:", "Phiên bản 1.0 (Hoàn thiện tháng 10/2026)")
    ]
    for i, (k, v) in enumerate(info_data):
        row = info_tbl.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = col_w[0]
        c1.width = col_w[1]
        set_cell_background(c0, "F8F9FA")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 80, 80, 120, 120)
        set_cell_margins(c1, 80, 80, 120, 120)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(11)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(11)
    set_table_borders(info_tbl, "B0C4DE", "8")

    doc.add_page_break()

    # ==========================================================
    # PHẦN I: TỔNG QUAN ĐỀ TÀI & ĐỐI TƯỢNG NGƯỜI DÙNG (ACTORS)
    # ==========================================================
    add_h1("PHẦN I: TỔNG QUAN ĐỀ TÀI & ĐỐI TƯỢNG NGƯỜI DÙNG")

    add_h2("1.1. Giới thiệu đề tài & 3 bài toán lớn giải quyết")
    add_p("Hệ thống 'Nền tảng đánh giá mã nguồn tự động và trợ giảng lập trình thông minh tích hợp AI' là website hỗ trợ dạy và học lập trình trực tuyến. Hệ thống cho phép giáo viên tạo và giao bài tập, sinh viên viết code trực tiếp trên Web IDE và nộp bài. Khi hết thời hạn, hệ thống tự động chạy và chấm code trong môi trường Sandbox cô lập an toàn, đồng thời AI phân tích chất lượng mã nguồn và đưa ra nhận xét sư phạm.")
    add_p("Nền tảng giải quyết trọn vẹn 3 bài toán lớn trong đào tạo CNTT:")
    add_bullet("Đối với Sinh viên: ", "Vừa được làm bài trên Web IDE chuẩn công nghiệp, vừa có một 'Gia sư AI 24/7' đồng hành, chỉ bảo cách viết code tối ưu (Big-O), chuẩn phong cách (Clean Code) và phòng chống lỗ hổng bảo mật (CWE/OWASP) theo phương pháp Socratic gợi mở tư duy, tuyệt đối không đưa sẵn đáp án.")
    add_bullet("Đối với Giảng viên: ", "Giảm tải 80% công sức chấm bài thủ công, tự động hóa quản lý lớp học và deadline. Giáo viên xem kết quả phân tích song song giữa mã nguồn, kết quả Test Case và gợi ý của AI để chấm bài theo Rubric, nắm giữ 100% quyền kiểm soát điểm số chính thức (Official Score).")
    add_bullet("Điểm sáng học thuật: ", "Ứng dụng kỹ thuật Evidence-Grounded AI (AI đưa ra nhận xét dựa trên bằng chứng thực thi thực tế của Sandbox) kết hợp công nghệ RAG (Retrieval-Augmented Generation) tra cứu cẩm nang môn học từ Vector Database ChromaDB, vận hành mượt mà với chi phí hạ tầng 0 đồng.")

    add_h2("1.2. Kiến trúc kỹ thuật và Bảng công nghệ lựa chọn (Tech Stack)")
    add_bullet("Frontend Web:", "Next.js 14 (App Router) + TypeScript + Tailwind CSS (hỗ trợ Dark Mode chuyên nghiệp cho lập trình viên).")
    add_bullet("Trình soạn thảo mã nguồn:", "Monaco Editor (nhúng từ lõi VS Code, hỗ trợ syntax highlighting đa ngôn ngữ, Autosave tự động và chế độ Read-only khi nộp bài).")
    add_bullet("Backend API Server:", "Python FastAPI (xử lý bất đồng bộ ASGI, tự động sinh tài liệu chuẩn OpenAPI/Swagger).")
    add_bullet("Cơ sở dữ liệu chính:", "PostgreSQL 15 (quản lý người dùng, bài tập, lớp học, bài nộp, sổ cái điểm số).")
    add_bullet("Hàng đợi bất đồng bộ & Cache:", "Redis 7 + Celery (chấm bài bất đồng bộ, chống nghẽn nghẽn khi nhiều sinh viên cùng nộp lúc chốt deadline).")
    add_bullet("Sandbox thực thi an toàn:", "Docker Container cô lập hoàn toàn (--network none, RAM 256MB, CPU 1 core, Timeout 2.0s, user nobody).")
    add_bullet("Vector Database:", "ChromaDB Local (lưu trữ và tra cứu tri thức giáo trình RAG dưới 30ms, không tốn chi phí bản quyền).")
    add_bullet("Trí tuệ nhân tạo (AI Engine):", "Google Gemini 1.5 Flash API (Cloud Free Tier) kết hợp dự phòng chuyển đổi sang Local LLM Ollama / Llama 3 8B (chạy offline bảo vệ đồ án).")

    add_h2("1.3. Mô hình RAG và Ma trận tri thức sư phạm 2 chiều")
    add_p("RAG (Retrieval-Augmented Generation) đóng vai trò số hóa cẩm nang sư phạm của trường để AI tra cứu trước khi đưa ra phản hồi: Khi sinh viên gặp lỗi (ví dụ: Maximum recursion depth), hệ thống trích xuất đúng bài học 'Đệ quy và Điều kiện dừng' từ ChromaDB, giúp AI dùng đúng thuật ngữ thầy cô dạy trên lớp để hướng dẫn.")
    add_bullet("Chiều 1 - Ngôn ngữ lập trình: ", "Python (PEP 8, AST, 100+ mẫu lỗi), C++ (Con trỏ, bộ nhớ, STL, 100+ lỗi crash), Java (OOP, Collections, Exception), JavaScript (ES6+, Async/Await, Closures).")
    add_bullet("Chiều 2 - 6 Trụ cột chuyên môn: ", "Trụ cột 1: Cấu trúc Dữ liệu & Giải thuật; Trụ cột 2: Phân tích Độ phức tạp Big-O; Trụ cột 3: Bộ quy tắc Clean Code & Code Smells; Trụ cột 4: An toàn lập trình & Lỗ hổng CWE Top 25/OWASP; Trụ cột 5: Cẩm nang chẩn đoán lỗi Runtime (Debugging Patterns); Trụ cột 6: Ngân hàng câu hỏi sư phạm Socratic.")

    add_h2("1.4. Đối tượng người dùng và Phân quyền RBAC (05 Vai trò)")
    add_p("Hệ thống thiết lập phân quyền kiểm soát truy cập theo vai trò (Role-Based Access Control) chặt chẽ cho 05 nhóm người dùng:")

    # Table actors
    actor_tbl = doc.add_table(rows=6, cols=3)
    actor_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w = [Inches(1.2), Inches(1.8), Inches(3.5)]
    headers = ["Nhóm tác nhân", "Định danh & Phạm vi", "Đặc điểm nhận dạng & Quyền hạn"]
    for j, h in enumerate(headers):
        cell = actor_tbl.rows[0].cells[j]
        cell.width = col_w[j]
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(10.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, 100, 100, 120, 120)

    actor_data = [
        ("Sinh viên (Student)", "Người học trực tiếp trong các lớp", "Đăng nhập tài khoản trường cấp; làm bài trực tiếp trên Web IDE Monaco; nhận kết quả Test Cases tự động; xem đánh giá Clean Code, Big-O, CWE; tương tác với Socratic AI Tutor; tra cứu lịch sử bài nộp và bảng điểm."),
        ("Giáo viên (Lecturer)", "Giảng viên phụ trách lớp học phần", "Quản lý ngân hàng bài tập; cấu hình Test Cases (Sample/Hidden) và Rubric; giao bài tập cho lớp và chốt 1 mốc deadline cứng duy nhất; xem tiến độ nộp bài; xem gợi ý AI; chấm bài theo Rubric và xác nhận Điểm chính thức (Official Score)."),
        ("Giáo vụ (Academic Staff)", "Cán bộ quản lý đào tạo Khoa/Bộ môn", "Phạm vi quản lý giới hạn trong Khoa/Bộ môn được phân công: Tạo lớp, chỉnh sửa lớp, quản lý vòng đời lớp (Đóng/Mở lại/Lưu trữ/Xóa mềm), phân công giảng viên giảng dạy và quản lý danh sách sinh viên thuộc lớp."),
        ("Quản trị viên (School Admin)", "Quản trị viên cấp trường/viện", "Toàn quyền quản lý dữ liệu danh mục toàn trường: Quản lý cơ cấu Khoa/Bộ môn; phân công Giáo vụ; nhập danh sách hàng loạt tài khoản từ file Excel/CSV 5 cột; khóa/mở/xóa tài khoản; phân quyền người dùng và đặt lại mật khẩu."),
        ("Quản trị viên hệ thống (SysAdmin)", "Kỹ sư vận hành hạ tầng kỹ thuật", "Kiểm soát tầng kỹ thuật: Cấu hình môi trường Docker Sandbox cô lập bảo mật; cấu hình hạn mức tài nguyên (CPU, RAM, Timeout); giám sát container realtime; cấu hình tham số AI Provider (Gemini/Ollama) và tra cứu System Audit Logs.")
    ]
    for i, row_data in enumerate(actor_data, start=1):
        row = actor_tbl.rows[i]
        for j, text in enumerate(row_data):
            cell = row.cells[j]
            cell.width = col_w[j]
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10)
            if j == 0:
                r.bold = True
            set_cell_margins(cell, 90, 90, 120, 120)
            if i % 2 == 0:
                set_cell_background(cell, "F9FBFD")
    set_table_borders(actor_tbl, "CCCCCC", "4")

    # ==========================================================
    # PHẦN II: MỤC TIÊU VÀ NHU CẦU CHÍNH CỦA NGƯỜI DÙNG
    # ==========================================================
    doc.add_page_break()
    add_h1("PHẦN II: MỤC TIÊU VÀ NHU CẦU CHÍNH CỦA NGƯỜI DÙNG")

    add_h2("2.1. Nhóm Sinh viên")
    add_bullet("Mục tiêu: ", "Hoàn thành bài tập lập trình trực tuyến đúng hạn, tiện lợi; hiểu rõ bản chất lỗi lập trình và nâng cao tư duy giải thuật thông qua phản hồi thông minh.")
    add_bullet("Nhu cầu Web IDE trực tiếp: ", "Không phải cài đặt trình biên dịch, IDE nặng nề trên máy cá nhân; chỉ cần mở trình duyệt là có sẵn Monaco Editor hỗ trợ phím tắt chuẩn VS Code.")
    add_bullet("Nhu cầu Autosave bảo vệ mã nguồn: ", "Tự động lưu bản nháp liên tục (Autosave) sau mỗi nhịp gõ, tránh rủi ro mất mã nguồn khi gặp sự cố ngắt kết nối mạng hoặc mất điện đột ngột.")
    add_bullet("Nhu cầu đánh giá khách quan & bảo mật: ", "Thực thi code an toàn qua Sandbox; biết rõ kết quả từng Test Case (AC, WA, TLE, RTE); ẩn dữ liệu Input/Output của Hidden Test Cases để tránh gian lận.")
    add_bullet("Nhu cầu Trợ giảng AI Socratic: ", "Không muốn nhận đáp án sẵn làm triệt tiêu tư duy; cần AI đóng vai trò gia sư gợi mở, chỉ ra dòng code nghi vấn và đặt câu hỏi định hướng dựa trên đúng giáo trình môn học của trường.")

    add_h2("2.2. Nhóm Giáo viên")
    add_bullet("Mục tiêu: ", "Tự động hóa khâu chấm thi, giảm 80% công sức lao động thủ công lặp lại; theo dõi tỷ lệ nộp bài của sinh viên chính xác và công bằng.")
    add_bullet("Nhu cầu chốt Deadline cứng & Thu bài tự động: ", "Cài đặt 1 mốc deadline duy nhất. Khi hết giờ, hệ thống tự động thu bản nháp mới nhất (Auto-Submit Draft), chấm dứt hoàn toàn tình trạng gửi bài trễ qua email.")
    add_bullet("Nhu cầu xem bài tập trung (Split-Screen View): ", "Màn hình trực quan hiển thị song song: Mã nguồn SV | Bảng kết quả thực thi Sandbox | Thẻ đánh giá của AI (Clean Code, Big-O, CWE Security).")
    add_bullet("Nhu cầu làm chủ điểm số chính thức: ", "AI chỉ đóng vai trò trợ lý đề xuất điểm; giáo viên là người trực tiếp chấm theo bảng tiêu chí Rubric và bấm nút 'Xác nhận điểm chính thức' (Official Score) vào sổ điểm.")

    add_h2("2.3. Nhóm Giáo vụ & Quản trị viên")
    add_bullet("Mục tiêu: ", "Quản lý tổ chức, người dùng và lớp học chính xác, đồng bộ; phân cấp rành mạch giữa cấp Trường và cấp Khoa/Bộ môn.")
    add_bullet("Nhu cầu Import dữ liệu nhanh chóng: ", "Khởi tạo tài khoản cho hàng trăm sinh viên/giảng viên chỉ bằng 1 thao tác tải lên file Excel/CSV chuẩn 5 cột, có kiểm tra lỗi trước khi lưu.")
    add_bullet("Nhu cầu quản lý vòng đời lớp học an toàn: ", "Theo dõi các trạng thái lớp: Hoạt động -> Đã đóng -> Lưu trữ (Archive) -> Xóa. Ngăn chặn tuyệt đối việc xóa mất lịch sử điểm số của sinh viên (chỉ cho phép Hard Delete khi lớp có 0 sinh viên và 0 bài tập).")

    add_h2("2.4. Nhóm Quản trị viên hệ thống (SysAdmin)")
    add_bullet("Mục tiêu: ", "Bảo đảm hạ tầng máy chủ vận hành liên tục, an toàn 100% trước các cuộc tấn công mã độc từ sinh viên và tối ưu hóa chi phí vận hành ở mức 0 đồng.")
    add_bullet("Nhu cầu Sandbox cô lập tuyệt đối: ", "Cấu hình Docker cấm kết nối mạng hoàn toàn (--network none), giới hạn RAM 256MB, CPU 1 core, timeout 2.0s để dập tắt fork bomb và ngăn chặn đọc trộm file hệ thống.")
    add_bullet("Nhu cầu cấu hình AI linh hoạt: ", "Chuyển đổi tức thì giữa Google Gemini 1.5 Flash (Cloud API) để demo mượt mà và Ollama Llama 3 (Local) để chạy offline khi báo cáo trước Hội đồng.")
    add_bullet("Nhu cầu kiểm toán hệ thống: ", "Tra cứu System Audit Logs chi tiết để phát hiện hành vi bất thường và phục vụ công tác hậu kiểm.")

    # ==========================================================
    # PHẦN III: NHIỆM VỤ CHÍNH & MA TRẬN 44 USE CASES
    # ==========================================================
    doc.add_page_break()
    add_h1("PHẦN III: NHIỆM VỤ CHÍNH VÀ ĐẶC TẢ CHI TIẾT 44 USE CASES")

    add_h2("3.1. Phân rã 44 Use Cases theo khối chức năng nghiệp vụ")
    add_bullet("Khối 1 - Xác thực & Tài khoản chung (UC-01 đến UC-06): ", "Áp dụng cho mọi người dùng (Đăng nhập, Đăng xuất, Quên mật khẩu, Xem profile, Cập nhật thông tin, Đổi mật khẩu).")
    add_bullet("Khối 2 - Không gian Sinh viên (UC-07 đến UC-16): ", "Xem bài tập, Viết code Web IDE Monaco, Upload file, Nộp bài, Kết quả Auto-Grader Sandbox, Đánh giá AI, Khung chat Socratic AI Tutor, Lịch sử nộp, Bảng điểm cá nhân.")
    add_bullet("Khối 3 - Cổng Quản lý Giáo viên (UC-17 đến UC-27): ", "Tạo bài, Sửa thông tin chung, Xóa bài, Hạn nộp, Test Cases, Rubric, Giao bài cho lớp, Xem bài nộp, Xem điểm, Tham khảo AI Review, Chấm bài thủ công & Xác nhận điểm chính thức.")
    add_bullet("Khối 4 - Phân hệ Quản trị Trường & Giáo vụ (UC-28 đến UC-39, UC-43): ", "Tạo tài khoản, Khóa/Mở, Xóa tài khoản, Phân quyền, Đặt lại mật khẩu, Import Excel 5 cột, Tạo/Sửa/Đóng/Mở/Lưu trữ/Xóa lớp, Quản lý sinh viên trong lớp, Phân công giảng viên, Quản lý Khoa/Bộ môn.")
    add_bullet("Khối 5 - Quản trị Hạ tầng SysAdmin (UC-40 đến UC-42, UC-44): ", "Cấu hình tham số AI, Cấu hình Docker Sandbox, Giám sát Docker Sandbox realtime, Quản lý System Audit Logs.")

    add_h2("3.2. Bảng đặc tả chi tiết 44 Use Cases (Từ UC-01 đến UC-44)")
    add_p("Dưới đây là bảng đặc tả chi tiết toàn bộ 44 Use Cases theo chuẩn công nghệ phần mềm:")

    # Function to add formatted UC Table
    def add_uc_table(uc_id, uc_name, desc, actor, pre_cond, post_cond, main_flow, alt_flow, exc_flow):
        tbl = doc.add_table(rows=8, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_w = [Inches(1.8), Inches(4.7)]
        
        uc_rows = [
            ("Mã Use Case", uc_id, True, "1F4E79", "FFFFFF"),
            ("Tên Use Case", uc_name, True, "2E75B6", "FFFFFF"),
            ("Mô tả tóm tắt", desc, False, "F2F4F8", "222222"),
            ("Tác nhân (Actor)", actor, False, "FFFFFF", "222222"),
            ("Tiền điều kiện", pre_cond, False, "F9FBFD", "222222"),
            ("Hậu điều kiện", post_cond, False, "FFFFFF", "222222"),
            ("Luồng tương tác chính", main_flow, False, "F9FBFD", "222222"),
            ("Luồng thay thế / Ngoại lệ", f"Luồng thay thế:\n{alt_flow}\n\nLuồng ngoại lệ:\n{exc_flow}", False, "FFFFFF", "222222")
        ]
        
        for idx, (label, val, is_header, bg_c, text_c) in enumerate(uc_rows):
            row = tbl.rows[idx]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width = c_w[0]
            c1.width = c_w[1]
            set_cell_background(c0, bg_c if is_header else "EAEFF5")
            set_cell_background(c1, bg_c if is_header else "FFFFFF")
            set_cell_margins(c0, 70, 70, 110, 110)
            set_cell_margins(c1, 70, 70, 110, 110)
            
            p0 = c0.paragraphs[0]
            r0 = p0.add_run(label)
            r0.bold = True
            r0.font.name = "Times New Roman"
            r0.font.size = Pt(9.5)
            if is_header:
                r0.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
            p1 = c1.paragraphs[0]
            r1 = p1.add_run(val)
            r1.font.name = "Times New Roman"
            r1.font.size = Pt(9.5)
            if is_header:
                r1.bold = True
                r1.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
        set_table_borders(tbl, "B0C4DE", "6")
        add_p("", space_after=6)

    # 44 Use cases data dictionary
    uc_list = [
        ("UC-01", "Đăng nhập hệ thống",
         "Cho phép người dùng xác thực tài khoản để bắt đầu phiên làm việc trên hệ thống.",
         "Người dùng (Tất cả vai trò)",
         "Người dùng đã có tài khoản được cấp trong hệ thống.",
         "Phiên đăng nhập được tạo thành công. Hệ thống cấp access_token và refresh_token JWT, điều hướng đến trang chính phù hợp vai trò.",
         "1. Người dùng truy cập trang đăng nhập.\n2. Hệ thống hiển thị biểu mẫu Email và Mật khẩu.\n3. Người dùng nhập thông tin và chọn 'Đăng nhập'.\n4. Hệ thống kiểm tra tính hợp lệ dữ liệu và truy vấn tài khoản.\n5. Đối chiếu mật khẩu băm (bcrypt) và kiểm tra trạng thái hoạt động.\n6. Hệ thống cấp cặp JWT tokens và chuyển đến Dashboard tương ứng vai trò.",
         "7a. Đăng nhập qua liên kết yêu cầu trước: Chuyển về trang yêu cầu ban đầu.\n7b. Mật khẩu tạm thời: Chuyển hướng bắt buộc sang màn hình đổi mật khẩu mới.",
         "E1. Thông tin không chính xác: Báo 'Email hoặc mật khẩu không chính xác'.\nE2. Tài khoản bị khóa: Báo 'Tài khoản đã bị khóa hoặc vô hiệu hóa'.\nE3. Lỗi hệ thống: Báo lỗi và giữ nguyên form."),

        ("UC-02", "Đăng xuất hệ thống",
         "Cho phép người dùng kết thúc an toàn phiên làm việc hiện tại trên hệ thống.",
         "Người dùng (Tất cả vai trò)",
         "Người dùng đang có phiên đăng nhập hợp lệ.",
         "Phiên làm việc kết thúc, token bị thu hồi/vô hiệu hóa, thông tin xác thực cục bộ bị xóa và chuyển về màn hình đăng nhập.",
         "1. Người dùng chọn 'Đăng xuất' trên thanh điều hướng.\n2. Hệ thống hiển thị hộp thoại xác nhận.\n3. Người dùng chọn xác nhận đăng xuất.\n4. Hệ thống đưa refresh_token vào blacklist thu hồi.\n5. Xóa sạch token trên LocalStorage/Cookies trình duyệt.\n6. Chuyển hướng người dùng về trang /login.",
         "3a. Người dùng hủy bỏ: Đóng popup và giữ nguyên phiên làm việc.",
         "E1. Phiên đã hết hạn trước đó: Tự động xóa dữ liệu cục bộ và đưa về /login."),

        ("UC-03", "Quên mật khẩu & Khôi phục",
         "Cho phép người dùng xác thực quyền sở hữu qua email để đặt lại mật khẩu khi bị quên.",
         "Người dùng (Tất cả vai trò)",
         "Người dùng đang ở trang đăng nhập và có quyền truy cập email đã đăng ký.",
         "Mật khẩu mới được băm và lưu vào CSDL; mã OTP/link khôi phục bị vô hiệu hóa.",
         "1. Người dùng chọn 'Quên mật khẩu' tại trang đăng nhập.\n2. Nhập email tài khoản và bấm 'Gửi yêu cầu'.\n3. Hệ thống tạo mã OTP/link reset mật khẩu có thời hạn 15 phút.\n4. Gửi email xác thực đến người dùng.\n5. Người dùng mở link/nhập OTP vào biểu mẫu đặt lại mật khẩu.\n6. Nhập mật khẩu mới, xác nhận và bấm 'Cập nhật mật khẩu'.\n7. Hệ thống cập nhật mật khẩu băm vào CSDL và chuyển về trang đăng nhập.",
         "5a. Không nhận được email: Người dùng yêu cầu gửi lại sau thời gian chờ 60s.",
         "E1. Email không tồn tại: Báo thông báo chung để bảo mật tài khoản.\nE2. Mã xác thực hết hạn: Báo mã không hợp lệ hoặc đã hết hạn.\nE3. Mật khẩu mới không đạt chuẩn bảo mật: Báo lỗi yêu cầu."),

        ("UC-04", "Xem thông tin cá nhân (Profile)",
         "Cho phép người dùng xem chi tiết thông tin tài khoản cá nhân đã lưu trong hệ thống.",
         "Người dùng (Tất cả vai trò)",
         "Người dùng đã đăng nhập có phiên làm việc hợp lệ.",
         "Thông tin cá nhân hiện tại được hiển thị đầy đủ, CSDL không thay đổi.",
         "1. Người dùng truy cập trang Thông tin cá nhân.\n2. Hệ thống xác thực token và quyền truy cập.\n3. Truy vấn dữ liệu người dùng từ CSDL.\n4. Hiển thị họ tên, mã định danh, email, số điện thoại, ảnh đại diện, vai trò và ngày tham gia.",
         "3a. Tải lại trang: Hệ thống đồng bộ dữ liệu mới nhất từ CSDL.",
         "E1. Token hết hạn: Yêu cầu đăng nhập lại.\nE2. Lỗi truy vấn CSDL: Báo 'Không thể tải thông tin cá nhân'."),

        ("UC-05", "Cập nhật thông tin cá nhân",
         "Cho phép người dùng chỉnh sửa và lưu các thông tin cá nhân được phép.",
         "Người dùng (Tất cả vai trò)",
         "Người dùng đã đăng nhập và thông tin cá nhân đã tồn tại.",
         "Thông tin hợp lệ được cập nhật vào CSDL; hiển thị thông báo thành công.",
         "1. Người dùng bấm 'Chỉnh sửa' tại trang cá nhân.\n2. Hệ thống mở form sửa: Họ tên, Số điện thoại, Ảnh đại diện.\n3. Người dùng cập nhật dữ liệu và bấm 'Lưu thay đổi'.\n4. Hệ thống kiểm tra tính hợp lệ (độ dài, định dạng ảnh).\n5. Cập nhật dữ liệu vào CSDL và hiển thị thông báo thành công.",
         "3a. Người dùng bấm 'Hủy': Giữ nguyên thông tin cũ.\n3b. Không có thay đổi: Hệ thống bỏ qua bước ghi CSDL.",
         "E1. Dữ liệu sai định dạng: Báo lỗi và giữ nguyên form nhập.\nE2. Lỗi lưu CSDL: Thông báo 'Cập nhật thông tin thất bại'."),

        ("UC-06", "Đổi mật khẩu",
         "Cho phép người dùng chủ động thay đổi mật khẩu hiện tại định kỳ hoặc bảo mật.",
         "Người dùng (Tất cả vai trò)",
         "Người dùng đã đăng nhập và nhớ mật khẩu hiện tại.",
         "Mật khẩu mới được băm và cập nhật vào CSDL; thu hồi các phiên đăng nhập cũ.",
         "1. Người dùng chọn 'Đổi mật khẩu' trong trang tài khoản.\n2. Nhập Mật khẩu hiện tại, Mật khẩu mới và Xác nhận mật khẩu mới.\n3. Bấm nút 'Đổi mật khẩu'.\n4. Hệ thống kiểm tra mật khẩu cũ chính xác và mật khẩu mới đạt chuẩn.\n5. Băm mật khẩu mới và lưu vào CSDL, thông báo thành công.",
         "2a. Người dùng bấm 'Hủy': Đóng form đổi mật khẩu.",
         "E1. Mật khẩu hiện tại không đúng: Báo 'Mật khẩu hiện tại không chính xác'.\nE2. Mật khẩu mới trùng mật khẩu cũ: Yêu cầu mật khẩu mới phải khác.\nE3. Xác nhận không khớp: Báo mật khẩu xác nhận không trùng khớp."),

        ("UC-07", "Xem danh sách bài tập",
         "Cho phép sinh viên xem và tra cứu danh sách bài tập được giao cho lớp mình tham gia.",
         "Sinh viên (Student)",
         "Sinh viên đã đăng nhập và được gán vào ít nhất một lớp học.",
         "Danh sách bài tập phù hợp được hiển thị trực quan; CSDL không thay đổi.",
         "1. Sinh viên truy cập mục 'Bài tập'.\n2. Hệ thống xác thực danh sách lớp sinh viên đang học.\n3. Truy vấn các bài tập được giao tương ứng.\n4. Hiển thị danh sách: Tên bài, Lớp, Độ khó, Thời hạn nộp (Deadline), Trạng thái làm bài và Điểm (nếu có).\n5. Sinh viên tìm kiếm, lọc theo môn hoặc trạng thái.",
         "5a. Không lọc: Hiển thị toàn bộ bài tập được giao.\n5b. Danh sách trống: Hiển thị thông báo 'Chưa có bài tập nào'.",
         "E1. Phiên hết hạn: Chuyển về màn hình đăng nhập.\nE2. Lỗi CSDL: Báo không thể tải danh sách bài tập."),

        ("UC-08", "Xem chi tiết bài tập & Ràng buộc",
         "Cho phép sinh viên xem chi tiết yêu cầu, mô tả bài toán và ràng buộc kỹ thuật của bài tập.",
         "Sinh viên (Student)",
         "Sinh viên thuộc lớp được giao bài tập này.",
         "Thông tin bài tập được hiển thị; nếu bấm 'Làm bài' sẽ chuyển sang Web IDE.",
         "1. Sinh viên chọn 1 bài tập từ danh sách.\n2. Hệ thống kiểm tra quyền truy cập và thời hạn bài tập.\n3. Hiển thị đề bài hỗ trợ Markdown và công thức LaTeX.\n4. Hiển thị chuẩn Input/Output, ràng buộc RAM/CPU, Sample Test Cases và tiêu chí Rubric công khai.\n5. Sinh viên bấm 'Làm bài' để mở Web IDE.",
         "5a. Bài tập đã hết hạn: Cho phép xem đề và kết quả nhưng khóa nút 'Làm bài'.",
         "E1. Bài không tồn tại: Báo 'Không tìm thấy bài tập'.\nE2. Không có quyền truy cập: Từ chối hiển thị.\nE3. Bài tập đã đóng: Báo bài tập đã kết thúc."),

        ("UC-09", "Viết code trên Web IDE (Monaco)",
         "Cho phép sinh viên viết, chỉnh sửa mã nguồn trực tiếp trên Web IDE và tự động lưu nháp.",
         "Sinh viên (Student)",
         "Bài tập đang mở và còn trong thời hạn nộp bài.",
         "Mã nguồn được lưu liên tục theo cơ chế Autosave Draft; editor hỗ trợ phím tắt và syntax highlight.",
         "1. Sinh viên bấm 'Làm bài' từ trang chi tiết.\n2. Hệ thống khởi tạo Web IDE Monaco với template code chuẩn.\n3. Sinh viên viết mã nguồn.\n4. Hệ thống tự động kích hoạt Autosave lưu bản nháp về CSDL theo chu kỳ 30 giây hoặc khi ngừng gõ 3 giây.\n5. Hiển thị trạng thái 'Đã lưu nháp lúc hh:mm:ss'.",
         "4a. Tải lại trang: Tự động nạp lại bản nháp gần nhất từ CSDL.\n4b. Rời khỏi trang: Tự động lưu nháp trước khi thoát.",
         "E1. Mất kết nối mạng: Cảnh báo không thể lưu nháp, kiểm tra kết nối.\nE2. Bài đã nộp hoặc hết hạn: Lập tức chuyển sang chế độ Read-only."),

        ("UC-10", "Upload file mã nguồn bài làm",
         "Cho phép sinh viên tải file mã nguồn có sẵn từ máy tính cá nhân nạp vào trình soạn thảo Web IDE.",
         "Sinh viên (Student)",
         "Màn hình làm bài đang mở; bài tập chưa nộp và chưa hết hạn.",
         "Nội dung file hợp lệ được nạp vào Monaco Editor và lưu thành bản nháp mới nhất.",
         "1. Sinh viên bấm 'Tải tệp lên' tại giao diện Web IDE.\n2. Chọn file mã nguồn từ máy tính (.py, .cpp, .java, .js).\n3. Hệ thống kiểm tra phần mở rộng, kích thước và mã hóa file.\n4. Đọc nội dung và nạp trực tiếp vào Monaco Editor.\n5. Kích hoạt lưu nháp tự động và thông báo 'Tải file thành công'.",
         "1a. Hủy chọn file: Đóng popup và giữ nguyên nội dung editor.",
         "E1. File không đúng định dạng cho phép: Báo lỗi đuôi file không hỗ trợ.\nE2. Kích thước file vượt quá giới hạn: Báo dung lượng vượt mức cho phép.\nE3. Bài đã khóa: Từ chối tải tệp."),

        ("UC-11", "Nộp bài chính thức",
         "Cho phép sinh viên gửi mã nguồn hiện tại thành bài nộp chính thức duy nhất; khóa editor ở chế độ Read-only.",
         "Sinh viên (Student)",
         "Bài tập chưa hết hạn; sinh viên đã có code hợp lệ trong bản nháp.",
         "Mã nguồn được lưu thành bài nộp duy nhất với trạng thái SUBMITTED; Editor bị khóa Read-only; bài nộp sẽ được chấm sau khi hết hạn.",
         "1. Sinh viên kiểm tra code và bấm nút 'Nộp bài'.\n2. Hệ thống kiểm tra thời hạn và hiển thị popup xác nhận cảnh báo: 'Code sẽ bị khóa và chỉ được chấm sau khi hết hạn deadline'.\n3. Sinh viên bấm 'Xác nhận nộp'.\n4. Hệ thống lưu bản nháp thành bài nộp chính thức (trigger_type = MANUAL).\n5. Chuyển trạng thái sang SUBMITTED và khóa Editor sang Read-only.\n6. Thông báo nộp bài thành công.",
         "2a. Sinh viên bấm 'Hủy': Đóng popup, giữ nguyên trạng thái nháp DRAFT.",
         "E1. Hết hạn trước khi bấm xác nhận: Khóa bài làm, tự chuyển sang Auto-Submit Draft.\nE2. Bản nháp rỗng: Báo lỗi không thể nộp bài trống.\nE3. Bài đã nộp trước đó: Từ chối thao tác."),

        ("UC-12", "Xem kết quả Auto-Grader",
         "Cho phép sinh viên xem chi tiết kết quả chạy kiểm thử tự động của bài nộp từ Docker Sandbox sau khi hết hạn.",
         "Sinh viên (Student)",
         "Bài nộp thuộc về sinh viên và hệ thống đã hoàn tất chấm tự động.",
         "Bảng kết quả Test Cases được hiển thị (AC, WA, TLE, RTE), ẩn dữ liệu Hidden Test Cases.",
         "1. Sinh viên mở bài nộp từ lịch sử làm bài.\n2. Hệ thống xác thực quyền truy cập và kiểm tra trạng thái chấm.\n3. Lấy kết quả từ CSDL.\n4. Hiển thị tổng điểm tạm tính, trạng thái từng Test Case, thời gian chạy thực tế và lượng RAM sử dụng.\n5. Dữ liệu Input/Output của Hidden Test Cases được bảo mật và ẩn đi.",
         "3a. Bài nộp đang chấm (GRADING): Hiển thị trạng thái đang xử lý và nút tải lại.",
         "E1. Bài nộp không tồn tại: Báo không tìm thấy bài nộp.\nE2. Chưa hết hạn/chưa chấm: Báo 'Kết quả chấm bài chưa sẵn sàng'."),

        ("UC-13", "Xem nhận xét AI phân tích mã nguồn",
         "Cho phép sinh viên xem thẻ đánh giá do AI tổng hợp từ Bằng chứng Sandbox và Cẩm nang RAG.",
         "Sinh viên (Student)",
         "Bài nộp đã có kết quả kiểm thử và hoàn thành phân tích AI.",
         "Thẻ đánh giá hiển thị 3 mảng: Clean Code, Ước lượng Big-O và Cảnh báo Lỗ hổng CWE/OWASP.",
         "1. Sinh viên mở trang kết quả bài nộp và chọn tab 'AI Review'.\n2. Hệ thống truy vấn nhận xét AI đã lưu.\n3. Hiển thị thẻ phân tích: Điểm phong cách Clean Code, độ phức tạp thời gian/không gian Big-O, cảnh báo lỗ hổng bảo mật CWE.\n4. Hiển thị các khuyến nghị cải thiện giải thuật.",
         "2a. AI Review đang được tạo: Hiển thị trạng thái chờ và tự động làm mới.",
         "E1. Lỗi AI Service: Hiển thị thông báo không thể tải phân tích AI."),

        ("UC-14", "Tương tác với Socratic AI Tutor",
         "Cho phép sinh viên trò chuyện với Trợ giảng AI để nhận gợi ý tư duy sửa bài theo phương pháp Socratic.",
         "Sinh viên (Student)",
         "Sinh viên đã có kết quả đánh giá cho bài nộp.",
         "AI trả lời theo hướng gợi mở tư duy, trích dẫn giáo trình RAG, tuyệt đối không đưa code giải hộ.",
         "1. Sinh viên bấm nút 'Hỏi AI Tutor' tại trang kết quả.\n2. Cửa sổ trượt (Drawer) AI mở ra với đầy đủ context: Đề bài + Code SV + Evidence lỗi Sandbox + Giáo trình RAG.\n3. Sinh viên nhập câu hỏi nghi vấn và bấm Gửi.\n4. Backend chuyển prompt kèm Guardrails sư phạm đến AI Engine.\n5. AI phản hồi bằng câu hỏi gợi mở logic.\n6. Sinh viên tiếp tục đối thoại liên tục.",
         "3a. Sinh viên bấm 'Tạo phiên mới': Xóa lịch sử chat cũ và tạo context mới.",
         "E1. Sinh viên yêu cầu 'Cho tôi đáp án/code': AI áp dụng Guardrails từ chối và hướng dẫn từng bước.\nE2. AI Service ngắt kết nối: Báo 'AI Tutor tạm thời gián đoạn'."),

        ("UC-15", "Xem bài đã nộp (Lịch sử làm bài)",
         "Cho phép sinh viên xem lại bài nộp chính thức duy nhất của từng bài tập đã làm.",
         "Sinh viên (Student)",
         "Sinh viên đã đăng nhập hệ thống.",
         "Hiển thị danh sách các bài nộp chính thức, thời gian nộp, cơ chế nộp (Thủ công / Hết hạn thu nháp).",
         "1. Sinh viên truy cập mục 'Lịch sử nộp bài'.\n2. Hệ thống truy vấn bài nộp chính thức của sinh viên theo từng bài tập.\n3. Hiển thị bảng: Tên bài, Lớp, Thời điểm nộp, trigger_type (MANUAL/AUTO_EXPIRED), Ngôn ngữ, Điểm tạm tính.\n4. Sinh viên bấm chọn bài tập để xem lại mã nguồn đã nộp.",
         "2a. Tìm kiếm/Lọc: Cho phép lọc theo môn học hoặc trạng thái.",
         "E1. Chưa nộp bài nào: Hiển thị bảng trống với thông báo phù hợp."),

        ("UC-16", "Xem bảng điểm cá nhân",
         "Cho phép sinh viên theo dõi tổng hợp điểm các bài tập trong các lớp học phần mình tham gia.",
         "Sinh viên (Student)",
         "Sinh viên đã đăng nhập hệ thống.",
         "Bảng điểm cá nhân hiển thị rõ ràng điểm chính thức (Official Score) và điểm tạm tính.",
         "1. Sinh viên chọn 'Bảng điểm' trên menu điều hướng.\n2. Hệ thống truy vấn kết quả các bài tập thuộc các lớp của sinh viên.\n3. Tổng hợp điểm theo môn học và cấu trúc trọng số.\n4. Hiển thị danh sách: Bài tập, Lớp, Điểm số, Trạng thái (Tạm tính / Chính thức), Ngày công bố.\n5. Sinh viên xem chi tiết hoặc xuất bảng điểm.",
         "3a. Bài chưa có điểm chính thức: Hiển thị điểm tạm tính hoặc trạng thái chờ chấm.",
         "E1. Lỗi CSDL: Báo không thể tải bảng điểm cá nhân."),

        ("UC-17", "Tạo bài tập mới",
         "Cho phép giáo viên tạo bài tập lập trình mới, nhập đề bài hỗ trợ Markdown và công thức LaTeX.",
         "Giáo viên (Lecturer)",
         "Giáo viên đã đăng nhập và có quyền tạo bài tập.",
         "Bài tập mới được tạo ở trạng thái Nháp hoặc Hoạt động trong Ngân hàng bài tập.",
         "1. Giáo viên bấm 'Tạo bài tập mới' trong Ngân hàng bài tập.\n2. Nhập thông tin: Tiêu đề, Mô tả, Đề bài (Markdown/LaTeX), Mức độ khó (Dễ/TB/Khó), Ngôn ngữ cho phép.\n3. Cài đặt giới hạn tài nguyên: RAM tối đa (MB), CPU Timeout (giây).\n4. Bấm 'Lưu bài tập'.\n5. Hệ thống kiểm tra dữ liệu và lưu vào CSDL, thông báo thành công.",
         "4a. Bấm 'Hủy': Đóng form tạo bài và không lưu dữ liệu.",
         "E1. Thiếu thông tin bắt buộc: Báo lỗi các trường chưa nhập.\nE2. Giới hạn tài nguyên không hợp lệ: Yêu cầu RAM và CPU > 0."),

        ("UC-18", "Chỉnh sửa thông tin chung bài tập",
         "Cho phép giáo viên cập nhật đề bài, mô tả, tài nguyên của bài tập do mình quản lý.",
         "Giáo viên (Lecturer)",
         "Bài tập tồn tại và thuộc quyền quản lý của giáo viên.",
         "Thông tin chung của bài tập được cập nhật thành công mà không ảnh hưởng bài nộp đã có.",
         "1. Giáo viên mở danh sách bài tập và chọn bài cần chỉnh sửa.\n2. Hệ thống hiển thị form thông tin chung hiện tại.\n3. Giáo viên chỉnh sửa đề bài, mức độ khó hoặc giới hạn tài nguyên.\n4. Bấm 'Lưu thay đổi'.\n5. Hệ thống cập nhật CSDL và hiển thị thông báo thành công.",
         "3a. Bài tập đã có sinh viên làm bài: Giới hạn chỉ cho sửa mô tả/đề bài, không cho sửa cấu hình ngôn ngữ.",
         "E1. Không tìm thấy bài tập: Báo lỗi không tồn tại.\nE2. Không có quyền sửa: Từ chối truy cập."),

        ("UC-19", "Xóa bài tập",
         "Cho phép giáo viên xóa bài tập theo chính sách xóa mềm (Soft Delete) để bảo toàn dữ liệu.",
         "Giáo viên (Lecturer)",
         "Bài tập tồn tại và do giáo viên quản lý.",
         "Bài tập được xóa mềm hoặc vô hiệu hóa; các bài nộp và điểm lịch sử được bảo toàn nguyên vẹn.",
         "1. Giáo viên chọn bài tập cần xóa từ danh sách.\n2. Bấm 'Xóa bài tập'.\n3. Hệ thống hiển thị popup xác nhận và cảnh báo dữ liệu liên quan.\n4. Giáo viên xác nhận xóa.\n5. Hệ thống kiểm tra: Nếu bài đã có lượt nộp -> Chuyển trạng thái sang Soft Delete (vô hiệu hóa); nếu chưa có lượt nộp -> Xóa vật lý.\n6. Thông báo thành công và cập nhật lại danh sách.",
         "4a. Bấm 'Hủy': Đóng popup và giữ nguyên bài tập.",
         "E1. Lỗi CSDL: Thông báo xóa bài tập thất bại."),

        ("UC-20", "Thiết lập hạn nộp bài (Deadline cứng)",
         "Cho phép giáo viên cài đặt 1 mốc deadline cứng duy nhất cho bài tập giao cho lớp.",
         "Giáo viên (Lecturer)",
         "Bài tập tồn tại và lớp học đang hoạt động.",
         "Mốc deadline cứng được áp dụng; kích hoạt tiến trình kiểm tra tự động khóa nộp khi hết giờ.",
         "1. Giáo viên chọn bài tập cần đặt thời hạn.\n2. Chọn ngày và giờ kết thúc nộp bài (Deadline).\n3. Bấm 'Lưu hạn nộp'.\n4. Hệ thống kiểm tra thời gian deadline phải lớn hơn thời điểm hiện tại.\n5. Cập nhật mốc deadline vào CSDL và thông báo thành công.",
         "2a. Điều chỉnh hạn nộp đã có: Cho phép chọn lại thời gian mới lớn hơn hiện tại.",
         "E1. Mốc thời gian trong quá khứ: Báo 'Hạn nộp phải lớn hơn thời điểm hiện tại'.\nE2. Lớp học đã đóng: Từ chối thiết lập."),

        ("UC-21", "Thiết lập bộ Test Cases (Sample & Hidden)",
         "Cho phép giáo viên thêm, sửa, xóa các trường hợp kiểm thử tự động (Test Cases) cho bài tập.",
         "Giáo viên (Lecturer)",
         "Giáo viên có quyền quản lý bài tập.",
         "Bộ Test Cases được cập nhật; phân loại rõ ràng giữa Sample (công khai) và Hidden (bảo mật).",
         "1. Giáo viên truy cập tab 'Test Cases' của bài tập.\n2. Bấm 'Thêm Test Case'.\n3. Nhập dữ liệu Input, Output chuẩn mong đợi, Trọng số điểm.\n4. Chọn loại Test Case: 'Sample Test' (sinh viên xem được) hoặc 'Hidden Test' (hệ thống giấu kín).\n5. Bấm 'Lưu Test Cases'.\n6. Hệ thống kiểm tra tính hợp lệ và lưu vào CSDL.",
         "2a. Xóa Test Case: Bấm icon thùng rác, xác nhận và lưu.",
         "E1. Input hoặc Output để trống: Báo lỗi không được để trống.\nE2. Trọng số điểm âm: Yêu cầu trọng số >= 0."),

        ("UC-22", "Thiết lập Rubric chấm điểm",
         "Cho phép giáo viên thiết lập bảng tiêu chí đánh giá chuẩn cho bài tập làm căn cứ chấm điểm.",
         "Giáo viên (Lecturer)",
         "Bài tập tồn tại trong hệ thống.",
         "Bảng Rubric được lưu; tổng trọng số các tiêu chí đạt đúng 100% (hoặc thang điểm 10).",
         "1. Giáo viên mở tab 'Thiết lập Rubric'.\n2. Cấu hình danh sách tiêu chí: Tên tiêu chí, Mô tả, Trọng số điểm.\n3. Tiêu chí mặc định gồm: Tính đúng đắn Test Cases, Clean Code PEP 8, Tối ưu thuật toán Big-O.\n4. Bấm 'Lưu Rubric'.\n5. Hệ thống kiểm tra tổng trọng số bằng 100%.\n6. Cập nhật Rubric vào CSDL.",
         "2a. Thêm tiêu chí tự chọn: Giáo viên bấm 'Thêm tiêu chí' và điền thông tin.",
         "E1. Tổng trọng số không bằng 100%: Báo lỗi tổng trọng số phải đạt đúng 100%.\nE2. Trùng tên tiêu chí: Báo tiêu chí bị trùng lặp."),

        ("UC-23", "Giao bài tập cho Lớp học",
         "Cho phép giáo viên giao bài tập đã có cho một hoặc nhiều lớp học phần do mình phụ trách.",
         "Giáo viên (Lecturer)",
         "Bài tập và lớp học đã tồn tại; giáo viên có quyền phụ trách lớp.",
         "Bài tập được liên kết với lớp; sinh viên trong lớp có thể nhìn thấy và làm bài.",
         "1. Giáo viên chọn bài tập cần giao từ Ngân hàng bài tập.\n2. Bấm nút 'Giao bài cho lớp'.\n3. Chọn một hoặc nhiều lớp phụ trách từ danh sách.\n4. Kiểm tra mốc deadline và bấm 'Xác nhận giao'.\n5. Hệ thống tạo bản ghi phân bổ bài tập cho lớp và lưu vào CSDL.\n6. Thông báo giao bài tập thành công.",
         "3a. Giao cho nhiều lớp cùng lúc: Hệ thống tạo liên kết cho tất cả các lớp được chọn.",
         "E1. Lớp học đã đóng: Báo 'Không thể giao bài cho lớp đã đóng'.\nE2. Chưa chọn lớp: Yêu cầu chọn ít nhất 1 lớp."),

        ("UC-24", "Xem danh sách bài nộp của Lớp",
         "Cho phép giáo viên theo dõi tiến độ nộp bài của toàn lớp, xem chi tiết bài làm của từng sinh viên.",
         "Giáo viên (Lecturer)",
         "Bài tập đã được giao cho lớp phụ trách.",
         "Hiển thị bảng danh sách sinh viên, thời điểm nộp, trạng thái chấm và mã nguồn.",
         "1. Giáo viên mở bài tập trong lớp học phần.\n2. Hệ thống hiển thị bảng tiến độ: Danh sách sinh viên, Mã SV, Trạng thái (Đã nộp/Chưa nộp), Thời gian nộp, Trigger nộp.\n3. Giáo viên bấm chọn một sinh viên để xem chi tiết mã nguồn và kết quả kiểm thử.",
         "2a. Lọc danh sách: Lọc theo sinh viên đã nộp, chưa nộp hoặc đã chấm.",
         "E1. Lỗi CSDL: Báo không thể tải danh sách bài nộp."),

        ("UC-25", "Xem bảng điểm bài tập của Lớp",
         "Cho phép giáo viên xem tổng quan kết quả điểm số của toàn bộ sinh viên đối với bài tập đã giao.",
         "Giáo viên (Lecturer)",
         "Bài tập đã giao cho lớp.",
         "Bảng điểm toàn lớp được hiển thị gồm điểm Auto-Grader, điểm gợi ý AI và Điểm chính thức.",
         "1. Giáo viên bấm 'Xem bảng điểm' của bài tập.\n2. Hệ thống tổng hợp điểm số của toàn bộ sinh viên trong lớp.\n3. Hiển thị bảng: Họ tên, MSSV, Điểm Test Case, Điểm AI, Điểm chính thức (Official Score).\n4. Giáo viên xem biểu đồ phân bố điểm số.",
         "3a. Lọc theo khoảng điểm: Hỗ trợ lọc danh sách sinh viên theo phổ điểm.",
         "E1. Chưa có bài chấm: Báo 'Chưa có kết quả điểm số'."),

        ("UC-26", "Xem kết quả AI đánh giá bài nộp",
         "Cho phép giáo viên xem phân tích chi tiết của AI về Clean Code, Big-O và CWE của bài nộp sinh viên.",
         "Giáo viên (Lecturer)",
         "Bài nộp đã hoàn tất quá trình chấm tự động và phân tích AI.",
         "Hiển thị báo cáo phân tích AI kèm dẫn chứng dòng code để giáo viên tham khảo trước khi chấm.",
         "1. Giáo viên mở bài nộp của sinh viên và chọn tab 'AI Review'.\n2. Hệ thống hiển thị nhận xét chi tiết: Chỉ số Cyclomatic Complexity, mẫu lỗi cú pháp flake8, độ phức tạp thuật toán và cảnh báo bảo mật CWE.\n3. Giáo viên sử dụng thông tin này để làm căn cứ chấm điểm Rubric.",
         "2a. Xem chi tiết vi phạm: Bấm vào cảnh báo để highlight dòng code lỗi tương ứng.",
         "E1. Bài nộp chưa phân tích AI: Báo 'Chưa có dữ liệu đánh giá AI'."),

        ("UC-27", "Chấm bài thủ công & Xác nhận Official Score",
         "Cho phép giáo viên chấm điểm theo Rubric, sửa đổi điểm và bấm nút công bố Official Score.",
         "Giáo viên (Lecturer)",
         "Bài nộp đã có trong hệ thống và bài tập đã thiết lập Rubric.",
         "Điểm số chính thức (Official Score) được ghi nhận vào sổ cái học phần và công bố cho sinh viên.",
         "1. Giáo viên mở màn hình Split-Screen Chấm bài.\n2. Nửa trái hiển thị mã nguồn SV và kết quả Sandbox; nửa phải hiển thị AI Review và Rubric.\n3. Giáo viên đánh giá từng tiêu chí Rubric và nhập điểm số thực tế.\n4. Điền nhận xét sư phạm.\n5. Bấm 'Lưu kết quả' (Lưu bản nháp chấm).\n6. Bấm nút 'Xác nhận điểm chính thức' (Official Score).\n7. Hệ thống ghi nhận điểm chính thức và công bố cho sinh viên.",
         "5a. Giáo viên bấm 'Lưu kết quả' nhưng chưa xác nhận: Điểm lưu ở trạng thái chờ duyệt, chưa công bố.",
         "E1. Điểm tiêu chí vượt quá trọng số: Báo lỗi điểm không hợp lệ.\nE2. Thiếu điểm tiêu chí: Yêu cầu chấm đủ các mục Rubric."),

        ("UC-28", "Tạo tài khoản người dùng thủ công",
         "Cho phép Quản trị viên khởi tạo tài khoản đơn lẻ cho Sinh viên, Giáo viên hoặc Giáo vụ.",
         "Quản trị viên (School Admin)",
         "Quản trị viên đã đăng nhập và có quyền quản lý tài khoản.",
         "Tài khoản được tạo với mật khẩu tạm thời; gửi email thông báo và yêu cầu đổi mật khẩu ở lần đầu login.",
         "1. Quản trị viên chọn 'Tạo tài khoản' trong danh sách người dùng.\n2. Nhập thông tin: Họ tên, Email, Mã định danh (MSSV/MSCB).\n3. Chọn vai trò: 'Sinh viên', 'Giáo viên' hoặc 'Giáo vụ'.\n4. Bấm 'Tạo tài khoản'.\n5. Hệ thống kiểm tra email duy nhất, sinh mật khẩu tạm thời ngẫu nhiên.\n6. Lưu tài khoản vào CSDL và gửi email kích hoạt đến người dùng.",
         "4a. Bấm 'Hủy': Đóng form tạo tài khoản.",
         "E1. Email đã được sử dụng: Báo lỗi email đã tồn tại.\nE2. Thiếu thông tin bắt buộc: Yêu cầu điền đủ các trường."),

        ("UC-29", "Khóa / Mở khóa tài khoản người dùng",
         "Cho phép Quản trị viên chuyển đổi trạng thái hoạt động của tài khoản người dùng.",
         "Quản trị viên (School Admin)",
         "Tài khoản người dùng tồn tại trong hệ thống.",
         "Trạng thái tài khoản được cập nhật; tài khoản bị khóa sẽ bị thu hồi token ngay lập tức.",
         "1. Quản trị viên chọn tài khoản từ danh sách người dùng.\n2. Bấm nút 'Khóa tài khoản' (nếu đang hoạt động) hoặc 'Mở khóa' (nếu đang khóa).\n3. Hệ thống hiển thị hộp thoại xác nhận.\n4. Quản trị viên bấm 'Xác nhận'.\n5. Cập nhật trạng thái tài khoản trong CSDL; nếu khóa -> Thu hồi toàn bộ JWT tokens hiện hành.\n6. Thông báo thao tác thành công.",
         "4a. Bấm 'Hủy': Giữ nguyên trạng thái tài khoản.",
         "E1. Cố gắng khóa tài khoản chính mình: Hệ thống từ chối thao tác bảo vệ.\nE2. Tài khoản không tồn tại: Báo lỗi."),

        ("UC-30", "Xóa tài khoản người dùng",
         "Cho phép Quản trị viên xóa tài khoản theo cơ chế xóa mềm để bảo toàn tính toàn vẹn dữ liệu điểm số.",
         "Quản trị viên (School Admin)",
         "Tài khoản người dùng tồn tại trong hệ thống.",
         "Tài khoản được xóa mềm (Soft Delete) khỏi hệ thống; dữ liệu điểm và bài nộp cũ không bị mất.",
         "1. Quản trị viên chọn tài khoản cần xóa.\n2. Bấm 'Xóa tài khoản'.\n3. Hệ thống kiểm tra dữ liệu: Nếu tài khoản đã có bài nộp/lịch sử giảng dạy -> Áp dụng Soft Delete (ẩn tài khoản, vô hiệu hóa đăng nhập); nếu tài khoản trắng -> Cho phép xóa vật lý.\n4. Hiển thị popup xác nhận cảnh báo dữ liệu.\n5. Quản trị viên xác nhận xóa.\n6. Cập nhật CSDL và thông báo thành công.",
         "5a. Bấm 'Hủy': Đóng popup và giữ nguyên tài khoản.",
         "E1. Không tìm thấy tài khoản: Báo lỗi tài khoản không tồn tại.\nE2. Lỗi CSDL: Báo xóa thất bại."),

        ("UC-31", "Phân quyền người dùng (RBAC)",
         "Cho phép Quản trị viên điều chỉnh vai trò và quyền hạn nghiệp vụ của người dùng.",
         "Quản trị viên (School Admin)",
         "Tài khoản người dùng tồn tại trong hệ thống.",
         "Vai trò của người dùng được cập nhật thành công và áp dụng cho các phiên đăng nhập tiếp theo.",
         "1. Quản trị viên mở trang 'Phân quyền người dùng'.\n2. Chọn tài khoản cần thay đổi vai trò.\n3. Chọn vai trò mới: Sinh viên, Giáo viên hoặc Giáo vụ.\n4. Bấm 'Xác nhận phân quyền'.\n5. Hệ thống kiểm tra tính hợp lệ và cập nhật vai trò vào CSDL.\n6. Thông báo cập nhật quyền thành công.",
         "4a. Bấm 'Hủy': Giữ nguyên quyền hiện tại.",
         "E1. Cố ý gán quyền SysAdmin: Từ chối thao tác (quyền SysAdmin cấu hình độc lập).\nE2. Người dùng không tồn tại: Báo lỗi."),

        ("UC-32", "Đặt lại mật khẩu cho người dùng",
         "Cho phép Quản trị viên chủ động reset mật khẩu cho người dùng khi được yêu cầu hỗ trợ.",
         "Quản trị viên (School Admin)",
         "Tài khoản người dùng tồn tại trong hệ thống.",
         "Mật khẩu tạm thời mới được tạo, băm và gửi về email người dùng; kích hoạt cờ bắt buộc đổi mật khẩu.",
         "1. Quản trị viên chọn tài khoản cần đặt lại mật khẩu.\n2. Bấm nút 'Đặt lại mật khẩu'.\n3. Hệ thống hiển thị hộp thoại xác nhận.\n4. Quản trị viên xác nhận thao tác.\n5. Hệ thống sinh mật khẩu ngẫu nhiên mới, băm mật khẩu và lưu vào CSDL.\n6. Gán cờ `is_temporary_password = true` và thu hồi các phiên đăng nhập cũ.\n7. Gửi email mật khẩu tạm mới đến người dùng và thông báo thành công.",
         "4a. Bấm 'Hủy': Đóng hộp thoại và giữ nguyên mật khẩu cũ.",
         "E1. Lỗi gửi email: Báo lỗi không thể gửi mật khẩu tạm thời.\nE2. Tài khoản bị vô hiệu hóa: Từ chối thao tác."),

        ("UC-33", "Nhập danh sách người dùng từ Excel/CSV",
         "Cho phép Quản trị viên tải file Excel/CSV chuẩn 5 cột để khởi tạo hàng loạt tài khoản người dùng.",
         "Quản trị viên (School Admin)",
         "Tệp Excel/CSV chuẩn bị đúng cấu trúc: [Mã SV/CB] [Họ tên] [Email] [Lớp] [Vai trò].",
         "Các tài khoản hợp lệ được tạo hàng loạt; hệ thống gửi email mật khẩu tạm và xuất báo cáo kết quả.",
         "1. Quản trị viên vào chức năng 'Nhập danh sách từ Excel/CSV'.\n2. Kéo thả hoặc chọn file .xlsx/.csv từ máy tính.\n3. Hệ thống kiểm tra cấu trúc 5 cột tiêu đề bắt buộc.\n4. Đọc từng dòng dữ liệu, kiểm tra cú pháp email và vai trò.\n5. Hiển thị màn hình Xem trước (Preview Data): Tổng dòng, số dòng hợp lệ, số dòng lỗi, danh sách email đã tồn tại.\n6. Quản trị viên chọn phương án xử lý trùng email (Bỏ qua hoặc Cập nhật họ tên) và bấm 'Tiến hành nhập'.\n7. Hệ thống tạo tài khoản hàng loạt, cấp mật khẩu tạm và lưu vào CSDL.\n8. Hiển thị báo cáo kết quả nhập dữ liệu chi tiết.",
         "6a. Bấm 'Hủy': Hủy bỏ toàn bộ quá trình, không lưu dữ liệu.\n6b. Chọn tệp khác: Tải lại tệp mới để kiểm tra preview.",
         "E1. Tệp sai cấu trúc 5 cột: Từ chối đọc file và báo lỗi cấu trúc.\nE2. Tệp không có dữ liệu: Báo file rỗng.\nE3. Không có bản ghi nào hợp lệ: Từ chối thực hiện lưu."),

        ("UC-34", "Tạo lớp học mới",
         "Cho phép Quản trị viên (toàn trường) hoặc Giáo vụ (trong Khoa phụ trách) tạo lớp học mới.",
         "Quản trị viên, Giáo vụ",
         "Người dùng có quyền quản trị lớp tương ứng phạm vi phân công.",
         "Lớp học mới được tạo ở trạng thái Hoạt động; lưu thông tin vào CSDL.",
         "1. Người dùng chọn 'Tạo lớp' trong Quản lý lớp học.\n2. Nhập thông tin: Tên lớp, Mã lớp, Niên khóa, Mô tả, Khoa/Bộ môn (Giáo vụ được tự động gán Khoa phụ trách).\n3. Bấm 'Tạo lớp'.\n4. Hệ thống kiểm tra mã lớp duy nhất và tính hợp lệ của dữ liệu.\n5. Lưu lớp mới vào CSDL ở trạng thái Hoạt động và thông báo thành công.",
         "3a. Bấm 'Hủy': Đóng form tạo lớp.",
         "E1. Mã lớp đã tồn tại: Báo lỗi mã lớp bị trùng.\nE2. Giáo vụ chọn Khoa ngoài phạm vi: Hệ thống từ chối thao tác."),

        ("UC-35", "Chỉnh sửa thông tin lớp học",
         "Cho phép Quản trị viên hoặc Giáo vụ cập nhật tên lớp, niên khóa, mô tả của lớp đang hoạt động.",
         "Quản trị viên, Giáo vụ",
         "Lớp học tồn tại và đang ở trạng thái Hoạt động.",
         "Thông tin lớp học được cập nhật thành công.",
         "1. Người dùng chọn lớp cần chỉnh sửa từ danh sách.\n2. Cập nhật thông tin: Tên lớp, Mô tả, Niên khóa.\n3. Bấm 'Lưu thay đổi'.\n4. Hệ thống kiểm tra tính hợp lệ dữ liệu và cập nhật CSDL.\n5. Thông báo chỉnh sửa thành công.",
         "3a. Bấm 'Hủy': Giữ nguyên thông tin lớp hiện tại.",
         "E1. Lớp đã đóng hoặc lưu trữ: Không cho phép chỉnh sửa trực tiếp.\nE2. Thao tác ngoài phạm vi Khoa: Từ chối quyền truy cập."),

        ("UC-36", "Đóng / Mở lại lớp học",
         "Quản lý trạng thái hoạt động của lớp: Giáo viên (lớp phụ trách), Giáo vụ (Khoa), Admin (toàn trường).",
         "Giáo viên, Giáo vụ, Quản trị viên",
         "Lớp học tồn tại trong hệ thống.",
         "Lớp chuyển từ Hoạt động sang Đã đóng (hoặc ngược lại); dữ liệu lớp được bảo toàn.",
         "1. Người dùng chọn lớp cần thay đổi trạng thái.\n2. Nếu lớp đang Hoạt động -> Hiển thị nút 'Đóng lớp'; nếu đang Đã đóng -> Hiển thị nút 'Mở lại lớp'.\n3. Bấm nút thay đổi trạng thái.\n4. Hệ thống hiển thị hộp thoại xác nhận.\n5. Bấm 'Xác nhận'.\n6. Cập nhật trạng thái lớp trong CSDL và thông báo thành công.",
         "5a. Bấm 'Hủy': Giữ nguyên trạng thái hiện tại.",
         "E1. Thao tác vượt quyền hạn: Báo không có quyền thao tác trên lớp này.\nE2. Trạng thái không phù hợp: Báo lỗi trạng thái."),

        ("UC-37", "Quản lý Lưu trữ, Khôi phục & Xóa lớp học",
         "Quản trị viên (toàn trường) và Giáo vụ (Khoa) quản lý vòng đời lớp học: Lưu trữ, Khôi phục, Xóa.",
         "Quản trị viên, Giáo vụ",
         "Lớp học đã ở trạng thái Đã đóng.",
         "Lớp được chuyển sang Lưu trữ (Archive), Khôi phục hoặc Hard Delete nếu đủ điều kiện (0 SV, 0 bài tập).",
         "1. Người dùng chọn lớp Đã đóng cần xử lý vòng đời.\n2. Chọn thao tác: 'Lưu trữ lớp', 'Khôi phục lớp' hoặc 'Xóa lớp'.\n3. Nếu chọn 'Xóa lớp': Hệ thống kiểm tra số lượng sinh viên và bài tập.\n4. Nếu lớp có 0 sinh viên và 0 bài tập -> Thực hiện Hard Delete (xóa vật lý hoàn toàn).\n5. Nếu lớp có sinh viên hoặc bài tập -> Hệ thống từ chối Hard Delete và tự động chuyển sang trạng thái Lưu trữ (Archive) để bảo toàn điểm số.\n6. Thông báo kết quả thao tác thành công.",
         "2a. Khôi phục lớp: Chuyển lớp từ 'Lưu trữ' về 'Đã đóng'.",
         "E1. Cố ý xóa lớp đang có bài tập: Báo lớp có dữ liệu, tự động chuyển lưu trữ.\nE2. Thao tác ngoài phạm vi Khoa: Báo không có quyền."),

        ("UC-38", "Quản lý sinh viên trong lớp học",
         "Cho phép Quản trị viên hoặc Giáo vụ thêm, xóa sinh viên thuộc danh sách lớp học.",
         "Quản trị viên, Giáo vụ",
         "Lớp học tồn tại và đang ở trạng thái Hoạt động.",
         "Danh sách sinh viên của lớp được cập nhật chính xác trong CSDL.",
         "1. Người dùng chọn lớp cần quản lý thành viên.\n2. Mở tab 'Danh sách sinh viên'.\n3. Chọn 'Thêm sinh viên': Chọn từ danh sách sinh viên chưa có lớp và bấm Thêm.\n4. Chọn 'Xóa khỏi lớp': Chọn sinh viên cần rút tên, xác nhận và bấm Xóa.\n5. Hệ thống kiểm tra và cập nhật CSDL, thông báo thành công.",
         "3a. Chọn nhiều sinh viên: Cho phép thêm/xóa hàng loạt sinh viên cùng lúc.",
         "E1. Sinh viên đã thuộc lớp này: Báo lỗi đã tồn tại trong lớp.\nE2. Lớp học đã đóng: Từ chối thêm/xóa thành viên."),

        ("UC-39", "Phân công Giáo viên vào lớp học",
         "Cho phép Quản trị viên hoặc Giáo vụ phân công một hoặc nhiều giảng viên giảng dạy cho lớp.",
         "Quản trị viên, Giáo vụ",
         "Lớp học và tài khoản giáo viên tồn tại trong hệ thống.",
         "Giáo viên được phân công có quyền quản lý bài tập, deadline và chấm điểm cho lớp đó.",
         "1. Người dùng chọn lớp cần phân công giảng viên.\n2. Mở chức năng 'Phân công giáo viên'.\n3. Chọn giáo viên từ danh sách và bấm 'Phân công'.\n4. Hệ thống kiểm tra giáo viên chưa được gán trước đó.\n5. Lưu liên kết phân công vào CSDL và thông báo thành công.",
         "3a. Hủy phân công: Chọn giáo viên cần rút tên, xác nhận hủy phân công.",
         "E1. Giáo viên đã được phân công lớp này: Báo trùng lặp.\nE2. Lớp học đã đóng: Không cho phép phân công mới."),

        ("UC-40", "Quản lý cấu hình tham số AI Engine",
         "Cho phép SysAdmin cấu hình mô hình LLM (Gemini/Ollama), nhiệt độ Temperature, Prompt và RAG.",
         "Quản trị viên hệ thống (SysAdmin)",
         "SysAdmin đã đăng nhập hệ thống.",
         "Cấu hình AI mới được lưu và áp dụng tức thì cho các yêu cầu phân tích mã nguồn và AI Tutor.",
         "1. SysAdmin mở màn hình 'Cấu hình AI Engine'.\n2. Chọn LLM Provider chính: Google Gemini 1.5 Flash (Cloud API) hoặc Ollama Llama 3 (Local Server).\n3. Điều chỉnh tham số: AI Temperature (0.1 - 0.3), Max Tokens, Top-P.\n4. Cấu hình kết nối ChromaDB Vector Store và Embedding Model.\n5. Bấm 'Kiểm tra kết nối' (Test Connection).\n6. Bấm 'Lưu cấu hình'. Hệ thống lưu vào CSDL và áp dụng ngay lập tức.",
         "5a. Bấm 'Hủy': Giữ nguyên cấu hình cũ.",
         "E1. Kiểm tra kết nối API thất bại: Báo lỗi kết nối API key hoặc server Ollama offline.\nE2. Tham số ngoài khoảng cho phép: Báo lỗi giá trị."),

        ("UC-41", "Cấu hình giới hạn Docker Sandbox",
         "Cho phép SysAdmin thiết lập các cờ bảo vệ cứng và giới hạn tài nguyên của Docker Sandbox Runner.",
         "Quản trị viên hệ thống (SysAdmin)",
         "Dịch vụ Docker Sandbox Runner đã tích hợp vào hệ thống.",
         "Các thông số bảo vệ cứng được lưu và áp dụng cho mọi container thực thi mã nguồn mới.",
         "1. SysAdmin mở màn hình 'Cấu hình Docker Sandbox'.\n2. Cấu hình các tham số cứng: RAM tối đa (mặc định 256MB), CPU giới hạn (1 core), Timeout thực thi (2.0s), Cờ cô lập mạng (--network none), Quyền người dùng (user: nobody non-root).\n3. Bấm 'Lưu cấu hình Sandbox'.\n4. Hệ thống kiểm tra tính hợp lệ và cập nhật tham số vào CSDL runner.",
         "2a. Khôi phục mặc định: Bấm 'Khôi phục mặc định' để gán lại thông số an toàn chuẩn.",
         "E1. Đặt RAM vượt quá tài nguyên máy chủ: Báo lỗi vượt quá giới hạn phần cứng.\nE2. Docker Daemon không kết nối được: Báo lỗi kết nối Docker."),

        ("UC-42", "Giám sát Docker Sandbox realtime",
         "Cho phép SysAdmin theo dõi trạng thái container, mức tiêu thụ RAM/CPU và cưỡng chế dừng container.",
         "Quản trị viên hệ thống (SysAdmin)",
         "SysAdmin đã đăng nhập hệ thống.",
         "Hiển thị bảng giám sát container thời gian thực; cho phép dừng container nghi ngờ fork bomb.",
         "1. SysAdmin mở trang 'Giám sát Docker Sandbox'.\n2. Hệ thống truy vấn Docker API và hiển thị: Số container đang chạy, mức tải CPU, mức tiêu thụ RAM tổng.\n3. Danh sách các phiên runner đang chạy kèm ID, thời gian chạy, mã sinh viên.\n4. SysAdmin có thể bấm nút 'Kill' để cưỡng chế dừng một container bất thường.\n5. Hệ thống kết thúc container, ghi nhật ký System Logs và cập nhật bài nộp sang trạng thái 'Bị gián đoạn'.",
         "2a. Dọn dẹp container rác: Bấm nút 'Dọn dẹp rác' để tự động xóa container zombie.",
         "E1. Docker Daemon mất kết nối: Hiển thị cảnh báo lỗi dịch vụ Docker."),

        ("UC-43", "Quản lý Cơ cấu Tổ chức, Khoa/Bộ môn & Gán Giáo vụ",
         "Cho phép Quản trị viên quản lý danh mục Khoa, Bộ môn và phân công tài khoản Giáo vụ phụ trách.",
         "Quản trị viên (School Admin)",
         "Quản trị viên có quyền quản lý cơ cấu tổ chức toàn trường.",
         "Cơ cấu Khoa/Bộ môn được cập nhật; Giáo vụ được gán đúng phạm vi quản lý.",
         "1. Quản trị viên mở trang 'Quản lý Tổ chức & Khoa/Bộ môn'.\n2. Chọn thao tác: Tạo Khoa/Viện mới, Tạo Bộ môn trực thuộc, Sửa, Khóa hoặc Xóa.\n3. Chọn chức năng 'Phân công Giáo vụ': Chọn tài khoản Giáo vụ và Khoa/Bộ môn phụ trách.\n4. Bấm 'Lưu phân công'.\n5. Hệ thống cập nhật CSDL và áp dụng phạm vi phân quyền cho tài khoản Giáo vụ.",
         "2a. Xóa Khoa/Bộ môn: Chỉ cho phép xóa khi không còn lớp học hoặc giảng viên trực thuộc.",
         "E1. Đang có dữ liệu lớp học liên kết: Từ chối xóa và yêu cầu lưu trữ dữ liệu trước.\nE2. Tên Khoa/Bộ môn trùng lặp: Báo lỗi tên đã tồn tại."),

        ("UC-44", "Quản lý & Tra cứu Nhật ký Hệ thống (System Audit Logs)",
         "Cho phép SysAdmin tra cứu, lọc và theo dõi nhật ký hoạt động hệ thống để giám sát an ninh và sự cố.",
         "Quản trị viên hệ thống (SysAdmin)",
         "SysAdmin đã đăng nhập hệ thống; nhật ký hệ thống đã được ghi nhận.",
         "Nhật ký kiểm toán được hiển thị chi tiết; hỗ trợ xuất báo cáo kiểm tra sự cố.",
         "1. SysAdmin mở trang 'Nhật ký Hệ thống' (System Logs).\n2. Hệ thống hiển thị bảng nhật ký: Thời gian (timestamp), User ID, Địa chỉ IP, Hành động (Action Type), Trạng thái (Thành công/Thất bại), Mô tả.\n3. SysAdmin chọn điều kiện lọc: Khoảng thời gian, loại sự kiện (Login, Submit, Kill container, Config AI), từ khóa.\n4. Bấm chọn 1 log để xem chi tiết payload JSON.\n5. Hỗ trợ bấm nút 'Xuất Logs' ra file Excel/CSV.",
         "4a. Xuất báo cáo: Chọn khoảng ngày và tải tệp nhật ký kiểm toán.",
         "E1. Không tìm thấy logs phù hợp: Hiển thị bảng trống với thông báo.\nE2. Lỗi xuất dữ liệu: Báo không thể tạo file xuất.")
    ]

    for uc in uc_list:
        add_uc_table(uc[0], uc[1], uc[2], uc[3], uc[4], uc[5], uc[6], uc[7], uc[8])

    # ==========================================================
    # PHẦN IV: HỒ SƠ KHÁCH HÀNG MỤC TIÊU (USER PERSONAS)
    # ==========================================================
    doc.add_page_break()
    add_h1("PHẦN IV: HỒ SƠ KHÁCH HÀNG MỤC TIÊU (USER PERSONAS)")
    add_p("Nhằm bảo đảm giao diện đáp ứng chuẩn trải nghiệm người dùng (UX) tối ưu, đồ án xây dựng 04 User Persona đại diện cho 4 nhóm đối tượng trọng tâm:")

    # Persona Table Formatter
    def add_persona_table(name_role, age_edu, tech_level, psychology, goals, pain_points, scenario):
        tbl = doc.add_table(rows=6, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_w = [Inches(1.8), Inches(4.7)]
        
        data = [
            ("Họ tên & Vai trò", name_role, True, "1F4E79"),
            ("Thông tin nhân khẩu", age_edu, False, "EAEFF5"),
            ("Trình độ công nghệ", tech_level, False, "FFFFFF"),
            ("Mục tiêu trên hệ thống", goals, False, "EAEFF5"),
            ("Khó khăn / Rào cản (Pain Points)", pain_points, False, "FFFFFF"),
            ("Kịch bản tương tác tiêu biểu", scenario, False, "F2F4F8")
        ]
        
        for idx, (label, val, is_header, bg_c) in enumerate(data):
            row = tbl.rows[idx]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width = c_w[0]
            c1.width = c_w[1]
            set_cell_background(c0, bg_c if is_header else "EAEFF5")
            set_cell_background(c1, bg_c if is_header else "FFFFFF")
            set_cell_margins(c0, 80, 80, 110, 110)
            set_cell_margins(c1, 80, 80, 110, 110)
            
            p0 = c0.paragraphs[0]
            r0 = p0.add_run(label)
            r0.bold = True
            r0.font.name = "Times New Roman"
            r0.font.size = Pt(10)
            if is_header:
                r0.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
            p1 = c1.paragraphs[0]
            r1 = p1.add_run(val)
            r1.font.name = "Times New Roman"
            r1.font.size = Pt(10)
            if is_header:
                r1.bold = True
                r1.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
        set_table_borders(tbl, "B0C4DE", "6")
        add_p("", space_after=8)

    add_h2("4.1. Persona 1: Nguyễn Văn An - Sinh viên ngành CNTT")
    add_persona_table(
        "Nguyễn Văn An - Sinh viên Lập trình trực tuyến",
        "20 tuổi | Sinh viên năm 2 Khoa CNTT | Đang học học phần Cấu trúc Dữ liệu & Giải thuật (DSA) bằng C++/Python",
        "Trung bình - Khá. Thành thạo VS Code và trình duyệt, nhưng ngại cài đặt môi trường thư viện phức tạp trên máy cá nhân.",
        "Tâm lý: Thường làm bài sát giờ nộp. Lo sợ bị mất code khi mạng chập chờn hoặc mất điện. Khi gặp lỗi runtime phức tạp (Recursion error, Segmentation fault) dễ nản chí và có xu hướng chép lời giải từ Internet mà không hiểu bản chất.",
        "1. Mở trình duyệt là code được ngay, không cần cấu hình compiler.\n2. Được tự động lưu nháp (Autosave) liên tục chống mất code.\n3. Được Trợ giảng AI Socratic chỉ dẫn từng bước theo tài liệu môn học của trường, giúp hiểu bản chất lỗi để tự sửa bài.",
        "1. Mất nhiều thời gian cài đặt IDE/Compiler cục bộ bị lỗi thư viện.\n2. Nộp bài muộn bị trừ điểm oan do quên bấm nộp trước deadline.\n3. Báo cáo lỗi của hệ thống cũ khô khan (chỉ báo WA/TLE), không hiểu vì sao sai thuật toán.",
        "An mở bài tập 'Tìm chu trình Euler' lúc 21h. Giao diện Web IDE hiển thị sẵn template code Python. An gõ code, hệ thống báo 'Đã lưu nháp lúc 21:15:30'. Khi nộp thử, hệ thống Sandbox báo TLE ở Test Case 3. An mở Drawer AI Tutor hỏi 'Tại sao code em chạy chậm?'. AI phân tích vòng lặp dòng số 4 của An có độ phức tạp O(N^2) và gợi mở: 'Theo Bài 4 Cấu trúc dữ liệu Đồ thị của khoa mình, em có thể dùng danh sách kề để giảm xuống O(V+E) được không?'. An tự sửa lại thuật toán và đạt tối đa điểm kiểm thử."
    )

    add_h2("4.2. Persona 2: ThS. Trần Thị Mai - Giảng viên phụ trách môn học")
    add_persona_table(
        "ThS. Trần Thị Mai - Giảng viên Bộ môn Kỹ thuật Phần mềm",
        "38 tuổi | Thạc sĩ CNTT | Giảng dạy hơn 10 năm các môn Lập trình Cơ bản, Lập trình Hướng đối tượng và Cấu trúc Dữ liệu",
        "Rất cao. Chuyên gia về Python, C++, Java và kiểm thử phần mềm.",
        "Tâm lý: Mỗi học kỳ phải chấm bài cho 3 lớp với hơn 250 sinh viên. Kiệt sức vì phải tải hàng trăm file .zip về máy để chạy thủ công. Thường xuyên bị sinh viên phàn nàn và gửi email nộp bài muộn với lý do 'quên nộp'.",
        "1. Tự động hóa khâu chạy Test Case và chốt nộp bài.\n2. Hệ thống tự động thu bài nháp mới nhất khi hết giờ (Auto-Submit Draft).\n3. Có AI hỗ trợ phân tích Clean Code, Big-O và CWE để giáo viên chấm theo Rubric nhanh chóng.\n4. Giữ 100% quyền phê duyệt và làm chủ điểm số chính thức (Official Score).",
        "1. Mất quá nhiều thời gian chấm bài lặp đi lặp lại.\n2. Khó phát hiện sinh viên viết code bừa bộn hoặc dính lỗ hổng bảo mật khi chỉ chấm bằng Test Cases đúng/sai thông thường.\n3. Áp lực nhập điểm vào sổ học phần trước hạn của phòng đào tạo.",
        "Cô Mai tạo bài tập lớn, tải lên 10 Test Cases (gồm 3 Sample và 7 Hidden) và thiết lập hạn nộp cứng đúng 23:59 ngày Chủ nhật. Đến hạn chót, hệ thống tự động khóa nộp và chạy Docker Sandbox chấm tự động toàn bộ lớp. Sáng thứ Hai, cô Mai vào màn hình Split-Screen Chấm bài: Nửa trái hiển thị code sinh viên và kết quả Test Case; nửa phải hiển thị phân tích AI Clean Code và bảng Rubric. Cô Mai lướt qua nhận xét AI, tinh chỉnh điểm theo tiêu chí và bấm 'Xác nhận điểm chính thức'. Toàn bộ bảng điểm lớp được công bố ngay lập tức."
    )

    add_h2("4.3. Persona 3: Lê Văn Hùng - Cán bộ Giáo vụ Khoa")
    add_persona_table(
        "Lê Văn Hùng - Chuyên viên Giáo vụ Khoa CNTT",
        "45 tuổi | Cử nhân Quản trị | Quản lý học vụ, phân lớp và phân công giảng viên cho Khoa CNTT",
        "Cơ bản - Văn phòng. Sử dụng thành thạo phần mềm Microsoft Excel và trình duyệt web.",
        "Tâm lý: Khối lượng công việc tăng vọt vào đầu kỳ và cuối kỳ. Rất sợ thao tác nhầm lẫn làm mất lịch sử điểm số hoặc xáo trộn phân công giảng viên.",
        "1. Quản lý lớp học nhanh chóng trong phạm vi Khoa/Bộ môn được phân công.\n2. Phân công giảng viên và sinh viên vào lớp học chính xác.\n3. Lưu trữ lớp học cũ (Archive) an toàn sau khi kết thúc môn học mà không sợ bị xóa mất dữ liệu điểm số lịch sử.",
        "1. Quy trình quản lý thủ công dễ gây nhầm lẫn mã lớp và danh sách sinh viên.\n2. Sợ bị thao tác xóa nhầm làm mất dữ liệu học tập của các kỳ trước.",
        "Đầu học kỳ mới, thầy Hùng tạo 15 lớp học phần cho Khoa CNTT, phân công cô Mai và các giảng viên phụ trách. Cuối kỳ, sau khi các lớp đã hoàn tất công bố điểm, thầy Hùng thực hiện chức năng 'Lưu trữ lớp' (Archive). Khi thử bấm 'Xóa lớp', hệ thống cảnh báo lớp đang có dữ liệu sinh viên và bài nộp nên từ chối Hard Delete, tự động bảo lưu an toàn dữ liệu vào kho lưu trữ."
    )

    add_h2("4.4. Persona 4: Đỗ Minh Tuấn - Kỹ sư Quản trị Hệ thống (SysAdmin)")
    add_persona_table(
        "Đỗ Minh Tuấn - Kỹ sư Quản trị Hạ tầng & DevOps",
        "30 tuổi | Kỹ sư Mạng máy tính & An toàn Thông tin | Quản trị hạ tầng máy chủ, Docker và dịch vụ AI",
        "Chuyên gia. Thành thạo Linux, Docker, Python FastAPI, Redis, ChromaDB, Kubernetes.",
        "Tâm lý: Đặt tiêu chí bảo mật, cô lập mã độc và tính sẵn sàng của hệ thống lên hàng đầu. Lo sợ sinh viên vô tình hoặc cố ý viết mã độc (fork bomb, ghi đè file hệ thống, mở socket mạng tấn công nội bộ). Áp lực kiểm soát chi phí dịch vụ AI ở mức 0 đồng.",
        "1. Sandbox Docker thực thi hoàn toàn cô lập, ngăn chặn 100% rủi ro an ninh mạng.\n2. Giám sát tài nguyên CPU/RAM realtime và kill ngay container zombie.\n3. Cấu hình chuyển đổi linh hoạt giữa Cloud Gemini Flash (Free API) và Local Ollama Llama 3 (Offline) ngay trên giao diện mà không cần sửa code.",
        "1. Nguy cơ máy chủ bị sập khi hàng trăm sinh viên cùng nộp bài sát giờ deadline.\n2. Mất kết nối Internet trong phòng bảo vệ đồ án khiến AI Cloud ngừng hoạt động.",
        "Tuấn cấu hình Docker Sandbox với các cờ cứng: `--network none`, RAM 256MB, CPU 1 core, timeout 2.0s. Tuấn giả lập chạy thử một đoạn mã độc fork bomb và mở kết nối socket mạng; kết quả Sandbox dập tắt hoàn toàn trong 2 giây. Tại phòng bảo vệ đồ án, phòng thi bị rớt mạng Internet, Tuấn chỉ cần vào màn hình Cấu hình AI, chuyển nút chọn từ 'Google Gemini' sang 'Ollama Local Llama 3', hệ thống tiếp tục chấm và sinh nhận xét AI offline mượt mà với chi phí 0 đồng."
    )

    # ==========================================================
    # PHẦN V: USER FLOWS - QUY TRÌNH NGƯỜI DÙNG CHO CÁC CHỨC NĂNG CHÍNH
    # ==========================================================
    doc.add_page_break()
    add_h1("PHẦN V: USER FLOWS - QUY TRÌNH NGƯỜI DÙNG CHO CÁC CHỨC NĂNG CHÍNH")

    add_h2("5.1. Flow 1: Sinh viên làm bài, nộp bài, nhận kết quả & Socratic AI Tutor")
    add_p("Quy trình thể hiện luồng thao tác khép kín của Sinh viên từ lúc mở đề bài đến khi nhận phản hồi gợi mở từ Trợ giảng AI (Liên kết UC-07, 08, 09, 10, 11, 12, 13, 14):")
    add_bullet("Bước 1: ", "Sinh viên đăng nhập hệ thống, chọn bài tập từ danh sách và bấm 'Làm bài'.")
    add_bullet("Bước 2: ", "Web IDE Monaco hiển thị đề bài, Sample Tests và template code chuẩn. Sinh viên viết code trực tiếp hoặc upload file mã nguồn.")
    add_bullet("Bước 3: ", "Hệ thống tự động kích hoạt Autosave lưu bản nháp về CSDL theo chu kỳ 30 giây hoặc sau 3 giây dừng gõ.")
    add_bullet("Bước 4: ", "Sinh viên bấm 'Nộp bài'. Hệ thống hiển thị popup cảnh báo xác nhận: 'Bài làm sẽ chuyển sang Read-only và được chấm khi hết hạn deadline'.")
    add_bullet("Bước 5: ", "Sinh viên bấm 'Xác nhận nộp'. Hệ thống chuyển trạng thái sang SUBMITTED và khóa editor.")
    add_bullet("Bước 6 (Hết Deadline): ", "Hệ thống tự động kích hoạt Worker, đưa code vào Docker Sandbox cô lập chạy bộ Test Cases, thu thập Execution Evidence và Static Analysis.")
    add_bullet("Bước 7: ", "AI Engine kết hợp Bằng chứng thực thi và tài liệu RAG từ ChromaDB để sinh Thẻ đánh giá Clean Code, Big-O, CWE Security.")
    add_bullet("Bước 8: ", "Sinh viên mở trang kết quả, xem bảng Test Case và mở Drawer 'Socratic AI Tutor' để hỏi đáp gợi mở tư duy sửa bài.")

    add_h2("5.2. Flow 2: Giáo viên tạo bài, giao bài, thu bài tự động & Chấm Official Score")
    add_p("Quy trình thể hiện chu trình quản trị bài tập và kiểm định điểm số của Giảng viên (Liên kết UC-17, 20, 21, 22, 23, 24, 26, 27):")
    add_bullet("Bước 1: ", "Giáo viên tạo bài tập mới, nhập đề bài hỗ trợ Markdown và công thức toán LaTeX.")
    add_bullet("Bước 2: ", "Thiết lập bộ Test Cases gồm Sample công khai và Hidden bảo mật kèm trọng số điểm.")
    add_bullet("Bước 3: ", "Cấu hình bảng Rubric đánh giá (Tính đúng đắn, Clean Code, Tối ưu thuật toán).")
    add_bullet("Bước 4: ", "Giao bài tập cho các lớp phụ trách và cài đặt 1 mốc Deadline cứng duy nhất.")
    add_bullet("Bước 5: ", "Đúng thời điểm Deadline, hệ thống tự động khóa nộp bài và thu bản nháp mới nhất (Auto-Submit Draft), tự động chấm điểm tự động qua Docker Sandbox.")
    add_bullet("Bước 6: ", "Giáo viên truy cập Cổng chấm bài Split-Screen: Xem song song Mã nguồn SV | Bảng Test Cases | Phân tích gợi ý của AI.")
    add_bullet("Bước 7: ", "Giáo viên chấm điểm từng tiêu chí theo Rubric, điền lời nhận xét sư phạm và bấm 'Lưu tạm thời'.")
    add_bullet("Bước 8: ", "Giáo viên bấm nút 'Xác nhận điểm chính thức' (Official Score) để ghi nhận điểm vào sổ cái học phần và công bố cho sinh viên.")

    add_h2("5.3. Flow 3: Quản trị viên Import danh sách từ file Excel/CSV 5 cột")
    add_p("Quy trình khởi tạo hàng trăm tài khoản an toàn qua file bảng tính (Liên kết UC-28, UC-33):")
    add_bullet("Bước 1: ", "Quản trị viên tải lên file .xlsx hoặc .csv.")
    add_bullet("Bước 2: ", "Hệ thống kiểm tra tính toàn vẹn của 5 cột tiêu đề: [Mã SV/CB], [Họ tên], [Email], [Lớp], [Vai trò]. Nếu sai cấu trúc -> Báo lỗi và từ chối.")
    add_bullet("Bước 3: ", "Hệ thống duyệt từng dòng dữ liệu, kiểm tra cú pháp email và xác định danh sách bản ghi hợp lệ, lỗi cú pháp hoặc trùng email đã có.")
    add_bullet("Bước 4: ", "Hiển thị màn hình Xem trước (Preview Data) thống kê trực quan số bản ghi hợp lệ và cảnh báo lỗi.")
    add_bullet("Bước 5: ", "Quản trị viên chọn tùy chọn xử lý trùng lặp và bấm 'Xác nhận nhập dữ liệu'.")
    add_bullet("Bước 6: ", "Hệ thống tạo User hàng loạt, cấp mật khẩu tạm thời ngẫu nhiên, gán cờ bắt buộc đổi mật khẩu ở lần đầu đăng nhập và gửi email thông báo.")

    add_h2("5.4. Flow 4: Quản lý vòng đời lớp học (Đóng, Mở lại, Lưu trữ & Hard Delete)")
    add_p("Quy trình bảo toàn dữ liệu lớp học chặt chẽ (Liên kết UC-34, 35, 36, 37):")
    add_bullet("Trạng thái Hoạt động: ", "Lớp học đang diễn ra bình thường, sinh viên làm bài và giảng viên giao bài tập.")
    add_bullet("Thao tác Đóng lớp: ", "Khi kết thúc học kỳ, Giáo viên/Giáo vụ bấm 'Đóng lớp'. Lớp chuyển sang trạng thái 'Đã đóng', sinh viên không thể làm bài mới.")
    add_bullet("Thao tác Lưu trữ (Archive): ", "Lớp 'Đã đóng' được đưa vào kho Lưu trữ để ẩn khỏi danh sách vận hành thường nhật, bảo toàn 100% dữ liệu bài nộp và điểm số.")
    add_bullet("Thao tác Xóa lớp: ", "Khi người dùng yêu cầu Xóa lớp: Hệ thống tự động kiểm tra số lượng sinh viên và bài tập. Nếu cả hai đều bằng 0 (0 SV, 0 bài tập) -> Cho phép Hard Delete xóa vật lý hoàn toàn. Nếu có ít nhất 1 sinh viên hoặc 1 bài tập -> Hệ thống từ chối xóa vật lý, tự động chuyển sang trạng thái Lưu trữ (Archive).")

    add_h2("5.5. Flow 5: Quản trị viên hệ thống Cấu hình & Giám sát Docker Sandbox, AI Provider")
    add_p("Quy trình vận hành hạ tầng kỹ thuật (Liên kết UC-40, 41, 42, 44):")
    add_bullet("Bước 1: ", "SysAdmin cấu hình giới hạn cứng Sandbox: RAM 256MB, CPU 1 core, timeout 2.0s, --network none.")
    add_bullet("Bước 2: ", "Lựa chọn LLM Provider: Chọn Google Gemini 1.5 Flash API hoặc Ollama Llama 3 Local, điều chỉnh Temperature (0.2). Bấm 'Kiểm tra kết nối'.")
    add_bullet("Bước 3: ", "Màn hình Giám sát Sandbox realtime hiển thị mức tải CPU/RAM, danh sách container đang chạy.")
    add_bullet("Bước 4: ", "Nếu phát hiện container chạy quá thời gian hoặc nghi vấn lặp vô tận, SysAdmin bấm nút 'Kill' để cưỡng chế dừng ngay lập tức.")
    add_bullet("Bước 5: ", "Toàn bộ thao tác cấu hình và can thiệp hạ tầng được tự động ghi nhận vào System Audit Logs.")

    # ==========================================================
    # PHẦN VI: DANH SÁCH MÀN HÌNH GIAO DIỆN CẦN THIẾT
    # ==========================================================
    doc.add_page_break()
    add_h1("PHẦN VI: DANH SÁCH MÀN HÌNH GIAO DIỆN CẦN THIẾT (SCREEN INVENTORY)")
    add_p("Hệ thống bao gồm 26 màn hình giao diện chính được thiết kế đồng bộ theo hệ thống Design System:")

    # Screen Table
    scr_tbl = doc.add_table(rows=27, cols=5)
    scr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_w = [Inches(0.9), Inches(1.8), Inches(1.1), Inches(1.1), Inches(2.2)]
    s_headers = ["Mã MH", "Tên màn hình", "Phân hệ / Actor", "Use Cases", "Mục đích & Thành phần chính"]
    for j, h in enumerate(s_headers):
        cell = scr_tbl.rows[0].cells[j]
        cell.width = c_w[j]
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, 80, 80, 100, 100)

    screens_data = [
        ("SCR-01", "Trang Đăng nhập (Login)", "Chung / All", "UC-01", "Form nhập Email, Mật khẩu, Nút đăng nhập, Liên kết quên mật khẩu."),
        ("SCR-02", "Quên mật khẩu & Reset", "Chung / All", "UC-03", "Nhập email nhận OTP/link reset mật khẩu; Form đặt mật khẩu mới."),
        ("SCR-03", "Hồ sơ cá nhân & Đổi pass", "Chung / All", "UC-04, 05, 06", "Xem/sửa họ tên, avatar; Form đổi mật khẩu bảo mật."),
        ("SCR-04", "Dashboard Sinh viên", "Sinh viên", "UC-07, 16", "Thống kê bài tập sắp đến hạn, tiến độ làm bài, thông báo điểm mới."),
        ("SCR-05", "Danh sách bài tập được giao", "Sinh viên", "UC-07", "Danh sách dạng card/bảng: Tên bài, lớp, độ khó, hạn nộp, trạng thái."),
        ("SCR-06", "Chi tiết bài tập & Hướng dẫn", "Sinh viên", "UC-08", "Đề bài Markdown/LaTeX, ràng buộc RAM/CPU, Sample Tests, Nút 'Làm bài'."),
        ("SCR-07", "Không gian Web IDE Monaco", "Sinh viên", "UC-09, 10, 11", "Editor Monaco, chọn ngôn ngữ, upload file, autosave status, nút Nộp bài."),
        ("SCR-08", "Kết quả Chấm & Thẻ Đánh giá AI", "Sinh viên", "UC-12, 13", "Bảng Test Cases (AC/WA/TLE), Thẻ đánh giá Clean Code, Big-O, CWE."),
        ("SCR-09", "Khung Chat Socratic AI Tutor", "Sinh viên", "UC-14", "Drawer trượt bên phải Web IDE, Markdown chat, gợi mở tư duy theo RAG."),
        ("SCR-10", "Lịch sử nộp & Chi tiết bài làm", "Sinh viên", "UC-15", "Xem bài nộp chính thức, thời gian nộp, trigger nộp, mã nguồn đã nộp."),
        ("SCR-11", "Bảng điểm cá nhân học phần", "Sinh viên", "UC-16", "Tổng hợp điểm các bài tập theo môn, trạng thái Tạm tính / Chính thức."),
        ("SCR-12", "Dashboard Giáo viên", "Giáo viên", "UC-23, 25", "Thống kê lớp phụ trách, tỷ lệ nộp bài, bài tập đang mở deadline."),
        ("SCR-13", "Quản lý Ngân hàng Bài tập", "Giáo viên", "UC-17, 18, 19", "Danh sách bài tập do GV tạo; tìm kiếm, lọc theo độ khó, tag DSA."),
        ("SCR-14", "Thiết lập Test Cases & Rubric", "Giáo viên", "UC-20, 21, 22", "Form cấu hình: Giới hạn tài nguyên, thêm Test Cases, định nghĩa Rubric."),
        ("SCR-15", "Giao bài cho Lớp & Chốt Deadline", "Giáo viên", "UC-23", "Chọn lớp, thiết lập 1 mốc deadline cứng, kích hoạt Auto-Submit Draft."),
        ("SCR-16", "Cổng Chấm bài Split-Screen", "Giáo viên", "UC-24, 26, 27", "2 cột song song: Cột trái (Code SV + Test), Cột phải (AI + Bảng Rubric)."),
        ("SCR-17", "Bảng điểm tổng kết Lớp học", "Giáo viên / GVụ", "UC-25, 38", "Bảng ma trận điểm toàn lớp theo từng bài tập, xuất file Excel bảng điểm."),
        ("SCR-18", "Dashboard Quản trị Trường", "Quản trị viên", "Toàn bộ Admin", "Tổng quan người dùng, số lượng lớp, khoa viện, lưu lượng sử dụng."),
        ("SCR-19", "Quản lý Người dùng & RBAC", "Quản trị viên", "UC-28 -> 32", "Danh sách User, bộ lọc vai trò, nút Khóa/Mở, Reset pass, Phân quyền."),
        ("SCR-20", "Import Danh sách từ Excel/CSV", "Quản trị viên", "UC-33", "Kéo thả file Excel 5 cột, bảng preview kiểm tra lỗi dòng, nút xác nhận."),
        ("SCR-21", "Quản lý Cơ cấu Khoa / Bộ môn", "Quản trị viên", "UC-43", "Cây thư mục đơn vị, tạo/sửa Khoa/Bộ môn, phân công Giáo vụ phụ trách."),
        ("SCR-22", "Quản lý Lớp & Vòng đời Lớp", "Giáo vụ / Admin", "UC-34 -> 37", "Quản lý lớp; thực hiện Đóng, Mở lại, Lưu trữ (Archive) và Xóa lớp."),
        ("SCR-23", "Quản lý SV & Phân công GV", "Giáo vụ / Admin", "UC-38, 39", "Gán/xóa sinh viên vào lớp; phân công một hoặc nhiều giảng viên giảng dạy."),
        ("SCR-24", "Dashboard Giám sát Sandbox", "SysAdmin", "UC-41, 42", "Biểu đồ tải CPU/RAM realtime của Sandbox runner, danh sách container, Kill."),
        ("SCR-25", "Cấu hình Tham số AI Engine", "SysAdmin", "UC-40", "Chọn Provider (Gemini/Ollama), thiết lập Prompt Template, Temperature."),
        ("SCR-26", "Tra cứu System Audit Logs", "SysAdmin", "UC-44", "Bộ lọc logs theo thời gian, IP, User ID, Action; xem JSON payload và xuất file.")
    ]

    for i, row_data in enumerate(screens_data, start=1):
        row = scr_tbl.rows[i]
        for j, text in enumerate(row_data):
            cell = row.cells[j]
            cell.width = c_w[j]
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9)
            if j == 0:
                r.bold = True
            set_cell_margins(cell, 70, 70, 90, 90)
            if i % 2 == 0:
                set_cell_background(cell, "F9FBFD")
    set_table_borders(scr_tbl, "CCCCCC", "4")

    # ==========================================================
    # PHẦN VII: BẢN ĐẶC TẢ YÊU CẦU GIAO DIỆN PHIÊN BẢN 1 (UI SPEC V1.0)
    # ==========================================================
    doc.add_page_break()
    add_h1("PHẦN VII: BẢN ĐẶC TẢ YÊU CẦU GIAO DIỆN PHIÊN BẢN 1 (UI SPEC V1.0)")

    add_h2("7.1. Tiêu chuẩn Thiết kế Hệ thống (Design System Standards)")
    add_bullet("Triết lý thiết kế: ", "Tối giản hiện đại, chuẩn công nghiệp, ưu tiên chế độ nền tối (Dark Mode) cho trình soạn thảo code nhằm giảm mỏi mắt và tăng tính thẩm mỹ chuyên nghiệp.")
    add_bullet("Bảng màu nhận diện (Color Palette):", "")
    add_p("  • Background chính: #0F172A (Slate 900) - Tông xám đậm công nghệ sang trọng.\n"
          "  • Card / Container: #1E293B (Slate 800) kết hợp viền mờ #334155 (Slate 700).\n"
          "  • Màu chủ đạo (Primary Accent): #3B82F6 (Electric Blue) hoặc #6366F1 (Indigo).\n"
          "  • Màu thành công (Success / AC): #10B981 (Emerald Green) - Báo hiệu Test Case đúng.\n"
          "  • Màu cảnh báo (Warning / TLE / WA): #F59E0B (Amber) - Cảnh báo vượt thời gian.\n"
          "  • Màu nguy hiểm (Danger / CWE / Bug): #EF4444 (Rose Red) - Lỗi cú pháp, runtime crash, lỗ hổng bảo mật.")
    add_bullet("Quy chuẩn Typography:", "")
    add_p("  • Giao diện điều hướng và văn bản: Inter / Roboto (sans-serif), cỡ chữ 13-14px, line-height 1.5.\n"
          "  • Trình soạn thảo mã nguồn Monaco: JetBrains Mono / Fira Code (monospaced), cỡ chữ 14px, hỗ trợ font ligatures (ký tự lập trình chuẩn).")

    add_h2("7.2. Đặc tả Chi tiết các Màn hình Trọng tâm")

    # Screen Spec 1: Web IDE
    add_h3("A. Màn hình Không gian Web IDE Monaco & Socratic AI Tutor (SCR-07, 08, 09)")
    add_p("Màn hình dành riêng cho Sinh viên thực hiện viết code, nộp bài và tương tác học tập với AI.")
    add_bullet("Bố cục phân vùng (Layout 3 cột):", "")
    add_p("  • Cột 1 (30% chiều rộng - Đề bài & Ràng buộc): Hiển thị tên bài, độ khó, thời hạn nộp đếm ngược realtime; nội dung đề bài hỗ trợ Markdown và công thức LaTeX; bảng Input/Output; giới hạn RAM 256MB, CPU 1.0s; danh sách Sample Test Cases và Rubric công khai.\n"
          "  • Cột 2 (45% chiều rộng - Monaco Code Editor): Thanh công cụ chọn ngôn ngữ (Python 3.11, C++ 17, Java 17, JS ES6); nút Tải tệp lên; phím tắt định dạng; trình soạn thảo Monaco có đánh số dòng, tự động hoàn thành từ khóa; thanh trạng thái phía dưới hiển thị Autosave: '[V] Đã lưu nháp lúc hh:mm:ss'.\n"
          "  • Cột 3 (25% chiều rộng - Kết quả kiểm thử & Phân tích AI): Tab 'Test Cases' hiển thị danh sách kiểm thử (AC, WA, TLE, RTE); Tab 'AI Review' hiển thị thẻ đánh giá Clean Code, Big-O, CWE; Nút lớn 'NỘP BÀI' (nổi bật màu xanh primary) và nút 'HỎI AI TUTOR'.")
    add_bullet("Cửa sổ trượt Socratic AI Tutor Drawer (SCR-09):", "")
    add_p("Khi bấm 'Hỏi AI Tutor', một cửa sổ trượt (Drawer) mượt mà xuất hiện từ mép phải màn hình đè nhẹ lên Cột 3. Drawer bao gồm khung chat hiển thị tin nhắn dạng hội thoại 2 chiều, định dạng Markdown có tô màu khối code. Khung nhập tin nhắn bên dưới cho phép sinh viên hỏi nghi vấn lỗi. AI trả lời mang tính gợi mở, trích dẫn đúng bài giảng từ kho RAG của trường, tuyệt đối không đưa thẳng code giải.")
    add_bullet("Quy tắc chuyển trạng thái & Ràng buộc (Validation & State):", "")
    add_p("  • Khi sinh viên bấm 'Nộp bài': Hiển thị Modal xác nhận cảnh báo: 'Bài làm sẽ chuyển sang chế độ Read-only và được chấm sau khi hết hạn 23:59. Bạn có chắc chắn muốn nộp?'. Sau khi bấm Xác nhận, editor lập tức bị khóa tính năng nhập (readOnly: true), nút Nộp bài bị ẩn hoặc vô hiệu hóa.\n"
          "  • Khi bài tập quá hạn deadline: Ngay cả khi sinh viên chưa bấm nộp, hệ thống Cron Job tự động thu bản nháp mới nhất (Auto-Submit Draft), khóa editor vĩnh viễn.")

    # Screen Spec 2: Teacher Grading
    add_h3("B. Cổng Chấm bài & Xác nhận Điểm chính thức của Giáo viên (SCR-16)")
    add_p("Màn hình chuyên biệt dành cho Giảng viên kiểm tra bài làm của sinh viên và chấm điểm theo Rubric.")
    add_bullet("Bố cục chia đôi màn hình (Split-Screen Grading View):", "")
    add_p("  • Nửa bên trái: Hiển thị thông tin sinh viên (Họ tên, MSSV, Lớp), bài nộp và thời điểm nộp (ghi rõ nộp thủ công hay Auto-Submit lúc hết giờ). Bên dưới là trình soạn thảo Monaco ở chế độ Read-only hiển thị mã nguồn của sinh viên kèm kết quả thực thi Sandbox từng Test Case.\n"
          "  • Nửa bên phải: Thẻ phân tích gợi ý tự động của AI (Collapse/Expand) đánh giá độ phức tạp thuật toán Big-O, điểm phong cách Clean Code và lỗi bảo mật CWE. Phía dưới là Bảng tiêu chí Rubric cho phép giáo viên nhập điểm trực tiếp cho từng tiêu chí (Tính đúng đắn, Phong cách code, Tối ưu hóa) kèm ô nhập nhận xét sư phạm.")
    add_bullet("Quy trình xác nhận Official Score:", "")
    add_p("  • Nút 'Lưu tạm thời': Cho phép giảng viên lưu kết quả chấm dạng Draft để xem lại sau, sinh viên chưa xem được điểm chính thức.\n"
          "  • Nút 'Xác nhận điểm chính thức' (Official Score): Khi bấm, hệ thống hiển thị hộp thoại xác nhận ghi nhận điểm vào sổ cái học phần. Sau khi xác nhận, điểm số chính thức được chốt và công bố tức thì cho sinh viên.")

    # Screen Spec 3: Import Excel
    add_h3("C. Màn hình Import Danh sách Người dùng từ Excel/CSV (SCR-20)")
    add_p("Màn hình dành cho Quản trị viên để khởi tạo tài khoản hàng loạt cho sinh viên và giáo viên.")
    add_bullet("Bố cục giao diện:", "")
    add_p("  • Khu vực trên: Vùng kéo thả file (Drag & Drop Zone) hỗ trợ định dạng .xlsx và .csv, có liên kết 'Tải file mẫu Excel 5 cột'.\n"
          "  • Khu vực dưới (Bảng Preview kiểm tra hợp lệ): Sau khi thả file, hệ thống tự động đọc và hiển thị bảng xem trước gồm các cột: Mã SV/CB | Họ và tên | Email | Lớp | Vai trò | Trạng thái kiểm tra. Mỗi dòng có nhãn màu trực quan: [Hợp lệ] màu xanh, [Lỗi cú pháp email] màu đỏ, [Trùng email] màu vàng.\n"
          "  • Thanh điều khiển phía dưới: Thống kê số lượng (Tổng số, Số dòng hợp lệ, Số dòng lỗi). Tùy chọn xử lý tài khoản đã tồn tại: Bỏ qua hoặc Cập nhật họ tên. Nút bấm 'Hủy bỏ' và 'Tiến hành nhập X bản ghi hợp lệ'.")
    add_bullet("Quy tắc nghiệp vụ:", "")
    add_p("  • Kiểm tra nghiêm ngặt 5 cột bắt buộc: Mã SV, Họ tên, Email, Lớp, Vai trò. Thiếu bất kỳ cột nào sẽ từ chối đọc file ngay lập tức.\n"
          "  • Tài khoản tạo mới tự động được gán cờ mật khẩu tạm thời và gửi email thông báo yêu cầu đổi mật khẩu ở lần đầu đăng nhập.")

    # Screen Spec 4: SysAdmin Dashboard
    add_h3("D. Dashboard Giám sát Docker Sandbox & Cấu hình Tham số AI (SCR-24, SCR-25)")
    add_p("Màn hình điều hành dành riêng cho Kỹ sư Quản trị Hệ thống (SysAdmin).")
    add_bullet("Bố cục phân hệ:", "")
    add_p("  • Phân hệ Giám sát Docker Sandbox realtime: Hiển thị thẻ trạng thái Docker Daemon (Active/Inactive), biểu đồ tải CPU tổng, biểu đồ tiêu thụ RAM tổng, số container đang thực thi. Bảng danh sách các container runner đang hoạt động kèm ID, loại ngôn ngữ (PyRunner, CppRunner), sinh viên nộp bài, lượng RAM đỉnh và Nút 'Kill' cưỡng chế dừng khẩn cấp.\n"
          "  • Phân hệ Cấu hình Tham số AI Engine: Bộ nút chọn Provider: [Google Gemini 1.5 Flash API (Cloud Free)] hoặc [Ollama Llama 3 8B (Local Server)]. Thanh trượt cấu hình AI Temperature (0.1 - 0.5), thanh nhập kết nối ChromaDB Vector Store Port 8000. Nút 'Kiểm tra kết nối' và nút 'Lưu cấu hình AI'.")
    add_bullet("Quy tắc vận hành khẩn cấp:", "")
    add_p("  • Khi SysAdmin bấm nút 'Kill' trên một container runner bất thường: Hệ thống ngay lập tức gửi tín hiệu SIGKILL dừng container, ghi nhật ký kiểm toán vào System Logs và cập nhật bài nộp tương ứng sang trạng thái 'Bị gián đoạn' (Interrupted).")

    add_h2("7.3. Tiêu chí Nghiệm thu Giao diện Phiên bản 1 (Deliverables & KPIs)")
    add_bullet("Tiêu chí 1 - Tính bao quát nghiệp vụ: ", "Giao diện hiện thực hóa đầy đủ 100% các chức năng được mô tả trong 44 Use Cases (UC-01 đến UC-44).")
    add_bullet("Tiêu chí 2 - Tương thích thiết bị: ", "Giao diện hiển thị mượt mà trên trình duyệt hiện đại (Chrome, Edge, Firefox), hỗ trợ độ phân giải chuẩn từ Full HD (1920x1080) đến Laptop (1366x768).")
    add_bullet("Tiêu chí 3 - Trải nghiệm Web IDE: ", "Monaco Editor tải nhanh dưới 1.5 giây, tự động lưu nháp mượt mà không gây giật lag (autosave trơn tru), chế độ Read-only khóa cứng mã nguồn chuẩn xác từng mili-giây.")
    add_bullet("Tiêu chí 4 - Tính an toàn & Khách quan: ", "Sinh viên không thể gian lận xem trước Input/Output của Hidden Test Cases; giáo viên làm chủ hoàn toàn điểm số chính thức (Official Score).")
    add_bullet("Tiêu chí 5 - Hiệu năng Socratic AI: ", "Cửa sổ Drawer AI Tutor mở nhanh, câu trả lời sinh từ Gemini Flash phản hồi trong 1-2 giây, trích dẫn chính xác bài học cẩm nang RAG của nhà trường.")

    # Concluding Callout Box
    add_callout_box(
        "Tài liệu Đặc tả Yêu cầu Giao diện Phiên bản 1.0 này đã được chuẩn hóa toàn diện theo các tiêu chuẩn công nghệ phần mềm, "
        "bám sát 44 Use Cases nghiệp vụ, kiến trúc kỹ thuật FastAPI - Next.js 14 - Docker Sandbox - RAG ChromaDB, "
        "sẵn sàng làm tài liệu căn cứ chính thức phục vụ công tác thẩm định, báo cáo đồ án và kiểm thử trước Hội đồng Đánh giá.",
        title="KẾT LUẬN & CAM KẾT NGHIỆM THU",
        border_color="1F4E79",
        bg_color="F2F4F8"
    )

    # Save document
    output_filename = "d:\\CNTT2311\\HK9\\DOAN4\\ai-coding-tutor\\Bao_Cao_Dac_Ta_Yeu_Cau_Giao_Dien_AI_Tutor.docx"
    doc.save(output_filename)
    print(f"Document successfully created at: {output_filename}")

if __name__ == "__main__":
    create_document()
