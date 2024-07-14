"""
Implements a LED using a Raspberry Pi.
Runs a S.O.S. signal.
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 18

# sets the pin as an output
GPIO.setup(led_pin, GPIO.OUT)
def turn_on_led(led_pin, secs, loop = 1):
    for i in range(loop):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(secs)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)
try:
    while True:
        turn_on_led(led_pin, 1, 3)
        turn_on_led(led_pin, 2, 3)
        turn_on_led(led_pin, 1, 3)


except KeyboardInterrupt:
    print('Program stopped by user.')

finally:
    GPIO.cleanup()

    