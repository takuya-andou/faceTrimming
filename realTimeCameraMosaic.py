#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
color = (255, 255, 255) # color of rectangle for face detection

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

        if len(facerect) > 0:
            for (x,y,w,h) in facerect:
		cut_img = image[y:y+h,x:x+w]
	        cut_face = cut_img.shape[:2][::-1]
	        cut_img = cv2.resize(cut_img,(cut_face[0]/30, cut_face[0]/30))
	        cut_img = cv2.resize(cut_img,cut_face,interpolation = cv2.cv.CV_INTER_NN)
	        image[y:y+h,x:x+w] = cut_img
                #cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

        count=0
        cv2.imshow('face detector', image)

cam.release()
cv2.destroyAllWindows()
