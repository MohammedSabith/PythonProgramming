
def fib(n):
	if(n<1):
		print("Invalid")
	
	if(n >= 1):
		print(0,end=" ")

	if(n >= 2):
		print(1,end=" ")

	if(n>2):
		fib1 = 0
		fib2 = 1
		while(n!=0):
			fib3 = fib1 + fib2
			print(fib3,end=" ")
			n -= 1
			fib1 = fib2
			fib2 = fib3

	print()


n = int(input("Enter n : "))
fib(n-2)