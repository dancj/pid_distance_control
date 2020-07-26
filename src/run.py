# Dan Thayer
# PID control servo motor and distance sensor.. just messing around

from range_sensor import measure_distance

# gains
k_p = 1.0
k_d = 1.0
k_i = 0.001


def run(target_dist):
    """
    Sense distance and drive motor towards a given target
    :param target_dist: distance in cm
    :return:
    """
    sum_err = 0.0
    last_err = 0.0
    while 1:
        dist = measure_distance()
        err = target_dist - dist
        sum_err += err
        signal = k_p*err + k_i*sum_err + k_d*(err-last_err)
        control(signal)
        last_err = err


def control(input):
    print("control w/ input ", input)


if __name__ == "__main__":
    print("starting control loop...")
    run(target_dist=4.0)
