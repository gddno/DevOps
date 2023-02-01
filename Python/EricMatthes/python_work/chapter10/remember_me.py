import json 
def greet_user():

    file_name = 'nameUser.json'
    try:
	    with open(file_name) as f_obj:
		    username = json.load(f_obj)
    except FileNotFoundError:
		    username = input("Please, enter your name: ")
		    with open(file_name, 'w') as f_obj:
			    json.dump(username, f_obj)
			    print("We'll remeber you when you come back, " + username + "!!!")
    else:
	    print("Welcome back, " + username + "!")


greet_user()