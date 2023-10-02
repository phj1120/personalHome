
from flask import Flask

from SensorManager import SensorManager

app = Flask(__name__)
manager = SensorManager()

@app.route('/')
def index():
    return 'idx'

@app.route('/mode/<keyword>')
def mode(keyword):
    manager.mode(keyword)
    return 'ok'

@app.route('/sensor/irled/<keyword>')
def irLed(keyword):
    manager.irLed(keyword)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
