import google.generativeai as genai

def summarise_document(text: str, api_key: str) -> str:
    """
    Generate a ≤150-word summary using Gemini 1.5 Pro (latest).
    """
    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

        response = model.generate_content(
            f"Summarize the following document in no more than 150 words:\n\n{text[:12000]}"
        )
        return response.text.strip()
    except Exception as e:
        raise RuntimeError(f"Gemini summarization error: {e}")
