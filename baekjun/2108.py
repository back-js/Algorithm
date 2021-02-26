'''

5
1
3
8
-2
2
예제 출력 1 
2
2
1
10

'''

N = int(input())
num = []
for i in range(N) :
    s = int(input())
    num.append(s)
num.sort()
cc = {}
a = int(sum(num)/N)
b = num[int(N/2)]



cc = {}
for i in num:
    s = num.count(i)
    cc[i] = s

cc_sort = sorted(cc.items(), key = lambda item: item[1], reverse = True)
v = 0
key_n = []
for key, value in cc_sort:
    if value >= v :
        v = value
        key_n.append(key)
key_n.sort()
c = key_n[1]
d = max(num) - min(num)

print(a)
print(b)
print(c)
print(d)

####

import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_s = Counter(nums).most_common()
print(round(sum(nums) / n))
print(nums[n // 2])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(nums[-1] - nums[0])