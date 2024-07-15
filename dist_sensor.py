"""
Distance sensor
"""
import RPi.GPIO as GPIO
import time 

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # make sure it is not active first
    GPIO.output(TRIG, False)
    time.sleep(2)

    # Activate pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the time taken for the ECHO pin (what receives the signal) to go
    # from high to low
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start

    # Calculate distance, speed of sound is 34300 cm/s
    speed_of_sound = 34300
    distance = pulse_duration * (speed_of_sound/2)

    return distance

try:
    while True:
        dist = measure_distance()
        print(f'Distance: {dist:.2f} cm')
        time.sleep(1)
except KeyboardInterrupt:
    print('Program interrupted by User.')

finally:
    GPIO.cleanup()

 
