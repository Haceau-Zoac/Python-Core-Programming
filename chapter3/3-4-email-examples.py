#!/usr/binn/env python
'email-examples.py - demo creation of email messages'

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

# multipart alternative: text and html
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '</body></html>', 'html'
    )
    email.attach(html)
    return email

# multipart: images
def make_img_msg(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition',
        f'attachment; filename="{fn}"')
    return email

def sendMsg(fr, to, msg, pwd):
    s = SMTP('smtp.qq.com')
    s.login(fr, pwd)
    s.sendmail(fr, to, msg)
    s.quit()

if __name__ == '__main__':
    print('Sending multipart alternative msg...')
    msg = make_mpa_msg()
    sender = input('sender > ')
    to = input('to > ')
    pwd = input('password > ')
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = 'multipart alternative test'
    sendMsg(sender, to, msg.as_string(), pwd)

    print('Sending image msg...')
    msg = make_img_msg(input('Image file > '))
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = 'image file test'
    sendMsg(sender, to, msg.as_string(), pwd)