num = [1,2,3,4,6,7,1,2,3,5,1,2,3]
c={}
for i in num:
    s = num.count(i)
    c[i] = s

cc_sort = sorted(c.items(), key = lambda item: item[1], reverse = True)
print(cc_sort)