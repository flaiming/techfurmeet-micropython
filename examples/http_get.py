import network
import time
import socket


def check_connection():
    # checks if board is connected to WIFI
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    time.sleep(1)
    return wlan.isconnected()


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


def main():
    if check_connection():
        http_get('https://www.seznam.cz/')
    else:
        print("You are not connected to WIFI! Run connect_to_wifi.py first.")


main()
