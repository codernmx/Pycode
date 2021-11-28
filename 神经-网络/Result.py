from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import random
import imutils
import cv2
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K
import scipy.io as scio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def getImg():
    dataFile = r'E:/room/test.mat'  # 单个的mat文件
    data = scio.loadmat(dataFile)

    i = 0
    for item in data['PD']:
        im = item.reshape(21, 14)
        url = 'E:/room/pd/pd' + str(i) + '.png'
        Image.fromarray(im).save(url)
        image = cv2.imread(url)
        cv2.putText(image, "p", (2, 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
        cv2.imwrite(url, image)

        i = i + 1

    j = 0
    for it in data['NC']:
        im = it.reshape(21, 14)
        url = 'E:/room/nc/nc' + str(j) + '.png'
        Image.fromarray(im).save(url)
        image = cv2.imread(url)
        cv2.putText(image, "n", (2, 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
        cv2.imwrite(url, image)
        j = j + 1


class LeNet:
    @staticmethod
    def build(width, height, depth, classes):
        # 初始化模型
        model = Sequential()
        inputShape = (height, width, depth)
        # 如果我们使用“通道优先”，更新输入形状
        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)
        # 第一组CONV => RELU => POOL层
        model.add(Conv2D(20, (5, 5), padding="same",
                         input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # 第二组CONV => RELU => POOL层
        model.add(Conv2D(50, (5, 5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # 第一个(也是唯一的)FC => RELU层

        model.add(Flatten())
        model.add(Dense(100))
        model.add(Activation("relu"))
        # softmax分类器
        model.add(Dense(classes))
        model.add(Activation("softmax"))
        # 返回构建的网络架构
        return model


def getFileList(dir, Filelist, ext=None):
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


def model_train(EPOCHS, INIT_LR, BS):
    # 初始化数据和标签
    data = []
    labels = []

    imagePaths = []
    img1 = []
    img2 = []
    path1 = 'E:/room/pd'
    path2 = 'E:/room/nc'
    # 抓取图像路径并随机打乱它们
    imagePaths1 = sorted(list(getFileList(path1, img1)))
    imagePaths2 = sorted(list(getFileList(path2, img2)))
    imagePaths = imagePaths1[0: 300] + imagePaths2[0: 90]
    seeds = random.randint(30, 100)
    random.seed(37)
    random.shuffle(imagePaths)

    # 循环遍历输入图像
    for imagePath in imagePaths:
        # 加载图像，对其进行预处理，并将其存储在数据列表中
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (21, 14))
        image = img_to_array(image)
        data.append(image)
        label = imagePath
        label = 1 if "nc" in label else 0
        labels.append(label)

    # 将原始像素强度缩放到范围[0,1]
    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)
    # 将数据划分为训练和测试分割，使用75%的数据进行训练，剩下的25%用于测试
    (trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25, random_state=42)
    # 将标签从整数转换为向量
    trainY = to_categorical(trainY, num_classes=2)
    testY = to_categorical(testY, num_classes=2)

    # 构造用于数据增强的图像生成器
    aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                             height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                             horizontal_flip=True, fill_mode="nearest")

    # 初始化模型
    print("[INFO] compiling model...")
    model = LeNet.build(width=21, height=14, depth=3, classes=2)
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
    # 培训网络
    print("[INFO] training network...")
    H = model.fit(x=aug.flow(trainX, trainY, batch_size=BS), validation_data=(testX, testY),
                  steps_per_epoch=len(trainX) // BS, epochs=EPOCHS, verbose=1)
    # 将模型保存到磁盘
    print("[INFO] serializing network...")
    model.save('E:/room/model/test.h5', save_format="h5")

    # 绘制培训损失和准确性
    plt.style.use("classic")
    plt.figure()
    N = EPOCHS

    plt.plot(np.arange(0, N), H.history["loss"], label="loss")
    # plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, N), H.history["accuracy"], label="acc")
    # plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
    plt.title("Accuracy of the original Lenet-5 model")
    plt.xlabel("Epoch:" + str(EPOCHS) + " BS:" + str(BS))
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig('E:/room/model/res.png')


def model_test():
    # 加载图片
    imagePaths = []
    img1 = []
    img2 = []
    path1 = 'E:/room/pd'
    path2 = 'E:/room/nc'
    # 抓取图像路径并随机打乱它们
    imagePaths1 = sorted(list(getFileList(path1, img1)))
    imagePaths2 = sorted(list(getFileList(path2, img2)))
    imagePaths = imagePaths1[230: len(imagePaths1)] + imagePaths2[50: len(imagePaths2)]
    total = len(imagePaths)
    print("total:  " + str(total))
    print(len(imagePaths))
    rightNum = 0
    for img in imagePaths:
        image = cv2.imread(img)
        orig = image.copy()
        # 对图像进行预处理以进行分类
        image = cv2.resize(image, (21, 14))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        # 加载训练好的卷积神经网络
        model = load_model('E:/room/model/test.h5')
        (pd, nc) = model.predict(image)[0]

        # 建立标签
        result = "nc" if pd < nc else "pd"
        if "nc" in img and result == "nc":
            rightNum = rightNum + 1
        if "pd" in img and result == "pd":
            rightNum = rightNum + 1
    print("准确率" + str(round(float(rightNum / total) * 100, 2)) + "%")


getImg()
model_train(100, 0.001, 60)
model_test()
