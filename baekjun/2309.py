'''
일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

예제 입력 1  복사
20
7
23
19
10
15
25
8
13
예제 출력 1  복사
7
8
10
13
19
20
23
'''
boy = []
for i in range(9) :
    s = int(input())
    boy.append(s)

from itertools import combinations

s = list(combinations(boy,7))
for i in range(len(s)):
    result = []
    if sum(s[i]) == 100 :
        for j in s[i]:
            result.append(j)
        result.sort()
        for k in result :
            print(k)
        break

    ####

s = []
for i in range(9):
    s.append(int(input()))
sum_s = sum(s)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (s[i] + s[j]) == 100:
            one = s[i]
            two = s[j]
s.remove(one)
s.remove(two)
s.sort()
for i in s:
    print(i)

