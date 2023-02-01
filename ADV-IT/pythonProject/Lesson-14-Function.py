
# def foo(name):
#     print("Hello " + name + " " + "you are the best!!!")
#     print("Hello")
# def summa(a, b):
#     print(int(a) + int(b))

# # def foo2():
# #     print("Goodbay")
# #     print("Goodbay")

# print("-----------------------------")

# name = input("Enter your name :")
# foo(name)
# print("_-_-_-_-_-_-_-_-_-_")
# a = input("Enter first number" + name  +": ")
# b = input("Enter second munber :")
# summa(a, b)

# def summa(a, b):
#     return a+b

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# x = summa(1, 2)
# print(x)

from argparse import _VersionAction


def factorial(x):
    """calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x+1): # for(int i = 0; i < x+1; i++)
        otvet = otvet * i 
    return otvet
# print(factorial(1))
# print(factorial(5))
for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

