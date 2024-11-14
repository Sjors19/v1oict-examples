from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)

def kort():
    gpio_pin.value(1)
    time.sleep(0.2)
    gpio_pin.value(0)
    time.sleep(0.1)

def lang():
    gpio_pin.value(1)
    time.sleep(1)
    gpio_pin.value(0)
    time.sleep(0.1)

while True:
    kort()
    kort()
    kort()
    lang()
    time.sleep(0.9)