import Rpi.GPIO as gpio
from datetime import datetime
import time

# if the time is after 7 then go into low sleep mode for 11 hours (hit pin 1)
# else go into low sleep mode for 1 hour (hit pin 2)

def main():

    sd_two = 23
    sd_eleven = 24

    gpio.setmode(gpio.BCM)
    gpio.setup(sd_two, gpio.OUT)
    gpio.setup(sd_eleven, gpio.OUT)

    now = datetime.now()

    seven_pm = datetime(2020, 11, 25, 19, 2)

    if(now <  seven_pm):
        print(now.strftime("%H:%M:%S"))
        print("do not shut down")
        # low power mode for 2 hours
        gpio.output(sd_two, gpio.HIGH)
        time.sleep(1)
        gpio.output(sd_two, gpio.LOW)


    else:
        print("do shutdown")
        print(now.strftime("%H:%M:%S"))
        # low power mode for 11 hours
        gpio.output(sd_eleven, gpio.HIGH)
        time.sleep(1)
        gpio.output(sd_eleven, gpio.LOW)


if __name__ == "__main__":
    main()

