def solution(n, t, m, p):
    num = ''

    for i in range(1000) :
        num += convert(i,n)

    result = ''
    start = p-1
    for i in range(t) :
        result += num[start]
        start += m

    print(result)

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base) # n을 base로 나눈 몫과 나머지를 튜플형태로 반환
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
solution(16,16,2,1)