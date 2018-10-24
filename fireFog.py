import RPi.GPIO as GPIO
import time

sensor=8
buzzer=40

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

while True:
    if(GPIO.input(sensor)==0):
        print('Flame Detected')
        GPIO.output(buzzer,True)
        time.sleep(1)

    if(GPIO.input(sensor)==1):
        #print('No Flame. Safe.')
        GPIO.output(buzzer,False)
        time.sleep(1)
