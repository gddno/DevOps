from urllib import request
import sys

myURL = "https://www.astahov.net"
try:
    otvet =request.urlopen(myURL)
    mytext1 = otvet.readlines()
    mytext2 = otvet.read()
    print(otvet)
    print(mytext2)
    for line in mytext1:
        print(line)
except Exception:
    print(sys.exc_info()[1])
else:
    print("Successful connection with " + str(myURL) + " site")