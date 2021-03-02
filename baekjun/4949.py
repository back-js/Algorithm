result = []

while True :
    stack = []
    s = list(input())
    if s == ['.'] :
        break

    for i in s :
        if i =='(' or i ==')' or i =='[' or i ==']':
            stack.append(i)
        if len(stack) > 1 :
            if stack[-1] == ')' and stack[-2] == '(' :
                stack.pop()
                stack.pop()
            elif stack[-1] == ']' and stack[-2] == '[' :
                stack.pop()
                stack.pop()
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
