from ipaddress import IPv4Address
from pydantic import BaseModel

class StartMessage(BaseModel):
    name : str
    ip : IPv4Address 

  

