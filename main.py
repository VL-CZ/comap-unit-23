import os.path
import cv2
from centering import centering
import matplotlib.pyplot as plt
import numpy as np
from recognition import recognition


def result():  # print result with parameters
    print("All LEDS on")
    pass


def read_img():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        recognition()
        result()
        if key == 27:  # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")


if __name__ == "__main__":
    read_img()
