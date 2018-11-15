import socket
import sys


s = socket.socket()

host = "127.0.0.1"
port = 6969
s.connect((host,port))

exp = raw_input("Enter the expression : ")

s.send(exp)

print("Data sent...")

res = s.recv(4096)

print "Result : " + res

s.close()