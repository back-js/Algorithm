'''
def solution(M,K,data):
    data.sort(reverse=True)
    result = 0
    count = 0
    if K == M :
        result+=sum(data)
    else :
        for i in range(M):
            for j in range(K):
                if count > M :
                    break
                result += data[i]
                count += 1
            if count > M :
                break
    print(result)

M=8
K=3
data = [2,4,5,4,6]

solution(M,K,data)

'''
n,m,k = map(int, input().split())
data =list(map(int, input().split()))

data.sort(