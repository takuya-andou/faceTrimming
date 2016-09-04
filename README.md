# faceTrimming

#共通の手順
1.targetディレクトリを作成。その下に入力したい写真を入れる。  
2.resultディレクトリを作成。ここに検出後のものが出てくる。  
3.haarcascadesディレクトリを作成。このディレクトリに、下記のURLからダウンロードした特徴量のファイルを置く。  
https://opencvlibrary.svn.sourceforge.net/svnroot/opencvlibrary/tags/latest_tested_snapshot/opencv/data/haarcascades/

#ファイルの説明
##faceTrimming.py
これが今回の目的のファイル。
動画から顔を検出して、顔の部分だけフレームごとに切り出す。  
（おまけ）枠を書いた動画も作る

##sample.py
写真から顔を検出して、枠を書く

##realTimeCamera.py
Webカメラから顔を検出して枠を書く

##realTimeCameraMosaic.py
Webカメラから顔を検出してモザイクをかける
