class Employee():
	"""Этот класс представляет работника"""
	def __init__(self,name,last_name):
		self.name = name
		self.last_name = last_name
		self.salary = 200000
		self.update_default = 5000

	def give_raise(self):
		"""Увеличивает оклад на 5000$"""
		update = int(input("Enter your apper salary: "))
		if update == 0:
			self.salary += self.update_default
			print(self.name.title()+" "+self.last_name.title()+" "+"you salary in year is: " + str(self.salary) + "$.")
		else:
			self.salary += update
			print(self.name.title()+" "+self.last_name.title()+" "+"you salary in year is: " + str(self.salary) + "$.")

Dima = Employee('dmitriy', 'zhuravlev')
Dima.give_raise()