import RPi.GPIO as GPIO
import time
import pigpio

 
# GPIO Pins on the RPi
GPIO_TRIGGER = 18
GPIO_ECHO = 24

SPEED_OF_SOUND = 34300  # cm/s
LOW = 0
HIGH = 1


class UltrasoundSensor:
    """
    This class controls the HC-SR04 ultransonic sensor using pigpio
    to send a pulse out and read how long it takes to come back

    Based on Sonar Ranger example from pigpio library here:
    http://abyz.me.uk/rpi/pigpio/examples.html#Python%20code
    """

    def __init__(self):
        self.pi = pigpio.pi()
        print("PI connected=", self.pi.connected)

        self.pi.set_mode(GPIO_TRIGGER, pigpio.OUTPUT)
        self.pi.set_mode(GPIO_ECHO, pigpio.INPUT)

        self.pi.callback(GPIO_TRIGGER, pigpio.EITHER_EDGE, self.ping_callback_func)
        self.pi.callback(GPIO_ECHO, pigpio.EITHER_EDGE, self.ping_callback_func)

        self.high_time = None
        self.time_elapsed = None
        self.ping_received = False
        self.triggered = False

    def distance(self):
        """
        Send a sound pulse by setting TRIG pin high.  When signal sent, the ECHO pin also goes high until the response
        is received.  The elapsed round-trip time (RTT) is therefore when the ECHO goes high until it goes low again.
        :return: distance in cm 
        """
        self.ping_received = False

        # send out a pulse from TRIG
        self.pi.gpio_trigger(GPIO_TRIGGER, pulse_len=10, level=1)
        start_time = time.time()

        while not self.ping_received:
            # wait for ping to come back to callback
            if (time.time() - start_time) > 5.0:
                print("Ping not received... timed out")
                return -1
            time.sleep(0.001)

        # dist = time * speed
        round_trip_distance = self.time_elapsed * SPEED_OF_SOUND / 1000000.0
        return round_trip_distance / 2

    def ping_callback_func(self, gpio, level, tick):
        """
        Callback in response to TRIG or ECHO pin changing sign
        Set self.time elapsed after a signal change
        :param gpio: pin that changed state
        :param level: 0=low, 1=high, 2=no change
        :param tick: microseconds since boot
        """
        if gpio == GPIO_TRIGGER:
            if level == LOW:
                # trigger just sent, time to reset everything in preparation of pulse
                self.triggered = True
                self.high_time = None
        else:
            if self.triggered:
                if level == HIGH:
                    # ECHO went high --> pulse sent
                    self.high_time = tick
                else:
                    # ECHO went low --> pulse received
                    if self.high_time is not None:
                        self.time_elapsed = tick - self.high_time
                        self.high_time = None
                        self.ping_received = True


if __name__ == '__main__':
    ranger = UltrasoundSensor()
    try:
        while True:
            dist = ranger.distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        ranger.pi.stop()
