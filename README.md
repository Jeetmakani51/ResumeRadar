# 🎯 ResumeRadar

AI-powered resume screener built with FastAPI + CrewAI. Upload a PDF, get instant skill extraction and candidate fit scoring — no manual reading required.

---

## How It Works

PDF Upload → pdfplumber extracts text → Agent 1 parses skills → Agent 2 scores fit → Results

Two AI agents work sequentially:
- **Data Scout** — extracts name, skills, and experience from the resume
- **Senior Recruiter** — compares skills against the job description and returns a Fit Score (0–100)

---

## Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | FastAPI                 |
| AI Agents | CrewAI                  |
| LLM       | Groq (Llama 3.3 70B)    |
| PDF Parse | pdfplumber              |
---

## Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/Jeetmakani51/ResumeRadar.git
cd ResumeRadar
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a `.env` file in the root:

GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key

ResumeRadar/
├── main.py          # FastAPI app + file upload endpoint
├── agents.py        # CrewAI agent definitions
├── tasks.py         # CrewAI task definitions
├── static/
│   └── index.html   # Frontend UI(to be worked on in future)
├── .env             # API keys (not committed)
├── requirements.txt
└── README.md

---

some phtotoes

<img width="2701" height="660" alt="Screenshot 2026-04-04 225505" src="https://github.com/user-attachments/assets/866b8e98-baa2-4518-b3f6-c27299616abb" />
<img width="2864" height="1485" alt="Screenshot 2026-04-04 225403" src="https://github.com/user-attachments/assets/73fc533a-c434-4c24-a0b7-31b61b41d2db" />
<img width="2858" height="1282" alt="Screenshot 2026-04-04 225332" src="https://github.com/user-attachments/assets/32fcfb2a-67ab-4bb5-8091-ca452d66b000" />

## License

MIT
