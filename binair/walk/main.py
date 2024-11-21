from machine import Pin
import time

switch_pin1 = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
switch_pin2 = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]


def leds(value, delay):
    for led in led_pins:
        if value % 2 == 1:
            led.value(1)
        else:
            led.value(0)
        value = value // 2
    time.sleep(delay)


delay = 0.2


def pat1():
    while True:
        leds(1, delay)
        leds(2, delay)
        leds(4, delay)
        leds(8, delay)
        leds(16, delay)
        leds(8, delay)
        leds(4, delay)
        leds(2, delay)
        if switch_pin2.value():
            pat2()


def pat2():
    while True:
        leds(17, delay)
        leds(10, delay)
        leds(4, delay)
        leds(10, delay)
        if switch_pin1.value():
            pat1()
while True:
    if switch_pin1.value():
        pat1()
    if switch_pin2.value():
        pat2()