N = int(input())

dp = [[0,0,0,0,0,0,0,0,0,0] for i in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
if N>=2 :
    for i in range(2,N+1):
        for j in range(len(dp[1])):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9 :
                dp[i][j] = dp[i-1][j-1]
            else :
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%1000000000)

