from ipaddress import IPv4Address
from pydantic import BaseModel

class ExitMessage(BaseModel):
    name : str
    ip : IPv4Address 

  
