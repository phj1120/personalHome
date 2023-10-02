import os
import time
import piir

from flask import Flask

remote = piir.Remote(os.path.dirname(os.path.abspath(__file__))+'/sensor.json', 17)
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/mode/<mode>')
def mode(mode):
    if(mode == 'sleep'):
        waitAndSend('night')
        waitAndSend('30')
        return 'ok'
    
    if(mode == 'wakeup'):
        waitAndSend('power')
        waitAndSend('night')
        for i in range(0, 30):
            waitAndSend('add')
    return 'ok'

@app.route('/sensor/irled/<keyword>')
def irLed(keyword):
    remote.send(keyword)
    return 'ok'

def waitAndSend(key):
    term = 0.2
    time.sleep(term)
    remote.send(key)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')