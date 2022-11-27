# -------------------------------------------------------
# Program by Zhuravlev D.D.
#
# Version       Date           Info
# 1.0           2022       Initial Version
# -------------------------------------------------------

mylist = [1, 45, 3, -10, 4, 454, 49, 768]

#
# mylist.sort()
# print(mylist)

def BubbleSort(mylist):
    index_last_item = len(mylist) - 1
    for z in range(0, index_last_item):
        for x in range(0, index_last_item - z):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist
print("Old list", mylist)
NewList = BubbleSort(mylist).copy()
print("New list", NewList)