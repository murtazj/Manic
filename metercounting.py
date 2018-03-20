#Interface the input of the sensor
import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(5, GPIO.OUT)         #LED output pin
#os.system('python meterupload.py')
count=0

while True:
    sensor=GPIO.input(7)
    #print("%s"%sensor)
    while(count<=160 and sensor==1):
        count=count+1
        print("%s gg",count)
        if(count==160):
            GPIO.output(5,1)

            time.sleep(0.01)
    
            GPIO.output(5,0)
            count=0

            
        while(sensor!=0):
            sensor=GPIO.input(7)









            

                
                
    
        

















