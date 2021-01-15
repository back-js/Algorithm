N = int(input())

dp = [[] for i in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
print(dp)
print(dp[1][1])