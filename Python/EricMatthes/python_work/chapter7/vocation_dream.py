list_plases = []

active = True

while active:
    place = input("Where you dream spend time for vocation?: ")
    if place == 'quit':
	    active = False
    else:
	    list_plases.append(place)
for one in list_plases:
    print(one)
