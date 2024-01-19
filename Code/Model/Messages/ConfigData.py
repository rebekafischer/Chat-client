class UserList:

    def __init__(self, name:str, ip:str) -> None:
        self.name = name
        self.ip = ip
    

    user_list = {'ip': 'name'} #Dictionary mit key:ip und value:name

#neuen user in dictionary anlegen 
    def add_new_user(self, name, ip):
        self.user_list[ip] = name 

    _instance = None #stores singelton instance 


    def __new__(cls): #responsible for new instance
        if cls._instance is None: #checks that no instance has been created yet 
            cls._instance = super(UserList, cls).__new__(cls) #creates instance 
        return cls._instance


    