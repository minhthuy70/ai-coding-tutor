"""
Tutor API Router
Author: AI Coding Tutor Team
Description:
    Endpoints tiếp nhận tin nhắn từ giao diện người dùng:
    - Tiếp nhận đồng thời Text câu hỏi, Danh sách file mã nguồn, Danh sách ảnh chụp lỗi
    - Tích hợp pipeline RAG & Socratic AI Engine
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import logging

from app.services.multimodal_service import multimodal_service
from app.services.tutor_service import tutor_service

logger = logging.getLogger("TutorRouter")

router = APIRouter(prefix="/tutor", tags=["Socratic AI Coding Tutor"])

class TextChatRequest(BaseModel):
    prompt: str
    language: Optional[str] = None

@router.post("/chat")
async def chat_text_only(req: TextChatRequest):
    """Endpoint xử lý câu hỏi dạng văn bản thuần túy."""
    try:
        result = await tutor_service.generate_tutor_response(
            prompt=req.prompt,
            language=req.language
        )
        return {
            "status": "success",
            "reply": result["reply"],
            "sources": result["sources"],
            "suggestedFollowUps": result["follow_ups"]
        }
    except Exception as e:
        logger.error(f"Lỗi khi xử lý chat text: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lỗi xử lý Trợ giảng AI: {str(e)}"
        )

@router.post("/multimodal-chat")
async def chat_multimodal(
    prompt: str = Form(""),
    language: Optional[str] = Form(None),
    code_files: List[UploadFile] = File(default=[]),
    image_files: List[UploadFile] = File(default=[])
):
    """
    Endpoint tiếp nhận dữ liệu Đa phương thức:
    - prompt: Nội dung câu hỏi của người dùng
    - language: Ngôn ngữ lập trình (python, cpp, java,...)
    - code_files: Danh sách file mã nguồn đính kèm
    - image_files: Danh sách ảnh chụp màn hình terminal / lỗi / code
    """
    try:
        # 1. Bóc tách file code
        processed_code_files = []
        for file in code_files:
            if file.filename:
                content = await file.read()
                data = multimodal_service.process_code_file(content, file.filename)
                processed_code_files.append(data)

        # 2. Bóc tách ảnh qua Vision OCR
        processed_images = []
        for img in image_files:
            if img.filename:
                img_bytes = await img.read()
                mime = img.content_type or "image/png"
                img_data = await multimodal_service.process_image_vision(
                    img_bytes,
                    img.filename,
                    mime
                )
                processed_images.append(img_data)

        # 3. Chạy qua RAG & Socratic LLM
        result = await tutor_service.generate_tutor_response(
            prompt=prompt,
            language=language,
            code_files_data=processed_code_files,
            images_data=processed_images
        )

        return {
            "status": "success",
            "reply": result["reply"],
            "sources": result["sources"],
            "suggestedFollowUps": result["follow_ups"],
            "filesCount": len(processed_code_files),
            "imagesCount": len(processed_images)
        }
    except Exception as e:
        logger.error(f"Lỗi xử lý multimodal-chat: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lỗi xử lý đa phương thức: {str(e)}"
        )

