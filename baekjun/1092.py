'''

문제
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
 

입력
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 
이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 
넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

예제 입력 1 
3
6 8 9
16
2 2 4 5 7 8 8 8 8 8 8 9 9 9 9 9
예제 출력 1 
2

'''
N = int(input()) # 크레인 댓수
crain = list(map(int,input().split()))
M = int(input()) # box 갯수
box = list(map(int,input().split()))

box.sort(reverse=True)
crain.sort(reverse=True) # nlogn
cnt = 0

if max(box) > max(crain) :
    print(-1)
else :
    while box :
        for i in crain : # 크레인 갯수 최대 50개 
            for j in range(len(box)) : # 최대 10000개 
                if i >= box[j] :
                    box.pop(j) # 최대 10000
                    break
        cnt += 1
    print(cnt)
# 5,000,000,000

#####

import sys

n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
cnt = 0

crane.sort(reverse=True)
box.sort(reverse=True)

if crane[0] < box[0]:
    cnt = -1

else:
    while box:
        for i in crane:
            if not box:
                break

            if crane[-1] < box[-1]:
                del crane[-1]

            for j in box:
                if i >= j:
                    del box[box.index(j)]
                    break
        cnt += 1

print(cnt)


