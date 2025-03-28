import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")  # 또는 "gemini-1.0-pro"

def review_code_with_gemini(code: str) -> str:
    prompt = f"""다음 코드를 리뷰해줘. 개선할 점이나 주의할 점이 있다면 알려줘.\n\n```java\n{code}\n```"""

    response = model.generate_content(prompt)
    return response.text.strip()