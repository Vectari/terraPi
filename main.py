from components.led_indicator import LEDIndicator
from components.temperature_sensor import TemperatureSensor
import time

def main():
    print("Aplikacja terrarium uruchomiona.")
    
    # Inicjalizacja komponentów
    status_led = LEDIndicator(pin=17)
    temp_sensor = TemperatureSensor()

    status_led.turn_on()

    try:
        while True:
            # Tu w przyszłości będą inne komponenty i logika
            data = temp_sensor.read()
            print(f"Temperatura: {data['temperature']}°C")
            time.sleep(5)

    except KeyboardInterrupt:
        print("Zamykanie aplikacji...")
        status_led.turn_off()

if __name__ == "__main__":
    main()
