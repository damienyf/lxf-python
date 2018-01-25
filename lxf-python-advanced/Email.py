
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 现在我们用Outlook或者Foxmail之类的软件写好邮件，
# 填上对方的Email地址，点“发送”，电子邮件就发出去了。
# 这些电子邮件软件被称为MUA：Mail User Agent——邮件用户代理。

# Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——邮件传输代理，
# 就是那些Email服务提供商，比如网易、新浪等等。
# 由于我们自己的电子邮件是163.com，所以，Email首先被投递到网易提供的MTA，
# 再由网易的MTA发到对方服务商，也就是新浪的MTA。这个过程中间可能还会经过别的MTA，
# 但是我们不关心具体路线，我们只关心速度。

# Email到达新浪的MTA后，由于对方使用的是@sina.com的邮箱，
# 因此，新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理。
# Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，
# 我们将这个长期保存邮件的地方称之为电子邮箱。

# 同普通邮件类似，Email不会直接到达对方的电脑，因为对方电脑不一定开机，开机也不一定联网。
# 对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上。

# 所以，一封电子邮件的旅程就是：

# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人


# 收邮件时，MUA和MDA使用的协议有两种：
# POP：Post Office Protocol，目前版本是3，俗称POP3；
# IMAP：Internet Message Access Protocol，目前版本是4，
# 优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

# 邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。
# 假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，
# 所以，你得填163提供的SMTP服务器地址：smtp.163.com，为了证明你是163的用户，
# SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

# 类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，
# 所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，
# 这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。


# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

# 邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
# 而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()