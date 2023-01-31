from urllib import request
import sys

myURL = "https://adv400.tripod.com/kartinka.jpg"
myFile = "D:\\DevOps\\DevOps\\SuportFiles\\myKartinka.jpg"
try:
    print ("Start Download file from: " + myURL)
    request.urlretrieve(myURL, myFile)
except Exception:
    print("Error!!!")
    print(sys.exc_info()[1])
    exit

print("File Downloaded and seved at: " + myFile)