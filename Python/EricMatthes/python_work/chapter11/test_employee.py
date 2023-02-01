import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.my_employee = Employee('dima','zhuravlev', 200000)

	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.salary, 250000)
	def test_give_custom_raise(self):
		self.my_employee.give_raise(70000)
		self.assertEqual(self.my_employee.salary, 270000)

if __name__ == "__main__":
	unittest.main()