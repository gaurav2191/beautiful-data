import Driver
import time

def executeSomething():
    Driver.Driver().run('..\config.txt')
    print "The code run at: ", time.asctime(time.localtime(time.time()))   
    time.sleep(10)

while True:
    executeSomething()
