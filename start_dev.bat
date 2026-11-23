@echo off
chcp 65001 > nul
echo ========================================================
echo   🚀 KHỞI ĐỘNG HỆ THỐNG AI-POWERED CODING TUTOR
echo ========================================================
echo.
echo [1/2] Đang khởi động Backend FastAPI (Port 8000)...
start "Backend - FastAPI Tutor" cmd /k "cd /d %~dp0backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

echo [2/2] Đang khởi động Frontend Next.js (Port 3000)...
start "Frontend - Next.js UI" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo ========================================================
echo   ✅ ĐÃ KHỞI CHẠY THÀNH CÔNG!
echo   🌐 Giao diện Web:    http://localhost:3000
echo   📚 Swagger API Docs: http://localhost:8000/docs
echo ========================================================
echo.
echo (Bạn có thể đóng cửa sổ này, 2 terminal Backend và Frontend vẫn tiếp tục chạy)
pause
