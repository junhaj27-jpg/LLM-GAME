import json
import re

def parse_response(raw):
    # 문자열 보장
    if not isinstance(raw, str):
        raw = str(raw)

    # JSON 부분 찾기
    match = re.search(r'\{.*\}', raw, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    # 실패 시 fallback
    return {
        "scene": raw,
        "hp": 100,
        "inventory": []
    }