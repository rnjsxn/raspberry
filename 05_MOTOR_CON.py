import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

MOTOR_P=11
MOTOR_N=13
MOTOR_EN=15
dc= [0,1,2,3,4,5,6,7,8,9,10,12,13,15,10,30,50,70,100]

GPIO.setup(MOTOR_P,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(MOTOR_N,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(MOTOR_EN,GPIO.OUT)

p= GPIO.PWM(MOTOR_EN,100)
p.start(0)


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