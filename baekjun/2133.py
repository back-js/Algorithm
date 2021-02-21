
N= int(input())

dp = [0] * 31
dp[2] = 3
for i in range(3,31) :
    k = i
    if i % 2 == 0  :
        s = 2 + dp[i-2] * 3
        while i > 2 :
            i -= 2
            s += dp[i-2] * 2
        dp[k] = s

print(dp[N])
