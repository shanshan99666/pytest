# handleemail
# 2022/10/14
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_mail(receivers, title, content):
    sender = '576648349@qq.com'
    print(receivers)
    mailto = receivers.split(",")
    print(mailto)
    try:
        msg = MIMEMultipart()
        msg['Subject'] = title
        to_user = ",".join(mailto)
        print("receivers...", to_user)
        msg['to'] = to_user
        msg['From'] = sender
        body = MIMEText(content, 'html', 'utf-8')
        msg.attach(body)
        smtp = smtplib.SMTP('smtp@qq.com', 587)
        smtp.starttls()
        smtp.login("576648349@qq.com", "rhroscgdwzcgbdbb")
        smtp.sendmail(sender, mailto, msg.as_string())
        print("send success")
        smtp.quit()
    except Exception as e:
        print("send failed is %s",e)