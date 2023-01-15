promt = "\nEnter your favorite city"
promt += "\nIf you want finishif our programm enter 'quit': "

while True:
    city = input(promt)

    if city == 'quit':
	    break
    else:
	    print("Oooo " + city.title() + " very beutiful city!!!!")