def make_shirt(razmer = 'L', text = 'I like Python'):
    print("\nYour razmer is: " + razmer + " and your text is: " + text.title())

def describe_city(city = 'moscow', cantry = 'russia'):
    print("\n" + city.title() + " is in " + cantry.title())

make_shirt('5', 'i love you')
make_shirt(text = 'you are the best', razmer = '20')
make_shirt()
describe_city(cantry = 'USA', city = 'new-Yeark')
describe_city()