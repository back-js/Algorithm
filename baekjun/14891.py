"""
예제 입력 1 
10101111
01111101
11001110
00000010
2
3 -1
1 1

예제 출력 1 
7

총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
예제 입력 2 
11111111
11111111
11111111
11111111
3
1 1
2 1
3 1
예제 출력 2 
15

예제 입력 3 
10001011
10000011
01011011
00111101
5
1 1
2 1
3 1
4 1
1 -1
예제 출력 3 
6
"""
from collections import deque


wheel = []
for i in range(4) :
    s = deque(list(map(int,input())))
    wheel.append(s)

n = int(input())

number = deque()
for i in range(n):
    s = list(map(int,input().split(' ')))
    number.append(s)

while number :
    s = number.popleft()
    a , b = s[0], s[1]
    a -= 1
    if wheel[a][6] != wheel[a+1][2] :












