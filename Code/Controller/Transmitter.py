import threading
from Model.ConfigData import ConfigData
from Controller.Receiver import Receiver
from Model.Messages.Message import Message
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import uvicorn

# Klasse Transmitter
class Transmitter:

    def __init__(self, participants: ConfigData) -> None:
        self.api = FastAPI()
        self.participants = participants 
        self.api.add_api_route(path="/message", endpoint=self.send_message, methods=['POST'])
        

    # auf userliste zugereifen, getAllParticipants()
    def get_all_participants(self):
        return self.participants.user_list
    
    
# message senden 
    def send_message(self, m: Message) -> Message:
        self.m = input("Enter your message")
        return m
        
    
# auf input warten
