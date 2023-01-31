import json



file_name = 'nameUser.json'

while True:
    name = input("Enter your name bro: ")
    if name != 'stop':
	    with open(file_name, 'w') as f_obj:
		    json.dump(name, f_obj)
    else:
	    break
