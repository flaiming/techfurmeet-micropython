# MicroPython workshop at TechFurMeet

This document contains useful information that will be used for [TechFurMeet](https://www.techfurmeet.org/) workshop. But feel free to use it anywhere else :)

[Link to presentation](https://docs.google.com/presentation/d/1s5l5uXPHnwexjAZdf8eqWwv_EDYjKUNP4exJiZsZvaw/edit?usp=sharing)

## Important links

* [Getting started with MicroPython on the ESP8266](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html)
* [Firmware for ESP8266 boards](http://micropython.org/download#esp8266)
* [MicroPython WebREPL](https://micropython.org/webrepl/) - allows you to connect to MicroPython interactive console over wifi and send/receive files from microcontroller.
* [MIcroPython course from Pyladies in Czech](http://naucse.python.cz/lessons/beginners/micropython/)

## Recommended tools

* [ESPlorer](https://esp8266.ru/esplorer/) - multiplatform GUI interface in Java. Enables you to run python code directly or from scripts, upload scripts to microcontroller and more.

## Optional tools (mainly for linux)

* [esptool.py](https://github.com/espressif/esptool) - command line tool to communicate with microcontroller. Useful for erasing and flashing firmware.
* [ampy](https://github.com/adafruit/ampy) - command line tool to interact with MicroPython board. Useful for managing files on microcontroller and run scripts.
* [picocom](https://github.com/npat-efault/picocom) - command line tool enabling connection to MicroPython interpret on microcontroller (quit with CTRL + a CTRL + q).

## How to flash MicroPython to ESP8266

1. Erase flash memory
```
sudo esptool.py --port /dev/ttyUSB0 -b 115200 erase_flash
```
2. Flash MicroPython
```
sudo esptool.py --port /dev/ttyUSB0 -b 115200 write_flash --flash_size=detect 0 esp8266-20171101-v1.9.3.bin
```
Then you can verify it's functionality by connecting to MicroPython shell:
```
sudo picocom -b 115200 /dev/ttyUSB0
```
