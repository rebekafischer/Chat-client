from Controller.DiscoveryService import DiscoveryService
from Controller.Transmitter import Transmitter
from Controller.Receiver import Receiver
from threading import Thread
import time
from Model.ConfigData import ConfigData

data = ConfigData(input("Geben Sie ihren Namen ein: "))
rec = Receiver(data)
discovery = DiscoveryService(data)
t = Thread(target=rec.start)

t.start()
discovery.start_advertisement()
discovery.search_participants()
trm = Transmitter(data)

discovery.stop_advertisement()
trm.send_exit_message()
rec.stop()
t.join()

