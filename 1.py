#!/bin/python

import sys
import pyautogui
import serial


try:
	arduino = serial.Serial("/dev/ttyACM0",timeout=1)
except:
	print('check')
	
#while True:
#	a = str(arduino.readline())
#	print(a)

while True:
	a = str(arduino.readline())
#	a = 'ba30 70\n'
	
	a += 'bbbbb'
#	print(a)
	x='0'
	y='0'
	i=2
	while a[i].isdigit():
		x += a[i]
		i=i+1
#		print("x")
#		print(i)
	i=i+1
	while a[i].isdigit():
		y += a[i]
		i=i+1
#		print("y")
#		print(i)
#	print(int(x))
#	print(int(y))
	pyautogui.moveRel((int(x)/1.3)*8, (int(y)/1.3)*8, duration=0.2)
	


print("aa000")
ser = serial.Serial('/dev/ttyACM0', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) 
ser.flushInput()
print("aa111")
ser.flushOutput()
print("aa222")
while True:
  data_raw = ser.readline()
  print("aa")
  print(data_raw)
  print("aacc")
  x='0'
  y='0'
  i=2
  while a[i].isdigit():
    x += a[i]
    i=i+1
    print("x")
#	print(i)
  print(int(x))
  i=i+1
  while a[i].isdigit():
    y += a[i]
    i=i+1
    print("y")
#	print(i)
  print(int(y))
  pyautogui.moveRel(x, y, duration=0.1)

