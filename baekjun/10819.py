from itertools import permutations

N = int(input())
L = list(map(int,input().split()))
P = list(permutations(L, len(L)))

result = []
for i in P :
    answer = 0
    for j in range(len(L)-1):
        s = abs(i[j] - i[j+1])
        answer += s
    result.append(answer)

print(max(result))
