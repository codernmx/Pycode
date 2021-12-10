import os
import imaplib,config,datetime,re,os
import email
import email.header
import re
dir_path = './secret/'
outputDirPath = os.path.join(".", "secret")
os.makedirs(outputDirPath, exist_ok=True)
num = "这次来到太阳系的地球，发现了很多神奇的地方，需要给总部发\
 送这个信息。 信息需要加密，\
密码就用我的生日好了，如果你看到这个，只要告诉我你要发送信息，我就会把生日告诉你。"

filePath = os.path.join(outputDirPath," info.text")
f = open(filePath, 'w+')
f.write(f'{num}')

imaplib_MAXLINE = 100000000

