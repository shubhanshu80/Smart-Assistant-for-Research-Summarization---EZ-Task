# 🧠 Gen AI Assistant for Research Summarization

A Streamlit-powered application using Google Gemini AI for:
- 📄 We can upload Document (PDF/TXT)
- 🧠 Auto-summarization (≤150 words)
- 💬 Free-form Q&A
- 💬 Free MCQ and Subjective Questions
- 🎯 Challenge Me Mode (Objective & Subjective quiz generation)

---

## 🌐 Live Demo
---
https://shubhanshu80-smart-assistant-for-genai-assistant-mainapp-ziodel.streamlit.app/
---

## 🚀 Features

- **PDF/TXT Upload**: Upload English documents up to 15 MB.
- **Auto-Summary**: Generates a concise ≤150-word summary using Gemini.
- **Ask Anything**: Ask free-form questions from the document content.
- **Challenge Me Mode**:
  - Objective: Auto-generated multiple-choice questions with scoring
  - Subjective: Auto-generated descriptive questions with answer inputs

---
## 📁 Project Structure

```
genai-assistant/
├── app.py                  # Streamlit frontend
├── .env                    # API keys (gitignored)
├── requirements.txt        # Dependencies
├── backend/
│   ├── file_parser.py      # PDF/TXT text extraction
│   ├── summarizer.py       # ≤150-word summary with Gemini
│   ├── qa_engine.py        # Free-form Q&A with citations
│   └── challenge.py        # Logic-based question generation & evaluation
```

```
Flow:

User uploads document → Text extracted → Auto-summary generated.

Ask Anything: Gemini answers queries with direct document references.

Challenge Me: Questions generated → User answers → AI evaluates + justifies.
```

---

## 🛠️ Setup Instructions
