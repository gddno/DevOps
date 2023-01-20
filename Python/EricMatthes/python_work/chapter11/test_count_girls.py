import unittest
from count_girls import CountGirls

class TestCountGirls(unittest.TestCase):

	def setUp(self):
		self.my_girl = CountGirls('nasty', 26, 2000)

	def test_default_price(self):
		self.my_girl.up_price()
		self.assertEqual(self.my_girl.price, 2500)
	def test_custom_price(self):
		self.my_girl.up_price(3000)
		self.assertEqual(self.my_girl.price, 5000)

if __name__ == '__main__':
	unittest.main()