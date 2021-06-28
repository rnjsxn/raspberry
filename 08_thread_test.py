import threading
import time

val=0

def add_func():
    global val
    while True:
        val+=1
        time.sleep(1)

def sub_func():
    global val
    while True:
        val-=1
        time.sleep(0.5)


try:
    t1=threading.Thread(target=add_func)
    t2=threading.Thread(target=sub_func)
    
    t1.start()
    t2.start()
    
    while True:
        print(val)
        time.sleep(1.1)
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    print("cleanup")
    GPIO.cleanup()
