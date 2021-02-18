import itertools
s = itertools.product([1,2], repeat=2)
print(sum(list(s)[1]))

