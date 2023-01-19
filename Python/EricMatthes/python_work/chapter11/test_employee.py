import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):

		self.test_employee = Employee('dima','zhuravlev')

	def test_give_default_raise(self):


	def test_give_custom_raise(self):
