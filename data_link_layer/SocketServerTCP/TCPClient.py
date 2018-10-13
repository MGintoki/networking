from socket import *


HOST = 'localhost'
PORT = 12000
BUFSIZE = 1024
ADDR = (HOST, PORT)


while True:
    tcpCliSocket = socket(AF_INET, SOCK_STREAM)
    tcpCliSocket.connect(ADDR)
    data = raw_input('>')
    if not data:
        break
    tcpCliSocket.send(data)
    data = tcpCliSocket.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    tcpCliSocket.close()
