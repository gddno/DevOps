import unittest
from name_functional import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
	    formatted_name = get_formatted_name('janis','joplin')
	    self.assertEqual(formatted_name,'Joplin Janis')
<<<<<<< HEAD
	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('dima','zhuravlev','two')
		self.assertEqual(formatted_name, 'Zhuravlev Dima Two')
if __name__ == '__main__':
	unittest.main()
=======

unittest.main()


















>>>>>>> 1588bb1c3be56a5cdd606a082cdd341944341d67
