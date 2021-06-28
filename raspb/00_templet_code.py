from tkinter import *
import RPi.GPIO as GPIO     # GPIO 모듈 입포트
import time                 # 시간 관련 모듈
import threading
from PIL import Image,ImageTk

# =========================== 하드웨어 설정 =================================
GPIO.setmode(GPIO.BOARD)

# 1. LED 설정 
led0_state = False
led1_state = False
LED0, LED1 = 11, 13
GPIO.setup((LED0, LED1), GPIO.OUT)

# 2. FND 설정
FND_DATA = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x27,
            0x7F,0x67,0x77,0x7C,0x39,0x5E,0x79,0x71]
FND_DATA_PIN =[19,21,23,29,31,33,35,37]  # A~DP
FND_DIGIT_PIN =[24,26,32,36,38,40]        # D5 ~ D0
GPIO.setup(FND_DATA_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FND_DIGIT_PIN, GPIO.OUT, initial=GPIO.HIGH)

# 사용자함수 
def FND_Display(num6):
    num6_list = list(str(num6))
    # print(num6_list)

    for i in range(6):
        GPIO.output(FND_DIGIT_PIN[i], GPIO.LOW)  # digit 이동
        for j in range(8):
            GPIO.output(FND_DATA_PIN[j], FND_DATA[int(num6_list[i])] & (0x01<<j))
        time.sleep(0.001)
        GPIO.output(FND_DIGIT_PIN[i], GPIO.HIGH)
        
try:
    while True:
        FND_Display(123456)
        

except KeyboardInterrupt:
    print("키보드 예외")
    
finally:
    print("Cleanup")
    GPIO.cleanup()
