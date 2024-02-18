from ctypes import cdll
from Model.ConfigData import ConfigData
from Model.Messages import ExitMessage
from Model.Messages.Message import Message
from Model.Messages.ExitMessage import ExitMessage
import requests

# Klasse Transmitter
class Transmitter:

    def __init__(self, cd: ConfigData) -> None:
        self.cd = cd
        self.transmitter_start()
        
    
    
# message  
    def transmitter_start(self) -> None:
        s: str = ""
        while "exit" not in s:
            m: Message = Message(
                message = s 
            )
            self.send_message(m)
            s = input("Geben Sie eine Nachricht ein: ")

    def send_message(self, m: Message) -> None:
        for ip in self.cd.user_list.keys(): #ab hier send message 
            participant = f"http://{ip.exploded}:8000/message"
            requests.post(participant, m.model_dump_json())

#exit
    def send_exit_message(self) -> None:
        em: ExitMessage = ExitMessage(name= self.cd.name, ip= self.cd.ip)
        for ip in self.cd.user_list.keys():
            participant = f"http://{ip.exploded}:8000/exit"
            requests.post(participant, em.model_dump_json())
