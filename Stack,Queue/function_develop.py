'''
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

-작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
-작업 진도는 100 미만의 자연수입니다.
-작업 속도는 100 이하의 자연수입니다.
-배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    day = []

    for i in range(len(progresses)):
        k = math.ceil((100- progresses[i]) / speeds[i])
        day.append(k)

    day = deque(day)
    while day :
        c = day.popleft()
        count = 1
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

    return answer


    ######################################## 다른 사람 풀이 공부

def solution(progresses, speeds):
        Q = []
        for p, s in zip(progresses, speeds):
            if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
                Q.append([-((p - 100) // s), 1])
            else:
                Q[-1][1] += 1
        return [q[1] for q in Q]

#############################################

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])

###########################################

import math

def solution(progresses, speeds):
    answer = []
    rest = []
    temp = []

    size = len(progresses)

    for i in progresses:
        rest.append(100 - i)

    for i in range(size):
        temp.append(math.ceil(rest[i] / speeds[i]))

    cnt = 0
    p = temp[0]
    for i in range(len(temp)):
        if p < temp[i]:
            answer.append(cnt)
            p = temp[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)


    return answer

