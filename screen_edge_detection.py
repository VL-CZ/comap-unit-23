import cv2
import numpy as np
import pytesseract

def screen_edge_detection(img=None):

    if img==None:
        img = cv2.imread('im.jpg')
    x,y,z= img.shape
    img = img[int(x*0.25):int(x*.7),int(y*0.15):int(y*0.9),:]
    cv2.imshow("res", img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

    # Second, process edge detection use Canny.

    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    # Then, use HoughLinesP to get the lines. You can adjust the parameters for better performance.

    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 25  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 50  # minimum number of pixels making up a line
    max_line_gap = 20  # maximum gap in pixels between connectable line segments
    

    line_image = np.copy(img) * 0  # creating a blank to draw lines on

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

    minx,miny = 1e8,1e8
    maxx,maxy =0,0
    for line in lines:
        for x1,y1,x2,y2 in line:
            is_vertical = abs(x1-x2)< abs(y1-y2)
            
            if is_vertical:
                minx = min(minx,x1,x2)
                maxx = max(maxx,x1,x2)
            else:
                miny = min(miny,y1,y2)
                maxy = max(maxy,y1,y2)

    centerx = (minx+maxx)/2
    centery = (miny+maxy)/2

    left,right,top,bot = [None for _ in range(4)]
    for line in lines:
        for x1,y1,x2,y2 in line:
            current = (x1,y1,x2,y2)
            xdiff = abs(x1-x2)
            ydiff = abs(y1-y2)
            is_vertical = abs(x1-x2)< abs(y1-y2)
            
            if is_vertical:
                if centerx > x1:
                    if left == None: left = current
                    mx1,my1,mx2,my2 = left
                    left = [current, left][np.argmax([abs(x1-x2),abs(mx1-mx2)])]
                else:
                    if right == None: right = current
                    mx1,my1,mx2,my2 = right
                    right = [current, right][np.argmin([abs(x1-x2),abs(mx1-mx2)])]
            else:
                if centery > y1:
                    if bot == None: bot = current
                    mx1,my1,mx2,my2 = bot
                    bot = [current, bot][np.argmax([abs(y1-y2),abs(my1-my2)])]
                else:
                    if top == None: top = current
                    mx1,my1,mx2,my2 = top
                    top = [current, top][np.argmin([abs(y1-y2),abs(my1-my2)])]

    for x1,y1,x2,y2 in [left,right,top,bot]:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

    lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)

    
    cv2.imshow("res", lines_edges)
    cv2.imwrite("res.jpg", lines_edges)

