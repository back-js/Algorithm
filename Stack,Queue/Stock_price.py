def solution(prices):
    answer = []
    for i in range(len(prices)):
        new_price = [x for x in prices[i:] if x<prices[i]]
        print([new_price])
        #location = prices.index(new_price[0])
        #result = location - i
        #answer.append[result]
    #print(answer)

solution([1, 2, 3, 2, 3])