import smtplib
from email.mime.text import MIMEText

msg_form = '842549758@qq.com'
passwd = 'zoxkqjpkdxjdbeei'
msg_to = '292478354@qq.com'

subject = 'python邮件测试'
content = '这是我使用Python smtplib及email模块发送的邮件'
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_form
msg['To'] = msg_to

try:
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(msg_form, passwd)
    s.sendmail(msg_form, msg_to, msg.as_string())
    print('发送成功')
except:
    print('发送失败')
finally:
    print('ok')
