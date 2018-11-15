f1 = open("studentScore.py","r+")

s = f1.read()
count = 0
st = ""
for i in s:
	j = i
	if(i=='\n'and count!=9):
		j = " "
		count += 1
	elif(count == 9):
		count = 0
	st += j

f1.close()
f2 = open("studentSc1.py","w+")
f2.write(st)
print(st)
