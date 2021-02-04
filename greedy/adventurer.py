n = int(input())
data = list(map(int,input().split()))
data.sort(reverse=True)
answer = 0

while len(data) > 0 :
    s = data.pop(0)
    for i in range(s-1):
        data.pop()
    answer += 1

print(answer)