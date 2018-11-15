import socket
import sys

s = socket.socket()

host = "127.0.0.1"
port = 6969

s.bind((host,port))
s.listen(5)

while True:
	c,addr = s.accept()
	print("Connected to ",addr)
	exp = c.recv(4096)
	print("Received ",exp)

	l = list(exp.split(" "))
	a = int(l[0])
	b = int(l[2])

	op = l[1]

	res = 0
	if(op == '+'):
		res = a + b
	elif(op == '-'):
		res = a - b
	elif(op == '*'):
		res = a * b
	elif(op =='/'):
		res = a / b

	print(res)
	res = str(res)
	c.send(res)

	break

s.close()