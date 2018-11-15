import socket
import sys

s = socket.socket()
host = "127.0.0.1"
port = 7777
s.connect((host,port))
fname = input("Enter filename : ")

try:
	fp = open(fname,"rb")
	data = fp.read()
	s.sendall(data)
	print("Data sent from client...")
	s.close()
	fp.close()

except FileNotFoundError:
	print("File Not Found")


