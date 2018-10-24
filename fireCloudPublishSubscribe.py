import RPi.GPIO as GPIO
import time
import sys
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import ssl

sensor=8
buzzer=38

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

def alarm(client,userdata,message):
    GPIO.output(buzzer,True)

# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("123afhlss456")
myMQTTClient.configureEndpoint("XXXXXXXXXXX.iot.us-west-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Desktop/cert/CA.crt", "/home/pi/Desktop/cert/XXXXXXXXXX-private.pem.key", "/home/pi/Desktop/cert/XXXXXXXXXX-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
 
#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("rpi/connect", "connected", 0)

while True:
    GPIO.output(buzzer,False)
    if(GPIO.input(sensor)==0):
        payload='{"sensor":"fire"}'
        print(myMQTTClient.publish("rpi/fire", payload, 0))
        myMQTTClient.subscribe("rpi/fire",1,alarm)
        time.sleep(1)
