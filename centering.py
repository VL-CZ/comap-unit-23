import cv2
import numpy as np

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15


def get_image_brightness(image):
    hsl = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2HLS)
    Lchannel = hsl[:, :, 1]
    lvalue = cv2.mean(Lchannel)[0]
    return lvalue


def alignImages(im1, im2):
    # Convert images to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # matches.sort(key=lambda x: x.distance, reverse=False)
    matches = tuple(sorted(matches, key=lambda x: x.distance))

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1_reg = cv2.warpPerspective(im1, h, (width, height))

    return im1_reg


def centering(filename):
    imFilename = r"C:\Users\Hoang\Desktop\centering\test_photos\20230404_143651.jpg"
    im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
    input_image_brightness = get_image_brightness(imFilename)

    # reference photo
    refFilename = r"C:\Users\Hoang\Desktop\centering\reference_photos\optimal.jpg"
    if input_image_brightness < 40:
        refFilename = r"C:\Users\Hoang\Desktop\centering\reference_photos\dark.jpg"
    elif input_image_brightness > 70:
        refFilename = r"C:\Users\Hoang\Desktop\centering\reference_photos\light.jpg"
    imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    imReg = alignImages(im, imReference)
    outFilename = "aligned.jpg"
    cv2.imwrite(outFilename, imReg)
