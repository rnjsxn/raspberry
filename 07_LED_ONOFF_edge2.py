import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED1=11
LED2=13
Sw1=16
Sw2=18

GPIO.setup(LED1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Sw1,GPIO.IN)
GPIO.setup(Sw2,GPIO.IN)

def LED1_Cntl(channel):
    print(channel)
    global LED1_state
    if Sw1==16:
        if LED1_state==False:
            GPIO.output(LED1,GPIO.HIGH)
            LED1_state= True
            print("LED1_ON")
        else:
            GPIO.output(LED1,GPIO.LOW)
            LED1_state= False
            print("LED1_OFF")
        
def LED2_Cntl(channel):
    print(channel)
    global LED2_state
    if Sw2==18:
        if LED2_state==False:
            GPIO.output(LED2,GPIO.HIGH)
            LED2_state= True
            print("LED2_ON")
        else:
            GPIO.output(LED2,GPIO.LOW)
            LED2_state= False
            print("LED2_OFF")

try:
    LED1_state=False
    LED2_state=True
    GPIO.add_event_detect(Sw1,GPIO.FALLING,callback=LED1_Cntl) #attachInterrupt
    GPIO.add_event_detect(Sw2,GPIO.FALLING,callback=LED2_Cntl)
    while True:
        pass
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()





