# OCR
身份证文字识别项目

crater:junjielv  2020/10/04
2020/10/4  身份证识别项目 ----v1.0

1、所需库：pytesseract.py
   安装：pip install pytesseract
   
2、运行video.py代码，调试在线摄像头

3、运行IDrec.py,进行身份证识别

功能1：图片处理后识别

功能2：图片直接识别

功能3：视频在线识别

2020/10/5
加：

1、中文文字识别（下载chi_sim.traineddata中文文字库：https://tesseract-ocr.github.io/tessdoc/Data-Files）
github官方很慢，可参考：https://pan.baidu.com/s/1uuSTBNo3byJib4f8eRSIFw ,密：8v8u
可参考：https://blog.csdn.net/qq_38161040/article/details/90668765


常见错误：

1）tesseract is not installed or it's not in your path

①需要在 window本地环境下安装：Tesseract-OCR  下载地址：https://github.com/tesseract-ocr/tesseract/wiki
②解压安装，并设置环境变量，可参考：https://blog.csdn.net/weixin_40569991/article/details/82082173
③打开anaconda\envs\yourvirenv\site-packages\pytesseract\pytesseract.py文件;将tesseract_cmd = r'd\Tesseract-OCR\tesseract.exe'
④重新在python中运行Idrec.py即可成功.

优点：

1、对身份证件的识别要好一些
2、对标准的大字体识别好些

缺点：
1、对广告拍字体的识别 效果特别差
2、对车牌的识别也特别差
