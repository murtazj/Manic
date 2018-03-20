#Interface the input of the sensor
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(13, GPIO.OUT)         #LED output pin

count=0

while True:
       i=GPIO.input(12)
      
       if i==1:
              #When output from motion sensor is LOW
             GPIO.output(13, 1)  #Turn OFF LED
             #print(i)
             count=count+1
             print("Sensor Count is ",count)
             

             while(i!=0):
                    i=GPIO.input(12)

             
 
       elif i<1:               #When output from motion sensor is HIGH
             GPIO.output(13, 0)  #Turn ON LED
             #print(i)

             while(i==0):
                    i=GPIO.input(12)

             
