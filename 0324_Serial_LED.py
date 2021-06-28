from serial import Serial
import RPi.GPIO as GPIO
import time
#ser=Serial('COM0',9600) #window
ser=Serial('/dev/ttyACM0',9600)

GPIO.setmode(GPIO.BOARD)

LED0=11
LED1=13

GPIO.setup(LED0,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.LOW)

try:
    while True:
        if ser.readable():
            res=ser.readline()
            print(res.decode()[:len(res)-1])
            if res==(b'LED0 ON\r\n'):
                GPIO.output(LED0,GPIO.HIGH)
                LED1_state=False
                print(res.decode()[:len(res)-1])
                time.sleep(1)
            else:
                GPIO.output(LED0,GPIO.LOW)
                LED1_state=True
                print(res.decode()[:len(res)-1])
                time.sleep(1)
                
            if res==(b'LED1 ON\r\n'):
                GPIO.output(LED1,GPIO.HIGH)
                LED1_state=False
                print(res.decode()[:len(res)-1])
                time.sleep(1)
            else:
                GPIO.output(LED1,GPIO.LOW)
                LED1_state=True
                print(res.decode()[:len(res)-1])
                time.sleep(1)
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()
        
        