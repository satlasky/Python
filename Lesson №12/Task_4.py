def del_from_tuple(tup, elem):
    try:
        index = tup.index(elem)
        return tup[:index] + tup[index + 1:]
    except ValueError:
        return tup


tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 'a', 'b', 'c', 'd')

print(del_from_tuple(tup1, 3))
print(del_from_tuple(tup2, 'e'))