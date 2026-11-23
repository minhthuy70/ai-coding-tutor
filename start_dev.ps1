# Khởi động đồng thời Backend FastAPI và Frontend Next.js trên Windows
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  🚀 KHỞI ĐỘNG HỆ THỐNG AI-POWERED CODING TUTOR" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

$rootDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "`n[1/2] Đang khởi động Backend FastAPI (Port 8000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$rootDir/backend'; python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

Write-Host "[2/2] Đang khởi động Frontend Next.js (Port 3000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$rootDir/frontend'; npm run dev"

Write-Host "`n========================================================" -ForegroundColor Cyan
Write-Host "  ✅ ĐÃ KHỞI CHẠY THÀNH CÔNG!" -ForegroundColor Green
Write-Host "  🌐 Giao diện Web:    http://localhost:3000" -ForegroundColor White
Write-Host "  📚 Swagger API Docs: http://localhost:8000/docs" -ForegroundColor White
Write-Host "========================================================" -ForegroundColor Cyan
