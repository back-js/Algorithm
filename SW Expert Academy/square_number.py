import time
start = time.time()

N = int(input())

aa = list(int(input()) for _ in range(N))

from math import sqrt

for a in range(len(aa)) :
    i = 1

    while True:
        F = aa[a] * i
        Squre = sqrt(F)
        if int(Squre) == Squre :
            s = a+1
            print(f'#{s} {i}')
            break
        else :
            i += 1

print(time.time()-start)

###################
prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)

2 3  5 6
answer = []
T = int(input())
for tc in range(T):
    A = int(input())
    res = 1
    if A**0.5 != int(A**0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    answer.append('#{} {}'.format(tc+1, res))
for ans in answer:
    print(ans)