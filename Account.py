"""
Design a class named Account that contains:
* A private int data field named id for the account.
* A private float data field named balance for the account.
* A private float data field named annualInterestRate that stores the
current interest rate.
* A constructor that creates an account with the specified id (default 0),
initial balance (default 100), and annual interest rate (default 0).
* The accessor and mutator methods for id , balance , and
annualInterestRate .
* A method named getMonthlyInterestRate() that returns the monthly
interest rate.
* A method named getMonthlyInterest() that returns the monthly
interest.
* A method named withdraws that withdraws a specified amount from
the account.
* A method named deposit that deposits a specified amount to the
account.
(Hint: The method getMonthlyInterest() is to return the monthly interest
amount, not the interest rate. Use this formula to calculate the monthly
interest: balance*monthlyInterestRate. monthlyInterestRate is
annualInterestRate / 12 . Note that annualInterestRate is a percent (like 4.5%).
You need to divide it by 100 .)
Write a test program that creates an Account object with an account id of
1122, a balance of $20,000, and an annual interest rate of 4.5%. Use the
withdraw method to withdraw $2,500, use the deposit method to deposit
$3,000, and print the id, balance, monthly interest rate, and monthly interest.
"""

class Account:
	def __init__(self,id=0,balance=100.0,annualInterestRate=0.0):
		self.__id = id
		self.__balance = balance
		self.__annualInterestRate = annualInterestRate

	def getId(self):
		return self.__id

	def set(self,id):
		self.__id = id

	def getBalance(self):
		return self.__balance

	def setBalance(self,balance):
		self.__balance = balance

	def getAnnualInterestRate(self):
		return self.__annualInterestRate

	def setAnnualInterestRate(self,annualInterestRate):
		self.__annualInterestRate = annualInterestRate


	def getMonthlyInterestRate(self):
		monthlyInterestRate = self.getAnnualInterestRate() / (12 * 100)
		return monthlyInterestRate

	def getMonthlyInterest(self):
		monthlyInterest = self.__balance * self.getMonthlyInterestRate()
		return monthlyInterest

	def withdraws(self,amount):
		self.__balance -= amount

	def deposits(self,amount):
		self.__balance += amount



a1 = Account(1122,20000,4.5)

a1.withdraws(2500)
print("After withdraw : ",a1.getBalance())
a1.deposits(3000)

print("id : ",a1.getId(),"\nBalance : ",a1.getBalance(),"\nmonthly interest rate : ",a1.getMonthlyInterestRate(),"\nmonthly interest : ",a1.getMonthlyInterest())
