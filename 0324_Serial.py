from serial import Serial
#ser=Serial('COM0',9600) #window
ser=Serial('/dev/ttyACM0',9600)

while True:
    if ser.readable():
        res=ser.readline()
        print(res.decode()[:len(res)-1]) #\-1
        print(res,type(res))
        
        #if res== b 'LED\r\n'
        #if res.decode()[:len(res)-1])
        
        #try:
    #while True:
        #if ser.readable():
           # res=ser.readline()
           # r=(str(res))
           # if res==(b'LED ON\r\n'):
              #  GPIO.output(LED1,GPIO.HIGH)
               # LED1_state=False
               # print(res.decode()[:len(res)-1])
           # else:
               # GPIO.output(LED1,GPIO.LOW)
               # LED1_state=True
               # print(res.decode()[:len(res)-1])