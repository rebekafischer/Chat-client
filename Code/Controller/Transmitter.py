# config data importieren 
import Api 
import threading
from Model.ConfigData import UserList
from Controller.Receiver import Receiver

# Klasse Transmitter
class Transmitter:

    def __init__(self) -> None:
        
        

    def get_user_input(self):
        user_input = input("Enter your message")
        print(user_input)

    # auf userliste zugereifen, getAllParticipants()
    def get_all_participants(self):
        return self.user_list
    
    
# message senden 
    def send_message(self, m: str) -> str:
        self.m = input("Enter your message")
        return m
        #an endpunkt senden
    
# auf input warten
