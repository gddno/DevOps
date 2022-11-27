import sys






filename = "../SupotFiles/list_of_password.txt"

while True:
    try:
        print("Inside Try")
        myfile = open(filename, mode = 'r', encoding= 'Latin-1')
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])
        filename = input("Input Correct file name! :")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print("Inside FINALLY")

print("====================EOF=====================")