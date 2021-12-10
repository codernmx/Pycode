import imaplib, email, os
imapserver = 'imap.qq.com'
emailuser = "2410047096@qq.com"
emailpasswd = "ifjtgcemwocqdiii"


conn = imaplib.IMAP4_SSL(imapserver)
conn.login(emailuser, emailpasswd)
conn.list()  # 列出邮箱中所有的列表，如：收件箱、垃圾箱、草稿箱。。。
conn.select('INBOX')  # 选择收件箱（默认）
result, dataid = conn.uid('search', None, "ALL")
mailidlist = dataid[0].split()  # 转成标准列表,获得所有邮件的ID

# 解析邮件内容
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, decode=True)


for id in mailidlist[0:5]:  #取邮件前5封
    result, data = conn.fetch(id, '(RFC822)')  # 通过邮件id获取邮件
    e = email.message_from_bytes(data[0][1])
    subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))
    mail_from = email.header.make_header(email.header.decode_header(e['From']))
    print("邮件的subject是%s" % subject)
    # print("邮件的发件人是%s" % mail_from)
    body = str(get_body(e), encoding='utf-8')  # utf-8 gb2312 GB18030解析中文日文英文
    # print("邮件内容是%s" % body,'------------------------->>>')
    keyword = '系统监测到你的帐号'
    if keyword in body:
        print('找到关键字------------------->>>>>>>>>>{}'.format(keyword))
    else:
        print('没有找到关键字')
conn.logout()