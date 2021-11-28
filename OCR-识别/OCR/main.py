
import sys
# import importlib
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
import time
time1 = time.time()
from PIL import Image
import pytesseract#ocr字符识别库
import cv2
#二值化算法
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

#去除干扰线算法
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img
#身份证号码识别
def identity_OCR(pic_path):
    #身份证号码截图
    img1=Image.open(pic_path)
    w,h=img1.size
    #将身份证放大3倍
    out=img1.resize((w*3,h*3),Image.ANTIALIAS)
    Image._show(out)
    cv2.waitKey(0)
    region = (125*3,200*3,370*3,250*3)
    #裁切身份证号码图片
    cropImg = out.crop(region)
    # print(cropImg)
    # Image._show(cropImg)
    # cv2.waitKey(0)
    # 转化为灰度图
    img= cropImg.convert('L')
    Image._show(img)
    cv2.waitKey(0)
    # 把图片变成二值图像。
    img1=binarizing(img,100)
    img2=depoint(img)
    code = pytesseract.image_to_string(img2)
    print("识别该身份证号码是:"+str(code))

#身份证号码识别
#英文图片识别
def identity_OCR_Nopro(pic_path):
    image = Image.open(pic_path)
    content = pytesseract.image_to_string(image)  # 解析图片
    print(content)
#中文图片识别
#要在pytesseract 库的 image_to_string() 方法里加个参数lang='chi_sim'，
#这个就是引用对应的中文语言包，中文语言包的全名是 chi_sim.traineddata

def identity_OCR_Chine(pic_path):
    from PIL import Image
    import pytesseract
    image = Image.open(pic_path)
    content = pytesseract.image_to_string(image, lang='chi_sim')  # 解析图片
    print(content)



#功能：video recognition
def identity_OCR_Video(pic_path):
    vid = cv2.VideoCapture(pic_path)
    while (1):
        try:
            return_value, frame = vid.read()
            if return_value:
                cv2.imshow("result", frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                code = pytesseract.image_to_string(frame,lang='chi_sim')
                print("识别该身份证号码是:" + str(code))
                cv2.waitKey(100)
            else:
                raise ValueError("No image!")
        except:
            print('异常')
        # time.sleep(2)
if __name__ == '__main__':
    pic_path="./zsx2.jpg"
    # identity_OCR(pic_path)  ##使用图片2 识别证件号
    identity_OCR_Video(0)  #调用摄像头
    # identity_OCR_Chine(pic_path) #中文识别
    # identity_OCR_Nopro(pic_path) #英文识别
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')


