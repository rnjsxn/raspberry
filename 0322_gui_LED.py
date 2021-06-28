from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED,GPIO.OUT,initial=GPIO.HIGH)

LED=11

def myFunc1():
    print(chk.get())
    if chk.get()==1:
        print("LED ON")
        
    else:
        print("LED OFF")

window = Tk()   

window.title("LED CONT")
window.geometry("400x210")

chk=IntVar()

cd1 = Checkbutton(window, text="LED ON/OFF",variable=chk,command=myFunc1)

cd1.pack()

window.mainloop()



