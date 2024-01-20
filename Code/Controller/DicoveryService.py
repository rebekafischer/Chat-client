# mdns senden
from zeroconf import Zeroconf, ServiceInfo
import socket


# mdns broadcast 

# mdns reply erhalten mit ip adresse
    

# Start Nachricht mit name und ip adresse senden 
beginning = StartMessage() # neues Objekt
beginning.post("/start") # Objekt an start schicken


# Exit Nachricht senden 
end = ExitMessage() #neues Objekt
end.post("/exit") #an exit endpunkt schicken 