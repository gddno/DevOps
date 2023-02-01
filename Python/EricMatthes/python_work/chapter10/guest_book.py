file_path = './files/guest_book.txt'

while True:
    name = input("Enter your name for guest_book: ")
    if name != 'stop':
	    print("Hi " + name + " your name add in guest book.")
	    with open(file_path, 'a') as file_object:
		    file_object.write(name + ".\n")
	    prichina = input("Why you like proggramming?: ")
	    with open(file_path, 'a') as prich:
		    prich.write(prichina + ".\n")
    else:
	    break