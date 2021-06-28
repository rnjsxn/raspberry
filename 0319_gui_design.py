from tkinter import *

window = Tk()        # 위젯 창을 만드는 클래스

window.title("윈도우 창 연습")
window.geometry("400x210")


button1 = Button(window, text="button A", font=("맑은 고딕", 15), bd=7, bg="#60d4d4", fg="#803737", relief='groove')
button2 = Button(window, text="button B", font=("맑은 고딕", 15), bd=7, bg="#60d4d4", fg="#803737", relief='groove')
button3 = Button(window, text="button C", font=("맑은 고딕", 15), bd=7, bg="#60d4d4", fg="#803737", relief='groove')
button4 = Button(window, text="button D", font=("맑은 고딕", 15), bd=7, bg="#60d4d4", fg="#803737", relief='groove')


button1.place(x=50, y=20, width=300, height=50)
button2.place(x=50, y=80, width=140, height=50)
button3.place(x=210, y=80, width=140, height=50)
button4.place(x=50, y=140, width=300, height=50)


window.mainloop()

