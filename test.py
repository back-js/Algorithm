
0 1 2 3 4 5 6 7 8 9
0 1 1 1 1 1 1 1 1 1
dp = [[] for i in range(N+1)]
dp[1] = 8
for i in range(N+1):
    if dp[i] == 0 :
        dp[i] = dp[i-1] * 2

