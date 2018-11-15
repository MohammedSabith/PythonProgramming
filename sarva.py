import socket
import sys

s = socket.socket()
print "Started..."
host = "127.0.0.1"
port = 6967

s.bind((host,port))
s.listen(5)

while True:
	c, addr = s.accept()
	fp = open("recv2.txt","wb")
	print "connected to ",addr
	data = c.recv(4096)
	if not data:
		break
	fp.write(data)
	break

fp.close()
s.close()

