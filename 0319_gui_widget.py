from tkinter import*

window=Tk()#className='기본 윈도우'#) #위젯 창을 만들어주는 클래스
#window2=Tk()

#화면을 구성하고 처리하는 코드
window.title("윈도우 창 연습")
#window.geometry("400X100")
#window.resizable(width=FALSE,height=FALSE)

#label
label1=Label(window,text="SWEDU~~ Python을")
label2=Label(window,text="열심히",font=("궁서체",30),fg='blue')
label3=Label(window,text="공부 중입니다.",bg='#FF0000',width=20,height=5,anchor=SE)

label1.pack() #라벨을 화면 표시
label2.pack()
label3.pack()

window.mainloop() #실행, 나가기 버튼을 누르기전에는 무한루프
# window2.mainloop() #window1을 실행 후 종료하면 window2가 실행이됨.

