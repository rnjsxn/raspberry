class Car:
    color= ""  #맴버 변수
    speed=0    #맴버 변수
    name=""    #맴버 변수
    count=0

    #생성자
    def __init__(self,value1="빨강",value2=0,value3="현대"):
        print("생성자호출완료 ")
        self.color=value1 #self.변수명(인스턴스변수)
        self.speed=value2
        self.name=value3
        Car.count+=1  #클래스이름.변수명(클래스변수) 클래스+1증가

    def speedPrint(self): #맴버함수는 반드시 매개변수로 self를 반드시 포함.
        print(self.speed)

    def colerPirnt(self):
        print(self.color)

    def upSpeed(self,value):
        self.speed +=value

    #def downSpeed(self,value): 
        #self.speed -=value
    def downSpeed(self,value):  #스피드값 음수가 안되게 변경
        self.speed -=value
        if self.speed<0:
            self.speed =0

    def chageColor(self,color):
        self.color=value

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getColor(self):
        return self.color

    def getMemberVar(self,value): #name,speed,color
        if value=='name':
            return self.name
        elif value=='speed':
            return self.speed
        elif value=='color':
            return self.color
        else: 
            return None

    def __del__(self):
        Car.count-=1

# myCar1=Car() #인스턴스 생성

# print("맴버변수 출력= ",myCar1.speed)
# print("맴버함수를 이용한 출력= ", end="")
# myCar1.speedPrint()
# myCar1.upSpeed(100)
# myCar1.speedPrint()

# myCar1.chageColor('blue')
# myCar1.colerPirnt()

# print("*"*30)
# myCar1.downSpeed(150)
# myCar1.speedPrint()

# print("*"*30)

# myCar2=Car("파랑",30)
# myCar2.speedPrint()
# myCar2.colerPirnt()

# print("*"*30)
# myCar3=Car()
# print(myCar3.getName(),myCar3.getSpeed(),myCar3.getColor())
# print(myCar3.getMemberVar('name'),myCar3.getMemberVar('speed'),myCar3.getMemberVar('color'))
myCar1=Car()
myCar1.speed=30
print("자동차1의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대 입니다." 
        %(myCar1.speed,Car.count)) #클래스 변수

myCar2=Car()
myCar2.speed=100
print("자동차1의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대 입니다." 
        %(myCar2.speed,Car.count))

myCar3=myCar1
myCar3.speed=80
print("자동차1의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대 입니다." 
        %(myCar3.speed,Car3.count)) 

print(hex(id(myCar1.speed)))
print(hex(id(myCar3.speed)))

del myCar1
del myCar2
del myCar3
print(Car.count)