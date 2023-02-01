from urllib import request, parse
import sys

myURL = "https://www.google.com/search?"
value = {'q': 'ANDESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print (mydata)
    myURL = myURL + mydata
    req = request.Request(myURL, headers = myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print(sys.exc_info()[1])