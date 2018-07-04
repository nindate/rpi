#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 3
ECHO = 2
samples = 50
discard = int(samples * 0.2)

summedtimes = 0
pulse_begin = 0
pulse_end = 0
avgdist = 0
sumdist = 0
timelist = []

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

print "Starting Measurement..."

while True:
	for x in range(0, samples):
		GPIO.output(TRIG,0)
		time.sleep(0.1)

		GPIO.output(TRIG,1)
		time.sleep(0.00001)
		GPIO.output(TRIG,0)

		while GPIO.input(ECHO) == 0:
			pulse_begin = time.time()

		while GPIO.input(ECHO) == 1:
			pulse_end = time.time()

		pulse_width = (pulse_end - pulse_begin)
		print (pulse_width)
		timelist.append(pulse_width)

	timelist.sort(key=None)

	for y in range(discard, (samples - discard)):
		summedtimes += timelist[y]

	sumdist = summedtimes * 34300 * 0.5
	avgdist = int((sumdist / (samples - (discard * 2))))
	if avgdist > 2 and avgdist < 400:
		print ('Distance ',avgdist , ' cms')
	else:
		print ('Error reading ',avgdist , ' cms. Range 2-400cms')

	time.sleep(1)

GPIO.cleanup
