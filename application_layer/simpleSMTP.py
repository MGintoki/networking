from smtplib import SMTP
from poplib import POP3
from time import sleep


SMTPServer = 'pop.qq.com'
POP3Server = 'pop.qq.com'

who = '1582427751@qq.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg
Hello World.
''' % {'who': who}

sendSvr = SMTP(SMTPServer, 13000)
errs = sendSvr.sendmail(who, [who])
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)


recvSvr = POP3(POP3Server)
recvSvr.user('1582427751@qq.com')
recvSvr.pass_('521zhuqiuyu')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep + 1]
print recvBody



