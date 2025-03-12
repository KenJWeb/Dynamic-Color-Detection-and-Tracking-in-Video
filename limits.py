import numpy as np
import cv2

def colors(color):

    if color == "blue":

        lowerLimit = np.array([90, 50, 50])
        upperLimit = np.array([130, 255, 255])

        return lowerLimit, upperLimit

    elif color == "yellow":

        lowerLimit = np.array([15 ,140, 50])
        upperLimit = np.array([35, 255, 255])

        return lowerLimit, upperLimit

    elif color == "green":
        lowerLimit = np.array([40, 50, 50])
        upperLimit = np.array([80, 255, 255])
        return lowerLimit, upperLimit

    elif color == "red":
        lowerLimit = np.array([-10, 150, 100])
        upperLimit = np.array([10, 255, 255])
        return lowerLimit, upperLimit
