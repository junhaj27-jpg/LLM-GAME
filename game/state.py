from pydantic import BaseModel, Field

class GameState(BaseModel):
    scene: str = "어두운 방에서 눈을 떴다."
    hp: int = 100
    inventory: list = Field(default_factory=list)