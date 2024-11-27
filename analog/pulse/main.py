from machine import ADC, PWM, Pin
import time

gpio_pin = Pin(20, Pin.OUT)
led = Pin(20, Pin.OUT)
adc = ADC(Pin(26))


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


while True:
    adc_value = adc.read_u16()
    timing = adc_value / 65535
    pulse(gpio_pin, timing, timing)
