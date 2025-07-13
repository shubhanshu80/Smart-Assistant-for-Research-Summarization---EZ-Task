"""
Challenge Mode – Objective + Subjective Quiz Generator using Gemini
-------------------------------------------------------------------
Supports:
1. Generating objective (MCQs)
2. Generating descriptive (subjective) questions
3. Evaluating objective answers
4. Evaluating subjective answers
"""

import google.generativeai as genai
import json
import re
from typing import List, Dict

def _get_model(api_key: str):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def generate_quiz(document_text: str, api_key: str, num_questions: int = 5) -> List[Dict]:
    model = _get_model(api_key)

    prompt = (
        f"Read the following document and generate {num_questions} MCQs.\n"
        f"Each question must have 4 options and the correct answer clearly marked with a letter A/B/C/D.\n"
        f"Return output strictly in this JSON format:\n"
        f'[{{"question": "...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "correct_option": "A"}}, ...]\n\n'
        f"Document:\n{document_text[:10000]}"
    )

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            match = re.search(r'\[\s*{.*?}\s*\]', content, re.DOTALL)
            if match:
                return json.loads(match.group(0))

        raise RuntimeError(f"Invalid JSON returned: {content[:300]}...")

    except Exception as e:
        raise RuntimeError(f"Gemini quiz generation error: {e}")

def generate_subjective_questions(document_text: str, api_key: str, num_questions: int = 3) -> List[str]:
    model = _get_model(api_key)

    prompt = (
        f"From the document below, generate {num_questions} descriptive questions.\n"
        f"Do NOT include answers or any extra text.\n\n"
        f"Document:\n{document_text[:10000]}"
    )

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()
        questions = [re.sub(r"^\s*\d+[\).]?\s*", "", line).strip()
                     for line in raw.splitlines() if line.strip()]
        return questions[:num_questions]
    except Exception as e:
        raise RuntimeError(f"Gemini subjective Q generation error: {e}")

def evaluate_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.strip().upper().startswith(correct_answer.strip().upper())

def evaluate_subjective(user_answer: str, question: str, api_key: str) -> str:
    model = _get_model(api_key)

    prompt = (
        f"You are an evaluator. Read the question and the student's answer.\n"
        f"Provide short feedback (1–2 lines). Do not assign marks.\n\n"
        f"Question: {question}\n"
        f"Answer: {user_answer}\n"
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Evaluation error: {e}"
