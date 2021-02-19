N = int(input())
dp = [1,2]
if N==1 or N==2 :
    print(N)
else :
    for i in range(2,N):
        n = dp[i-2]+dp[i-1]
        dp.append(n)

    print(dp[-1]%10007)

