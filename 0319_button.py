from tkinter import*
import sys
print(sys.argv)

def LED_Cntl():
    print("LED ON, LED OFF")

window=Tk() #위젯 창을 만들어주는 클래스

#화면을 구성하고 처리하는 코드
window.title("윈도우 버튼 연습")

#button1= Button(window, text="창 닫기",font=("맑은고딕",30),fg='red',command=quit)
button1= Button(window, text="창 닫기",fg='red',command=quit)
button2= Button(window, text="LED Cntl",fg='blue',command=LED_Cntl)

button1.pack()
button2.pack()

window.mainloop()