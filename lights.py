import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 16
AMBER = 8
GREEN = 21

SLEEP_TIME = 2

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(AMBER, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

try:
    while True:
        GPIO.output(RED, GPIO.HIGH)
        print("STOP")
        time.sleep(SLEEP_TIME)
        GPIO.output(RED, GPIO.LOW)
        

        GPIO.output(AMBER, GPIO.HIGH)
        print("GET READY....")
        time.sleep(SLEEP_TIME)
        GPIO.output(AMBER, GPIO.LOW)
      

        GPIO.output(GREEN, GPIO.HIGH)
        print("GO.....")
        time.sleep(1)
        GPIO.output(GREEN, GPIO.LOW)
        

except KeyboardInterrupt:
    GPIO.cleanup()