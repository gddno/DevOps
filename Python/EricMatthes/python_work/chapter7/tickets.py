promt = "\nPlease enter your age and will know price for your ticket: "

while True:
    age = input(promt)
    age = int(age)
    if age <= 3:
	    print("Please go free")
    elif 3 < age <= 12:
	    print("Price will be 10$")
    else:
	    print("Price will be 15$")
