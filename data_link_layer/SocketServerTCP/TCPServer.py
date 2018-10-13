from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)



HOST = ''
PORT = 12000
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):

    def handle(self):
        print "connect from ",  self.client_address
        print "message: ", self.rfile.readline()


tcpServ = TCP(ADDR, MyRequestHandler)
print "wait for connection.."
tcpServ.serve_forever()
