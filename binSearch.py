
def binSearch(l,k):
	n = len(l)
	low = 0
	high = n-1
	while(low<=high):
		mid = (low + high)//2
		if(l[mid] == k):
			print(mid)
			return
		elif(k<l[mid]):
			high = mid -1
		else:
			low = mid + 1

	print("Not found")


l = [1,2,45,68,98,100,234]
k = int(input("Enter element : "))
print(l)
binSearch(l,k)