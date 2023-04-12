import os.path
import cv2
from centering import centering
import matplotlib.pyplot as plt
import numpy as np
from recognition import recognize_led_colors, Led, Color


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
        recognize_led_colors()
        result()
        if key == 27:  # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")


if __name__ == "__main__":
    # read_img()
    leds = [Led(68, 297), Led(96, 300), Led(176, 300), Led(371, 300), Led(454, 297), Led(486, 297)]
    colors = [Color.GREEN, Color.RED]

    for i in range(2, 18):
        img_path = os.path.join(os.getcwd(), f'images/framedisp_manual_{i}.jpg')
        image = cv2.imread(img_path)

        statuses = recognize_led_colors(image, leds, colors)
        statuses_str = [f'LED {i}: {s.name}' for i, s in enumerate(statuses)]
        print(statuses_str)

        cv2.imshow('IMG', image)
        cv2.waitKey(0)
