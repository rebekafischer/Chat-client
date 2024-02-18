from ipaddress import IPv4Address
from pydantic import BaseModel

class StartMessage(BaseModel):
    name : str
    ip : IPv4Address 

    def ip_serializer(self, ip: IPv4Address, _info)-> str:
        return self.ip.exploded

  

