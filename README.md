# LLM-GAME
# 🧠 LLM 스토리 게임

## 📌 프로젝트 소개

이 프로젝트는 OpenAI API를 활용하여 플레이어의 입력에 따라 실시간으로 이야기가 생성되는 **텍스트 기반 인터랙티브 게임**입니다.

고정된 스토리가 아닌,
👉 AI가 직접 세계를 생성하고
👉 플레이어의 행동에 따라 스토리가 변화합니다.

---

## 🎮 주요 기능

### 🧠 AI 기반 스토리 생성

* GPT 모델을 활용한 동적 스토리 생성
* 자연어 입력 기반 진행

### 🔄 상태 관리 시스템

* 체력(HP), 인벤토리 관리
* 턴 기반 게임 진행

### 💬 채팅형 UI

* Streamlit 기반 인터페이스
* 직관적인 입력/출력 구조

### 🛡️ 안정성 처리

* JSON 파싱 실패 대비
* API 응답 오류 처리
* fallback 로직 적용

---

## 📁 프로젝트 구조

```
LLM-GAME/
├── app.py
├── requirements.txt
├── .env  (gitignore 처리)
└── game/
    ├── state.py
    ├── engine.py
    ├── prompt.py
    ├── llm.py
    └── utils.py
```

---

## ⚙️ 실행 방법

### 1️⃣ 환경 활성화

```bash
conda activate llm310
```

### 2️⃣ 패키지 설치

```bash
pip install -r requirements.txt
```

### 3️⃣ 실행

```bash
python -m streamlit run app.py
```

---

## 🔑 환경 변수 설정

`.env` 파일 생성:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🎯 사용 방법

* 입력창에 행동 입력
  👉 예: `문을 연다`, `주변을 조사한다`

* AI가 다음 스토리 생성

---

## 🧠 기술 스택

* Python
* OpenAI API (gpt-4o-mini)
* Streamlit
* Pydantic

---

## 🚀 향후 개선 방향

* RAG 기반 기억 시스템
* 선택지 UI
* 전투 시스템
* 저장/불러오기 기능
* 웹 배포

---

## 💡 프로젝트 의의

이 프로젝트는
👉 LLM을 활용한 인터랙티브 시스템 설계
👉 AI 기반 애플리케이션 개발 경험을 보여주는 프로젝트입니다.

---

## 🧠 한 줄 요약

> **"AI가 실시간으로 이야기를 만들어주는 게임 엔진"**
