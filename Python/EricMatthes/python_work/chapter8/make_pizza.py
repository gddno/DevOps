def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the folowwing ttoppings: ")
    for topping in toppings:
	    print("- " + topping)
