1
3
5
2 6

N = int(input())
dp = [1,3]
if N ==1 :
    print(N)

elif N == 2 :
    print(3)

else :
    for i in range(2,N):
        s = dp[i-2] +dp[i-1] + 1
        dp.append(s)
    print(dp[-1]%10007)