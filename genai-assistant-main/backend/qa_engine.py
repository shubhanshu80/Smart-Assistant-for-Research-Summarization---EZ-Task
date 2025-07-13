import google.generativeai as genai

def answer_question(document_text: str, question: str, api_key: str) -> dict:
    """
    Use Gemini 1.5 Pro to answer a question and provide justification.
    """
    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")


        prompt = (
            f"You are a helpful assistant. Use ONLY the content in the following document.\n\n"
            f"DOCUMENT:\n{document_text[:12000]}\n\n"
            f"QUESTION:\n{question}\n\n"
            "Answer the question, then add a 'Justification:' section quoting the supporting line."
        )

        response = model.generate_content(prompt)
        content = response.text.strip()

        if "Justification:" in content:
            answer, justification = content.split("Justification:", 1)
            return {"answer": answer.strip(), "justification": justification.strip()}

        return {"answer": content, "justification": ""}
    except Exception as e:
        raise RuntimeError(f"Gemini Q&A error: {e}")
