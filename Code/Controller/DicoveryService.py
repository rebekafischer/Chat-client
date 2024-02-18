#!/usr/bin/env python3

""" Example of browsing for a service.

The default is HTTP and HAP; use --find to search for all available services in the network
"""

from time import sleep
from Model.Messages.StartMessage import StartMessage
from Model.ConfigData import ConfigData
import requests
import socket
from Model.MyListener import MyListener
from ipaddress import IPv4Address
from requests import Response
import json

from zeroconf import (
    IPVersion,
    ServiceBrowser,
    Zeroconf,
    ServiceInfo,
)

class DiscoveryService:

   
    def __init__(self, cd: ConfigData) -> None:
        self.cd = cd
        self.zeroconf = Zeroconf(ip_version = IPVersion.All)
        
        self.info = ServiceInfo(
            "_chatti._tcp.local.",
            cd.name + '._chatti._tcp.local.',
            addresses=[cd.ip.packed],
            port=8000,
            properties={},
            server=socket.gethostname() + '.local.'
        )

        
        

    def start_advertisement(self):
        self.zeroconf.register_service(self.info)


    def search_participants(self):
        sl: MyListener = MyListener()
        browser = ServiceBrowser(self.zeroconf,[self.info.type], listener=sl)
        sleep(10)
        browser.cancel()
        browser.join()

        sm: StartMessage = StartMessage(name=self.cd.name, ip=self.cd.ip)
        self.send_startmessage(sm, sl)



    def send_startmessage(self, sm: StartMessage, ml: MyListener):
        for ip in ml._userlist:
            participant = f"http://{ip}:8000/start"
            res: Response = requests.post(participant, sm.model_dump_json())
            temp: StartMessage = StartMessage.model_validate_json(res.content)

            self.cd.user_list[temp.ip] = temp.name
        
    

    def stop_advertisement(self) -> None:
        self.zeroconf.unregister_service(self.info)
        self.zeroconf.close()



