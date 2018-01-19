from machine import Pin
from time import sleep

# pin 2 = internal LED
led = Pin(2, Pin.OUT)

# turn LED on (for some unknown reason)
led.off()
sleep(2)
# turn LED off
led.on()
