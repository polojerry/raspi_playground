import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(40, GPIO.OUT)

try:
    while True:
        GPIO.output( , GPIO.HIGH)
        print("Light Onnnnnnnn")

        time.sleep(2)

        GPIO.output(40, GPIO.LOW)
        print("Light offffff")

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()