tup = (1, 3, 5, 7, 9, 5, 8)
elem = 5

def slicer(tup, elem):
    if elem not in tup:
        return tuple()
    elif tup.count(elem) == 1:
        return tup[tup.index(elem):]
    else:
        start = tup.index(elem)
        end = tup.index(elem, start+1)
        return tup[start:end+1]

result = slicer(tup, elem)
print(result)