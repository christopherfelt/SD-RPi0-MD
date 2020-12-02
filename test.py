import RPi.GPIO as gpio
import time


if __name__ == "__main__":
    gpio.setmode(gpio.BCM)
    # gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

    print("light is on")
    # gpio.output(23, gpio.HIGH)
    # time.sleep(1)
    # gpio.output(23, gpio.LOW)
    # time.sleep(1)
    gpio.output(24, gpio.HIGH)
    time.sleep(3)
    gpio.output(24, gpio.LOW)
    print("light is off")
    gpio.cleanup()
    #test
