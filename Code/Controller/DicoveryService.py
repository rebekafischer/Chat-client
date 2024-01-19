# mdns senden
from zeroconf import Zeroconf, ServiceInfo
import socket
import Api 


# mdns broadcast 
def publish_mdns_service(service_name, service_type, port):
    # Get the local IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Create a Zeroconf object
    zeroconf = Zeroconf()

    # Create a ServiceInfo object with the service details
    info = ServiceInfo(
        service_type,
        f"{service_name}.{service_type}",
        addresses=[socket.inet_aton(ip_address)],
        port=port,
        properties={"description": "My mDNS Service"},
    )

    # Register the service
    zeroconf.register_service(info)


# mdns reply erhalten mit ip adresse
    

# Start Nachricht mit name und ip adresse senden 
beginning = StartMessage() # neues Objekt
beginning.post("/start") # Objekt an start schicken


# Exit Nachricht senden 
end = ExitMessage() #neues Objekt
end.post("/exit") #an exit endpunkt schicken 