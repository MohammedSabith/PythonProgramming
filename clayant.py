import socket
import sys

s = socket.socket()

host = "127.0.0.1"
port = 6967

s.connect((host,port))
fname = raw_input("Enter filename : ")

try:
	fp = open(fname,"rb")
	data = fp.read()
	s.sendall(data)
	print "data sent"
	fp.close()

except FileNotFoundError:
	print("FileNotFoundError")

s.close()
