# 🧠 Gen AI Assistant for Research Summarization

A Streamlit-powered application using Google Gemini AI for:
- 📄 Document upload (PDF/TXT)
- 🧠 Auto-summarization (≤150 words)
- 💬 Free-form Q&A
- 🎯 Challenge Me Mode (Objective & Subjective quiz generation)

---

## 🌐 Live Demo

https://genai-assistant-by-anmol.streamlit.app

## 🚀 Features

- **PDF/TXT Upload**: Upload English documents up to 15 MB.
- **Auto-Summary**: Generates a concise ≤150-word summary using Gemini.
- **Ask Anything**: Ask free-form questions from the document content.
- **Challenge Me Mode**:
  - Objective: Auto-generated multiple-choice questions with scoring
  - Subjective: Auto-generated descriptive questions with answer inputs

---

## 📁 Folder Structure

```
genai-assistant/
├── app.py
├── .env
├── requirements.txt
├── backend/
│   ├── file_parser.py
│   ├── summarizer.py
│   ├── qa_engine.py
│   └── challenge.py
```

---

## 🛠️ Setup Instructions

1. **Clone this repo**
```bash
git clone https://github.com/anmolecule94/genai-assistant
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

> Get your API key here: https://makersuite.google.com/app/apikey

5. **Run the app**
```bash
streamlit run app.py
```

---

## 📦 Requirements

- Python 3.9 or 3.10
- API key from Google Gemini (via MakerSuite)
