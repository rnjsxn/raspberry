import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BOARD)

LED1=11
LED2=13

GPIO.setup(LED1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.LOW)

def LED1_func():
    while True:
        GPIO.output(LED1,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(LED1,GPIO.LOW)
        time.sleep(0.3)
        
def LED2_func():
    while True:
        GPIO.output(LED2,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(LED2,GPIO.HIGH)
        time.sleep(0.3)

try:
    t1=threading.Thread(target=LED1_func)
    t2=threading.Thread(target=LED2_func)
    
    t1.start()
    t2.start()

    while True:
        pass
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()