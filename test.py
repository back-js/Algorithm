from collections import deque


wheel = []
for i in range(4) :
    s = deque(list(map(int,input())))
    wheel.append(s)

print(wheel)