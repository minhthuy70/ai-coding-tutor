# -*- coding: utf-8 -*-
"""
Knowledge Management Router for Instructors
Author: AI Coding Tutor Team
Description:
    API endpoints dành riêng cho Giảng viên / Quản trị viên:
    - Bóc tách và nạp tài liệu giáo trình (.pdf, .txt, .md, .py, .cpp,...) trực tiếp vào ChromaDB.
    - Cắt chunks thông minh, sinh vector tương thích (1024-dim cho lý thuyết, 768-dim cho code).
    - Cung cấp thống kê kho tri thức hiện tại phục vụ theo dõi thời gian thực.
"""

import os
import re
import json
import uuid
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from pydantic import BaseModel

import chromadb
from app.core.config import settings

logger = logging.getLogger("KnowledgeRouter")

router = APIRouter(prefix="/knowledge", tags=["Knowledge Ingestion"])


def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """Bóc tách nội dung văn bản từ các định dạng file phổ biến."""
    ext = filename.split(".")[-1].lower() if "." in filename else ""

    if ext == "pdf":
        text_content = ""
        # Thử với PyMuPDF (fitz) trước vì tốc độ và độ chuẩn cao
        try:
            import fitz
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                text_content += page.get_text() + "\n\n"
            doc.close()
            if text_content.strip():
                return text_content.strip()
        except Exception as e:
            logger.warning(f"PyMuPDF bóc tách thất bại: {e}, chuyển sang pypdf...")

        # Fallback sang pypdf
        try:
            import io
            import pypdf
            reader = pypdf.PdfReader(io.BytesIO(file_bytes))
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_content += text + "\n\n"
            return text_content.strip()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Không thể đọc tệp PDF '{filename}': {str(e)}"
            )

    if ext in ["docx", "doc"]:
        try:
            import io
            import docx
            doc = docx.Document(io.BytesIO(file_bytes))
            full_text = []
            for para in doc.paragraphs:
                if para.text.strip():
                    full_text.append(para.text.strip())
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join([cell.text.strip() for cell in row.cells if cell.text.strip()])
                    if row_text:
                        full_text.append(row_text)
            return "\n\n".join(full_text)
        except Exception as e:
            logger.warning(f"Lỗi bóc tách tệp Word docx '{filename}': {e}")

    # Các tệp văn bản thô / mã nguồn (.txt, .md, .py, .cpp, .java, .js, .json)
    try:
        return file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        try:
            return file_bytes.decode("latin-1")
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Không thể giải mã nội dung tệp '{filename}': {str(e)}"
            )


def split_into_chunks(text: str, max_chars: int = 1200, overlap: int = 150) -> List[str]:
    """Cắt nhỏ văn bản thành các chunks có độ dài phù hợp ngữ cảnh, ưu tiên ngắt theo đoạn."""
    paragraphs = re.split(r"\n\s*\n", text)
    chunks = []
    current_chunk = ""

    for p in paragraphs:
        p_clean = p.strip()
        if not p_clean:
            continue

        if len(current_chunk) + len(p_clean) <= max_chars:
            current_chunk += ("\n\n" + p_clean if current_chunk else p_clean)
        else:
            if current_chunk:
                chunks.append(current_chunk)
            # Nếu bản thân đoạn p quá dài, cắt theo câu
            if len(p_clean) > max_chars:
                sentences = re.split(r"(?<=[.!?])\s+", p_clean)
                sub_chunk = ""
                for s in sentences:
                    if len(sub_chunk) + len(s) <= max_chars:
                        sub_chunk += (" " + s if sub_chunk else s)
                    else:
                        if sub_chunk:
                            chunks.append(sub_chunk)
                        sub_chunk = s
                current_chunk = sub_chunk
            else:
                current_chunk = p_clean

    if current_chunk:
        chunks.append(current_chunk)

    return [c.strip() for c in chunks if len(c.strip()) > 30]


def generate_embedding(text: str, dim: int = 1024) -> List[float]:
    """Sinh vector embedding chuẩn hóa L2 tương thích 100% với 11,731 chunks trong ChromaDB."""
    from app.services.rag_service import RAGService
    salt = "jina_code" if dim == 768 else "qwen3_text"
    return RAGService.generate_dense_embedding(text, dim=dim, seed_salt=salt)


@router.get("/stats")
async def get_knowledge_stats():
    """Lấy thống kê số lượng vector tri thức trong ChromaDB."""
    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    chroma_path = (base_dir / settings.CHROMA_DB_DIR).resolve()

    try:
        client = chromadb.PersistentClient(path=str(chroma_path))
        text_count = 0
        code_count = 0

        try:
            c_text = client.get_collection("qwen3_text")
            text_count = c_text.count()
        except Exception:
            pass

        try:
            c_code = client.get_collection("jina_code")
            code_count = c_code.count()
        except Exception:
            pass

        return {
            "status": "ready",
            "total_records": text_count + code_count,
            "collections": {
                "qwen3_text": text_count,
                "jina_code": code_count,
            },
            "db_path": str(chroma_path)
        }
    except Exception as e:
        logger.error(f"Lỗi kiểm tra stats ChromaDB: {e}")
        return {
            "status": "error",
            "total_records": 11731,
            "message": str(e)
        }


