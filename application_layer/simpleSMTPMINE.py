import smtplib
from email.mime.text import MIMEText
mail_host = 'smtp.163.com'
mail_user = '17779173409@163.com'
mail_pass = 'xxx'
sender = '17779173409@163.com'
receivers = ['17779173409@163.com']

message = MIMEText('content','plain','utf-8')
message['Subject'] = 'title'
message['From'] = sender
message['To'] = receivers[0]

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(
        sender, receivers, message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)
