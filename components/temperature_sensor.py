# components/temperature_sensor.py

import os
import glob

class TemperatureSensor:
    def __init__(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folders = glob.glob(base_dir + '28*')  # DS18B20 zawsze zaczyna się od 28
        if not device_folders:
            raise RuntimeError("Nie znaleziono czujnika DS18B20.")
        self.device_file = os.path.join(device_folders[0], 'w1_slave')

    def _read_raw(self):
        with open(self.device_file, 'r') as f:
            return f.readlines()

    def read(self):
        lines = self._read_raw()
        if lines[0].strip()[-3:] != 'YES':
            return {'temperature': None}

        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return {'temperature': round(temp_c, 2)}
        return {'temperature': None}
