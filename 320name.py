bid = int(input("Enter bill id:"))
cid = int(input("Enter cust id:"))

bamt = float(input("Enter bill amt:"))
cname = input("Enter name:")

while True:
	if(len(cname)>3 and len(cname)<20):
		break
	else:
		cname = input("Enter name:")


print("Bill id : ",bid)
print("Cust id : ",cid)
print("Bill amount : ",bamt)
print("Cust name : ",cname )