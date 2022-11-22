from functools import reduce

L = [1, 3, 5, 3, 5, 44, 23, 0, -8] 
print(reduce(lambda x, y: x if x > y else y, L))
print(reduce(lambda x, y: max(x, y), L))
