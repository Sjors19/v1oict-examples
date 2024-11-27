from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import machine


i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

adc_value = machine.ADC(4).read_u16()
V = (3.3 / 65535) * adc_value
temp = 27 - (V - 0.706) / 0.001721


while True:
    lcd.move_to(0, 0)
    lcd.putstr("Temperatuur:")
    lcd.move_to(0, 1)
    lcd.putstr(f'{temp : .1f} Graden')