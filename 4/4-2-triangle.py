import RPi.GPIO as GPIO
import time
def decimal2binary(chislo):
    return [int(element) for element in bin(chislo)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

vremya = float(input())
min = int(input())
max = int(input())
vremya=vremya/((max-min)*2-2)
num = min
a=0
while True:
    while num<max:
        binchislo= decimal2binary(num)
        GPIO.output(dac, binchislo)
        num+=1
        time.sleep(vremya)
    while num>min:
        binchislo= decimal2binary(num)
        GPIO.output(dac, binchislo)
        num-=1
        time.sleep(vremya)
    a+=1

GPIO.output(dac, 0)
GPIO.cleanup()