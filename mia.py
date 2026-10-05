from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="M.I.A Backend", version="1.0")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "M.I.A Core is online and operational, bro."}

@app.post("/ask")
def ask_mia(data: PromptRequest):
    reply = f"M.I.A processed your command: '{data.prompt}'. All systems nominal."
    return {"response": reply}
