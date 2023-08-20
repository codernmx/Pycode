# PyCode-Github/爬虫-所有/所有做过的案例/下载图片
# _*_ coding: utf-8 _*_
# @Time : 2022/4/13 18:29
# @FileName : 千图成像.py
# @Author : Maisy
# @SoftWare : PyCharm
from PIL import Image
import os
import numpy as np


# 获取图像的平均颜色值
def compute_mean(imgPath):
    '''
    获取图像平均颜色值
    :param imgPath: 缩略图路径
    :return: （r，g，b）整个缩略图的rgb平均值
    '''
    im = Image.open(imgPath)
    im = im.convert("RGB")  # 转为 rgb模式
    # 把图像数据转为数据序列。以行为单位，每行存储每个像素点的色彩
    '''如：
     [[ 60  33  24] 
      [ 58  34  24]
      ...
      [188 152 136] 
      [ 99  96 113]]

     [[ 60  33  24] 
      [ 58  34  24]
      ...
      [188 152 136] 
      [ 99  96 113]]
    '''
    imArray = np.array(im)
    # mean()函数功能：求指定数据的取均值
    R = np.mean(imArray[:, :, 0])  # 获取所有 R 值的平均值
    G = np.mean(imArray[:, :, 1])
    B = np.mean(imArray[:, :, 2])
    return (R, G, B)


def getImgList():
    """
    获取缩略图的路径及平均色彩
    :return: list，存储了图片路径、平均色彩值。
    """
    imgList = []
    for pic in os.listdir("img/"):
        imgPath = "img/" + pic
        imgRGB = compute_mean(imgPath)
        imgList.append({
            "imgPath": imgPath,
            "imgRGB": imgRGB
        })
    return imgList


def computeDis(color1, color2):
    '''
    计算两张图的颜色差，计算机的是色彩空间距离。
    dis = (R**2 + G**2 + B**2)**0.5
    参数：color1，color2 是色彩数据 （r，g，b）
    '''
    dis = 0
    for i in range(len(color1)):
        dis += (color1[i] - color2[i]) ** 2
    dis = dis ** 0.5
    return dis


def create_image(bgImg, imgDir, N=10, M=50):
    '''
    根据背景图，用头像填充出新图
    bgImg：背景图地址
    imgDir：头像目录
    N：背景图缩放的倍率
    M：头像的大小（MxM）
    '''
    # 获取图片列表
    imgList = getImgList()

    # 读取图片
    bg = Image.open(bgImg)
    # bg = bg.resize((bg.size[0] // N, bg.size[1] // N))  # 缩放。建议缩放下原图，图片太大运算时间很长。
    bgArray = np.array(bg)
    width = bg.size[0] * M  # 新生成图片的宽度。每个像素倍放大 M 倍
    height = bg.size[1] * M  # 新生成图片的高度

    # 创建空白的新图
    newImg = Image.new('RGB', (width, height))

    # 循环填充图
    for x in range(bgArray.shape[0]):  # x，行数据,可以用原图宽替代
        for y in range(bgArray.shape[1]):  # y，列数据，,可以用原图高替代
            # 找到距离最小的图片
            minDis = 10000
            index = 0
            for img in imgList:
                dis = computeDis(img['imgRGB'], bgArray[x][y])
                if dis < minDis:
                    index = img['imgPath']
                    minDis = dis
            # 循环完毕，index 就是存储了色彩最相近的图片路径
            #         minDis 存储了色彩差值
            # 填充
            tempImg = Image.open(index)  # 打开色差距离最小的图片
            # 调整图片大小，此处可以不调整，因为我在下载图的时候就已经调整好了
            tempImg = tempImg.resize((M, M))
            # 把小图粘贴到新图上。注意 x，y ，行列不要搞混了。相距 M 粘贴一张。
            newImg.paste(tempImg, (y * M, x * M))
            print('(%d, %d)' % (x, y))  # 打印进度。格式化输出 x，y

    # 保存图片
    newImg.save('final.jpg')  # 最后保存图片


create_image('test.jpg', 'img/')