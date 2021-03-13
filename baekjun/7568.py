N = int(input())
array = []
for i in range(N) :
    a, b = map(int,input().split())
    array.append([a,b])
result = []

for i in array :
    cnt = 1
    a, b = i[0], i[1]
    for j in array :
        x, y = j[0], j[1]
        if a < x and b < y :
            cnt += 1
    print(cnt,end=' ')




