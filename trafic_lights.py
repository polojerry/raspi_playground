import RPi.GPIO as GPIO
import time 

GREEN = 19
BLUE = 13
RED = 5

SLEEP_TIME = 3

GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

try :
    while True :
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(SLEEP_TIME)

        GPIO.output(BLUE, GPIO.HIGH)
        time.sleep(SLEEP_TIME)

        GPIO.output(RED, GPIO.HIGH)
        time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
    GPIO.cleanup()
    