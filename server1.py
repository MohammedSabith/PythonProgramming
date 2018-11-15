import socket
import sys

s = socket.socket()

host = "127.0.0.1"
port = 7777

s.bind((host,port))
s.listen(5)

print("started...")

while True:
	c,addr = s.accept()
	print("Connected to ",addr,"...")
	fp = open("recv.txt","wb")
	data = c.recv(4096)
	if not data:
		break
	fp.write(data)
	print("Data received...")
	break

s.close()
fp.close()

