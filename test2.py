from itertools import combinations
array = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
a = list(combinations(array,3))
n_array = []

for i in a :
    s = sum(i)
    if (500 - s) > 0  :
        #cnt = 21 - s
       n_array.append(s)

print(n_array)



