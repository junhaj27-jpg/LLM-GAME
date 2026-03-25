from game.prompt import build_prompt
from game.llm import call_llm
from game.utils import parse_response
from game.state import GameState

def run_turn(state: GameState, user_input: str):
    prompt = build_prompt(state, user_input)

    raw = call_llm(prompt, user_input)
    parsed = parse_response(raw)

    new_state = GameState(
        scene=parsed.get("scene", state.scene),
        hp=parsed.get("hp", state.hp),
        inventory=parsed.get("inventory", state.inventory)
    )

    return {
        "response": parsed.get("scene", raw),
        "state": new_state
    }