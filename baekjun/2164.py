from collections import deque

N = int(input())
s = deque([])
for i in range(1,N+1) :
    s.append(i)

while True :
    s.popleft()
    if len(s) > 1 :
        a = s.popleft()
        s.append(a)
    else :
        break

print(s.pop())