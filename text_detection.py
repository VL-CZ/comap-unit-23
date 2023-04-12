# import required packages for performing OCR
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#tesseract download: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe


# Reading image file from where the text is to be extracted
# img1 = cv2.imread('OpenCV-OCR-1.jpg.webp')
import cv2
import pytesseract

img = cv2.imread("cropped.png")
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thr = cv2.adaptiveThreshold(gry, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, 35, 7)
cv2.imwrite('thresh_1.jpg', thr  )

txt = pytesseract.image_to_string(thr, config="--psm 3")
print(txt)
