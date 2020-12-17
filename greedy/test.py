from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)):
        k = math.ceil((100- progresses[i]) / speeds[i])
        day.append(k)
    day = deque(day)
    print(day)
    while day :
        c = day.popleft()
        count = 1
        print(c)
        del2 =[]
        for i in range(len(day)):
            if c >= day[i]:
                count +=1
                del2.append(day[i])
            else :
                break
        answer.append(count)
        for i in del2:
            day.remove(i)

    print(answer)



solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])