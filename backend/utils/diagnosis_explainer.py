from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")
print(f"[GROQ] API key loaded: {'YES' if api_key else 'NO - check .env!'}")

client = Groq(api_key=api_key)

def generate_llm_explanation(pred, confidence, heatmap):
    label = "malignant" if pred > 0.5 else "benign"

    if confidence > 0.6:
        confidence_text = "high"
    elif confidence > 0.55:
        confidence_text = "moderate"
    else:
        confidence_text = "low"

    max_val = heatmap.max()

    if max_val > 0.75:
        focus = "strong"
    elif max_val > 0.4:
        focus = "moderate"
    else:
        focus = "diffuse"

    prompt = f"""
    You are an AI medical assistant.

    A skin lesion image was analyzed by a deep learning model.

    Prediction: {label}
    Confidence: {confidence:.2f}

    The model used Grad-CAM and focused on specific regions of the lesion.

    Explain WHY this specific image was classified as {label}.

    Focus on:
    - Visual patterns like asymmetry, border irregularity, color variation
    - What the model might have detected in the highlighted regions
    - Keep it specific to THIS case, not general theory

    Give 2–3 concise lines. Write the explanation as a single paragraph. Do not use bullet points or dashes
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        explanation = response.choices[0].message.content.strip()
        print(f"[GROQ] Explanation generated: {explanation[:80]}...")
        return explanation

    except Exception as e:
        print(f"[GROQ] LLM ERROR: {e}")

        if label == "malignant":
            return "The model detected irregular patterns suggesting abnormal tissue regions. The highlighted areas indicate possible malignancy."
        else:
            return "The lesion appears consistent and lacks strong irregular features. The model suggests it is likely benign."
