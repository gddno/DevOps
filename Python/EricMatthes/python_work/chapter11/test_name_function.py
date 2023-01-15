import unittest
from name_functional import get_formatted_name

class NamesTestCase(unittest.TestCase):
    

    def test_first_last_name(self):
	    formatted_name = get_formatted_name('janis','joplin')
	    self.assertEqual(formatted_name,'Joplin Janis')

unittest.main()