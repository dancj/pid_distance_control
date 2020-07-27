# Reads distance data from ultrasonic range sensor (HC-SR04)
#
# Code based on tutorial at ref: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

ULTRASONIC_SPEED = 34300  # cm/s

# set GPIO Pins
GPIO_TRIGGER = 18   # starts an ultrasonic pulse
GPIO_ECHO = 24      # receives pulse at the end

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def measure_distance(debug=False):

    # send 10microsecond burst on transmitter (TRIG)
    # send low first for cleaner high pulse
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.000005)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.000010)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # time difference between start and arrival
    print("stop, start = {}, {}".format(start_time,stop_time)) 
    elapsed = stop_time - start_time
    round_trip_distance = (elapsed * ULTRASONIC_SPEED)

    return round_trip_distance / 2.0


if __name__ == '__main__':
    print("starting some test measurements with the distance sensor")
    try:
        while True:
            dist = measure_distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
