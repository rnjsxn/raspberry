import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED=11
Sw=5

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Sw,GPIO.IN)

def LED_Cntl(channel):
    print(channel)
    global LED_state
    if LED_state==False:
        GPIO.output(LED,GPIO.HIGH)
        LED_state= True
    else:
        GPIO.output(LED,GPIO.LOW)
        LED_state= False

try:
    LED_state=False
    GPIO.add_event_detect(Sw,GPIO.FALLING,callback=LED_Cntl)
    while True:
        pass
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()



