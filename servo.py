import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SAVO_PIN = 18

GPIO.setup(SAVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SAVO_PIN, 50)

pwm.start(0)


def set_angle(angle):

    duty = angle/(18+2)

    GPIO.output(SAVO_PIN, True)
    pwm.ChangeDutyCycle(duty)

    time.sleep(1)

    GPIO.output(SAVO_PIN, False)
    pwm.ChangeDutyCycle(0)

set_angle(360)
set_angle(180)
set_angle(90)
set_angle(45)

pwm.stop()
GPIO.cleanup()