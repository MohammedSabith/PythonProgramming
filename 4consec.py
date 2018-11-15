l = []
l = input("Enter list : ").split(" ")

n = len(l)

for i in range(n-3):
	if(l[i]==l[i+1] and l[i]==l[i+2] and l[i]==l[i+3]):
		print("4 consecutive ",l[i])
		break

