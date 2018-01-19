import socket
import time
import network
from machine import Pin
import neopixel


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED strip control</title> </head>
<center><h2>A simple webserver for controlling LED strip with Micropython</h2></center>
Format: red-green-blue, for example 255-0-0 for red light<br />
<form>
{buttons}
<input type="submit" name="Submit"/>
</form>

<form method="get">
<textarea name="data"></textarea>
<input type="submit" name="Submit"/>
</form>
</html>
"""

sta_if = network.WLAN(network.STA_IF)
time.sleep(2)
print(sta_if.ifconfig())

pin1 = Pin(2, Pin.OUT)
pin1.on()

#Setup Socket WebServer
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

np = neopixel.NeoPixel(Pin(4), 10)


print('listening on', addr)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(2048)
    print("Content = %s" % str(request))

    btn_template = """
    LED no. {i}: <input type="text" name="color_{i}" value=""/><br />
    """
    buttons = []
    for i in range(10):
        buttons.append(btn_template.format(i=i))
    response = html.format(buttons='<br/>'.join(buttons))
    print(response)
    conn.send(response)
    conn.close()

    data = str(request).split()[1]
    if data.startswith('/?'):
        for params in data[2:].split('&'):
            param, val = params.split('=')
            if '_' in param:
                key, num = param.split('_')
                if key == 'color':
                    if val and len(val.split('-')) == 3:
                        try:
                            np[int(num)] = tuple(map(int, val.split('-')))
                        except ValueError:
                            print('Wrong value of %s' % val)
        np.write()
