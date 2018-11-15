from threading import Thread

class MyThread(Thread):
	
	def __init__(self,ThreadId,name,s):
		Thread.__init__(self)
		self.name = name
		self.s = s


	def run(self):
		print("starting ",self.name,"...")
		if(self.name == "palindrome"):
			self.checkPal()
		elif(self.name == "vowel"):
			self.countVow()


	def checkPal(self):
		st = self.s
		if(st[::] == st[::-1]):
			print("palindrome")
		else:
			print("not palindrome")


	def countVow(self):
		st = self.s
		st = st.lower()
		vow = "aeiou"
		cnt = 0
		for i in st:
			if(i in vow):
				cnt += 1

		print("Vowel count = ",cnt)


st = input("Enter string : ")
t1 = MyThread(1,"palindrome",st)
t2 = MyThread(2,"vowel",st)

t1.start()
t2.start()

t1.join()
t2.join()

print("Exiting main thread")
