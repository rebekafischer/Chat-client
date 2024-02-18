from Controller.DicoveryService import DiscoveryService
from Controller.Transmitter import Transmitter
from Controller.Receiver import Receiver
from threading import Thread
import time
from Model.ConfigData import ConfigData

data = ConfigData(input("Geben Sie ihren Namen ein: \n"))
rec = Receiver(data)
t = Thread(target=rec.run_api)
discovery = DiscoveryService(data)
t.start()
discovery.start_advertisement()
trm = Transmitter(data)
discovery.stop_advertisement()
trm.send_exit_message()

t.join()

