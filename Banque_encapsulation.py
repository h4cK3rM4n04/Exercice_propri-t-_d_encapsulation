#coding:utf-8

class BankAccount:

	"""docstring for BankAccount"""

	def __init__(self, account_number, initial_balance):

		self._account_number = account_number
		self._initial_balance = initial_balance

	def deposit(self, amount):
		self._initial_balance += amount
		if self._initial_balance < 0:
			self._initial_balance = 0

	def withdraw(self, amount):
		self._initial_balance -= amount
		if self._initial_balance < 0:
			self._initial_balance = 0

	def get_AccountNumber(self):
		return self._account_number

	def _get_balance(self):
		return self._initial_balance

	x = property(_get_balance, get_AccountNumber)


if __name__ == "__main__":

	balance_1 = BankAccount(412, 50)
	balance_2 = BankAccount(5612, 25)
	balance_3 = BankAccount(52, 56)

	balance_3.withdraw(55)
	print(balance_3.x)