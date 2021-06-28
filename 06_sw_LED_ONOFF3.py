import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED= 11
Sw=7

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Sw,GPIO.IN)

try:
    LED_state=False
    while True:
        key_in=GPIO.input(Sw)
        print(key_in)
        if key_in==0:
            if LED_state==False:
                GPIO.output(LED,GPIO.HIGH)
                LED_state= True
            else:
                GPIO.output(LED,GPIO.LOW)
                LED_state= False
        else:
            pass
        
        time.sleep(0.3)
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()


