import os
import time
import piir

class SensorManager:
    def __init__(self):
        self.remote = piir.Remote(os.path.dirname(os.path.abspath(__file__))+'/sensor.json', 17)

    def waitAndSend(self, key):
        term = 0.2
        time.sleep(term)
        self.send(key)
        return
    
    def send(self, key):
        self.remote.send(key)
        return

    def mode(self, keyword):
        if(keyword == 'sleep'):
            self.waitAndSend('night')
            self.waitAndSend('30')
            return
        
        if(keyword == 'wakeup'):
            self.waitAndSend('power')
            self.waitAndSend('night')
            for i in range(0, 30):
                self.waitAndSend('add')
                print(i)
            self.waitAndSend('night')
            return
        return

    def irLed(self, keyword):
        self.send(keyword)
        return