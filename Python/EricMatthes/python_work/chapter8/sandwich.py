def sandwich(*toppings):
    print("\nList choise toppings: ")
    for topping in toppings:
	    print("-" + topping)

sandwich('peiper', 'cheese', 'bicon', 'cucumber')
sandwich('chicken')
sandwich('milk', 'panapple')