from collections import deque

n = int(input())
stack = deque([])
for i in range(n) :
    a = str(input())

    if a == 'pop' :
        if len(stack) > 0 :
            aa = stack.popleft()
            print(aa)
        elif len(stack) == 0 :
            print(-1)
            
    elif a == 'size' :
        print(len(stack))
    
    elif a == 'empty' :
        if len(stack) > 0 :
            print(0)
        elif len(stack) == 0 :
            print(-1)
    
    elif a == 'front' :
        if len(stack) > 0 :
            print(stack[0])
        elif len(stack) == 0 :
            print(-1)

    elif a == 'back' :
        if len(stack) > 0 :
            print(stack[-1])
        elif len(stack) == 0 :
            print(-1)

    elif 'push' in a :
        s,b = a.split(' ')
        stack.append(int(b))