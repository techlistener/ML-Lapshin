import cv2

result_scale_percent = 50
BLUE = (255, 0, 0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')

width = int(img.shape[1] * result_scale_percent / 100)
height = int(img.shape[0] * result_scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow('Detection result', img)
cv2.waitKey()