a = input().split('-')
cnt = 0

cnt += eval(a[0])
for i in range(1,len(a)) :
    cnt -= eval(a[i])

print(cnt)