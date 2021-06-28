from tkinter import *
import RPi.GPIO as GPIO     # GPIO 모듈 입포트
import time                 # 시간 관련 모듈
import threading
from PIL import Image, ImageTk

#=========================== 윈도우 창 설정 =================================
window = Tk()        # 위젯 창을 만드는 클래스

window.title("FND6 출력")
window.geometry("500x250")

#=========================== 전역변수 =================================
data = '000000'

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
FND_DIGIT_PIN =[24,26,32,36,38,40] 
GPIO.setup(FND_DATA_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FND_DIGIT_PIN, GPIO.OUT, initial=GPIO.HIGH)

# 사용자함수
def LED0_Cntl():
    global led0_state
    if led0_state==False:
        label_LED0.config(state=NORMAL)
        #led0_btn.config(text="LED0 ON", fg="red")
        led0_state = True
    else:
        label_LED0.config(state=DISABLED)
        led0_state = False

def LED1_Cntl():
    global led1_state
    if led1_state==False:
        label_LED1.config(state=NORMAL)
        led1_state = True
    else:
        label_LED1.config(state=DISABLED)
        led1_state = False
        
def FND_disp(a):
    global data
    print("숫자가 입력됐습니다.")
    data = entry_FND.get()
    print(type(data), data)

def FND_Display(num6):
    #num6_list = list(str(num6))
    num6_list = list("%06d" % num6)
    # print(num6_list)

    for i in range(6):
        GPIO.output(FND_DIGIT_PIN[i], GPIO.LOW)  # digit 이동
        for j in range(8):
            GPIO.output(FND_DATA_PIN[j], FND_DATA[int(num6_list[i])] & (0x01<<j))
        time.sleep(0.001)
        GPIO.output(FND_DIGIT_PIN[i], GPIO.HIGH)

# 쓰레드 함수
def Thread_FND6():
    global data
    while True:
        FND_Display(int(data))
        
        if thread_stop==True:
            break
        
def Thread_LED0():
    while True:
        if led0_state==True:
            GPIO.output(LED0, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(LED0, GPIO.LOW)
            time.sleep(0.3)
        else:
            GPIO.output(LED0, GPIO.LOW)
            
        if thread_stop==True:
            break

def Thread_LED1():
    while True:
        if led1_state==True:
            GPIO.output(LED1, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED1, GPIO.LOW)
            time.sleep(0.5)
        else:
            GPIO.output(LED1, GPIO.LOW)
        
        if thread_stop==True:
            break

try:
    thread_stop = False
    t1 = threading.Thread(target=Thread_FND6)
    t2 = threading.Thread(target=Thread_LED0)
    t3 = threading.Thread(target=Thread_LED1)
    
    t1.start()
    t2.start()
    t3.start()
    
    # GUI 설정
    # FND
    img_FND = Image.open('image_file/FND.png')
    disp_FND = ImageTk.PhotoImage(img_FND)
    label_FND = Label(window, image=disp_FND)    
    label_FND.place(x=10, y=10)
    
    label_help = Label(window, text='Input Data\n(0~999999)',\
                       font=('time', 11, 'bold'), bg='#004483', fg='white')
    label_help.place(x=10, y=70)
    
    entry_FND = Entry(window, text='Input FND Data', width=6,\
                      font=('time', 19, 'bold'), justify='right')
    entry_FND.place(x=110, y=72)
    entry_FND.bind('<Return>', FND_disp)
    
    # LED
    img_LED0 = Image.open('image_file/LED_ON.png')
    disp_LED0 = ImageTk.PhotoImage(img_LED0)
    label_LED0 = Label(window, image=disp_LED0, state=DISABLED)    
    label_LED0.place(x=30, y=125)
    
    img_LED1 = Image.open('image_file/LED_ON.png')
    disp_LED1 = ImageTk.PhotoImage(img_LED1)
    label_LED1 = Label(window, image=disp_LED1, state=DISABLED)    
    label_LED1.place(x=130, y=125)
    
    led0_btn = Button(window, text="LED0", font=("맑은 고딕", 12),
                     bd=7, bg="#60d4d4", fg="#803737", relief='groove', command=LED0_Cntl)
    led1_btn = Button(window, text="LED1", font=("맑은 고딕", 12),
                     bd=7, bg="#60d4d4", fg="#803737", relief='groove', command=LED1_Cntl)

    led0_btn.place(x=10, y=200)
    led1_btn.place(x=110, y=200)
    
    window.mainloop()
    
except KeyboardInterrupt:
    print("키보드 예외")
    
finally:
    thread_stop = True
    t1.join()   # 쓰레드가 종료 될때까지 대기
    print("Cleanup")
    GPIO.cleanup()
