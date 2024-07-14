"""
Implements a button in Raspberry Pi.
"""
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

btn_pin = 17

GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('Program started.')

try:
    while True:
        button_state = GPIO.input(btn_pin)

        if button_state == GPIO.LOW:
            print('Button was pressed.')     
        time.sleep(0.15)

except KeyboardInterrupt:
    print('Program interrupted by User.')

finally:
    GPIO.cleanup()

