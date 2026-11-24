import urllib.request
import json
import base64
import io
import os
from PIL import Image, ImageDraw
from dotenv import load_dotenv

load_dotenv()

def test_live_gemini_vision():
    # 1. Tạo 1 ảnh chụp màn hình terminal giả lập
    img = Image.new('RGB', (650, 220), color=(20, 20, 25))
    d = ImageDraw.Draw(img)
    d.text((25, 25), "Traceback (most recent call last):", fill=(255, 120, 120))
    d.text((25, 55), "  File 'app.py', line 18, in <module>", fill=(210, 210, 210))
    d.text((25, 85), "    total = calculate_average(grades[100])", fill=(210, 210, 210))
    d.text((25, 115), "IndexError: list index out of range", fill=(255, 90, 90))
    d.text((25, 155), ">>> Process finished with exit code 1", fill=(150, 150, 150))

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    key = os.getenv("GEMINI_API_KEY", "")
    if not key:
        print("[!] Lỗi: Chưa cấu hình GEMINI_API_KEY trong file .env")
        return
    model_name = os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={key}"

    prompt = """
    Bạn là Socratic Coding Tutor. Hãy quan sát ảnh chụp terminal:
    1. Trích xuất chính xác 100% dòng code và thông báo lỗi.
    2. Đưa ra 1 câu gợi ý Socratic ngắn gọn giúp sinh viên tự tìm ra nguyên nhân mà không giải bài hộ.
    """

    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": img_b64
                    }
                }
            ]
        }]
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    
    print(f"[*] Đang gửi ảnh terminal tới Google Gemini Vision ({model_name})...")
    with urllib.request.urlopen(req, timeout=20) as res:
        res_json = json.loads(res.read().decode())
        reply = res_json['candidates'][0]['content']['parts'][0]['text']
        print("\n================= PHẢN HỒI TỪ GOOGLE GEMINI VISION THẬT =================")
        print(reply)
        print("=========================================================================\n")

if __name__ == "__main__":
    test_live_gemini_vision()
