from pydantic import BaseModel

class StartMessage(BaseModel):
    name : str
    ip : str 

  

