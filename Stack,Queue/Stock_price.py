'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''


def solution(prices):
    result = []
    for i in prices:
        prices[i]
        new = prices[i+1:]
        for j in new:
            if new[j] >= prices[i]:
                pass
            else :
                result.append(j+1)
                break




solution([1, 2, 3, 2, 3])
################################################################################## 이중 for문

def solution(prices):
    answer = []
    for i in range(len(prices)-1): # 마지막 전까지 ,, 마지막에는 비교할 수 없이 그냥 0이기에
        count = 0
        for j in range(i+1, len(prices)): # 마지막까지.
            if(j == len(prices) - 1 or prices[i] > prices[j]): # 끝날 때 답에 count + 1 해준 값을 넣고 끝낸다.
                answer.append(count+1)
                break
            else :
                count +=1
    answer += [0] # 마지막 요소는 비교할 것도 없이 그냥 내려가고 그런게 없으니 0을 더해줌.
    return answer
################################################################################### deque 사용

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
