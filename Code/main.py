from Controller.Receiver import Receiver
from threading import Thread
import time
from Model.ConfigData import ConfigData

data = ConfigData("Rebeka")
rec = Receiver(data)

t = Thread(target=rec.run_api)
t.start()


for i in range(0, 24):
    print("thread still running")
    time.sleep(5)

t.join()

