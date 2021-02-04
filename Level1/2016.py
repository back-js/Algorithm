def solution(a, b):
    day = 0
    if a == 1:
        day = 0
    elif a == 2:
        day = 31
    elif a == 3:
        day = 60
    elif a == 4:
        day = 91
    elif a == 5:
        day = 121
    elif a == 6:
        day = 152
    elif a == 7:
        day = 182
    elif a == 8:
        day = 213
    elif a == 9:
        day = 244
    elif a == 10:
        day = 274
    elif a == 11:
        day = 305
    elif a == 12:
        day = 335

    result = day + b - 1
    answer = ''

    if result % 7 == 0:
        answer = 'FRI'
    elif result % 7 == 1:
        answer = 'SAT'
    elif result % 7 == 2:
        answer = 'SUN'
    elif result % 7 == 3:
        answer = 'MON'
    elif result % 7 == 4:
        answer = 'TUE'
    elif result % 7 == 5:
        answer = 'WED'
    elif result % 7 == 6:
        answer = 'THU'
    return answer