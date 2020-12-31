s = '1 2 3 4'


def solution(s):
    list_s = list(map(int, s.split()))
    result = []
    result.append(min(list_s))
    result.append(max(list_s))
    answer = ''
    for i in range(len(result)):
        answer += str(result[i])
        if i == len(result)-1:
            pass
        else :
            answer += ' '
    return answer

print(solution(s))