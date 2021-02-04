''''''

def solution(n):
    result = [0,1]
    cnt = 2
    while True:
        new = result[cnt-1]+result[cnt-2]
        result.append(new)
        cnt += 1
        if cnt == 100000:
            break
    answer = result[n]%1234567

    return answer

#####

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
