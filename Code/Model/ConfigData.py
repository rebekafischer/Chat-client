from typing import Any
import netifaces as ni
from ipaddress import IPv4Address 
from threading import Lock

class ConfigData:

    def __init__(self, name: str, port: int = 8000) -> None:
        gateway = ni.gateways()['default'][ni.AF_INET][1]
        self.ip: IPv4Address = IPv4Address(ni.ifaddresses(gateway)[ni.AF_INET][0]['addr']) 
        self.name: str = name
        self.port: int = port 
        self.user_list: dict[IPv4Address, str] = {}
