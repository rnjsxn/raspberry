class Car: #부모클래스
    speed=0    #맴버 변수

    def upSpeed(self,value): #속도 제한없음
        self.speed +=value
        print("현재 속도(부모클래스): %d" %self.speed)

    def downSpeed(self,value):  #스피드값 음수가 안되게 변경
        self.speed -=value

class Sedan(Car):  #car의 자식 클래스
    seatNum=0

    def getSetNum(self):  #속도를 150으로 제한하는 함수를 재정의
        return self.seatNum

    def upSpeed(self,value): #속도 제한없음
        self.speed +=value
        if self.speed>150:
            self.speed=150
        print("현재 속도(서브클래스): %d" %self.speed)

    def downSpeed(self,value):  #스피드값 음수가 안되게 변경
        self.speed -=value
        if self.speed<0:
            self.speed=0
        print("현재 속도(서브클래스): %d" %self.speed)

sedan1=Sedan()