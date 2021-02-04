
from itertools import permutations

n = int(input())
k = list(map(int,input().split()))

kk = list(permutations(k))
print(kk)
