from components.led_indicator import LEDIndicator
from components.temperature_sensor import TemperatureSensor
from components.display import Display
import time

def main():
    print("Aplikacja terrarium uruchomiona.")
    
    status_led = LEDIndicator(pin=17)
    temp_sensor = TemperatureSensor()
    display = Display()

    status_led.turn_on()

    try:
        while True:
            temps = temp_sensor.read_all()
            print(f"Temperatury: {temps}")

            # Formatowanie temperatur
            t1 = f"{temps[0]}°C" if temps[0] is not None else "---"
            t2 = f"{temps[1]}°C" if len(temps) > 1 and temps[1] is not None else "---"

            display.show_text(f"T1: {t1}\nT2: {t2}")
            time.sleep(5)

    except KeyboardInterrupt:
        print("Zamykanie aplikacji...")
        status_led.turn_off()
        display.clear()

if __name__ == "__main__":
    main()
