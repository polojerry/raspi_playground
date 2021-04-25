import RPi.GPIO as GPIO
import time

import light as LIGHTS
import proximity_sensor as PROXIMITY
import relay_motor as RELAY

SLEEP_TIME = 0.005

#SETING MODE
GPIO.setmode(GPIO.BCM)

try :
    while True: 
        PROXIMITY.proximity_trigger_low()
        print("Waiting to settle")
        time.sleep(0.5)

        print("calculating the distance")
        PROXIMITY.proximity_trigger_high
        time.sleep(0.00001)
        PROXIMITY.proximity_trigger_low()

        while GPIO.input(PROXIMITY.ECHO) == 0:
            start_time = time.time()

        while GPIO.input(PROXIMITY.ECHO) == 1:
            end_time = time.time()

    
        distance = PROXIMITY.calculate_distance(start_time,end_time)
        print("Distance: ", distance, "cm")

        if(distance <10):
            LIGHTS.warning_on() 
            RELAY.motor_off()
        else :
            LIGHTS.lights_off()
            RELAY.motor_on()

except KeyboardInterrupt :
    GPIO.cleanup()




