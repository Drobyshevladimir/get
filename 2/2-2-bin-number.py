import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [1, 1, 1, 1, 1, 1, 1, 1]
GPIO.setup(dac, GPIO.OUT)
for i in range(len(dac)):
    GPIO.output(dac[i], number[i])
time.sleep(10)
GPIO.output(dac, 0)
GPIO.cleanup()
