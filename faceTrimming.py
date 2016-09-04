# -*- coding: utf-8 -*-

# 参考
# http://www.takunoko.com/blog/python%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%8B-part1-opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98/

# 動画ファイルから、顔を検出

import cv2
import time

# 分類器へのパス
# cascade_path = "haarcascade_profileface.xml"
cascade_path = "haarcascades/haarcascade_frontalface_default.xml"

# 動画パス
video_path = "target/test.mov"

# colorはBGRの順番?
color = (0, 187, 254) #黄
#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)

# 動画のエンコード　とりあえず、これで動く拡張子はm4vで
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
# 動画ファイル読み込み
cap = cv2.VideoCapture(video_path)

out = cv2.VideoWriter("face_out.m4v", fourcc, 30.0, (1280,720))

frame_num = 0
img_cnt = 0
# フレームごとの処理
while(cap.isOpened()):
  ret, frame = cap.read()
  if (ret == False):
    break
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #最後の引数は最小値：ここを小さくしすぎると他のそれっぽい部分も検出してしまった。
  facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))
 
  print("frame : %d" % frame_num)
  if len(facerect) > 0:
    #検出した顔を囲む矩形の作成
    for (x,y,w,h) in facerect:
      # 該当の箇所だけ切り出し
      cv2.imwrite("result/kiri"+str(frame_num)+".png", frame[y:y+h, x:x+w])
      cv2.rectangle(frame, (x,y),(x+w,y+h), color, thickness=7)
      #cv2.imwrite("result/"+frame_num+".png", frame)
      img_cnt += 1
  #不要かもしれないけど、動画にもする
  out.write(frame)
  frame_num += 1
 
cap.release()
cv2.destroyAllWindows()
out.release()
