N = int(input())

dp=[0]*20
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,14) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(N) :
    s = int(input())
    print(dp[s])


