import os
import streamlit as st
from dotenv import load_dotenv

# ───── Load API Key ─────
load_dotenv()
gemini_key = os.getenv("GOOGLE_API_KEY")
if not gemini_key:
    st.error("❌ GOOGLE_API_KEY is not set. Add it to .env or environment.")
    st.stop()

# ───── Local Module Imports ─────
from backend.file_parser import extract_text
from backend.summarizer import summarise_document
from backend.qa_engine import answer_question
from backend.challenge import (
    generate_quiz,
    evaluate_answer,
    generate_subjective_questions,
    evaluate_subjective
)

# ───── Page Config ─────
st.set_page_config("🧠 GenAI Research Assistant", "🤖", layout="wide")

# ───── Sidebar: Author Info ─────
st.sidebar.image("https://github.com/user-attachments/assets/fa39ee7a-ed66-47ad-9a07-aa6e6099cd7c", width=100)  # Replace with your photo if you want

st.sidebar.title("👤 Author Info")
st.sidebar.markdown("""
**Name:** Shubhanshu Singh  
**Email:** [shubhanshusingh8081@gmail.com](mailto:shubhanshusingh8081@gmail.com)  
**Contact:** +91 9335208375  
---
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/shubhanshu80/)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shubhanshu-singh-15a8bb275/)
""")

# ───── Custom CSS ─────
st.markdown("""
    <style>
    body {
        background-color: #f9fafb;
    }

    h1, h2, h3 {
        color: #1f2937;
    }

    .stButton>button {
        border-radius: 8px;
        background: linear-gradient(135deg, #4f46e5, #6366f1);
        color: #ffffff;
        font-weight: 600;
        border: none;
        padding: 0.6em 1.4em;
        box-shadow: 0 4px 12px rgba(79,70,229,0.3);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #4338ca, #4f46e5);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(67,56,202,0.4);
    }

    .stFileUploader {
        border: 2px dashed #4f46e5;
        border-radius: 12px;
        padding: 1em;
        background-color: #000000;
        color: #ffffff;
    }

    .stTextInput>div>div>input {
        border-radius: 6px;
        border: 1px solid #d1d5db;
        padding: 0.4em;
        background-color: #111111;
        color: #ffffff;
    }

    .stRadio>div {
        background-color: #111111;
        border-radius: 10px;
        padding: 1em;
        color: #ffffff;
    }

    .stExpander {
        border-radius: 10px;
        background-color: #111111;
        border: 1px solid #333333;
        color: #ffffff;
    }

    .stExpanderSummary {
        font-weight: 600;
    }

    .stSpinner {
        color: #4f46e5 !important;
    }

    .stMarkdown {
        background-color: #111111;
        color: #ffffff;
        border-radius: 8px;
        padding: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# ───── App Title & Intro ─────
st.title("🤖 GenAI Research Assistant- By Shubhanshu Singh")
st.markdown(
    "Upload a **PDF or TXT** research paper, generate a smart summary, ask questions, "
    "and challenge yourself with quizzes — all powered by Gemini AI! 🔍📚"
)

# ───── Upload Section ─────
st.header("📂 Upload Document")

uploaded_file = st.file_uploader(
    "Drag & drop your file here",
    type=["pdf", "txt"],
    help="Supported formats: PDF and TXT."
)

if uploaded_file:
    with st.spinner("📄 Extracting text from your document..."):
        doc_text = extract_text(uploaded_file)
    if not doc_text.strip():
        st.error("⚠️ No text found. Please upload a valid text-based document.")
        st.stop()
    st.success("✅ Document successfully extracted!")
    st.session_state["doc_text"] = doc_text

    # ───── Summarization Section ─────
    st.header("📝 Document Summary")
    if "summary" not in st.session_state:
        with st.spinner("🧠 Generating smart summary..."):
            try:
                st.session_state["summary"] = summarise_document(doc_text, gemini_key)
            except Exception as e:
                st.error(f"❌ Error during summarization: {e}")
                st.stop()
    with st.expander("🔍 View Summary"):
        st.markdown(st.session_state["summary"])

    # ───── Q&A Section ─────
    st.header("💬 Ask Questions")
    question = st.text_input("Type your question about the document here:")

    if question:
        with st.spinner("🤖 Thinking..."):
            try:
                result = answer_question(doc_text, question, gemini_key)
                st.markdown(f"**✅ Answer:** {result['answer']}")
                if result.get("justification"):
                    st.markdown(f"**📚 Justification:** {result['justification']}")
            except Exception as e:
                st.error(f"❌ Q&A error: {e}")

    # ───── Challenge Me Section ─────
    st.header("🎯 Challenge Yourself")
    challenge_type = st.radio(
        "Choose your challenge type:",
        ["Objective Quiz (MCQ)", "Subjective Quiz"],
        horizontal=True
    )

    if st.button("✨ Generate Challenge"):
        with st.spinner("🔍 Preparing challenge questions..."):
            try:
                if challenge_type.startswith("Objective"):
                    quiz = generate_quiz(doc_text, gemini_key)
                    st.session_state["quiz"] = quiz
                    st.session_state.pop("subjective", None)
                    st.success(f"✅ {len(quiz)} MCQs generated.")
                else:
                    subjective = generate_subjective_questions(doc_text, gemini_key)
                    st.session_state["subjective"] = subjective
                    st.session_state.pop("quiz", None)
                    st.success(f"✅ {len(subjective)} subjective questions generated.")
            except Exception as e:
                st.error(f"❌ Challenge generation error: {e}")

    # ───── Objective Quiz ─────
    if "quiz" in st.session_state:
        st.subheader("📝 Objective Quiz")
        score = 0
        responses = []

        for i, q in enumerate(st.session_state["quiz"], start=1):
            st.markdown(f"**Q{i}. {q['question']}**")
            user_ans = st.radio("Choose an option:", q["options"], key=f"q{i}")
            responses.append((user_ans, q["correct_option"]))
            st.markdown("---")

        if st.button("✅ Submit Objective Answers"):
            for ans, correct in responses:
                if ans.strip().upper().startswith(correct.upper()):
                    score += 1
            st.success(f"🎉 Your Score: {score}/{len(responses)}")

    # ───── Subjective Quiz ─────
    if "subjective" in st.session_state:
        st.subheader("📝 Subjective Questions")
        subjective_answers = []

        for i, q in enumerate(st.session_state["subjective"], start=1):
            st.markdown(f"**Q{i}. {q}**")
            ans = st.text_area("Your Answer:", key=f"subjective_q{i}")
            subjective_answers.append((q, ans))

        if st.button("✅ Submit Subjective Answers"):
            st.markdown("### 🧾 Feedback")
            for i, (q, ans) in enumerate(subjective_answers, start=1):
                st.markdown(f"**Q{i}. {q}**")
                st.markdown(f"🖊️ **Your Answer:** {ans if ans.strip() else '_No answer provided._'}")
                with st.spinner("🔍 Evaluating..."):
                    feedback = evaluate_subjective(ans, q, gemini_key)
                st.markdown(f"📋 **Evaluation:** {feedback}")
                st.markdown("---")
else:
    st.info("📥 Please upload a document to get started!")
