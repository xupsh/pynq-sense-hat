# PYNQ-Sense-HAT

This repo contains the pip install package for Sense HAT on PYNQ. It's only support PYNQ Z2 board.

## Quick Start

In order to install it on your PYNQ board, connect to the board, open a terminal and type:

### Online Install
```shell
# (on PYNQ v2.3 or v2.4 only)
sudo pip3 install git+https://github.com/xupsh/pynq-sense-hat.git
```
### Standalone Install
```shell
# (on PYNQ v2.3 or v2.4 only)
cd pynq-sense-hat
sudo python setup.py install
```

NOTE: This command must be run as root.

## About Sense Hat

Sense HAT is a multiple devices integrated platform designed for Raspber Pi. All the devices on the Board can be access via IIC bus 1(GPIO2 as SDA and GPIO3 as SCL) with different device address. 

![](./boards/Pynq-Z2/notebooks/data/Sense_HAT_intro.jpg)

1.LED matrix controller: This microcontroller drives the LED matrix. Address:0x46  
2.LED matirx: This 8x8 LED matrix displays characters or pictures.  
3.LSM9DS1: The all-in-one gyroscope, accelerometer, and magnetometer will measure the orientation of objects, an increase in speed, and the strength and direction of a magnetic field.  
4.Joystick: This five-button joystick allows for up, down, left, and right movements, as well as an Enter via a click.  
5.LPS25H: A temperature and humidity sensor.  
6.HTS221: A barometric pressure sensor.  
