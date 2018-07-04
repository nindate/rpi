#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 3
ECHO = 2

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)

print "Starting Measurement..."

GPIO.output(TRIG,1)
time.sleep(0.00001)
GPIO.output(TRIG,0)

while GPIO.input(ECHO) == 0:
	pass
start = time.time()

while GPIO.input(ECHO) == 1:
	pass
stop = time.time()

duration = stop - start 
distance = round((duration * 17150),2)
#print (stop - start) * 17000
print "distance is " +str(distance)+ " cm"

GPIO.cleanup
