visitors = ['Cleopatra', 'teslo', 'stalin']
visitors[0] = 'Afroditaa'
#pop_visitor = visitors.pop(0)
message = f"Dear {visitors[0].title()} you can visiting to famouse retoran"
print(message)

print(visitors)
print("i will make more visitors")
visitors.insert(0, 'Cesore')
print(visitors)
visitors.insert(2, 'Chingiz Han')
print(visitors)
visitors.append('Monika')
print(visitors)
message = f"Dear {visitors[0].title()} you can visiting to famouse retoran"
print(message)
message = f"Dear {visitors[1].title()} you can visiting to famouse retoran"
print(message)
message = f"Dear {visitors[2].title()} you can visiting to famouse retoran"
print(message)
message = f"Dear {visitors[3].title()} you can visiting to famouse retoran"
print(message)
message = f"Dear {visitors[4].title()} you can visiting to famouse retoran"
print(message)
message = f"Dear {visitors[5].title()} you can visiting to famouse retoran"
print(message)
pop_visitor = visitors.pop()
print(f"Sorry {pop_visitor} you dont't go to restoran")
pop_visitor = visitors.pop()
print(f"Sorry {pop_visitor} you dont't go to restoran")
pop_visitor = visitors.pop()
print(f"Sorry {pop_visitor} you dont't go to restoran")
pop_visitor = visitors.pop()


print(f"Dear {visitors[0]} you mast go to restoran")
print(f"Dear {visitors[1]} you mast go to restoran")
del visitors[1]
del visitors[0]
print(visitors)
visitors = ['Cleopatra', 'teslo', 'stalin']
len_visitors = len(visitors)
print(f"I meet {len_visitors} visitors")