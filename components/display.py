# components/display.py

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

class Display:
    def __init__(self, width=128, height=64):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(width, height, i2c)
        self.width = width
        self.height = height
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

    def show_text(self, text):
        # Czyszczenie ekranu
        self.display.fill(0)
        self.display.show()

        # Tworzenie obrazu
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=self.font, fill=255)

        # Wyświetlenie obrazu
        self.display.image(image)
        self.display.show()

    def clear(self):
        self.display.fill(0)
        self.display.show()
