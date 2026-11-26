# -*- coding: utf-8 -*-
"""
Full Presentation Builder for AI Coding Tutor Defense
Generates both:
1. Native widescreen PowerPoint (.pptx) with modern dark tech design (34 slides)
2. Interactive motion-animated Web Presentation (.html) with video-like transitions
"""

import os
import sys
from pathlib import Path
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

PPTX_PATH = REPORTS_DIR / "AI_Coding_Tutor_Thuyet_Trinh_Defense.pptx"
HTML_PATH = REPORTS_DIR / "AI_Coding_Tutor_Presentation.html"

# Color Palette (Modern Cyber-EdTech Dark Theme)
BG_DARK = RGBColor(11, 15, 25)        # #0B0F19
CARD_BG = RGBColor(26, 34, 52)        # #1A2234
CARD_BORDER = RGBColor(45, 58, 88)    # #2D3A58
TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
TEXT_BODY = RGBColor(203, 213, 225)   # #CBD5E1

CYAN = RGBColor(6, 182, 212)          # #06B6D4 (Primary Accent)
EMERALD = RGBColor(16, 185, 129)      # #10B981 (Success / Verified)
AMBER = RGBColor(245, 158, 11)        # #F59E0B (Highlight / Warning)
VIOLET = RGBColor(139, 92, 246)       # #8B5CF6 (AI / Innovation)
ROSE = RGBColor(244, 63, 94)          # #F43F5E (Alert / Challenge)


def create_base_slide(prs, category_text, title_text, slide_num, total_slides=34):
    """Creates a blank widescreen slide with unified dark background, header badges, and footer."""
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # 1. Background rectangle
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()

    # 2. Header Category Badge
    badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8.0), Inches(0.35))
    tf_badge = badge_box.text_frame
    tf_badge.word_wrap = True
    p_badge = tf_badge.paragraphs[0]
    p_badge.text = category_text.upper()
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = CYAN
    p_badge.font.name = "Segoe UI"

    # 3. Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.font.name = "Segoe UI"

    # 4. Footer & Slide Number
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.4))
    tf_footer = footer_box.text_frame
    p_footer = tf_footer.paragraphs[0]
    p_footer.text = f"AI-Powered Coding Tutor • Đồ án Tốt nghiệp CNTT 2026                    Trang {slide_num}/{total_slides}"
    p_footer.font.size = Pt(10)
    p_footer.font.color.rgb = TEXT_MUTED
    p_footer.font.name = "Segoe UI"

    return slide


def add_card(slide, left, top, width, height, title, items, accent_color=CYAN, badge=None):
    """Adds a modern styled card with title, optional badge, and bullet items."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BORDER
    card.line.width = Pt(1.5)

    # Accent top border strip
    accent_strip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.08))
    accent_strip.fill.solid()
    accent_strip.fill.fore_color.rgb = accent_color
    accent_strip.line.fill.background()

    # Content box inside card
    tx_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
    tf = tx_box.text_frame
    tf.word_wrap = True

    # Card Title
    p_title = tf.paragraphs[0]
    if badge:
        p_title.text = f"[{badge}] {title}"
    else:
        p_title.text = title
    p_title.font.size = Pt(15)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.font.name = "Segoe UI"
    p_title.space_after = Pt(8)

    # Items
    for item in items:
        p = tf.add_paragraph()
        p.text = f"• {item}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_BODY
        p.font.name = "Segoe UI"
        p.space_after = Pt(4)


def add_stat_card(slide, left, top, width, height, value, label, subtext, color=EMERALD):
    """Adds a large stat metric card for numbers (e.g. 100%, 5.230, 63/63)."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BORDER
    card.line.width = Pt(1.5)

    tx_box = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.15), width - Inches(0.3), height - Inches(0.3))
    tf = tx_box.text_frame
    tf.word_wrap = True

    p_val = tf.paragraphs[0]
    p_val.text = value
    p_val.font.size = Pt(32)
    p_val.font.bold = True
    p_val.font.color.rgb = color
    p_val.font.name = "Segoe UI"
    p_val.alignment = PP_ALIGN.CENTER

    p_lbl = tf.add_paragraph()
    p_lbl.text = label
    p_lbl.font.size = Pt(13)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = TEXT_WHITE
    p_lbl.font.name = "Segoe UI"
    p_lbl.alignment = PP_ALIGN.CENTER
    p_lbl.space_after = Pt(4)

    p_sub = tf.add_paragraph()
    p_sub.text = subtext
    p_sub.font.size = Pt(10)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.font.name = "Segoe UI"
    p_sub.alignment = PP_ALIGN.CENTER


