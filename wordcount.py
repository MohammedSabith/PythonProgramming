fname = input("Enter filename : ")

try:
	fp = open(fname,"r+")
	l = fp.readlines()
	fp.close()
	lines = len(l)
	char = 0
	word = 0
	for i in l:
		char += len(i)
		word += len(i.split(" "))

	print("Lines = ",lines,"\nWords = ",word,"\nChars = ",char)

except:
	print("File not found")