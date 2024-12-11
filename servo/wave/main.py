from machine import Pin
import time

servo_pin = Pin(21, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)

def servo_pulse(position):
    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
    """
    high = ((2 * (position / 100 )) + 0.5) / 1000
    low = 0.02 - high
    pulse(servo_pin, high, low)


while True:
    for i in range(0, 100, 1):
        servo_pulse(i)
        time.sleep(0.02)
    for i in range(100, 0, -1):
        servo_pulse(i)
        time.sleep(0.02)
