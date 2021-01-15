'''
- 0 1
2 1 0
3 1 1
4 2 1
5 3 2
6 5 3
7 8 5
'''
N = int(input())
dp = [[0]*2 for i in range(N+1) ]
dp[1] = [0,1]

if N >= 2 :
    dp[2] = [1, 0]
    for i in range(3,N+1):
        for j in range(2):
            if j == 0 :
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            else :
                dp[i][j] = dp[i-1][j-1]

print(sum(dp[N]))