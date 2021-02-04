n= int(input())
step = []
for i in range(n):
    s = int(input())
    step.append(s)
dp = [0 for _ in range(n)]
# 계단을 밟고, 다음계단을 밟는경우
# 계단을 밟고, 다음계단을 밟지않는 경우
6
10 20 15 25 10 20


n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])

