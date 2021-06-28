import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED= 11
Sw=7

GPIO.setup(LED,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(Sw,GPIO.IN)

try:
    while True:
        key_in=GPIO.input(Sw)
        print(key_in)
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()
