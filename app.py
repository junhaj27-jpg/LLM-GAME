import streamlit as st
from game.engine import run_turn
from game.state import GameState

st.set_page_config(page_title="LLM 게임", layout="wide")

# 🔥 먼저 초기화
if "state" not in st.session_state:
    st.session_state.state = GameState()

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 LLM 스토리 게임")

# 🔥 그 다음 사용
st.sidebar.json(st.session_state.state.dict())

# 입력
user_input = st.chat_input("행동을 입력하세요...")

if user_input:
    result = run_turn(st.session_state.state, user_input)

    st.session_state.state = result["state"]
    st.session_state.history.append((user_input, result["response"]))

# 출력
for u, r in st.session_state.history:
    st.chat_message("user").write(u)
    st.chat_message("assistant").write(r)