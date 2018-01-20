"""
Module for measurement of temperature and humidity with DHT22 sensor and sending data to ThingSpeak.
Aimed for ESP8266 and Micropython.
"""
import time

import machine
import network
import socket
import dht

PIN_DHT = 2
CONNECT_WAIT = 20
SLEEP_INTERVAL = 30
WIFI_SSID = 'OAZA'
WIFI_PASSWORD = ''


def read_temp_hum():
    d = dht.DHT22(machine.Pin(PIN_DHT))
    d.measure()
    temp2 = d.temperature()
    humi = d.humidity()
    return temp2, humi


def wlan_connect(wlan):
    """Wait for wifi to be connected before attempting mqtt."""
    if wlan.isconnected():
        return True
    for _ in range(CONNECT_WAIT):
        if wlan.isconnected():
            return wlan
        else:
            wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        time.sleep(1)
    else:
        return None


def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()


def send_data(wlan, temp, hum):
    http_get("https://api.thingspeak.com/update?api_key=7HYDO7KRHIJNKX2S&field8={}&field7={}".format(
        temp,
        hum,
    ))


def run():
    led = machine.Pin(2, machine.Pin.OUT)
    # get sensor values
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    while True:
        led.off()
        temp, hum = read_temp_hum()
        print("temp: %s, %s" % (temp, hum))
        print('connecting')
        if wlan_connect(wlan):
            print('sending data')
            send_data(wlan, temp, hum)
        print('sleeping...')
        led.on()
        time.sleep(30)


run()

