def junkOff(s):
	junk =  "'!()-[]{};:''',\<>/?@#$%^&*_~"

	ns = ""
	for i in s:
		if(i not in junk):
			ns += i

	print(ns)




junkOff("s-[ab}:ith;'")
