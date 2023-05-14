def sieve(lst):
    unique_lst = list(set(lst))
    unique_lst.reverse()
    return tuple(unique_lst)

print(sieve([2, 3, 4, 4, 5, 6, 6, 6, 7]))