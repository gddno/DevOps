#import get_formatted_name from name_functional
from name_functional import get_formatted_name

print("If you wont stop programm enter 'q'")
while True:
	first = input("Enter first name: ")
	if first == 'q':
		break
	last = input("Enter last name: ")
	if first == 'q':
		break
	full_name = get_formatted_name(first,last)
	print("Your full name: " + full_name)