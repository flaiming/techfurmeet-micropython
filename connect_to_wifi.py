import network
import time

# deactivate AP
ap = network.WLAN(network.AP_IF)
ap.active(False)

# activate static network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# connect to local WIFI
wlan.connect('TFM-Attendees')

# wait until connected
while not wlan.isconnected():
    print('connecting...')
    time.sleep(1)
print('Connected!')
print('Current network config:', wlan.ifconfig())
