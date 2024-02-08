from Controller.Transmitter import Transmitter
from Controller.Receiver import Receiver
from threading import Thread
import time
from Model.ConfigData import ConfigData

data = ConfigData("Rebeka")
rec = Receiver(data)
t = Thread(target=rec.run_api)
t.start()
trm = Transmitter(data)

t.join()

