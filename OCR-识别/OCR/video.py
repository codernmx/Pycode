###############################################################################
#createor:     junjielv199108
#reate time:  2020/10/01/15/59
###############################################################################
import cv2
import numpy
cap = cv2.VideoCapture(0)# 调整参数实现读取视频或调用摄像头
while 1:
    ret, frame = cap.read()
    try:
        if ret:
            cv2.imshow("cap", frame)
            if cv2.waitKey(100) & 0xff == ord('q'):
                break;
    except:
        print(1)
cap.release()
cv2.destroyAllWindows()