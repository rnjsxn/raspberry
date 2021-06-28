import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED= 11
Sw=7
LED_state=False

GPIO.setup(LED,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(Sw,GPIO.IN)

try:
    while True:
        key_in=GPIO.input(Sw)
        print(key_in)
        if key_in==0: 
            GPIO.output(LED,GPIO.HIGH)
            LED_state=False
        else:
            GPIO.output(LED,GPIO.LOW)
            LED_state=True
        
        time.sleep(0.3)
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()

