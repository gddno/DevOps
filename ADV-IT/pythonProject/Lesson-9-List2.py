#           0     1       2        3      4

cars = ['bmw', 'lada', 'seat', 'skoda', 'vw']

for car in cars:
    print(car.upper())

for number in range(1, 6):
    print(number)

my_number_list = list(range(0, 10))

print (my_number_list)

for x in my_number_list:
    x = x * 2 
    print(x)
my_number_list.sort(reverse=True)
print(my_number_list)

print(max(my_number_list))
print(min(my_number_list))
print("Sum of list: " + str(sum(my_number_list)))
print(cars)
my_Cars = cars[:1]
print(my_Cars)
My_cars = cars[-1:]
print(My_cars)
new_array_cars = cars[:]
print(new_array_cars)