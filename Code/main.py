from Controller.Receiver import Receiver
from threading import Thread
import time

rec = Receiver()

#t = Thread(target=rec.run_api)
#t.start()

rec.run_api()

for i in range(0, 24):
    print("thread still running")
    time.sleep(5)

#t.join()