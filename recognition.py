from enum import Enum

import cv2
import numpy as np


class Led:
    def __init__(self, x, y):
        self.x, self.y, self.diameter = x, y, 25


class Display:
    def __init__(self, x, y):
        self.x, self.y, self.width, self.height = x, y, 300, 150


class Color(Enum):
    RED = 1
    GREEN = 2


class LedStatus(Enum):
    RED = 1
    GREEN = 2
    OFF = 3
    ON = 4


def _is_pixel_empty(pixel):
    return pixel[0] == pixel[1] == pixel[2] == 0


def _get_mask(image, color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if color == Color.RED:
        mask1 = cv2.inRange(hsv_image, (0, 50, 20), (5, 255, 255))
        mask2 = cv2.inRange(hsv_image, (175, 50, 20), (180, 255, 255))

        return cv2.bitwise_or(mask1, mask2)
    elif color == Color.GREEN:
        green_led_lower, green_led_upper = (36, 25, 25), (70, 255, 255)
        return cv2.inRange(hsv_image, green_led_lower, green_led_upper)
    else:
        return None


def _has_color(mask, led):
    empty, colored = 0, 0
    for x in range(led.x - led.diameter // 2, led.x + led.diameter // 2):
        for y in range(led.y - led.diameter // 2, led.y + led.diameter // 2):
            c = mask[y, x]
            if _is_pixel_empty(c):
                empty += 1
            else:
                colored += 1

    colored_ratio = colored / (colored + empty)
    return colored_ratio >= 0.2


def recognize_led_colors(image, leds, possible_colors):
    # cv2.imshow('IMG', image)

    masks = {}

    for color in possible_colors:
        mask = _get_mask(image, color)
        masks[color] = cv2.bitwise_and(image, image, mask=mask)
        # cv2.imshow("Mask", res)

    led_statuses = [LedStatus.OFF] * len(leds)
    i = 0

    for led in leds:
        for color in possible_colors:
            if _has_color(masks[color], led):
                led_statuses[i] = LedStatus(color.value)
        i += 1

    # DISPLAY MASK
    # display_mask = cv2.inRange(hsv_image, (0, 0, 168), (172, 111, 255))
    #
    # res = cv2.bitwise_and(image, image, mask=display_mask)
    # cv2.imshow("Display mask", res)
    #
    # cv2.waitKey(0)

    return led_statuses


def recognize_leds(image, leds):
    statuses = recognize_led_colors(image, leds, [c.value for c in Color])
    on_off_statuses = [s if s == LedStatus.OFF else LedStatus.ON for s in statuses]
    return on_off_statuses


def recognize_display(image, display):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    display_mask = cv2.inRange(hsv_image, (0, 0, 168), (172, 111, 255))
    mask = cv2.bitwise_and(image, image, mask=display_mask)

    empty, colored = 0, 0
    for x in range(display.x - display.width // 2, display.x + display.width // 2):
        for y in range(display.y - display.diameter // 2, display.y + display.height // 2):
            c = mask[y, x]
            if _is_pixel_empty(c):
                empty += 1
            else:
                colored += 1

    colored_ratio = colored / (colored + empty)
    return colored_ratio >= 0.5
