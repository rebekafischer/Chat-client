from ctypes import cdll
from Model.ConfigData import ConfigData
from Model.Messages.Message import Message
import requests

# Klasse Transmitter
class Transmitter:

    def __init__(self, cd: ConfigData) -> None:
        self.cd = cd
    
    
# message  
    def transmitter_start(self) -> None:
        s: str = ""
        while "exit" not in s:
            s = input("Geben Sie eine Nachricht ein: ")
            m: Message = Message(
                message = s 
            )
            self.send_message(m)

    def send_message(self, m: Message) -> None:
        for ip in self.cd.user_list.keys(): #ab hier send message 
            participant = f"{ip.exploded}/message"
            requests.post(participant, m.model_dump())
        
