import netifaces as ni
from ipaddress import IPv4Address 

class ConfigData:

    def __init__(self, name: str, port: int = 8000) -> None:
        self.ip: str = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        #{18: [{'addr': ''}], 2: [{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}], 30: [{'peer': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'addr': '::1'}, {'peer': '', 'netmask': 'ffff:ffff:ffff:ffff::', 'addr': 'fe80::1%lo0'}]}
        self.name: str = name
        self.port: int = port 
        self.user_list: dict[IPv4Address, str] = {}


    _instance = None #stores singelton instance 


    def __new__(cls): #responsible for new instance
        if cls._instance is None: #checks that no instance has been created yet 
            cls._instance = super(ConfigData, cls).__new__(cls) #creates instance 
        return cls._instance
