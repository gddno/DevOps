bicycles = ['train', 'tras', 'mount', 'short', 'bmx', 'children']
message = f"Bicycle by number 3 is {bicycles[2].title()}!!!"
print(message)

name_of_frends = ['polina', 'sasha', 'lena', 'artemii', 'ulyana', 'dima', 'lera', 'sveta']
print(name_of_frends[0])
print(name_of_frends[1])
print(f"This is my love freind {name_of_frends[4]}")
bikes = ['Honda', 'bmw', 'suzuki']
message = f"My favorite bike is {bikes[2]}"
print(message)
bikes[1] = 'harley'
bikes.append('ducati')
bikes = []
bikes.append('ducati')
bikes.append('honda')
bikes.append('suzuki')
bikes.insert(1, 'ig')
pop_bikes = bikes.pop(1)
print(bikes)
print('----------------')
print(f"Poped bike from list is {pop_bikes}")
print(bikes)
too_expensive = 'ducati'
bikes.remove(too_expensive)
print(bikes)
print(f"\nA {too_expensive.title()} is too expensive for you!!!")