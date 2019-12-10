import smtplib
from email.mime.text import MIMEText
msg_from='1443648790@qq.com'  #发送方邮箱
passwd='tmvcpmpiayuniehb'     #填入发送方邮箱的授权码
msg_to='1159107353@qq.com'    #收件人邮箱
subject="python邮件测试"  #主题
content="加油，博文哥哥,8玩了"   #正文
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
i=0
while True:
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465) #邮件服务器及端口号
        s.login(msg_from, passwd)  #登录SMTP服务器
        s.sendmail(msg_from, msg_to, msg.as_string())#发邮件 as_string()把MIMEText对象变成str
        print("发送成功")
    except s.SMTPException:
        print("发送失败")
    i+=1
    if i>=10:
        break
s.quit()
