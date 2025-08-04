import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask_cors import CORS


from flask import Flask, jsonify
from components.temperature_sensor import TemperatureSensor

app = Flask(__name__)
CORS(app)
sensor = TemperatureSensor()

@app.route('/api/temperature')
def get_temperature():
    temps = sensor.read_all()
    return jsonify({'temperatures': temps})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
