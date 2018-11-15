l = []
l = input("Enter list : ").split(" ")

n = len(l)

#print(l)


minl = 0
for i in range(1,n):
	if(l[i]<l[minl]):
		minl = i


print("Index of smallest element : ",minl)