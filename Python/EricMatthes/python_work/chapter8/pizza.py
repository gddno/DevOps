def make_pizza(size, *toppings):
    print("\n Making " +str(size) + "-inch" + " pizza with the following toppings: ")
    for topping in toppings:
	    print("- " + topping)
make_pizza(16, 'peperoni', 'olive', 'extra cheese')
make_pizza(22, 'green pepers')