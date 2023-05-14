def tpl_sort(t):
    if all(isinstance(i, int) for i in t):
        return tuple(sorted(t))
    else:
        return t

input_tuple = (3, 1, 4, 2)
output_tuple = tpl_sort(input_tuple)
print(output_tuple)