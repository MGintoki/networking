import ftplib
import os
import socket


HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)  # 不知为何此行代码无法执行
    except (socket.error, socket.gaierror) as e:
        print "error cannot reach ", HOST
    print "connected to host: ", HOST

    try:
        f.login()
    except ftplib.error_perm:
        print "error, cannot login anonymously"
        f.quit()
        return
    print "f.login as anonymous"

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print "error cannot cd to ", DIRN
        f.quit()
        return

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write())
    except ftplib.error_perm:
        print "error cannot read file"
        os.unlink(FILE)
    else:
        print "download success", FILE
    f.quit()


if __name__ == '__main__':
    main()
