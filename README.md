# 🧠 Gen AI Assistant for Research Summarization

A Streamlit-powered application using Google Gemini AI:
- 📄 We can upload Document (PDF/TXT)
- 🧠 Auto-summarization (≤150 words)
- 💬 Free-form Q&A
- 💬 Free MCQ and Subjective Questions
- 🎯 Challenge Me Mode (Objective & Subjective quiz generation)

---

## 🌐 Live Demo
---
https://shubhanshu80-smart-assistant-for-genai-assistant-mainapp-w7znct.streamlit.app/
---
## Video Demo Running

https://github.com/user-attachments/assets/af337737-1e70-440a-a617-a6b46c3f2303

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

1. **Clone this repo**
```bash
https://github.com/shubhanshu80/Smart-Assistant-for-Research-Summarization---EZ-Task.git
cd genai-assistant
```

2. **Create a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your Gemini API key**
- Create a `.env` file in the root with:
```
GOOGLE_API_KEY=your-gemini-api-key-here
```
5. **Run the app**
```
streamlit run app.py
```
##  Requirements
> Get your API key here: https://makersuite.google.com/app/apikey

- API key from Google Gemini (via MakerSuite)
