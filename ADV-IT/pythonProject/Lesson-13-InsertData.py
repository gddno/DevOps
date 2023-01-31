# name = input("Please enter your name: " )

# print("Privet " + name)

# x1 = input("Enter X :")
# y1 = input("ENter Y :")
# summa = int(x1) + int(y1)
# print(summa)

# message = ""

# while True:
#     message = input ("Enter Password ")
#     if message == 'sekret':
#         break
#     print(message + " Password not correct")
# print("Password was: " + message)

mylist = []

msg = ""

while msg !='stop'.upper():
    msg = input("Enter new item, and STOP to finish : ")
    mylist.append(msg)
print(mylist)