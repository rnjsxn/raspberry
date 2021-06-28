import RPi.GPIO as GPIO     # GPIO 모듈 입포트
import time                 # 시간 관련 모듈
import threading

GPIO.setmode(GPIO.BOARD)    # 

LED0,LED1 = 11,13

GPIO.setup((LED0,LED1), GPIO.OUT, initial=GPIO.LOW)

# 사용자 함수
def LED0_func():
    while True:
        GPIO.output(LED0, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(LED0, GPIO.LOW)
        time.sleep(0.3)

def LED1_func():
    while True:
        GPIO.output(LED1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED1, GPIO.LOW)
        time.sleep(0.5)

try:
    t1 = threading.Thread(target=LED0_func)
    t2 = threading.Thread(target=LED1_func)
    
    t1.start()
    t2.start()
    
    while True:
        pass

except KeyboardInterrupt:
    print("키보드 예외")
    
finally:
    print("Cleanup")
    GPIO.cleanup()