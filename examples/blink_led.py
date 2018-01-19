# blink led 20x

from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)

for i in range(10):
    led.off()
    sleep_ms(50)
    led.on()
    sleep_ms(50)