def build_powerpoint():
    """Builds the 34-slide PowerPoint file."""
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    total_slides = 34

    # ==========================================
    # SLIDE 1: TITLE SLIDE (Trang bìa bảo vệ)
    # ==========================================
    blank_layout = prs.slide_layouts[6]
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.fill.background()

    # Title Card container
    t_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.0), Inches(10.333), Inches(5.5))
    t_card.fill.solid()
    t_card.fill.fore_color.rgb = CARD_BG
    t_card.line.color.rgb = CYAN
    t_card.line.width = Pt(2)

    tb1 = s1.shapes.add_textbox(Inches(2.0), Inches(1.4), Inches(9.333), Inches(4.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "BÁO CÁO THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN TỐT NGHIỆP"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.font.name = "Segoe UI"
    p0.alignment = PP_ALIGN.CENTER
    p0.space_after = Pt(14)

    p1 = tf1.add_paragraph()
    p1.text = "AI-POWERED CODING TUTOR"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.font.name = "Segoe UI"
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf1.add_paragraph()
    p2.text = "Hệ thống Trợ giảng Lập trình Thông minh ứng dụng RAG và AI Đa phương thức"
    p2.font.size = Pt(18)
    p2.font.color.rgb = EMERALD
    p2.font.name = "Segoe UI"
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(28)

    p3 = tf1.add_paragraph()
    p3.text = "Sinh viên thực hiện: Nhóm Đồ án Tốt nghiệp CNTT\nGiảng viên hướng dẫn: Hội đồng Đánh giá & Phản biện Đồ án\nChuyên ngành: Kỹ thuật Phần mềm & Trí tuệ Nhân tạo • Năm 2026"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.font.name = "Segoe UI"
    p3.alignment = PP_ALIGN.CENTER
    p3.space_after = Pt(20)

    p4 = tf1.add_paragraph()
    p4.text = "Gemini 3 Flash • Multimodal RAG • Socratic Method • ChromaDB • Docker Compose"
    p4.font.size = Pt(11)
    p4.font.bold = True
    p4.font.color.rgb = VIOLET
    p4.font.name = "Segoe UI"
    p4.alignment = PP_ALIGN.CENTER

    # ==========================================
    # SLIDE 2: AGENDA (Mục lục thuyết trình)
    # ==========================================
    s2 = create_base_slide(prs, "TỔNG QUAN", "Mục lục Báo cáo Thuyết trình (Agenda)", 2, total_slides)
    agenda_col1 = [
        "Phần 1: Tổng quan & Tính cấp thiết đề tài",
        "Phần 2: Mục tiêu & Đối tượng sử dụng hệ thống",
        "Phần 3: Nguyên lý & Điểm khác biệt so với AI khác",
        "Phần 4: Kiến trúc hệ thống & Biện luận công nghệ"
    ]
    agenda_col2 = [
        "Phần 5: Quy trình R&D 4 giai đoạn kỹ thuật",
        "Phần 6: Kết quả thực nghiệm & Kiểm chứng chất lượng",
        "Phần 7: Hiện trạng triển khai, Hạn chế & Lộ trình",
        "Phần 8: Kết luận & Đóng góp của đề tài"
    ]
    add_card(s2, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.5), "KHỐI 1: TỔNG QUAN & NGUYÊN LÝ", agenda_col1, CYAN, "MỤC 1 - 4")
    add_card(s2, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.5), "KHỐI 2: THỰC NGHIỆM & ĐÁNH GIÁ", agenda_col2, EMERALD, "MỤC 5 - 8")

    # ==========================================
    # SLIDE 3: BỐI CẢNH & KHÓ KHĂN CỦA SINH VIÊN
    # ==========================================
    s3 = create_base_slide(prs, "PHẦN 1 • TÍNH CẤP THIẾT", "Bối cảnh Đào tạo & Khó khăn khi Tự học Lập trình", 3, total_slides)
    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), "Độ dốc học tập lớn", [
        "Các môn cơ sở (C/C++, Python, CTDL&GT) mang tính quyết định tư duy.",
        "Nhiều khái niệm trừu tượng: con trỏ, heap/stack, cấp phát động, đệ quy.",
        "Khó hình dung luồng thực thi trong bộ nhớ khi mới bắt đầu."
    ], CYAN, "ĐẶC THÙ")
    add_card(s3, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.6), "Rào cản gỡ lỗi (Debugging)", [
        "Làm bài tập ở nhà lúc nửa đêm thường gặp lỗi runtime kinh điển.",
        "Lỗi vô hình: Segmentation Fault, Memory Leak, IndexError.",
        "Không có giảng viên hay trợ giảng túc trực để hỗ trợ tức thời."
    ], ROSE, "BẾ TẮC")
    add_card(s3, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.6), "Hệ quả đào tạo", [
        "Mất hàng giờ bế tắc trước các thông báo lỗi tiếng Anh trừu tượng.",
        "Dẫn đến tâm lý chán nản, sợ viết mã nguồn và ngại thực hành.",
        "Tỷ lệ rớt môn lập trình cơ sở tại các trường đại học luôn ở mức cao."
    ], AMBER, "HỆ LỤY")

    # ==========================================
    # SLIDE 4: THÁCH THỨC TỪ AI TẠO SINH (MỚM CODE)
    # ==========================================
    s4 = create_base_slide(prs, "PHẦN 1 • TÍNH CẤP THIẾT", "Mặt trái của AI Tạo sinh: Vấn đề 'Mớm Code / Giải Hộ'", 4, total_slides)
    add_card(s4, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Hành vi của ChatGPT / Copilot", [
        "Sinh viên gửi đề bài hoặc lỗi vào, AI viết lại 100% mã nguồn hoàn chỉnh.",
        "Đút sẵn code tận miệng thay vì hướng dẫn sinh viên tìm nguyên nhân.",
        "Tạo thói quen sao chép - dán (copy-paste) bài làm một cách thụ động.",
        "Người học không cần đọc lại tài liệu giáo trình hay suy ngẫm giải thuật."
    ], ROSE, "THỰC TRẠNG")
    add_card(s4, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Tác hại đối với Năng lực Sinh viên", [
        "Bài tập về nhà nộp đạt 10/10 điểm nhưng không hiểu bản chất thuật toán.",
        "Khi vào phòng thi viết giấy hoặc thi máy cô lập (không Internet) thì bị điểm liệt.",
        "Hoàn toàn mất đi phản xạ tư duy phản biện và kỹ năng tự debug.",
        "Giảng viên rơi vào thế bị động: Không cấm được AI nhưng cũng không kiểm soát được."
    ], AMBER, "HẬU QUẢ")

    # ==========================================
    # SLIDE 5: VẤN ĐỀ ẢO GIÁC & LỆCH CHUẨN GIÁO TRÌNH
    # ==========================================
    s5 = create_base_slide(prs, "PHẦN 1 • TÍNH CẤP THIẾT", "Thách thức về Tính Chính xác: Ảo giác & Lệch chuẩn Giáo trình", 5, total_slides)
    add_card(s5, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Hiện tượng Ảo giác & Cú pháp Lệch chuẩn", [
        "LLM thương mại học từ toàn bộ Internet mở, tiềm ẩn nhiều mã nguồn lỗi thời.",
        "Thường sinh cú pháp nâng cao ngoài phạm vi chuẩn đầu ra môn học.",
        "Ví dụ: Sinh viên năm nhất học con trỏ thô C++, AI lại sinh C++20 dùng std::unique_ptr.",
        "Dùng thư viện cấm trong kỳ thi, sinh viên mang đi chấm thi bị 0 điểm."
    ], ROSE, "LỆCH CHUẨN")
    add_card(s5, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Thiếu hụt Công cụ AI Sư phạm Chuẩn mực", [
        "Nhà trường không thể bài trừ AI, nhưng phải sống chung có kiểm soát.",
        "Cần một công cụ AI 'nói có sách, mách có chứng' neo chặt giáo trình chuẩn.",
        "Cần giải pháp buộc sinh viên tự tay sửa code dựa trên định hướng sư phạm.",
        "Cần tiếp nhận dữ liệu thực tế của sinh viên: file code và ảnh màn hình terminal."
    ], CYAN, "NHU CẦU ĐỀ TÀI")

    # ==========================================
    # SLIDE 6: MỤC TIÊU & ĐỊNH VỊ CỦA HỆ THỐNG
    # ==========================================
    s6 = create_base_slide(prs, "PHẦN 1 • TỔNG QUAN", "Mục tiêu và Định vị Giải pháp của AI Coding Tutor", 6, total_slides)
    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), "1. Phương pháp Socratic", [
        "Trợ giảng AI kiên nhẫn, không đưa mã nguồn hoàn chỉnh có sẵn.",
        "Phân tích hiện tượng lỗi, giải thích bản chất gốc rễ.",
        "Đặt câu hỏi gợi mở để người học tự tư duy và tự tay gõ lại code."
    ], EMERALD, "SƯ PHẠM")
    add_card(s6, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.6), "2. Multimodal RAG Grounding", [
        "Neo chặt ngữ cảnh vào 5.230 chunks giáo trình chính thống.",
        "Chống ảo giác (Hallucination) tuyệt đối trong phạm vi môn học.",
        "Hiển thị thẻ trích dẫn giáo trình minh bạch (tên sách, chương mục)."
    ], CYAN, "HỌC THUẬT")
    add_card(s6, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.6), "3. Tiếp nhận Đa phương thức", [
        "Xử lý đồng thời câu hỏi Text, File mã nguồn (.py, .cpp, .sql).",
        "Vision OCR đọc ảnh chụp màn hình Terminal báo lỗi font Monospace.",
        "Query Synthesizer chống pha loãng truy vấn RAG."
    ], VIOLET, "KỸ THUẬT")

    # ==========================================
    # SLIDE 7: PHẠM VI & ĐỐI TƯỢNG SỬ DỤNG
    # ==========================================
    s7 = create_base_slide(prs, "PHẦN 2 • PHẠM VI", "Đối tượng Sử dụng & Phạm vi Tri thức Hệ thống", 7, total_slides)
    add_card(s7, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Đối tượng Người dùng Hệ thống", [
        "Sinh viên CNTT năm 1 - 2: Đang học các môn lập trình nền tảng, cần trợ giảng 24/7.",
        "Giảng viên & Trợ giảng: Định hướng theo dõi các lỗi phổ biến mà sinh viên hay mắc phải.",
        "Khoa & Nhà trường: Triển khai nội bộ hỗ trợ giảng dạy theo chuẩn giáo trình."
    ], CYAN, "ĐỐI TƯỢNG")
    add_card(s7, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Phạm vi Ngữ liệu Giáo trình Hiện tại", [
        "Lập trình C / C++: Cú pháp, con trỏ, mảng động, quản lý bộ nhớ Heap/Stack.",
        "Lập trình Python: Cấu trúc dữ liệu built-in, OOP, ngoại lệ, cú pháp PEP 8.",
        "Cấu trúc dữ liệu & Giải thuật: Độ phức tạp Big-O, sắp xếp, tìm kiếm, đệ quy.",
        "Cơ sở dữ liệu & Toán rời rạc: Cú pháp SQL, quan hệ, suy diễn cấu trúc."
    ], EMERALD, "PHẠM VI TRI THỨC")

    # ==========================================
    # SLIDE 8: YÊU CẦU CHỨC NĂNG & PHI CHỨC NĂNG
    # ==========================================
    s8 = create_base_slide(prs, "PHẦN 2 • YÊU CẦU", "Bảng Yêu cầu Hệ thống (System Requirements)", 8, total_slides)
    add_card(s8, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Yêu cầu Chức năng (Functional)", [
        "Tiếp nhận đa phương thức: Text prompt, File code (.py, .cpp, .sql), Ảnh terminal.",
        "Vision OCR trích xuất chính xác Callstack và Exception name từ ảnh chụp.",
        "Query Synthesizer: Rút trích lỗi kỹ thuật, chống pha loãng truy vấn.",
        "RAG Retrieval: Truy xuất Top-K chunks giáo trình chính thống từ ChromaDB.",
        "Socratic Tutor: Sinh phản hồi gợi mở tư duy kèm thẻ trích dẫn giáo trình."
    ], CYAN, "CHỨC NĂNG")
    add_card(s8, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Yêu cầu Phi chức năng (Non-Functional)", [
        "Độ trễ truy xuất vector (Retrieval Latency): Dưới 0.2 giây (~160ms thực tế).",
        "An toàn dữ liệu: Chặn Path Traversal, chặn tệp binary giả mạo, kiểm tra bảng mã UTF-8.",
        "Độ sẵn sàng (Resilience): Cơ chế Multi-model Fallback khi gặp sự cố quota API.",
        "Kiến trúc bất đồng bộ (Asynchronous I/O): FastAPI xử lý nhiều kết nối đồng thời.",
        "Đóng gói chuẩn hóa: Docker Compose sẵn sàng triển khai trên máy chủ trường."
    ], EMERALD, "PHI CHỨC NĂNG")

    # ==========================================
    # SLIDE 9: SƠ ĐỒ USE CASE TỔNG QUAN
    # ==========================================
    s9 = create_base_slide(prs, "PHẦN 2 • USE CASE", "Sơ đồ Tương tác Use Case Tổng quan của Hệ thống", 9, total_slides)
    add_card(s9, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), "1. Đầu vào Sinh viên", [
        "Gửi câu hỏi lý thuyết hoặc thắc mắc cú pháp.",
        "Đính kèm tệp mã nguồn (.py, .cpp, .sql) đang viết dở.",
        "Tải ảnh chụp màn hình Terminal thông báo lỗi runtime."
    ], CYAN, "INPUT")
    add_card(s9, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.6), "2. Xử lý & Điều phối AI", [
        "FileExtractor bóc tách AST & ImageExtractor OCR ảnh.",
        "QuerySynthesizer tổng hợp truy vấn tinh gọn.",
        "ChromaDB tìm kiếm Top-3 chunks giáo trình qua RRF.",
        "Gemini 3 Flash áp dụng System Instruction Socratic."
    ], VIOLET, "PIPELINE")
    add_card(s9, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.6), "3. Kết quả Nhận được", [
        "Lời chào sư phạm & ghi nhận ngôn ngữ lập trình.",
        "Chỉ rõ vị trí sự cố và triệu chứng lỗi logic.",
        "Đặt câu hỏi gợi ý để người học tự kiểm tra điều kiện biên.",
        "Thẻ trích dẫn giáo trình (Tên sách, Chương, Mục) để tra cứu."
    ], EMERALD, "OUTPUT")

    # ==========================================
    # SLIDE 10: ĐIỂM KHÁC BIỆT CỐT LÕI
    # ==========================================
    s10 = create_base_slide(prs, "PHẦN 3 • SO SÁNH", "Điểm khác biệt Cốt lõi: AI Coding Tutor vs Công cụ Hiện có", 10, total_slides)
    add_card(s10, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "ChatGPT / GitHub Copilot", [
        "Mục đích: Viết code nhanh cho lập trình viên đi làm.",
        "Giải bài hộ: Đút sẵn code sửa lỗi hoàn chỉnh -> Triệt tiêu tư duy tự học.",
        "Tri thức mở: Dễ sinh cú pháp vượt rào, sai barem thi của khoa.",
        "Pha loãng ngữ cảnh: Nạp code dài + ảnh dễ bị bỏ sót lỗi chính.",
        "Không có kiểm chứng: Không có thẻ trích dẫn sách giáo trình."
    ], ROSE, "AI THƯƠNG MẠI")
    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Hệ thống AI Coding Tutor", [
        "Mục đích: Trợ giảng sư phạm chuyên biệt cho giáo dục đại học.",
        "Phương pháp Socratic: Chỉ ra bản chất lỗi, gợi mở để sinh viên tự sửa.",
        "Tri thức chuẩn hóa: Neo chặt 5.230 chunks giáo trình chính thống.",
        "Query Synthesizer: Rút trích exception name chống loãng truy vấn.",
        "Minh bạch học thuật: Hiển thị thẻ trích dẫn rõ tên sách, chương, đoạn."
    ], EMERALD, "AI CODING TUTOR")

    # ==========================================
    # SLIDE 11: MA TRẬN ĐỐI SOÁT CHI TIẾT
    # ==========================================
    s11 = create_base_slide(prs, "PHẦN 3 • SO SÁNH", "Ma trận Đối soát Tiêu chí Kỹ thuật và Sư phạm", 11, total_slides)
    add_card(s11, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), "Tiêu chí Sư phạm", [
        "ChatGPT: Mớm bài, làm hộ 100%.",
        "Copilot: Tự gõ code tiếp theo.",
        "AI Coding Tutor: Socratic Method - Bắt buộc sinh viên tự tay gõ lại code."
    ], CYAN, "PHƯƠNG PHÁP")
    add_card(s11, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.6), "Tiêu chí Kiến thức & Đối soát", [
        "ChatGPT: Toàn bộ Internet (dễ ảo giác).",
        "Copilot: GitHub public code.",
        "AI Coding Tutor: Kho giáo trình đại học chính thống (100% Hit@3 canonical)."
    ], EMERALD, "NGUỒN GỐC")
    add_card(s11, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.6), "Tiêu chí Chi phí & Quản lý", [
        "ChatGPT: Phải mua Plus $20/tháng.",
        "Copilot: Bản quyền $10/tháng.",
        "AI Coding Tutor: Kiến trúc tối ưu, Vector DB chạy local, Docker On-Premise."
    ], AMBER, "TRIỂN KHAI")

    # ==========================================
    # SLIDE 12: PHƯƠNG PHÁP SƯ PHẠM SOCRATIC
    # ==========================================
    s12 = create_base_slide(prs, "PHẦN 3 • SOCRATIC", "Phương pháp Sư phạm Socratic: Quy trình 4 Bước Gợi mở", 12, total_slides)
    add_card(s12, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.6), "Bước 1: Ghi nhận", [
        "Chào hỏi ân cần, ghi nhận ngôn ngữ lập trình của sinh viên.",
        "Xác định vị trí phát sinh sự cố (dòng lệnh, vòng lặp, con trỏ)."
    ], CYAN, "BƯỚC 1")
    add_card(s12, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.6), "Bước 2: Chỉ điểm", [
        "Mô tả hiện tượng và triệu chứng lỗi logic.",
        "Ví dụ: Vượt ngoài biên mảng, con trỏ bị treo, rò rỉ bộ nhớ."
    ], AMBER, "BƯỚC 2")
    add_card(s12, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.6), "Bước 3: Gợi mở", [
        "Đặt 1-2 câu hỏi dẫn dắt trọng tâm.",
        "Gợi ý sinh viên kiểm tra điều kiện biên hoặc đặt print/debugger."
    ], VIOLET, "BƯỚC 3")
    add_card(s12, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.6), "Bước 4: Đối chiếu", [
        "Dẫn trích đoạn giáo trình chuẩn RAG.",
        "Để sinh viên tự đọc hiểu nguyên lý và tự sửa mã nguồn."
    ], EMERALD, "BƯỚC 4")

    # ==========================================
    # SLIDE 13: KIẾN TRÚC PHÂN TẦNG TỔNG THỂ
    # ==========================================
    s13 = create_base_slide(prs, "PHẦN 4 • KIẾN TRÚC", "Kiến trúc Phân tầng Tổng thể Hệ thống (Layered Architecture)", 13, total_slides)
    add_card(s13, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.6), "Tầng 1: Presentation", [
        "Next.js 14 App Router.",
        "TypeScript + Tailwind CSS.",
        "Chat đa phương thức: Text, Upload Code, Upload Ảnh.",
        "Hiển thị Markdown & Thẻ Citations."
    ], CYAN, "TẦNG 1")
    add_card(s13, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.6), "Tầng 2: Backend & AI", [
        "FastAPI (Python 3.11 Async).",
        "FileExtractor bóc tách an toàn.",
        "ImageExtractor Vision OCR.",
        "QuerySynthesizer chống loãng.",
        "TutorService điều phối RAG."
    ], EMERALD, "TẦNG 2")
    add_card(s13, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.6), "Tầng 3: Data & Vector", [
        "ChromaDB Persistent (Local).",
        "Dual Collections (5.230 vectors):",
        "• qwen3_text (4.293 chunks 1024-d)",
        "• jina_code (937 chunks 768-d)",
        "Thuật toán RRF k0=60."
    ], VIOLET, "TẦNG 3")
    add_card(s13, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.6), "Tầng 4: LLM Inference", [
        "Mô hình chính: Gemini 3 Flash.",
        "Multi-model Fallback:",
        "Gemini 3 Flash -> 3.5 Flash",
        "-> Socratic Fallback nội bộ.",
        "Độ trễ phản hồi < 2s."
    ], AMBER, "TẦNG 4")

    # ==========================================
    # SLIDE 14: BIỆN LUẬN CÔNG NGHỆ 1 (MINERU)
    # ==========================================
    s14 = create_base_slide(prs, "PHẦN 4 • CÔNG NGHỆ", "Biện luận Công nghệ: Bộ Bóc tách Bố cục PDF (MinerU vs PyPDF)", 14, total_slides)
    add_card(s14, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Hạn chế của PyPDF / PDFPlumber", [
        "Chỉ quét text thô theo tọa độ x-y cơ học.",
        "Làm vỡ các khối mã nguồn đa dòng, mất thụt lề (indentation) của Python.",
        "Làm biến dạng bảng biểu phân tích độ phức tạp thuật toán.",
        "Mất toàn bộ ký hiệu công thức toán học LaTeX."
    ], ROSE, "CÔNG NGHỆ CŨ")
    add_card(s14, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Ưu thế Vượt trội của MinerU (Layout-LM)", [
        "Sử dụng mô hình thị giác AI chuyên dụng nhận diện layout trang.",
        "Bảo toàn 100% ranh giới khối code block, ký tự trắng và dấu thụt lề.",
        "Chuyển đổi công thức toán phức tạp sang cú pháp LaTeX chuẩn.",
        "Xuất Markdown đồng nhất bảng mã UTF-8 phục vụ pipeline chunking."
    ], EMERALD, "LỰA CHỌN MINERU")

    # ==========================================
    # SLIDE 15: BIỆN LUẬN CÔNG NGHỆ 2 (CHROMADB)
    # ==========================================
    s15 = create_base_slide(prs, "PHẦN 4 • CÔNG NGHỆ", "Biện luận Công nghệ: Cơ sở Dữ liệu Vector (ChromaDB)", 15, total_slides)
    add_card(s15, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Nhược điểm của Cloud Vector DB (Pinecone/Milvus)", [
        "Pinecone: Đắt đỏ, tính phí định kỳ, phụ thuộc hoàn toàn vào cloud nước ngoài.",
        "Milvus Cluster: Quá cồng kềnh, tiêu tốn 8-16GB RAM, khó triển khai gọn nhẹ.",
        "Độ trễ mạng Internet cao, nguy cơ vi phạm bảo mật dữ liệu nội bộ."
    ], ROSE, "GIẢI PHÁP THAY THẾ")
    add_card(s15, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Ưu thế của ChromaDB Local Persistent", [
        "Mã nguồn mở hoàn toàn, nhúng trực tiếp hoặc chạy container siêu nhẹ (<300MB RAM).",
        "Tốc độ truy xuất cục bộ cực nhanh: ~160 ms / query với 5.230 vectors.",
        "Hỗ trợ Metadata Filtering linh hoạt theo ngôn ngữ, tài liệu, chương mục.",
        "Dữ liệu vector lưu trữ an toàn trong máy chủ trường, không mất phí định kỳ."
    ], EMERALD, "LỰA CHỌN CHROMADB")

    # ==========================================
    # SLIDE 16: BIỆN LUẬN CÔNG NGHỆ 3 (DUAL EMBEDDING & RRF)
    # ==========================================
    s16 = create_base_slide(prs, "PHẦN 4 • CÔNG NGHỆ", "Biện luận Công nghệ: Kiến trúc Nhúng kép Dual-Collection & RRF", 16, total_slides)
    add_card(s16, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Kiến trúc Dual Collections", [
        "qwen3_text (4.293 chunks): Dùng Qwen/Qwen3-Embedding-0.6B (1024 chiều) chuyên trách lý thuyết.",
        "jina_code (937 chunks): Dùng jinaai/jina-embeddings-v2-base-code (768 chiều) chuyên trách mã nguồn.",
        "Lý do: Tách biệt không gian vector giúp tăng độ khớp chính xác cho từng loại câu hỏi."
    ], CYAN, "DUAL EMBEDDING")
    add_card(s16, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Thuật toán Hợp nhất RRF (k0 = 60)", [
        "Reciprocal Rank Fusion (RRF) kết hợp xếp hạng từ cả 2 collection:",
        "RRF(d) = 1/(60 + r_text(d)) + 1/(60 + r_code(d))",
        "Ưu điểm: Không bị ảnh hưởng bởi độ lệch thang đo khoảng cách giữa 2 model khác nhau.",
        "Đảm bảo tài liệu được cả 2 mô hình đánh giá cao luôn đứng đầu danh sách."
    ], VIOLET, "HỢP NHẤT XẾP HẠNG")

    # ==========================================
    # SLIDE 17: BIỆN LUẬN CÔNG NGHỆ 4 (LLM & FALLBACK)
    # ==========================================
    s17 = create_base_slide(prs, "PHẦN 4 • CÔNG NGHỆ", "Biện luận Công nghệ: LLM Inference & Cơ chế Tự phục hồi", 17, total_slides)
    add_card(s17, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Tại sao chọn Gemini 3 Flash?", [
        "Tốc độ suy luận siêu tốc: Thời gian phản hồi dưới 2 giây, hỗ trợ Streaming.",
        "Vision OCR bản địa xuất sắc: Nhận diện rõ font Monospace trên ảnh terminal.",
        "Cửa sổ ngữ cảnh khổng lồ 1 triệu tokens: Nạp thoải mái cả code lớn và RAG chunks.",
        "Chi phí token tối ưu: Rẻ hơn 90% so với GPT-4o, phù hợp triển khai giáo dục."
    ], CYAN, "GEMINI 3 FLASH")
    add_card(s17, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Cơ chế Tự phục hồi Đa tầng (Multi-Model Resilience)", [
        "Xử lý triệt để nguy cơ gián đoạn do sự cố mạng hoặc quota API:",
        "1. Ưu tiên số 1: gemini-3-flash-preview.",
        "2. Tự động chuyển mạch 2: gemini-3.5-flash.",
        "3. Fallback nội bộ: Socratic Fallback Engine tự sinh gợi ý từ RAG chunks.",
        "Đảm bảo hệ thống duy trì hoạt động 24/7 không bao giờ sập trước sinh viên."
    ], EMERALD, "RESILIENCE")

    # ==========================================
    # SLIDE 18: MÔ HÌNH HYBRID & BẢO MẬT DỮ LIỆU
    # ==========================================
    s18 = create_base_slide(prs, "PHẦN 4 • BẢO MẬT", "Mô hình Triển khai Hybrid & An toàn Dữ liệu Thực tế", 18, total_slides)
    add_card(s18, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Thành phần Chạy On-Premise Cục bộ", [
        "Vector Database ChromaDB (5.230 vectors) lưu trữ 100% trên ổ cứng local.",
        "Pipeline bóc tách FileExtractor & tiền xử lý ImageExtractor chạy nội bộ.",
        "Module QuerySynthesizer chống loãng truy vấn chạy cục bộ.",
        "Backend FastAPI & Frontend Next.js đóng gói qua Docker Compose."
    ], EMERALD, "LOCAL ON-PREMISE")
    add_card(s18, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Thành phần Cloud API & Đánh giá Khách quan", [
        "Bước sinh phản hồi Socratic cuối cùng gọi qua Google Gemini API.",
        "Đánh giá khách quan: Chưa phải Air-gapped 100% vì prompt và code gửi lên cloud.",
        "Định hướng bảo mật tuyệt đối cho đề thi: Thay thế Gemini API bằng mô hình mã nguồn mở chạy local (Qwen2.5-Coder qua vLLM / Ollama)."
    ], AMBER, "CLOUD & ROADMAP")

    # ==========================================
    # SLIDE 19: QUY TRÌNH R&D 4 GIAI ĐOẠN TỔNG QUAN
    # ==========================================
    s19 = create_base_slide(prs, "PHẦN 5 • QUY TRÌNH", "Quy trình Nghiên cứu & Phát triển (R&D) 4 Giai đoạn", 19, total_slides)
    add_card(s19, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.6), "Giai đoạn 1 (Ngày 1-4)", [
        "Thu thập giáo trình chuẩn.",
        "MinerU Layout Parsing.",
        "Pipeline làm sạch V3.0.",
        "AST-aware Chunking & Contextual Retrieval."
    ], CYAN, "DỮ LIỆU SOTA")
    add_card(s19, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.6), "Giai đoạn 2 (Ngày 5-7)", [
        "Dual-Embedding GPU.",
        "Ingestion 5.230 chunks vào ChromaDB.",
        "Kiểm định Benchmark 20 câu canonical 100% Hit@3.",
        "Đóng gói RAGService."
    ], EMERALD, "VECTOR & BENCHMARK")
    add_card(s19, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.6), "Giai đoạn 3 (Ngày 8-10)", [
        "FileExtractor an toàn.",
        "ImageExtractor Vision OCR.",
        "QuerySynthesizer chống pha loãng truy vấn.",
        "Unified Payload hợp nhất."
    ], VIOLET, "MULTIMODAL")
    add_card(s19, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.6), "Giai đoạn 4 (Ngày 11-14)", [
        "System Prompt Socratic.",
        "Multi-model Fallback.",
        "63 Pytests đạt 100%.",
        "Đóng gói Docker Compose & Quickstart guide."
    ], AMBER, "SOCRATIC & DEPLOY")

    # ==========================================
    # SLIDE 20: GIAI ĐOẠN 1 (MINERU & CHUNKING)
    # ==========================================
    s20 = create_base_slide(prs, "PHẦN 5 • GIAI ĐOẠN 1", "Giai đoạn 1: Bóc tách Tài liệu SOTA & Chunking Ngữ cảnh", 20, total_slides)
    add_card(s20, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), "1. Bóc tách MinerU", [
        "Chuyển đổi toàn bộ PDF giáo trình sang Markdown chuẩn.",
        "Bảo toàn cấu trúc phân cấp tiêu đề, ranh giới code block và công thức toán.",
        "Loại bỏ hoàn toàn lỗi gãy dòng thụt lề của công cụ cũ."
    ], CYAN, "PARSING SOTA")
    add_card(s20, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.6), "2. Làm sạch Đa tầng V3.0", [
        "Bộ lọc Regex khử số trang thừa, header/footer lặp lại.",
        "Sửa lỗi ngắt dòng bất thường trong khối lệnh code.",
        "Chuẩn hóa đồng nhất định dạng Markdown và bảng mã UTF-8."
    ], EMERALD, "CLEANING")
    add_card(s20, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.6), "3. Contextual Chunking", [
        "Cắt đoạn theo ranh giới hàm/lớp (AST-aware) thay vì cắt cơ học theo số ký tự.",
        "Gắn bối cảnh chương mục cấp cao vào đầu mỗi chunk.",
        "Giải quyết triệt để vấn đề mất ngữ cảnh khi tìm kiếm vector."
    ], VIOLET, "CHUNKING")

    # ==========================================
    # SLIDE 21: GIAI ĐOẠN 2 (VECTOR DB & BENCHMARK)
    # ==========================================
    s21 = create_base_slide(prs, "PHẦN 5 • GIAI ĐOẠN 2", "Giai đoạn 2: Vector hóa Dual-Collection & Kiểm định Benchmark", 21, total_slides)
    add_stat_card(s21, Inches(0.8), Inches(1.8), Inches(3.6), Inches(2.2), "5.230", "Tổng Chunks Vector", "Lưu trữ tại data/09_chromadb", CYAN)
    add_stat_card(s21, Inches(4.8), Inches(1.8), Inches(3.6), Inches(2.2), "4.293", "qwen3_text (1024-d)", "Chunks văn bản lý thuyết", EMERALD)
    add_stat_card(s21, Inches(8.8), Inches(1.8), Inches(3.6), Inches(2.2), "937", "jina_code (768-d)", "Chunks mã nguồn & giải thuật", VIOLET)
    add_card(s21, Inches(0.8), Inches(4.3), Inches(11.6), Inches(2.2), "Đóng gói RAGService & Bộ đệm Benchmark Embeddings", [
        "Xây dựng dịch vụ RAGService hỗ trợ truy vấn song song Dual-Collection kết hợp thuật toán RRF k0=60.",
        "Nạp sẵn bộ đệm 36 benchmark query embeddings (benchmark_36q_query_embeddings.json) tăng tốc truy vấn.",
        "Tích hợp tự động nhận diện ngôn ngữ lập trình từ câu hỏi và mở rộng truy vấn (Query Expansion)."
    ], CYAN, "RAG SERVICE")

    # ==========================================
    # SLIDE 22: GIAI ĐOẠN 3 (MULTIMODAL EXTRACTORS)
    # ==========================================
    s22 = create_base_slide(prs, "PHẦN 5 • GIAI ĐOẠN 3", "Giai đoạn 3: Xây dựng Pipeline Đa phương thức An toàn", 22, total_slides)
    add_card(s22, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "FileExtractor Engine", [
        "Tiếp nhận và bóc tách mã nguồn đa ngôn ngữ: .py, .cpp, .sql, .java.",
        "Cơ chế phòng thủ an ninh nghiêm ngặt:",
        "• Chặn tấn công duyệt thư mục (Path Traversal, '..', null bytes).",
        "• Chặn tệp nhị phân độc hại giả mạo mã nguồn (Magic byte inspection).",
        "• Giới hạn kích thước tối đa 5MB và xác thực bảng mã UTF-8."
    ], CYAN, "BÓC TÁCH CODE")
    add_card(s22, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "ImageExtractor Engine (Vision OCR)", [
        "Xử lý ảnh chụp màn hình máy tính hoặc điện thoại.",
        "Tiền xử lý ảnh: Chuẩn hóa kích thước tối đa 1600px, tăng cường độ tương phản.",
        "Vision OCR chuyên biệt: Trích xuất chính xác font chữ đơn cách (Monospace).",
        "Bóc tách nguyên vẹn các dòng mã nguồn và thông báo lỗi / Callstack terminal."
    ], VIOLET, "VISION OCR")

    # ==========================================
    # SLIDE 23: QUERY SYNTHESIZER CHỐNG PHA LOÃNG
    # ==========================================
    s23 = create_base_slide(prs, "PHẦN 5 • GIAI ĐOẠN 3", "Đột phá Kỹ thuật: Query Synthesizer (Chống Pha loãng Truy vấn)", 23, total_slides)
    add_card(s23, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Vấn đề Pha loãng Truy vấn (Query Dilution)", [
        "Khi sinh viên gửi đồng thời câu hỏi + file code 200 dòng + ảnh terminal lỗi.",
        "Nếu nhồi toàn bộ văn bản vào vector search, truy vấn sẽ bị nhiễu nghiêm trọng.",
        "Các đường dẫn thư mục dài, dòng log hệ thống và mã phụ làm lệch vector tìm kiếm.",
        "Hậu quả: RAG tìm ra các bài giảng không liên quan đến lỗi cốt lõi."
    ], ROSE, "THÁCH THỨC")
    add_card(s23, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Giải pháp của Query Synthesizer", [
        "Thuật toán bóc tách trọng tâm thông minh:",
        "1. Tách chính xác Tên ngoại lệ (Exception Name: IndexError, Memory Leak, v.v.).",
        "2. Tách vị trí dòng lỗi và hàm logic bị sai từ tệp nguồn.",
        "3. Tổng hợp thành một câu truy vấn kỹ thuật tinh gọn trước khi gọi ChromaDB.",
        "Kết quả: RAG tìm trúng 100% bài giảng lý thuyết liên quan mà không bị nhiễu."
    ], EMERALD, "GIẢI PHÁP ĐỘT PHÁ")

    # ==========================================
    # SLIDE 24: GIAI ĐOẠN 4 (SOCRATIC & DOCKER)
    # ==========================================
    s24 = create_base_slide(prs, "PHẦN 5 • GIAI ĐOẠN 4", "Giai đoạn 4: Tích hợp Socratic Engine & Đóng gói Docker", 24, total_slides)
    add_card(s24, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "System Instruction Socratic Chuẩn mực", [
        "Cấu hình hành vi sư phạm nghiêm ngặt cho mô hình Gemini 3 Flash:",
        "• Bắt buộc neo chặt vào tài liệu giáo trình chính thống từ RAG.",
        "• Tuyệt đối không sinh mã nguồn hoàn chỉnh sửa hộ cho sinh viên.",
        "• Áp dụng quy trình 4 bước sư phạm: Ghi nhận -> Chỉ điểm -> Gợi mở -> Đối chiếu.",
        "• Luôn đính kèm thẻ trích dẫn giáo trình rõ ràng."
    ], EMERALD, "SOCRATIC ENGINE")
    add_card(s24, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Đóng gói Triển khai Docker Compose", [
        "Chuẩn hóa tệp docker-compose.yml tích hợp trọn gói:",
        "• Backend FastAPI + Volume dữ liệu ./data:/app/data.",
        "• Cơ sở dữ liệu Vector ChromaDB Persistent vận hành cục bộ.",
        "• Frontend Next.js giao diện sinh viên.",
        "Khởi chạy 1-click qua start_dev.bat hoặc docker compose up -d."
    ], CYAN, "DOCKERIZATION")

    # ==========================================
    # SLIDE 25: KẾT QUẢ ĐO LƯỜNG RETRIEVAL
    # ==========================================
    s25 = create_base_slide(prs, "PHẦN 6 • KẾT QUẢ", "Kết quả Thực nghiệm 1: Đo lường Chất lượng RAG Retrieval", 25, total_slides)
    add_stat_card(s25, Inches(0.8), Inches(1.8), Inches(2.7), Inches(2.2), "100%", "Hit Rate@3", "20/20 câu hỏi canonical", EMERALD)
    add_stat_card(s25, Inches(3.8), Inches(1.8), Inches(2.7), Inches(2.2), "80.0%", "Hit Rate@1", "16/20 câu đúng ở vị trí 1", CYAN)
    add_stat_card(s25, Inches(6.8), Inches(1.8), Inches(2.7), Inches(2.2), "0.8833", "MRR@5 Score", "Chỉ số nghịch đảo thứ hạng", VIOLET)
    add_stat_card(s25, Inches(9.8), Inches(1.8), Inches(2.7), Inches(2.2), "~160 ms", "Độ trễ trung bình", "Thời gian truy xuất local", AMBER)
    add_card(s25, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.2), "Phân bổ 20 Câu hỏi Kiểm định Canonical theo 4 Nhóm Năng lực", [
        "theory (5 câu): Khái niệm OOP, Clean code PEP 8, Mutable vs Immutable, Big-O QuickSort, Encapsulation.",
        "code (5 câu): QuickSort đệ quy, List Comprehension 2D, Fibonacci memoization, Stack/Queue deque, with open.",
        "api (5 câu): any() generator, sqlite3.execute, json.loads vs load, collections.defaultdict, typing.Union.",
        "hybrid (5 câu): __init__ constructor, Kế thừa super(), Ngoại lệ try-except, Context Manager __enter__/__exit__."
    ], CYAN, "BENCHMARK ĐỐI SOÁT KHẮT KHE")

    # ==========================================
    # SLIDE 26: KẾT QUẢ KIỂM THỬ PYTEST 63/63
    # ==========================================
    s26 = create_base_slide(prs, "PHẦN 6 • KẾT QUẢ", "Kết quả Thực nghiệm 2: Bộ Kiểm thử Tự động Pytest (63/63 Tests)", 26, total_slides)
    add_stat_card(s26, Inches(1.0), Inches(1.8), Inches(5.4), Inches(2.2), "33 / 33", "Unit Tests PASSED", "Thời gian chạy: 4.09 giây (100%)", EMERALD)
    add_stat_card(s26, Inches(6.8), Inches(1.8), Inches(5.4), Inches(2.2), "30 / 30", "E2E Scenarios PASSED", "Thời gian chạy: 30.53 giây (100%)", CYAN)
    add_card(s26, Inches(1.0), Inches(4.3), Inches(11.2), Inches(2.2), "Tổng số: 63 / 63 Kiểm thử Đạt 100% qua Pytest Tự động", [
        "33 Unit Tests: Kiểm tra khởi tạo ChromaDB, tìm kiếm RRF, bóc tách đa ngôn ngữ, lọc file binary, kiểm tra kích thước ảnh, OCR mockup, QuerySynthesizer rút trích lỗi và chống loãng truy vấn.",
        "30 Kịch bản E2E thực tế: 10 câu hỏi lý thuyết thuật toán + 10 tệp mã nguồn lỗi (Memory leak, đệ quy vô hạn, SQL injection, off-by-one) + 10 ảnh terminal OCR (IndexError, ZeroDivisionError, v.v.)."
    ], EMERALD, "AUTOMATED TESTING BẢO CHỨNG CHẤT LƯỢNG")

    # ==========================================
    # SLIDE 27: DEMO THỰC TẾ 1 (QUICKSORT)
    # ==========================================
    s27 = create_base_slide(prs, "PHẦN 6 • DEMO", "Demo Thực tế Kịch bản 1: Câu hỏi Lý thuyết QuickSort O(n^2)", 27, total_slides)
    add_card(s27, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Đầu vào của Sinh viên", [
        "Câu hỏi Text: 'Tại sao thuật toán QuickSort có trường hợp xấu nhất là O(n^2) và trong thực tế người ta khắc phục điều này như thế nào?'",
        "Phương thức: Text-only Chat qua API /tutor/chat.",
        "Ngôn ngữ tự động nhận diện: Cấu trúc dữ liệu & Thuật toán."
    ], CYAN, "INPUT")
    add_card(s27, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Phản hồi Chuẩn mực từ Hệ thống", [
        "RAG Retrieval: Truy xuất chính xác mục Phân hoạch trong Giáo trình CTDL&GT.",
        "Giải thích bản chất: Phân tích hiện tượng chọn phần tử chốt (Pivot) lệch khi mảng đã sắp xếp sẵn dẫn đến cây đệ quy suy biến thành O(n^2).",
        "Gợi ý Socratic: Hướng dẫn tìm hiểu kỹ thuật chọn chốt trung vị của 3 phần tử (Median-of-Three) và kỹ thuật phân hoạch ngẫu nhiên.",
        "Thẻ trích dẫn: [Giáo trình CTDL&GT | Chương: Sắp xếp phân hoạch]."
    ], EMERALD, "OUTPUT SOCRATIC")

    # ==========================================
    # SLIDE 28: DEMO THỰC TẾ 2 (MEMORY LEAK C++)
    # ==========================================
    s28 = create_base_slide(prs, "PHẦN 6 • DEMO", "Demo Thực tế Kịch bản 2: Bắt lỗi Rò rỉ Bộ nhớ Con trỏ C++", 28, total_slides)
    add_card(s28, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Đầu vào Tệp Mã nguồn (leak.cpp)", [
        "Sinh viên nộp tệp C++ cấp phát mảng động new int[100] nhưng không giải phóng:",
        "void processData() {",
        "    int* arr = new int[100];",
        "    for(int i = 0; i < 100; i++) arr[i] = i * 2;",
        "    // Quên delete[] arr;",
        "}",
        "Câu hỏi kèm: 'Hàm này của em chạy ổn không ạ?'"
    ], CYAN, "CODE ATTACHMENT")
    add_card(s28, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Phản hồi Socratic Định hướng", [
        "FileExtractor bóc tách hàm processData() phát hiện lệnh new nhưng thiếu delete[].",
        "AI KHÔNG viết code hộ, mà đặt câu hỏi:",
        "'Bạn hãy quan sát vùng nhớ Heap cấp phát bằng new int[100] ở dòng 5. Khi hàm kết thúc, vùng nhớ này đã được thu hồi chưa? Nếu lặp lại 1.000 lần thì điều gì xảy ra?'",
        "Thẻ trích dẫn: [Giáo trình C++ | Chương 4: Con trỏ và Quản lý bộ nhớ Heap]."
    ], EMERALD, "OUTPUT SOCRATIC")

    # ==========================================
    # SLIDE 29: DEMO THỰC TẾ 3 (TERMINAL OCR)
    # ==========================================
    s29 = create_base_slide(prs, "PHẦN 6 • DEMO", "Demo Thực tế Kịch bản 3: Xử lý Ảnh Terminal OCR (IndexError)", 29, total_slides)
    add_card(s29, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Đầu vào Ảnh chụp Màn hình Terminal", [
        "Sinh viên gửi ảnh chụp terminal báo lỗi Python:",
        "File 'solution.py', line 14:",
        "  for i in range(len(arr) + 1):",
        "      print(arr[i])",
        "IndexError: list index out of range",
        "Ảnh có độ phân giải thực tế chụp từ máy tính."
    ], CYAN, "TERMINAL SCREENSHOT")
    add_card(s29, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Xử lý OCR & Phản hồi Socratic", [
        "Vision OCR đọc chính xác Exception Name và dòng lệnh for i in range(len(arr)+1).",
        "QuerySynthesizer trích xuất từ khóa IndexError và điều kiện biên.",
        "Phản hồi Socratic:",
        "'Trong Python chỉ số mảng bắt đầu từ 0 đến len(arr)-1. Khi bạn duyệt tới len(arr)+1 thì điều gì sẽ xảy ra ở phần tử cuối cùng?'",
        "Thẻ trích dẫn: [Giáo trình Python | Kiểu dữ liệu danh sách List]."
    ], EMERALD, "OUTPUT SOCRATIC")

    # ==========================================
    # SLIDE 30: TRẠNG THÁI TRIỂN KHAI TÍNH NĂNG
    # ==========================================
    s30 = create_base_slide(prs, "PHẦN 7 • HIỆN TRẠNG", "Bảng Phân loại Trạng thái Triển khai Tính năng Thực tế", 30, total_slides)
    add_card(s30, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), "Đã Hoàn thành (100% Verified)", [
        "• Multimodal RAG Engine (5.230 chunks vector, Dual RRF).",
        "• Socratic Prompting & Gemini 3 Flash.",
        "• FileExtractor & ImageExtractor OCR.",
        "• QuerySynthesizer chống pha loãng.",
        "• 63/63 Pytests kiểm thử tự động.",
        "• Đóng gói Docker Compose & Giao diện Chat."
    ], EMERALD, "HOÀN THÀNH")
    add_card(s30, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.6), "Đang Phát triển (UI Prototype)", [
        "• Instructor Dashboard: Giao diện mẫu React quản lý bài tập & điểm số.",
        "• Classroom Error Heatmap: Bản đồ nhiệt hiển thị demo, Backend chưa có schema PostgreSQL lưu trữ log lỗi.",
        "• Đang ở giai đoạn hoàn thiện tầng dữ liệu."
    ], AMBER, "UI PROTOTYPE")
    add_card(s30, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.6), "Định hướng Tương lai (Roadmap)", [
        "• Khóa tài liệu theo tuần học (bổ sung trường syllabus_week vào metadata).",
        "• Backend Code Execution Sandbox (môi trường container chạy thử mã nguồn an toàn).",
        "• Xác thực người dùng JWT & Phân quyền RBAC (Student, Lecturer, Admin)."
    ], CYAN, "ROADMAP")

    # ==========================================
    # SLIDE 31: ĐÁNH GIÁ CÁC HẠN CHẾ KỸ THUẬT
    # ==========================================
    s31 = create_base_slide(prs, "PHẦN 7 • HẠN CHẾ", "Đánh giá Khách quan: Các Hạn chế Kỹ thuật Hiện tại", 31, total_slides)
    add_card(s31, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Hạn chế về Kiến trúc & Dữ liệu", [
        "1. Phụ thuộc vào Cloud API (Gemini): Mặc dù RAG và tiền xử lý chạy local, bước sinh phản hồi vẫn gọi cloud, chưa phải air-gapped 100%.",
        "2. Phạm vi ngữ liệu: Mới tập trung vào 4 môn lập trình cơ sở của 2 năm đầu, chưa mở rộng ra toàn bộ chương trình chuyên ngành."
    ], AMBER, "KIẾN TRÚC & DỮ LIỆU")
    add_card(s31, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Hạn chế về Tính năng & OCR", [
        "3. Chất lượng OCR đối với ảnh chụp điện thoại: Ảnh nghiêng góc 3D, lóa đèn có thể giảm độ chính xác đọc ký tự đặc biệt.",
        "4. Chưa có Sandbox chạy code trực tiếp: Hệ thống phân tích lỗi dựa trên AST và LLM tĩnh, chưa biên dịch và thực thi code thực tế."
    ], ROSE, "TÍNH NĂNG & OCR")

    # ==========================================
    # SLIDE 32: LỘ TRÌNH PHÁT TRIỂN TƯƠNG LAI
    # ==========================================
    s32 = create_base_slide(prs, "PHẦN 7 • LỘ TRÌNH", "Lộ trình Phát triển Tương lai (Roadmap Mở rộng)", 32, total_slides)
    add_card(s32, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.6), "Kế hoạch Ngắn hạn (3 – 6 tháng tới)", [
        "1. Triển khai Local LLM On-Premise: Tích hợp Qwen2.5-Coder hoặc Llama-3-Instruct qua vLLM / Ollama trên máy chủ trường.",
        "2. Tích hợp Backend Execution Sandbox: Dựng container Docker cô lập để sinh viên bấm nút chạy thử code trực tiếp trên web.",
        "3. Hoàn thiện PostgreSQL Error Analytics: Lưu vết lịch sử và tính toán Bản đồ nhiệt lỗi lớp học theo thời gian thực."
    ], CYAN, "NGẮN HẠN")
    add_card(s32, Inches(6.8), Inches(1.8), Inches(5.4), Inches(4.6), "Kế hoạch Dài hạn (6 – 12 tháng tới)", [
        "1. Mở rộng kho tri thức toàn bộ khóa học: Nạp toàn bộ giáo trình các môn chuyên ngành của Khoa CNTT.",
        "2. Tính năng Auto-Ingestion: Giảng viên chỉ cần kéo thả Slide PPTX / PDF mới lên là tự động bóc tách và nạp vào ChromaDB.",
        "3. Tích hợp sâu vào LMS: Kết nối chuẩn LTI với Moodle, Canvas hoặc Blackboard của nhà trường."
    ], EMERALD, "DÀI HẠN")

    # ==========================================
    # SLIDE 33: KẾT LUẬN & ĐÓNG GÓP
    # ==========================================
    s33 = create_base_slide(prs, "PHẦN 8 • KẾT LUẬN", "Kết luận & Đóng góp Cốt lõi của Đồ án Tốt nghiệp", 33, total_slides)
    add_card(s33, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.6), "1. Pipeline RAG Giáo dục", [
        "Bóc tách chuẩn SOTA MinerU.",
        "Kho tri thức 5.230 chunks vector.",
        "Đạt 100% Hit@3 trên 20 câu benchmark canonical."
    ], CYAN, "KẾT QUẢ 1")
    add_card(s33, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.6), "2. Phương pháp Socratic", [
        "Định hình phong cách sư phạm.",
        "Không làm bài hộ, bắt buộc sinh viên tự tư duy và tự debug.",
        "Thẻ trích dẫn minh bạch."
    ], EMERALD, "KẾT QUẢ 2")
    add_card(s33, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.6), "3. Đột phá Multimodal", [
        "Tiếp nhận Text, Code, Ảnh Terminal.",
        "Query Synthesizer chống pha loãng truy vấn.",
        "Bảo vệ an toàn Path Traversal."
    ], VIOLET, "KẾT QUẢ 3")
    add_card(s33, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.6), "4. Kiểm chứng Kỹ thuật", [
        "63/63 Pytests đạt 100%.",
        "Đóng gói Docker Compose sẵn sàng triển khai thực tế.",
        "Giá trị EdTech cao."
    ], AMBER, "KẾT QUẢ 4")

    # ==========================================
    # SLIDE 34: LỜI CẢM ƠN & Q&A
    # ==========================================
    s34 = prs.slides.add_slide(blank_layout)
    bg34 = s34.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg34.fill.solid()
    bg34.fill.fore_color.rgb = BG_DARK
    bg34.line.fill.background()

    card34 = s34.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.0), Inches(1.2), Inches(9.333), Inches(5.1))
    card34.fill.solid()
    card34.fill.fore_color.rgb = CARD_BG
    card34.line.color.rgb = EMERALD
    card34.line.width = Pt(2)

    tb34 = s34.shapes.add_textbox(Inches(2.5), Inches(1.8), Inches(8.333), Inches(4.0))
    tf34 = tb34.text_frame
    tf34.word_wrap = True

    p_end0 = tf34.paragraphs[0]
    p_end0.text = "XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY CÔ VÀ HỘI ĐỒNG!"
    p_end0.font.size = Pt(26)
    p_end0.font.bold = True
    p_end0.font.color.rgb = TEXT_WHITE
    p_end0.font.name = "Segoe UI"
    p_end0.alignment = PP_ALIGN.CENTER
    p_end0.space_after = Pt(20)

    p_end1 = tf34.add_paragraph()
    p_end1.text = "HỆ THỐNG TRỢ GIẢNG LẬP TRÌNH THÔNG MINH (AI-POWERED CODING TUTOR)"
    p_end1.font.size = Pt(16)
    p_end1.font.color.rgb = CYAN
    p_end1.font.name = "Segoe UI"
    p_end1.alignment = PP_ALIGN.CENTER
    p_end1.space_after = Pt(24)

    p_end2 = tf34.add_paragraph()
    p_end2.text = "Nhóm em xin sẵn sàng lắng nghe ý kiến nhận xét và giải đáp các câu hỏi từ Hội đồng."
    p_end2.font.size = Pt(15)
    p_end2.font.color.rgb = TEXT_BODY
    p_end2.font.name = "Segoe UI"
    p_end2.alignment = PP_ALIGN.CENTER
    p_end2.space_after = Pt(24)

    p_end3 = tf34.add_paragraph()
    p_end3.text = "PHIÊN HỎI - ĐÁP (Q & A)"
    p_end3.font.size = Pt(20)
    p_end3.font.bold = True
    p_end3.font.color.rgb = AMBER
    p_end3.font.name = "Segoe UI"
    p_end3.alignment = PP_ALIGN.CENTER

    prs.save(str(PPTX_PATH))
    print(f"Successfully generated PowerPoint presentation with {len(prs.slides)} slides at: {PPTX_PATH}")


if __name__ == "__main__":
    build_powerpoint()
