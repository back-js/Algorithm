
dp = [1,3]

for i in range(2,10):
    s = dp[i-2] +dp[i-1] + 1
    dp.append(s)
print(dp)