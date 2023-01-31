def show_magician(list_magicians):
    print("\nLook the list most famouses magicians: ")
    for magician in list_magicians:
	    print(magician + ';')
def make_great(list):
    new_list = []
    print("\nGreate list: ")
    while list:
	    name = list.pop()
	    name = 'Greate ' + name
	    new_list.append(name)
    for new_name in new_list:
	    print(new_name)
origi_list = ['modric', 'ronaldo', 'olivie', 'pogma', 'messi']
show_magician(origi_list)
make_great(origi_list[:])
show_magician(origi_list)