# -*- coding: utf-8 -*-
def sendEmail(mailAddress, mailText):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText(mailText, 'plain', 'utf-8')
    msg['From'] = formataddr(["", 'ittest_mail@sina.com'])
    msg['To'] = formataddr([mailText, mailAddress])
    msg['Subject'] = "主题"
    try:
        server = smtplib.SMTP("smtp.sina.com", 25)
        server.login("ittest_mail@sina.com", "XXXXPWD")
        server.sendmail('ittest_mail@sina.com', [mailAddress], msg.as_string())
        server.quit()
        return True
    except:
        return False


userInputEmailAdd = input("请输入你要发送的邮件地址：  ")
userInputEmailContent = input("请输入你想说的话：  ")
if sendEmail(userInputEmailAdd, userInputEmailContent):
    print("发送成功")
else:
    print("发送失败。。。。。")