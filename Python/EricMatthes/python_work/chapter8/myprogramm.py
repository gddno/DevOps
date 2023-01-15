def swap(first, second):
    while first:
	    cu = first.pop()
	    second.append(cu)
    print(second)
