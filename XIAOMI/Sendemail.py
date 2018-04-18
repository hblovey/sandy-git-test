#coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from Emailinfo import get_emailinfo
from Getfilepath import get_path

def send_email(arg,path):

    message=MIMEMultipart()
#邮件主题
    message['Subject']=Header(arg['Subject'],'utf-8')
#邮件正文有三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message.attach(MIMEText(arg['content'], 'plain', 'utf-8'))
#构造附件
    att=MIMEText(open(path,'rb').read(),'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="log.txt"'
    message.attach(att)

    smtp=smtplib.SMTP_SSL(arg['smtp_host'],465)
    smtp.login(arg['user'],arg['pwd'])
    smtp.sendmail(arg['sender'],arg['receiver'],message.as_string())
    smtp.quit()
    print('邮件发送成功')

if __name__=='__main__':
    arg=get_emailinfo(r'.\emailMsg.txt')
    path=get_path(r'.\Log')
    send_email(arg,path)
