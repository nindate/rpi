import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Set Red LED to PIN 24
pin_red = 24
GPIO.setup(pin_red, GPIO.OUT)

# Set Yellow LED to PIN 12
pin_yellow = 12
GPIO.setup(pin_yellow, GPIO.OUT)

# Set Green LED to PIN 26
pin_green = 26
GPIO.setup(pin_green, GPIO.OUT)

for i in range(0,2,1):
	GPIO.output(pin_red, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(pin_red, GPIO.LOW)
	GPIO.output(pin_green, GPIO.HIGH)
	time.sleep(7)
	GPIO.output(pin_green, GPIO.LOW)
	GPIO.output(pin_yellow, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(pin_yellow, GPIO.LOW)
	GPIO.output(pin_red, GPIO.HIGH)
	time.sleep(2)

GPIO.cleanup()
