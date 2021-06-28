import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
      #a,b, c, d, e, f, g, h
D_PIN=[19,21,23,29,31,33,35,37]
F_PIN=[24,26,32,36,38,40]
FND_DATA = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x27,0x7F,0x6F
            ,0x77,0x7c,0x39,0x5E,0x79,0x71]
GPIO.setup(D_PIN,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(F_PIN,GPIO.OUT,initial=GPIO.HIGH)

try:
    for i in F_PIN:
        GPIO.output(i,GPIO.LOW)
    
    for i in FND_DATA:
        for j in range(0,8):
            GPIO.output(D_PIN[j], i &(0x01 << j))
        time.sleep(0.7)    
    while True:
        pass
    
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()

    
