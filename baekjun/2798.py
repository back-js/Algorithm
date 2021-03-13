N , M = map(int,input().split())
array = list(map(int,input().split()))

from itertools import combinations

a = list(combinations(array,3)) # 
n_array = []

for i in a :
    s = sum(i)
    if (M - s) >= 0  :
       n_array.append(s)

print(max(n_array))

# 시간 복잡도 고려 안해도 돼나 ?