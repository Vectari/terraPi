import os
import glob

class TemperatureSensor:
    def __init__(self):
        base_dir = '/sys/bus/w1/devices/'
        self.device_files = [
            os.path.join(folder, 'w1_slave')
            for folder in glob.glob(base_dir + '28*')
        ]
        if not self.device_files:
            raise RuntimeError("Nie znaleziono żadnych czujników DS18B20.")

    def _read_raw(self, device_file):
        try:
            with open(device_file, 'r') as f:
                return f.readlines()
        except IOError:
            return []

    def _read_single(self, device_file):
        try:
            lines = self._read_raw(device_file)
            if len(lines) < 2:
                return None

            if lines[0].strip()[-3:] != 'YES':
                return None

            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                return round(float(temp_string) / 1000.0, 1)
        except (IndexError, ValueError):
            return None

        return None

    def read_all(self):
        results = []
        for i, df in enumerate(self.device_files):
            temp = self._read_single(df)
            if temp is None:
                print(f"Błąd odczytu z czujnika {i}")
            results.append(temp)
        return results
