import random as rand

n = int(input("Enter n : "))
l = [0,1]

for i in range(n):
	for j in range(n):
		print(rand.randint(0,1),end=" ") #rand.choice(l)

	print()