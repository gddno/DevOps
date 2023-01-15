def get_formatted_name(first_name, last_name):
    full_name = last_name.title() + ' ' + first_name.title()
    return full_name

while True:
    print("\nWhat is your name: ")
    print("(if you wona quit enter 'q')")
    f_name = input("First name: ")
    if f_name == 'q':
	    break
    l_name = input("Last name: ")
    if l_name == 'q':
	    break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")