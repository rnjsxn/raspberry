class Car: #부모클래스
    speed=0    #맴버 변수

    def upSpeed(self,value):
        self.speed +=value

    #def downSpeed(self,value): 
        #self.speed -=value
    def downSpeed(self,value):  #스피드값 음수가 안되게 변경
        self.speed -=value

class Sedan(Car):  #car의 자식 클래스
    seatNum=0

    def getSetNum(self):
        return self.seatNum

class Truck(Car):
    capacity=0

    def getCapacity(self):
        return self.capacity

sedan1=Sedan()
truck1=Truck()

print(sedan1.speed)
print(truck1.speed)

sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.seatNum=5
truck1.capacity=50

print("승용차의 속도는 %dkm, 좌석수는 %d개입니다." %(sedan1.upSpeed,sedan1.getSetNum()))
print("트럭의 속도는 %dkm, 총중량은 %d개입니다." %(truck1.upSpeed,truck1.getSetNum()))

