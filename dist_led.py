"""
dist_light_sensor.py

Uses a distance and light sensor. If distance is greater than certain threshold it will
light the LED.
"""
import RPi.GPIO as GPIO
import time

led_pin = 18
trig_pin = 23
echo_pin = 24
THRESH = 60

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def measure_distance():
    
    # Ensure that Trig pin is inactive 
    GPIO.output(trig_pin, False)
    time.sleep(2)


    # Send pulse
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    # Now measure how long it takes Echo pin to go from low to high
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    # Calculate distance
    pulse_duration = pulse_end - pulse_start
    speed_of_sound = 34300
    distance = pulse_duration * (speed_of_sound/2)
    return distance 


try:
    while True:
        distance = measure_distance()
        if distance < THRESH:
            print(f'Too close! Step back!\n {distance:.2f}')
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Program interrupted by User.')

finally:
    GPIO.cleanup()


    
        