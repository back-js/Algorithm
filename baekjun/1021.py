from collections import deque

n,m = map(int,input().split())
target = list(map(int,input().split()))
s = []
for i in range(1,n+1) :
    s.append(i)

def left(stack) :
    s = stack.pop(0)
    stack.append(s)

def right(stack) :
    s = stack.pop()
    stack.insert(0,s)

cnt = 0
for t in target :
    w = s.index(t)
    while s[0] != t :
        cnt += 1
        if w > (len(s)//2) :
            right(s)
        else :
            left(s)
    s.pop(0)

print(cnt)

