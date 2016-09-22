#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time
import sys
import numpy as np
param = sys.argv
# 認識対象ファイルの指定
image_path = "target/image.jpg"
# 認識対象ファイルの読み込み
image = cv2.imread(image_path)

# グレースケールに変換
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔認識用特徴量のファイル指定
cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
# カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)
# 顔認識の実行
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))


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

    # 結果の出力
    cv2.imwrite("result/"+str(param[1])+".png", image)