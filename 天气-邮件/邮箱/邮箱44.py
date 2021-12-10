import imaplib, email, os
imapserver = 'imap.qq.com'
emailuser = "2410047096@qq.com"
emailpasswd = "ifjtgcemwocqdiii"
attachementdir = r"d:\a"  # 附件存放的位置
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


# search('FROM','abc@outlook.com',conn)  根据输入的条件查找特定的邮件
def search(key, value, conn):
    result, data = conn.search(None, key, '"()"'.format(value))
    return data


# 获取附件
def get_attachements(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()

        if bool(filename):
            filepath = os.path.join(attachementdir, filename)
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))


for id in mailidlist[0:5]:  #取邮件前5封
    result, data = conn.fetch(id, '(RFC822)')  # 通过邮件id获取邮件
    e = email.message_from_bytes(data[0][1])
    subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))
    mail_from = email.header.make_header(email.header.decode_header(e['From']))
    # print("邮件的subject是%s" % subject)
    # print("邮件的发件人是%s" % mail_from)
    body = str(get_body(e), encoding='utf-8')  # utf-8 gb2312 GB18030解析中文日文英文
    # print("邮件内容是%s" % body,'------------------------->>>')
    if '系统监测到你的帐号2410047096@qq.com于2' in body:
        print('找到关键字')
    else:
        print('没有找到关键字')
conn.logout()