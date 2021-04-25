import RPi.GPIO as GPIO
import time

#PROCIMITY SENSOR PINS
ECHO = 27
TRIG = 17

#PROCIMITY SENSOR SETUP
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def proximity_trigger_high():
    GPIO.output(TRIG, GPIO.HIGH)

def proximity_trigger_low():
    GPIO.output(TRIG, GPIO.LOW)

def calculate_distance(start_time, end_time):
    pulse_duration = end_time - start_time
    distance = pulse_duration * 17150
    return distance