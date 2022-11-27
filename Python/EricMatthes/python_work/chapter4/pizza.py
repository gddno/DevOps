my_pizza = ['margarita', 'peperony', '4chis']
your_pizza = my_pizza[:]
#for pizza in pizza_list:
 #   print(f"I like {pizza} pizza!!!")
#print("\nI really love pizza!!!")
my_pizza.append('mama_pizza')
your_pizza.append('papa_pizza')
print(my_pizza)
print(your_pizza)
print('My favorite pizza:')
for pizza in my_pizza:
    print(pizza)
print('Your favorite pizza:')
for pizza in your_pizza:
    print(pizza)
