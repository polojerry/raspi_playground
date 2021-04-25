import RPi.GPIO as GPIO
import time 

#PIN CONSTANTS
GREEN = 4
WHITE = 19
YELLOW = 6
RED = 5
BLUE = 21

SLEEP_TIME = 0.005

#SETING MODE
GPIO.setmode(GPIO.BCM)

#LEDS SETUP
GPIO.setup(WHITE, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)


def lights_on(color):
    GPIO.output(color, GPIO.HIGH)

def lights_off(color):
    GPIO.output(color, GPIO.LOW)

def delay():
    time.sleep(SLEEP_TIME)

def lights_on_off(color):
    lights_on(color)
    delay()
    lights_off(color)

def warning_on():
    lights_on(RED)
    delay()
    lights_off(RED)

    lights_on(WHITE)
    delay()
    lights_off(WHITE)

    lights_on(YELLOW)
    delay()
    lights_off(YELLOW)

    lights_on(GREEN)
    delay()
    lights_off(GREEN)

    lights_on(BLUE)
    delay()
    lights_off(BLUE)

def warning_off():
  
    lights_off(RED)
    lights_off(WHITE)
    lights_off(YELLOW)
    lights_off(GREEN)
    lights_off(BLUE)