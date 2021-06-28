import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED= 19
dc= [0,1,2,3,4,5,6,7,8,9,10,12,13,15,10,30,50,70,100]

GPIO.setup(LED,GPIO.OUT)

p= GPIO.PWM(LED,100) #100Hz
p.start(0)           #dutycycle = 0

try:
    while True:
        for val in dc:
            p.ChangeDutyCycle(val)
            time.sleep(0.5)
        dc.reverse()    
        
except KeyboardInterrupt:
    p.stop()
    
finally:
    print("Cleanup")
    GPIO.Cleanup()

