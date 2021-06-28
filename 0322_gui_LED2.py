from tkinter import *
import RPi.GPIO as GPIO
import time

window = Tk()        # 위젯 창을 만드는 클래스

window.title("LED CONT")
window.geometry("400x210")

GPIO.setmode(GPIO.BOARD)
LED1=19
LED2=11
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.LOW)
LED1_state=False
LED2_state=False

#Hardware

def LED1_Cntl():
    global LED1_state
    if LED1_state==False:
        GPIO.output(LED1,GPIO.HIGH)
        #led1_bin['text']="LED1 ON"
        #led1_bin['fg']='red'
        led1_bin.config(text="LED1 ON",bg="#60d4d4")
        LED1_state= True 
    else:
        GPIO.output(LED1,GPIO.LOW)
        #led1_bin['text']="LED1 OFF"
        #led1_bin['fg']='blue'
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
    led1_bin= Button(window, text="LED1 ON/OFF", font=("맑은 고딕", 15), bd=7, bg="#60d4d4",
                fg="#803737", relief='groove',command=LED1_Cntl)
    
    led2_bin= Button(window, text="LED2 ON/OFF", font=("맑은 고딕", 15), bd=7, bg="#60d4d4",
                fg="#803737", relief='groove',command=LED2_Cntl)
    
    led1_bin.place(x=50, y=80, width=140, height=50)
    led2_bin.place(x=210, y=80, width=140, height=50)

    window.mainloop()
    
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()

