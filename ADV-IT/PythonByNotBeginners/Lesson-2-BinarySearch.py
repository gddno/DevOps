# -------------------------------------------------------
# Program by Zhuravlev D.D.
#
# Version       Date           Info
# 1.0           2022       Initial Version
#--------------------------------------------------------

mylist = [1,243,33,43,20,3445,465,42,12,2,12,43,546,576,5,76,88]

mylist.sort()
count = 0
#a = mylist
#print(a)
for element in mylist:
    #if element%5 == 0:
        count += 1
print("Count elemets of list = ", count)

def binary_search(list, search_number, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if search_number == mylist[mid]:
            return mid
        elif search_number < mylist[mid]:
            return binary_search(mylist, search_number,start, mid - 1)
        else:
            return binary_search(mylist, search_number, mid+1, stop)




search_number = 575
x = binary_search(mylist, search_number, 0, count)

if x == False:
    print("Item", search_number,"Not Found!")
else:
    print("Item", search_number, "Found at Index ", x-1)