# AI-Powered Coding Tutor & Auto-Grader

Research project on an AI-powered platform for automated code assessment and intelligent programming tutoring.

## Research Areas

- Automated Programming Assessment
- Code Execution and Auto-Grading
- Static Code Analysis
- LLM-based Code Analysis
- AI Programming Tutor
- Secure Code Execution
- Code Quality Assessment

## Objectives

The system aims to evaluate student source code using:

1. Traditional test-case based grading
2. Static code analysis
3. Algorithm complexity analysis
4. Security analysis
5. LLM-based code understanding
6. AI-generated pedagogical feedback

## Research Direction

Traditional Auto-Grader
        +
Static Analysis
        +
Execution Evidence
        +
LLM
        ↓
AI-Powered Code Assessment & Tutor

## Project Status

- **Sprint:** Day 1 Foundation Complete (01/10/2026)
- **Architecture:** Modular Monolith (FastAPI + Next.js + PostgreSQL + Redis)

## Quick Start / Chạy hệ thống

### Yêu cầu tiên quyết (Prerequisites)
- **Docker Desktop đang chạy** (Docker Engine daemon hoạt động trên máy host).
- Docker Compose v2+.
- Git.

### 1. Chuẩn bị biến môi trường
Tạo file `.env` từ mẫu `.env.example`:
```bash
cp .env.example .env
```
*(Lưu ý: Không commit file `.env` chứa cấu hình nội bộ lên Git).*

### 2. Khởi động toàn bộ hệ thống
Khởi chạy đồng thời 4 dịch vụ (Frontend, Backend, PostgreSQL, Redis) qua Docker Compose:
```bash
docker compose up -d --build
```

### 3. Kiểm tra trạng thái containers
```bash
docker compose ps
```

### 4. Kiểm tra sức khỏe hệ thống (Health Check)
Kiểm tra kết nối giữa FastAPI, PostgreSQL và Redis:
```bash
curl http://localhost:8000/api/health
```
Kết quả mong đợi (HTTP 200 OK):
```json
{
  "status": "ok",
  "database": "connected",
  "redis": "connected",
  "environment": "development"
}
```

### 5. Danh sách Ports & URLs truy cập

| Dịch vụ | Port | URL / Điểm truy cập |
| :--- | :--- | :--- |
| **Frontend (Next.js)** | `3000` | http://localhost:3000 |
| **Backend API (FastAPI)** | `8000` | http://localhost:8000 (API Docs: http://localhost:8000/docs) |
| **Backend Health Check** | `8000` | http://localhost:8000/api/health |
| **PostgreSQL Database** | `5432` | `localhost:5432` |
| **Redis Cache / Broker** | `6379` | `localhost:6379` |

### 6. Dừng hệ thống
```bash
docker compose down
```

## Team

- [Your Name]

## License

MIT