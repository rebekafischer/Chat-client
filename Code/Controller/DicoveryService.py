import time
import socket
from network import MDNS 
from Model.ConfigData import ConfigData


class DiscoveryService: 
    # mdns broadcast 
    def __init__(self) -> None: 
        self.mdns = MDNS()
    MDNS.set_name(hostname = ip, instance_name = "my_instance") #hostname und instance name setzen 
    MDNS.add_service("_http", MDNS.PROTO_TCP, 80) #TCP service hinzufügen 

    time.sleep(60) # um anderen devices zeit zu geben die services zu entdecken 
    # mdns reply erhalten mit ip adresse
        

    # Start Nachricht mit name und ip adresse senden 
    beginning = StartMessage() # neues Objekt
    beginning.post("/start") # Objekt an start schicken


    # Exit Nachricht senden 
    end = ExitMessage() #neues Objekt
    end.post("/exit") #an exit endpunkt schicken 