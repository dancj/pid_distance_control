#Libraries
import RPi.GPIO as GPIO
import time
import pigpio

 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
pi = pigpio.pi()
print("connected=", pi.connected)

pi.set_mode(GPIO_TRIGGER, pigpio.OUTPUT)
pi.set_mode(GPIO_ECHO, pigpio.INPUT)

pi.callback(GPIO_TRIGGER, pigpio.EITHER_EDGE, callback_func)
pi.callback(GPIO_ECHO, pigpio.EITHER_EDGE, callback_func)


def callback_func(gpio, level, tick):
    pass

def distance():
    """
    Send a sound pulse by setting TRIG pin high.  When signal sent, the ECHO pin also goes high until the response
    is received.  The elapsed round-trip time (RTT) is therefore when the ECHO goes high until it goes low again.

    """
    # send out a pulse from TRIG
    pi.gpio_trigger(GPIO_TRIGGER, pulse_len=10, level=1) 
    StartTime = time.time()

    pi.set_watchdog(GPIO_ECHO, wdog_timeout=1000)
    StopTime = time.time()

    print("logged start {} and stop {}".format(StartTime, StopTime))

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        pi.stop()
