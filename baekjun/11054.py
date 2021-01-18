#10
#1 5 2 1 4 3 4 5 2 1
# 1 2 2 1 3 3 4 5 2 1
#1 2 5 4 3 4 1 2 5 1
# 1 2 3 3 3 4 1 2 5 1
n = int(input())
a = list(map(int, input().split()))
a_r = list(reversed(a))
dp_up = [0 for i in range(n)]
dp_down = [0 for i in range(n)]
result = []
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp_up[i] < dp_up[j]:
            dp_up[i] = dp_up[j]
    dp_up[i] += 1

for i in range(n):
    for j in range(i):
        if a_r[i] > a_r[j] and dp_down[i] < dp_down[j]:
            dp_down[i] = dp_down[j]
    dp_down[i] += 1



for k in range(n):
    s = dp_down[k] + dp_up[n-k-1]
    result.append(s-1)

print(max(result))