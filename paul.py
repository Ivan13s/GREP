import cv2

# incarca imaginea sau deschide fluxul de video
import imutils as imutils

image = cv2.imread("imagine.jpeg")
#video_capture = cv2.VideoCapture(0)

# convertește imaginea la niveluri de gri
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# aplică un filtru de reducere a zgomotului pentru a îmbunătăți detectarea
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# detectează marginile în imaginea grayscale
edged = cv2.Canny(gray, 35, 125)

# găsește formele în imagine
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# bucla prin forme și le desenează în imagine
for c in cnts:
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

# afișează imaginea rezultată
cv2.imshow("Imagine", image)
cv2.waitKey(0)