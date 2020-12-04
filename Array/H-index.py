def solution(citations):
    result = []
    for i in range(1,max(citations)+1):
        plus = []
        minus = []
        for j in citations:
            if j/i >= 1 :
                plus.append(j)
            else :
                minus.append(j)
        if len(plus) >= i and len(minus) <= i :
            result.append(i)
        print(result)

solution([3,0,6,1,5,8,9,10])