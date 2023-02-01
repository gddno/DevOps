import json

file_name = 'favorite_namber.json'

def give_number():
    number = input("Enter please your favorite number: ")
    try:
	    with open(file_name, 'w') as f_obj:
		    json.dump(number, f_obj)
		    print("Your favorite number is " + number + "!!!")
    except FileNotFoundError:
	    return None
    else:
	    return number
	    
def read_number():
    with open(file_name) as f_obj:
	    know = json.load(f_obj)
	    print("I know your favorite number: " + know + ".")

def get_new_number():
    number = input("Enter new favorite nimber: ")
    with open(file_name, 'w') as f_obj:
	    json.dump(number, f_obj)
    return number


give_number()
read_number()
get_new_number()
