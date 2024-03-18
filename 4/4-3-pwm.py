import RPi.GPIO as GPIO

def decimal2binary(chislo):
    return [int(element) for element in bin(chislo)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24,100)
p.start(1)
p.stop()
input()
p.stop()
GPIO.cleanup()
#while True:
#    a=float(input())
 #   p = GPIO.PWM(24,a)



