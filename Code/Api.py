from fastapi import FastAPI
from pydantic import BaseModel
from Controller.Receiver import Receiver

app = FastAPI()
recv = Receiver()

# Start
@app.post("/start")
recv.receive_message()

#Exit
@app.post("/exit")
def exit_post(l: Logout):
    return l.model_dump()

#Message
@app.post("/message")
def message_post(s: Send):
    return s.model_dump()
