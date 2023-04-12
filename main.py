def take_screenshot():
    return None

def center_image(image):
    return None

def detect_led(image):
    return None

def detect_display(image):
    return None

def main():
    screenshot = take_screenshot()
    centered = center_image(screenshot)
    result = detect_led(centered)
    result = detect_display(centered)
    print("All LEDS on")


if __name__ == "__main__":
    main()
