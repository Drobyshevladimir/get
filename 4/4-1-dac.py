import RPi.GPIO as GPIO

def decimal2binary(chislo):
    return [int(element) for element in bin(chislo)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)


dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
print('введите число')
chislo = input()
while not chislo == 'q':
    try:
        chislo=int(chislo)
        if chislo>-1 and chislo <256:
            binchislo= decimal2binary(chislo)
            print((3.3*chislo/256*1000)//1/1000)
        


            GPIO.output(dac, binchislo)
        else:
            print('wrong type')
    except Exception:
        print('wrong type')
    print('введите число')
    chislo=input()



GPIO.output(dac, 0)
GPIO.cleanup()