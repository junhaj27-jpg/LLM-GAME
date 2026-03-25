from openai import OpenAI
from dotenv import load_dotenv
import os

print("KEY:", os.getenv("OPENAI_API_KEY"))
load_dotenv()  # 👈 이거 없으면 무조건 실패

client = OpenAI()  # 👈 api_key 넣지 마라

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt, user_input):
    try:
        res = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        # 안전하게 텍스트 추출
        if hasattr(res, "output") and res.output:
            content = res.output[0].content
            if content and hasattr(content[0], "text"):
                return content[0].text

        return "아무 일도 일어나지 않았다."

    except Exception as e:
        return f"에러 발생: {str(e)}"