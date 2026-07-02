# CampusBooks 📚

ISBN 기반 수업별 중고 교재 거래 플랫폼

> 교재를 팔고, 바꾸고, 나눠요. ISBN 검색 한 번으로 책 정보를 자동으로 불러와 빠르게 등록하세요.

---

## 주요 기능

- ISBN 검색으로 책 정보(제목, 저자, 출판사, 정가) 자동완성
- 팔아요 / 바꿔요 / 드려요 세 가지 거래 유형
- 정가 대비 할인율 자동 계산
- 같은 책의 최저가 / 평균가 / 최대 할인율 비교
- 수업(Course)별 교재 필터링
- 책 상태 · 거래 장소 · 메모 입력

---

## 기술 스택

| 구분 | 기술 |
|---|---|
| Frontend | React 18, Vite, react-router-dom |
| Backend | Django 6, Django REST Framework |
| Database | PostgreSQL (배포) / SQLite (로컬) |
| 외부 API | 카카오 책 검색 API |
| Deploy | Vercel (Frontend) · Render (Backend) |

---

## 배포 URL

| | URL |
|---|---|
| 프론트엔드 | https://lion-lab.vercel.app |
| 백엔드 API | https://bookswap-backend-yrbk.onrender.com/api |

---

## 디렉토리 구조

```
lionLab/
├── backend/
│   ├── books/
│   │   ├── models.py          # Book, Listing, Course, TradeRequest
│   │   ├── views/
│   │   │   ├── __init__.py    # ISBN 검색 + Book 자동저장
│   │   │   ├── book_views.py  # BookViewSet + 가격비교 액션
│   │   │   ├── listing_views.py
│   │   │   └── course_views.py
│   │   ├── serializers/
│   │   ├── isbn_service.py    # 카카오 API 호출
│   │   └── urls.py
│   ├── mysite/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── render.yaml            # Render 배포 설정
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── api/               # 백엔드 API 호출 함수
    │   ├── components/
    │   ├── pages/
    │   └── routes/
    └── package.json
```

---

## 실행 방법

### Backend

```bash
cd backend

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env
# .env 파일에 KAKAO_API_KEY, SECRET_KEY 입력

# 마이그레이션 및 실행
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 환경변수

### backend/.env

```
SECRET_KEY=your-django-secret-key
DEBUG=True
KAKAO_API_KEY=your-kakao-rest-api-key
```

### frontend/.env

```
VITE_API_BASE_URL=http://localhost:8000/api
```

---

## API 주요 엔드포인트

| Method | Endpoint | 설명 |
|---|---|---|
| GET | `/api/books/` | 교재 목록 조회 |
| GET | `/api/books/isbn/?query={ISBN}` | ISBN으로 책 검색 + 자동저장 |
| GET | `/api/books/{id}/price-compare/` | 가격 비교 (최저가/평균가/할인율) |
| GET | `/api/listings/` | 판매글 목록 조회 |
| POST | `/api/listings/` | 판매글 등록 |
| GET | `/api/courses/` | 수업 목록 조회 |

---

## 팀원

| 이름 | 역할 | GitHub |
|---|---|---|
| 권태열 | 외부 API · 할인율 로직 · CORS · 배포 | @gtae10 |
| 팀원2 | FE | - |
| 팀원3 | BE | - |

---

## 회고

**잘한 점**
- ISBN 기반 책 정보 자동완성으로 등록 UX 개선
- Book / Listing 분리 설계로 확장성 확보
- 배포 환경까지 완성

**아쉬운 점**
- 더미 데이터가 적어 초기 UX가 아쉬움
- 로그인/인증 기능 미구현
