def solution(expression):
    result = []
    tmp =''
    for i in range(len(expression)):
        if expression[i] not in ['+','-','*'] :
            tmp += str(expression[i])
        else :
            result.append(int(tmp))
            result.append(str(expression[i]))
            tmp =''
        if i == len(expression) - 1 :
            result.append(int(tmp))
    cnt = 0
    order = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','+','-'],['*','-','+']]
    for i in order :
        copy_expression = result
        for operator in i :
            idx = 0  # 연산자를 하나씩 가져와서
            while idx < len(copy_expression):
                if copy_expression[idx] == operator:  # 연산해준다.
                    if operator == '-':
                        cal = int(copy_expression[idx-1]) - int(copy_expression[idx+1])
                    elif operator == '+':
                        cal = int(copy_expression[idx-1]) + int(copy_expression[idx+1])
                    else:
                        cal = int(copy_expression[idx-1]) * int(copy_expression[idx+1])

                    copy_expression = copy_expression[:idx-1] + list(str(cal).split()) + copy_expression[idx+2:]  # 계산 한 후 계산값을 배열에 넣어준다.

                else:
                    idx += 1
            
            if cnt < abs(int(copy_expression[0])):
                cnt = abs(int(copy_expression[0]))
    return cnt




solution('100-200*300-500+20')