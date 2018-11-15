s1 = input("Enter s1 : ")
s2 = input("Enter s2 : ")

f = ""

for i in s1:
	if(i.isupper()):
		f += i

for i in s2:
	if(i.isupper()):
		f += i

print(f)
