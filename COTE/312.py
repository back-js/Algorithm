N = str(input())
num = list(N)
cnt = int(num.pop(0))
while num :
    s = num.pop(0)
    if cnt == 0 :
        cnt += int(s)
    else :
        if s == '0' or s == '1' :
            cnt += int(s)
        else :
            cnt *= int(s)

print(cnt)

