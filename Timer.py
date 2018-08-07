# -*- coding: utf-8 -*-
import psutil
import threading


class Person(object):
    def sendEmail(mailAddress, mailText):
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText(mailText, 'plain', 'utf-8')
        msg['From'] = formataddr(["Tsg", 'ittest_mail@sina.com'])
        msg['To'] = formataddr([mailText, mailAddress])
        msg['Subject'] = "内存告警"
        try:
            server = smtplib.SMTP("smtp.sina.com", 25)
            server.login("ittest_mail@sina.com", "XXXPWD")
            server.sendmail('ittest_mail@sina.com', [mailAddress], msg.as_string())
            server.quit()
            return True
        except:
            return False
        # if sendEmail(userInputEmailAdd, userInputEmailContent):
        #     print("发送成功")
        # else:
        #     print("发送失败。。。。。")

    def __init__(self):
        print("init person")

    def speak(self):
        Host = [r"\\172.16.119.30\C$", r"\\172.16.119.30\D$", r"\\172.16.119.30\E$", r"\\172.16.119.30\f$"]
        for x in Host:
            str = psutil.disk_usage(x)
            print(str.percent)
            if str.percent > 80:
                print("大了" + x)
                if Person.sendEmail('@@@@@收件人@@@@',"警告"+x+"存储不足"):
                    print("发送成功")
                else:
                    print("发送失败。。。。。")
            else:
                print("小了" + x)
            # print(x)

if __name__ == "__main__":
    p = Person()
    while True:
        timer = threading.Timer(30, Person.speak, (p,))
        print("start")
        timer.start()
        timer.join()
        print("after join")