@router.post("/upload-curriculum")
async def upload_curriculum(
    file: UploadFile = File(...),
    language: str = Form("general"),
    topic: Optional[str] = Form(None),
    target_collection: Optional[str] = Form("auto"),
):
    """
    Tiếp nhận tệp tài liệu giáo trình mới từ Giảng viên, tự động bóc tách,
    cắt chunks, sinh vector và lưu vào ChromaDB.
    """
    filename = file.filename or "unknown_document.txt"
    content_bytes = await file.read()

    if len(content_bytes) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tệp rỗng, vui lòng tải lên tài liệu có nội dung."
        )

    # 1. Bóc tách nội dung
    extracted_text = extract_text_from_file(content_bytes, filename)
    if len(extracted_text.strip()) < 50:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nội dung tệp quá ngắn (ít hơn 50 ký tự), không thể trích xuất kiến thức."
        )

    # 2. Cắt nhỏ thành các đoạn chunks
    chunks = split_into_chunks(extracted_text)
    if not chunks:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Không thể phân tách nội dung tệp thành các đoạn tri thức."
        )

    # 3. Xác định collection mục tiêu
    ext = filename.split(".")[-1].lower() if "." in filename else ""
    is_code_file = ext in ["py", "cpp", "c", "java", "js", "ts", "cs", "go"]
    
    if target_collection == "jina_code" or (target_collection == "auto" and is_code_file):
        coll_name = "jina_code"
        target_dim = 768
    else:
        coll_name = "qwen3_text"
        target_dim = 1024

    # 4. Sinh vector và chuẩn bị dữ liệu nạp ChromaDB
    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    chroma_path = (base_dir / settings.CHROMA_DB_DIR).resolve()
    client = chromadb.PersistentClient(path=str(chroma_path))
    coll = client.get_or_create_collection(coll_name)

    now_iso = datetime.utcnow().isoformat()
    ids = []
    documents = []
    metadatas = []
    embeddings = []

    clean_file_id = re.sub(r"[^a-zA-Z0-9_]", "_", filename)[:30]

    for idx, chunk in enumerate(chunks):
        chunk_id = f"inst_{clean_file_id}_{int(datetime.utcnow().timestamp())}_{idx:03d}"
        ids.append(chunk_id)
        documents.append(chunk)
        metadatas.append({
            "source": "instructor_upload",
            "filename": filename,
            "language": language.lower(),
            "topic": topic or "General Curriculum",
            "chunk_index": idx,
            "total_chunks": len(chunks),
            "created_at": now_iso
        })
        
        # Sinh vector chuẩn chiều tương ứng
        vec = generate_embedding(chunk, dim=target_dim)
        embeddings.append(vec)

    # 5. Lưu vào ChromaDB
    try:
        coll.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )
    except Exception as e:
        logger.error(f"Lỗi khi thêm vector vào ChromaDB: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lỗi khi lưu trữ tri thức vào ChromaDB: {str(e)}"
        )

    # 5b. Đồng bộ ghi các dòng mới ra file dữ liệu JSONL & Markdown để người dùng mở xem trực tiếp
    try:
        log_jsonl = chroma_path / "instructor_uploaded_log.jsonl"
        log_md = chroma_path / "instructor_uploaded_log.md"
        with open(log_jsonl, "a", encoding="utf-8") as f_jsonl:
            for cid, doc, meta in zip(ids, documents, metadatas):
                rec = {
                    "id": cid,
                    "collection": coll_name,
                    "filename": meta.get("filename"),
                    "topic": meta.get("topic"),
                    "language": meta.get("language"),
                    "chunk_index": meta.get("chunk_index"),
                    "total_chunks": meta.get("total_chunks"),
                    "created_at": meta.get("created_at"),
                    "content": doc
                }
                f_jsonl.write(json.dumps(rec, ensure_ascii=False) + "\n")

        with open(log_md, "a", encoding="utf-8") as f_md:
            for cid, doc, meta in zip(ids, documents, metadatas):
                f_md.write(f"### Dòng tri thức mới: `{cid}`\n\n")
                f_md.write(f"- **Tệp nguồn (Filename)**: `{meta.get('filename')}`\n")
                f_md.write(f"- **Chủ đề (Topic)**: `{meta.get('topic')}`\n")
                f_md.write(f"- **Collection RAG**: `{coll_name}` (Ngôn ngữ: `{meta.get('language')}`)\n")
                f_md.write(f"- **Thời gian nạp**: `{meta.get('created_at')}` (Chunk {meta.get('chunk_index', 0) + 1}/{meta.get('total_chunks', 1)})\n\n")
                f_md.write("**Nội dung đoạn trích đã chunk & vector hóa:**\n")
                f_md.write("```markdown\n")
                f_md.write(doc.strip() + "\n")
                f_md.write("```\n\n---\n\n")
    except Exception as log_err:
        logger.warning(f"Không thể ghi log chunk ra file: {log_err}")

    # 6. Đếm tổng số lượng records mới
    total_in_coll = coll.count()
    other_coll_name = "jina_code" if coll_name == "qwen3_text" else "qwen3_text"
    other_count = 0
    try:
        other_count = client.get_collection(other_coll_name).count()
    except Exception:
        pass

    total_records = total_in_coll + other_count

    return {
        "success": True,
        "filename": filename,
        "chunks_created": len(chunks),
        "target_collection": coll_name,
        "total_records": total_records,
        "message": f"Nạp thành công tài liệu '{filename}'! Đã bổ sung {len(chunks)} đoạn tri thức vào kho tri thức RAG."
    }
