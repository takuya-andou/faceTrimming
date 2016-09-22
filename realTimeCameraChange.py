#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
cascade_path = "haarcascades/haarcascade_frontalface_default.xml"

cam = cv2.VideoCapture(0)
count=0

while True:
    ret, capture = cam.read()
    if not ret:
        print('error')
        break
    count += 1
    if count > 1:
        image = capture.copy()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(200, 200))

        if len(facerect) ==2:
            x1 = facerect[0][0]
            y1 = facerect[0][1]
            w1 = facerect[0][2]
            h1 = facerect[0][3]
            x2 = facerect[1][0]
            y2 = facerect[1][1]
            w2 = facerect[1][2]
            h2 = facerect[1][3]

            cut_img1 = image[y1:y1+h1,x1:x1+w1]
            cut_img2 = image[y2:y2+h2,x2:x2+w2]

            cut_img1 = cv2.resize(cut_img1,(h2,w2))
            cut_img2 = cv2.resize(cut_img2,(h1,w1))

            image[y2:y2+h2,x2:x2+w2] = cut_img1
            image[y1:y1+h1,x1:x1+w1] = cut_img2

        count=0
        cv2.imshow('face detector', image)

cam.release()
cv2.destroyAllWindows()
