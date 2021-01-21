target = int(input())
N = int(input())
s= list(input().split())

number = [0,1,2,3,4,5,6,7,8,9]

result = []
for i in range(1000000):
    broken = False
    for j in str(i):
        if j in s:
            broken = True
    if broken == True :
        pass
    else :
        result.append(abs(target-i))

print(min(min(result)+len(str(target-min(result))),target-100))