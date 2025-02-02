import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 7, 100, 100
    upperLimit = hsvC[0][0][0] + 7, 255, 255

    calc_lower = np.array(lowerLimit, dtype=np.uint8)
    calc_upper = np.array(upperLimit, dtype=np.uint8)

    return calc_lower, calc_upper #the interval of values 