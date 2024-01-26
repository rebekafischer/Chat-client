from pydantic import BaseModel

class ExitMessage(BaseModel):
    name : str
    ip : str 

  
