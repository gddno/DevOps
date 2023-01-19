import unittest
from city_functions import get_param


class NameTestCase(unittest.TestCase):
	def test_country_city(self):
		result = get_param('Russia','Krasnodar')
		self.assertEqual(result, 'Russia Krasnodar')
	def test_country_city_count(self):
		result = get_param('Russia','Krasnodar','500000')
		self.assertEqual(result, 'Russia Krasnodar 500000')
if __name__ == '__main__':
	unittest.main()