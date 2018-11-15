'''Suppose  that  a  text  file  contains  an  unspecified  number  of  scores.  Write  a  program 
that  reads  the  scores  from  the  file  and  displays  their  total  and  average.  Scores  are 
separated by blanks. Your program should prompt the user to enter a filename.'''

fname = input("Enter the filename : ")
try:
	fp = open(fname,"r+")
	l = fp.readlines()
	fp.close()

	count = 0
	val = 0

	for i in l:
		d = list(map(int,i.split(" ")))
		count += len(d)
		val += sum(d)

	print("Sum = ",val,"\nAvg = ",(val/count))


except FileNotFoundError:
	print("File not found")
