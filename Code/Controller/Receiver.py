from ipaddress import IPv4Address
import uvicorn

#from Model.ConfigData import ConfigData
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from Model.ConfigData import ConfigData
from Model.Messages.StartMessage import StartMessage
from Model.Messages.Message import Message
from Model.Messages.ExitMessage import ExitMessage




# Klasse Receiver
class Receiver():

    def __init__(self, cd: ConfigData) -> None:
        self.api = FastAPI()
        self.api.add_api_route(path="/message", endpoint=self.receive_message, methods=['POST']) #gibt die Route an um zum Endpunkt zu gelangen mit entsprechender Methode
        self.api.add_api_route(path="/start", endpoint=self.receive_start_message, methods=['POST'])
        self.api.add_api_route(path="/exit", endpoint=self.receive_exit_message, methods=['POST'])
        self.cd = cd 


    def run_api(self):
        uvicorn.run(self.api, host=self.cd.ip, port=8000) #startet die Api
        
    

        

# empfängt StartMessage
    def receive_start_message(self, sm: StartMessage) -> StartMessage:
        self.cd.user_list[sm.ip] = sm.name 
        return sm 
   

# empfängt Nachrichten 
    def receive_message(self, m: str) -> str:
        print(m)
        return m

# empfängt ExitMessage
    def receive_exit_message(self, em: str) -> str:
        return em 

        