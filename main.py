import string
import secrets
from typing import Any
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Tip(BaseModel):
    questionnaire: dict[str, Any]
    identity: dict[str, Any] | None = None # None if tip is anonymous

class TipAuth(BaseModel):
    key: str

def generate_random_key(length: int = 16) -> str:
    return "".join(secrets.choice(string.digits + string.ascii_letters) for _ in range(length))

app = FastAPI()
tips = {}

@app.post("/tips", response_model=TipAuth)
def create_tip(data: Tip):
    key = generate_random_key()
    while key in tips: # make sure key is not a duplicate
        key = generate_random_key()
    tips[key] = data.model_dump()
    return TipAuth(key=key)

@app.post("/auth", response_model=Tip)
def retrieve_tip(auth: TipAuth):
    if auth.key not in tips: # no tip found with provided key
        raise HTTPException(401, "unauthorized")
    return tips[auth.key]