from tkinter import *
import RPi.GPIO as GPIO
import time                
import threading
from PIL import Image,ImageTk #image file

window = Tk()        

window.title("FND6 output")
window.geometry("400x400")

data='0000000'

GPIO.setmode(GPIO.BOARD)

# 1. LED 설정 
LED1=11
LED2=13

GPIO.setup(LED1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.LOW)
LED1_state=False
LED2_state=False

# 2. FND 설정
FND_DATA = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x27,
            0x7F,0x67,0x77,0x7C,0x39,0x5E,0x79,0x71]
FND_DATA_PIN =[19,21,23,29,31,33,35,37]  # A~DP
FND_DIGIT_PIN =[24,26,32,36,38,40]        # D5 ~ D0
GPIO.setup(FND_DATA_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FND_DIGIT_PIN, GPIO.OUT, initial=GPIO.HIGH)

# 사용자함수

def FND_disp(a):
    global data
    print("Number input ")
    data=entry_FND.get()
    print(type(data),data)
    
def FND_Display(num6):
    num6_list = list("%06d" %num6)
    #print(num6_list)
    for i in range(6):
        GPIO.output(FND_DIGIT_PIN[i], GPIO.LOW)  # digit 이동
        for j in range(8):
            GPIO.output(FND_DATA_PIN[j], FND_DATA[int(num6_list[i])] & (0x01<<j))
        time.sleep(0.001)
        GPIO.output(FND_DIGIT_PIN[i], GPIO.HIGH)
        
def Thread1_func():
    global data
    while True:
        FND_Display(int(data))
        
        if thread_stop==True:
            break
        
def LED1_func():
    global LED1_state
    while True:
        if LED1_state==True:
            GPIO.output(LED1,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(LED1,GPIO.LOW)
            time.sleep(0.3)
        else:
            GPIO.output(LED1,GPIO.LOW)
            
        if thread_stop==True:
            break
        
def LED2_func():
    global LED2_state
    while True:
        if LED2_state==True:
            GPIO.output(LED2,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(LED2,GPIO.LOW)
            time.sleep(0.3)
        else:
            GPIO.output(LED2,GPIO.LOW)
            
        if thread_stop==True:
            break
        
def LED1_Cntl():
    global LED1_state
    if LED1_state==False:
        GPIO.output(LED1,GPIO.HIGH)
        led1_bin.config(text="LED1 ON",bg="#60d4d4")
        LED1_state= True 
    else:
        GPIO.output(LED1,GPIO.LOW)
        led1_bin.config(text="LED1 OFF",bg="#60d4d4")
        LED1_state= False
              
def LED2_Cntl():
    global LED2_state
    if LED2_state==False:
        GPIO.output(LED2,GPIO.HIGH)
        #led2_bin['text']="LED2 ON"
        #led2_bin['fg']='red'
        led2_bin.config(text="LED2 ON",bg="#60d4d4")
        LED2_state= True
    else:
        GPIO.output(LED2,GPIO.LOW)
        #led2_bin['text']="LED2 OFF"
        #led2_bin['fg']='red'
        led2_bin.config(text="LED2 OFF",bg="#60d4d4")
        LED2_state= False
         
try:
    #thread Setting
    thread_stop=False
    t1=threading.Thread(target=Thread1_func) 
    t2=threading.Thread(target=LED1_func)
    t3=threading.Thread(target=LED2_func)
    
    t1.start()
    t2.start()
    t3.start()
    
    #GUI Setting
    img_FND=Image.open('image_file/FND.png')
    disp_FND=ImageTk.PhotoImage(img_FND)
    label_FND=Label(window,image=disp_FND)
    
    img_LED=Image.open('image_file/LED_ON.png')
    disp_LED=ImageTk.PhotoImage(img_LED)
    label_LED=Label(window,image=disp_LED)
    
    label_help=Label(window,text='Input Data\n(0~999999)',\
                     font=('time',14,'bold'),bg='#004483',fg='white')
    
    led1_bin= Button(window, text="LED1 ON/OFF", font=("맑은 고딕", 15), bd=7, bg="#60d4d4",
                fg="#803737", relief='groove',command=LED1_Cntl)
    
    entry_FND=Entry(window,text='Input FND Data',\
                    width=6,font=('time',19,'bold'),justify='right')
    
    entry_FND.bind('<Return>',FND_disp)
    
    label_FND.pack()
    label_help.pack()
    entry_FND.pack()
    led1_bin.place(x=50, y=80, width=140, height=50)
    led2_bin.place(x=210, y=80, width=140, height=50)
    
    window.mainloop()
    
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    thread_stop=True
    t1.join() #thread finish ->wait
    t2.join()
    t3.join()
    print("cleanup")
    GPIO.cleanup()
