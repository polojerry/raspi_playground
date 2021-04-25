import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RELAY_RC_PIN = 21

GPIO.setup(RELAY_RC_PIN, GPIO.OUT)


def switch_():
    number = int(input('''
    Enter:
    1 for On,
    2 for Off
    
    '''))

    try :

        if(number == 1):
            GPIO.output( RELAY_RC_PIN, GPIO.HIGH)
        elif(number == 2 ):
            GPIO.output(RELAY_RC_PIN, GPIO.LOW)
        else:
            print("Invalid Input")    
    
    except KeyboardInterrupt:
        GPIO.cleanup()

switch_()