import cv2


def recognition(image):
    cv2.imshow('IMG', image)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # GREEN
    green_led_lower, green_led_upper = (36, 25, 25), (70, 255, 255)
    green_led_mask = cv2.inRange(hsv_image, green_led_lower, green_led_upper)

    res = cv2.bitwise_and(image, image, mask=green_led_mask)
    cv2.imshow("Green mask", res)

    # RED
    mask1 = cv2.inRange(hsv_image, (0, 50, 20), (5, 255, 255))
    mask2 = cv2.inRange(hsv_image, (175, 50, 20), (180, 255, 255))

    red_led_mask = cv2.bitwise_or(mask1, mask2)

    res = cv2.bitwise_and(image, image, mask=red_led_mask)
    cv2.imshow("Red mask", res)

    # DISPLAY MASK
    display_mask = cv2.inRange(hsv_image, (0, 0, 168), (172, 111, 255))

    res = cv2.bitwise_and(image, image, mask=display_mask)
    cv2.imshow("Display mask", res)

    cv2.waitKey(0)
