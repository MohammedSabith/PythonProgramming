def vowCount(s):
	s = s.lower()
	vow = 'aeiou'
	d = dict.fromkeys(vow,0)
	for i in s:
		if(i in vow):
			d[i] += 1

	print("Vowel frequency : ",d)


def numCap(s):
	cnt = 0
	for i in s:
		if(i.isupper()):
			cnt += 1

	print("Number of caps : ",cnt)


s = input("Enter string : ")
numCap(s)
vowCount(s)

