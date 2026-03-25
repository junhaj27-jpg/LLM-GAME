def build_prompt(state, user_input):
    return f"""
너는 텍스트 RPG 게임 마스터다.

현재 상태:
- 장면: {state.scene}
- 체력: {state.hp}
- 인벤토리: {state.inventory}

플레이어 행동:
{user_input}

JSON 형식으로만 응답:
{{
    "scene": "새로운 장면",
    "hp": 숫자,
    "inventory": []
}}
"""