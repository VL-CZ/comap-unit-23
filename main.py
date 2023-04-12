from centering import center_image
from display_detection import detect_display
from led_detection import detect_led
from printer import print_result
from screenshots import take_screenshot


def main():
    screenshot = take_screenshot()
    centered = center_image(screenshot)
    result = detect_led(centered)
    result = detect_display(centered)
    print_result(result)


if __name__ == "__main__":
    main()
