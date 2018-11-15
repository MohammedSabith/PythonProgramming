def easyPal(s):
	if(s[::]==s[::-1]):
		return True
	else:
		return False

def hardPal(s):
	n = len(s)
	for i in range(n//2):
		print(i," -> ",-i-1)
		if(s[i]!=s[-i-1]):
			break
	else:
		return True

	return False



st = input("Enter string : ")
print("Hard pal : ",hardPal(st))
 