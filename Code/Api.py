from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    ip: str
    name: str

class Logout(BaseModel):
    ip: str

class Send(BaseModel):
    message: str

app = FastAPI()

# Start
@app.post("/start")
def start_post(s_m: Message):
    return s_m.model_dump()

@app.get("/start")
def start_get(s_m: Message):
    return s_m.model_dump()

#Exit
@app.post("/exit")
def exit_post(l: Logout):
    return l.model_dump()

@app.get("/exit")
def exit_get(l: Logout):
    return l.model_dump()

#Message
@app.post("/message")
def message_post(s: Send):
    return s.model_dump()

@app.get("/message")
def message_get(s: Send):
    return s.model_dump()