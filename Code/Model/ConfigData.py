from typing import Any
import netifaces as ni
from ipaddress import IPv4Address 
from threading import Lock

class ConfigData:

    def __init__(self, name: str, port: int = 8000) -> None:
        gateway = ni.gateways()['default'][ni.AF_INET][1]
        self.ip: str = ni.ifaddresses(gateway)[ni.AF_INET][0]['addr']
        #{18: [{'addr': ''}], 2: [{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}], 30: [{'peer': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'addr': '::1'}, {'peer': '', 'netmask': 'ffff:ffff:ffff:ffff::', 'addr': 'fe80::1%lo0'}]}
        self.name: str = name
        self.port: int = port 
        self.user_list: dict[IPv4Address, str] = {}

    
class SingeltonMeta(type):

    _instances = {}

    _lock: Lock = Lock() #synchronisiert Threads beim ersten Zugriff auf singelton 

    def __call__(self, cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance= super().__call__(*args, **kwargs)
                cls._instances[cls] = instance 
        return cls._instances[cls]


# class Singleton:
#     instance = None

#     @staticmethod
#     def get_instance():
#         if Singleton.instance is None:
#             Singleton()
#         return Singleton.instance
    
#     def __init__(self):
#         if Singleton.instance is None:
#             Singleton.instance = self 