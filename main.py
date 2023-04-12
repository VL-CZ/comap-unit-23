import os.path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def recognition():
    img_path = os.path.join(os.getcwd(), 'images/img0.jpg')
    image = cv2.imread(img_path)
    cv2.imshow('IMG', image)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # red_led_lower, red_led_upper = (345, 73, 76), (300, 1.17, 100)
    # red_led_mask = cv2.inRange(hsv_image, red_led_lower, red_led_upper)

    green_led_upper, green_led_lower = (120, 15, 97), (255, 255, 255)
    # green_led_lower, green_led_upper = (0, 0, 0), (255, 255, 255)
    green_led_mask = cv2.inRange(hsv_image, green_led_lower, green_led_upper)

    fin = cv2.bitwise_and(image, image, mask=green_led_mask)
    cv2.imshow("FIN", fin)

    result()


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
        if key == 27:  # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")


if __name__ == "__main__":
    # read_img()
    #
    # img_path = os.path.join(os.getcwd(), 'images/Eding.png')
    # img = cv2.imread(img_path)
    # # convert to HSV
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # # set lower and upper color limits
    # lower_val = (50, 100, 170)
    # upper_val = (70, 255, 255)
    # # Threshold the HSV image to get only green colors
    # mask = cv2.inRange(hsv, lower_val, upper_val)
    # # apply mask to original image - this shows the green with black blackground
    # only_green = cv2.bitwise_and(img, img, mask=mask)
    #
    # cv2.imshow("FINAL", only_green)
    # cv2.waitKey(0)

    for i in range(2, 18):
        img_path = os.path.join(os.getcwd(), f'images/framedisp_manual_{i}.jpg')
        image = cv2.imread(img_path)
        cv2.imshow('IMG', image)

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # GREEN
        green_led_lower, green_led_upper = (36, 25, 25), (70, 255, 255)
        green_led_mask = cv2.inRange(hsv_image, green_led_lower, green_led_upper)

        res = cv2.bitwise_and(image, image, mask=green_led_mask)
        cv2.imshow("Green", res)

        # RED
        mask1 = cv2.inRange(hsv_image, (0, 50, 20), (5, 255, 255))
        mask2 = cv2.inRange(hsv_image, (175, 50, 20), (180, 255, 255))

        red_led_mask = cv2.bitwise_or(mask1, mask2)

        res = cv2.bitwise_and(image, image, mask=red_led_mask)
        cv2.imshow("Red", res)

        # DISPLAY MASK
        display_mask = cv2.inRange(hsv_image, (0, 0, 168), (172, 111, 255))

        res = cv2.bitwise_and(image, image, mask=display_mask)
        cv2.imshow("Display", res)

        cv2.waitKey(0)
