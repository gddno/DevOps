

cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto'] 

print(cities)
print(len(cities))
print(cities[2].upper())

cities[2] = 'Tula'
print(cities[2].upper())

cities.append('Kursk')
cities.append('Yalta')
print(cities)
cities.insert(0, 'Feodosiay')
print(cities)
cities.insert(2, 'Krasnodar')
print(cities)

del cities[1]
print(cities)
cities.remove('Toronto')
print(cities)

delety_city = cities.pop()
print(delety_city)
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
cities.reverse()
print(cities)