from ipaddress import IPv4Address
from fastapi.encoders import jsonable_encoder
from uvicorn import Server, Config
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Model.ConfigData import ConfigData
from Model.Messages.StartMessage import StartMessage
from Model.Messages.Message import Message
from Model.Messages.ExitMessage import ExitMessage



class Receiver():

    def __init__(self, cd: ConfigData) -> None:
        self.api = FastAPI()
        self.api.add_api_route(path="/message", endpoint=self.receive_message, methods=['POST']) #gibt die Route an um zum Endpunkt zu gelangen mit entsprechender Methode
        self.api.add_api_route(path="/start", endpoint=self.receive_start_message, methods=['POST'])
        self.api.add_api_route(path="/exit", endpoint=self.receive_exit_message, methods=['POST'])
        self.cd = cd 
        self.server :Server = Server(
            Config(self.api, self.cd.ip.exploded, access_log = False)
        )


    def start(self)-> None:
        self.server.run()
    
    def stop(self)-> None:
        self.server.should_exit = True 


# empfängt StartMessage
    def receive_start_message(self, sm: StartMessage) -> StartMessage:
        self.cd.user_list[sm.ip] = sm.name 
        return StartMessage(name=self.cd.name, ip=self.cd.ip)
   

# empfängt Nachrichten 
    def receive_message(self, m: Message, request: Request) -> None:
        ipv4 : IPv4Address = IPv4Address(request.client.host)
        print(self.cd.user_list[ipv4]+ ': ' + m.message)
    
    

# empfängt ExitMessage
    def receive_exit_message(self, em: ExitMessage) -> None:
        self.cd.user_list.pop(em.ip)
          

        