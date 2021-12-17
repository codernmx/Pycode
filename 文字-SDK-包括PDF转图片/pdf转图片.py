import datetime
import os
import time

import fitz  # fitz就是pip install PyMuPDF




# 新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）

# 获取文件夹所有路径
def getAllFile(path):
    allPath = []
    for root, dirs, files in os.walk(path):
        for file in files:
            singlePath = os.path.join(root, file)
            allPath.append(singlePath)
    # 打印文件名
    return allPath

def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount)[0:1]:
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建
        allFile = getAllFile(dir)
        pix.writePNG(imagePath + '/' + '%s.png' % (len(allFile)+1))  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    # 1、PDF地址
    dir = r"./img"  # toImg 的文件夹
    dir1 = r"./pdfFile"
    imagePath = './img'
    allPdfFile = getAllFile(dir1)
    for i in allPdfFile:
        pyMuPDF_fitz(i, imagePath)
        print(i,imagePath)
    # 2、需要储存图片的目录



