from tkinter import*

def myFunc():
    print(chk.get())
    if chk.get()==1:
        print("버튼 확인")
    else:
        print("버튼 no")

window=Tk() #위젯 창을 만들어주는 클래스

#화면을 구성하고 처리하는 코드
window.title("윈도우 체크버튼 연습")
window.geometry("200x100")

#checkButton
chk=IntVar()
cb1= Checkbutton(window,text="클릭하세요",variable=chk,command=myFunc)

cb1.pack()

window.mainloop()