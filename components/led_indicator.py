from gpiozero import LED

class LEDIndicator:
    def __init__(self, pin=17):
        self.led = LED(pin)

    def turn_on(self):
        self.led.on()

    def turn_off(self):
        self.led.off()
