import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED= 19
GPIO.setup(LED,GPIO.OUT)

try:
    while True:
        GPIO.output(LED,GPIO.LOW) #LED OFF
        
finally:
    print("Cleanup")
    GPIO.cleanuop()

    
    
