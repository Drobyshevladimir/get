import RPi.GPIO as GPIO
from time import sleep
def decimal2binary(chislo):
    return [int(element) for element in bin(chislo)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
p = GPIO.PWM(21,  100)
p.start(0)
try:
    while True:
        t=int(input())
        p.ChangeDutyCycle(t)
        print((1000*3.3*t/100)//1/1000)
        sleep(0.5)
except ValueError:
    print('wrong value')
p.stop()
GPIO.output(21,0)
GPIO.cleanup()