
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
btn_pin = 17
led_pin = 18

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        btn_state = GPIO.input(btn_pin)

        if btn_state == GPIO.LOW: # Button has been pressed
            GPIO.output(led_pin, GPIO.HIGH) # Turn on the LED
            print('LED turned on.')
        else:
            GPIO.output(led_pin, GPIO.LOW) # Turn off the LED
except KeyboardInterrupt:
    print('Program interrupted by User.')

finally:
    GPIO.cleanup()


