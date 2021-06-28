import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED= 19,21,23,29,31,33,35,37
GPIO.setup(LED,GPIO.OUT)

while True:
    for i in LED:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(0.5)