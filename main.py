import os.path
import cv2
from centering import centering
import matplotlib.pyplot as plt
import numpy as np
from recognition import recognize_led_colors, Led, Color, recognize_leds, Display, recognize_display

# CONFIG
LEDS = [Led(68, 297), Led(96, 300), Led(176, 300), Led(371, 300), Led(454, 297), Led(486, 297)]
COLORS = [Color.GREEN, Color.RED]
DISPLAY = Display(273, 163)


def result(statuses):  # print result with parameters
    statuses_str = [f'LED {i}: {s.name}' for i, s in enumerate(statuses)]
    print(statuses_str)


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

        # LED colors
        print('LED statuses')
        led_colors = recognize_led_colors(frame, LEDS, COLORS)
        result(led_colors)

        # # LED statuses
        # print('LED statuses: ')
        # leds = recognize_leds(frame, LEDS)
        # result(leds)

        # Display status
        is_display_on = recognize_display(frame, DISPLAY)
        display_status = 'ON' if is_display_on else 'OFF'
        print(f'DISPLAY: {display_status}')

        if key == 27:  # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")


if __name__ == "__main__":
    read_img()
