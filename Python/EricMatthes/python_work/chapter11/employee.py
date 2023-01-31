class Employee():
	"""Этот класс представляет работника"""
	def __init__(self,name,last_name, salary):
		self.name = name.title()
		self.last_name = last_name.title()
		self.salary = salary

	def give_raise(self, amount = 50000):
		"""Увеличивает оклад на 5000$"""
		self.salary += amount
		# update = int(input("Enter your apper salary: "))
		# if update == 0:
		# 	self.salary += self.update_default
		# 	print(self.name.title()+" "+self.last_name.title()+" "+"you salary in year is: " + str(self.salary) + "$.")
		# else:
		# 	self.salary += update
		# 	print(self.name.title()+" "+self.last_name.title()+" "+"you salary in year is: " + str(self.salary) + "$.")

Dima = Employee('dmitriy', 'zhuravlev', 2000000)
Dima.give_raise()