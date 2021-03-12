'''
문제
수빈이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 수빈이가 정수를 하나씩 외칠때마다 
동생은 지금까지 수빈이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 수빈이가 외친 수의 개수가 
짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 수빈이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 
동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 수빈이가 외치는 수가 주어졌을 때,
 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 수빈이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
 그 다음 N줄에 걸쳐서 수빈이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 수빈이의 동생이 말해야하는 수를 순서대로 출력한다.
-99 1 2 5 7 10
예제 입력 1 
7
1
5
2
10
-99
7
5
예제 출력 1 
1
1
2
2
2
2
5

0 1 2 3
'''

N = int(input())
array = []
result = []
for i in range(N) : # N
    array.append(int(input()))

array_sort = sorted(array) # NlogN

while array :
    s = len(array_sort)
    
    if s % 2 == 0 :
        k = (s//2) - 1
        result.append(array_sort[k])
    else :
        k = s//2
        result.append(array_sort[k])

    p = array.pop()
    array_sort.remove(p)

result.reverse()
for i in result:
    print(i)


import heapq
import sys

# 중앙값 기준으로 작은 값 = left, 큰 값 = right
left, right = [], []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        # max_heap.
        heapq.heappush(left, (-num, num))
    else:
        # min_heap.
        heapq.heappush(right, (num, num))

    # 오른쪽 값에 원소가 있으면서,
    # 왼쪽 값이 오른쪽 값보다 큰 경우... left원소보다 right원소가 더 커야 하는 조건에 위배
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
    
    print(left[0][1])