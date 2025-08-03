from components.led_indicator import LEDIndicator
from components.temperature_sensor import TemperatureSensor
from components.display import Display
import time

def main():
    print("Aplikacja terrarium uruchomiona.")
    
    # Inicjalizacja komponentów
    status_led = LEDIndicator(pin=17)
    temp_sensor = TemperatureSensor()
    display = Display()

    status_led.turn_on()

    try:
        while True:
            # Tu w przyszłości będą inne komponenty i logika
            data = temp_sensor.read()
            temp = data['temperature']
            print(f"Temperatura: {temp}°C")

            if temp is not None:
                display.show_text(f"Temp: {temp}°C")
            else:
                display.show_text("Brak odczytu")
            time.sleep(5)

    except KeyboardInterrupt:
        print("Zamykanie aplikacji...")
        status_led.turn_off()
        display.clear()

if __name__ == "__main__":
    main()
