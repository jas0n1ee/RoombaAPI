#!/usr/bin/env python
import time
import serial
import sys
import struct
class API(object):
    def __init__(self, serialdevice):
        self.ser = serial.Serial(
            port=serialdevice,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        if not self.ser.isOpen():
            self.ser.open()

    def reconfig(self,serialdevice,brate,parity,stopbits,bytesize):
        self.ser = serial.Serial(
            port=serialdevice,
            baudrate=brate,
            parity=parity,
            stopbits=stopbits,
            bytesize=bytesize
        )
        if not self.ser.isOpen():
            self.ser.open()  

    def start(self):
        self.ser.write(bytearray([128]))
    def reset(self):
        self.ser.write(bytearray([7]))
    def stop(self):
        self.ser.write(bytearray([173]))
    def setSafeMode(self):
        self.ser.write(bytearray([131]))
    def setFullMode(self):
        self.ser.write(bytearray([132]))
    def clean(self):
        self.ser.write(bytearray([135]))
    def drive(self,speed,radius):
        self.ser.write(bytearray([137]))
        b_speed = struct.pack('>h',speed)
        b_radius = struct.pack('>h',radius)
        self.ser.write(bytearray(b_speed))
        self.ser.write(bytearray(b_radius))
    def digit(self,four):
        self.ser.write(bytearray([163] + four)) 

def easySetup():
    h = API('/dev/tty.usbserial-DA01NW67')
    h.start()
    h.setSafeMode()
    return h


