N = int(input())

for i in range(N) :
    stack = []
    s = list(input())
    while s :
        a = s.pop(0)
        stack.append(a)
        if len(stack) > 1:
            if stack[-1] == ')' and stack[-2] == '(' :
                stack.pop()
                stack.pop()
    if len(stack) == 0 :
        print('YES')
    else :
        print('NO')