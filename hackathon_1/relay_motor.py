import RPi.GPIO as GPIO
import time

#SETING MODE
GPIO.setmode(GPIO.BCM)

#RELAY CONSTANT
RELAY_IN_1 = 16

#RELAY SETUP
GPIO.setup(RELAY_IN_1,GPIO.OUT)

def motor_on():
    GPIO.output(RELAY_IN_1, GPIO.HIGH)

def motor_off():
    GPIO.output(RELAY_IN_1, GPIO.LOW)