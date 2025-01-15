import lgpio

LED_PIN = 17

# Inicjalizacja portu GPIO
handle = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(handle, LED_PIN)

# Ustawienie pinu
lgpio.gpio_write(handle, LED_PIN, 1)

lgpio.gpiochip_close(handle)
