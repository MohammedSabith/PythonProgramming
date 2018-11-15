
d = {'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}

sort_d = sorted(d,key=d.get,reverse=True)

print(sort_d[:3])

# maxd = 'John'

# #print(max(d.values()))

# def max(d):
# 	for i in d:
# 		if(d[i]>d[maxd]):
# 			maxd = i

# 	print(maxd)

l = [86.5,91.2,84.5,72.1,80.5]
n = ['John','Jack','Jill','Harry','Joe']

val = 0
for i in l:
	val += i

avg = val/float(len(l))

for i in range(3):
	maxd = l.index(max(l))
	print(n[maxd]," ",l[maxd])
	l[maxd] = -1

print(avg)