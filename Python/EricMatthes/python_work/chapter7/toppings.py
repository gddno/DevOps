promt = "\nPlese enter topping witch you wont: "
promt += "\nIf you want finishid programm enter 'quit': "
active = True

while active:
    topping = input(promt)
    
    if topping == 'quit':
	    active = False
    elif topping == 'hi':
	    break
    else:
	    print("You add " + topping + " very nice choice:)")