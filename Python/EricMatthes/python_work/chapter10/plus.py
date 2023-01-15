while True:
    a = input("Please enter first number: ")
    b = input("Please enter second number: ")
    try:
	    c = int(a) + int(b)
    except ValueError:
	    pass
    else:
	    print(c)
