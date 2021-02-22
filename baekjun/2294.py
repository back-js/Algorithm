N, K = map(int,input().split())
coin = []
for i in range(N) :
    s = int(input())
    coin.append(s)


arr = [1000000] * 10001
arr[0] = 0

for i in coin :
    for j in range(i,10001) :
        arr[j] = min(arr[j-i]+1, arr[j])

if arr[K] == 1000000:
    print(-1)
else :
    print(arr[K])

