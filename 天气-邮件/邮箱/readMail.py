import imaplib,config,datetime,re,os
import email
import email.header

imaplib_MAXLINE = 100000000

with imaplib.IMAP4_SSL(\
    config.qqImapServer,config.qqImapPort) as mailObj:
    mailObj.login(config.FromEmail,config.code)
    mailObj.select("INBOX",readonly=True)
    IDList = mailObj.uid(\
        "search","(SINCE 20-Nov-2021)")[1][0].split()
    targetUIDs =[]
    for uid in IDList:
        resStatus,data = mailObj.uid("fetch",uid,\
            "(BODY[HEADER.FIELDS (SUBJECT)])")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        subject = str(\
            email.header.make_header(\
                email.header.decode_header(\
                email_message["Subject"])))
        print("Email has subject : {}".format(subject))
        keyword = "登录"
        if re.search(keyword,subject,re.IGNORECASE):
            print("找到测试邮件")
            targetUIDs.append(uid)
        else:
            print("没有找到测试邮件")

    if len(targetUIDs) == 0:
        print("没有找到任何邮件！")
    else :
        for uid in targetUIDs:
            resStatus,data = mailObj.uid("fetch",uid,"RFC822")
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            #header detail
            date_tuple = email.utils.parsedate_tz(\
                email_message["Date"])

            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(\
                    email.utils.mktime_tz(date_tuple))
                local_date_message = "%s" %(str(local_date.strftime(\
                    "%a, %d %b %Y %H:%M:%S")))

            email_from = str(\
            email.header.make_header(\
                email.header.decode_header(\
                email_message["From"])))

            email_to =   str(\
            email.header.make_header(\
                email.header.decode_header(\
                email_message["To"])))

            subject = str(\
            email.header.make_header(\
                email.header.decode_header(\
                email_message["Subject"])))

            print("Email Info :\n\
                Sender : {}\n\
                    Receiver : {}\n\
                        Subject : {}\n On\
                            {}".format(\
                                email_from,\
                                    email_to,\
                                        subject,\
                                            local_date_message))

            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    codec = part.get_content_charset()
                    if codec:
                        print(body.decode(codec))
                    else :
                        print(body.decode("gb18030"))
                else :
                    fileName = part.get_filename()
                    if fileName:
                        deCodedFileName = str(\
                            email.header.make_header(\
                                email.header.decode_header(\
                                    fileName)))
                        downloadPath = os.path.join(".",deCodedFileName)
                        with open(downloadPath,"wb") as attachment:
                            attachment.write(part.get_payload(decode=True))
                        print("attachment is downloaded in{}".format(\
                            os.path.abspath(downloadPath)))
                    