'''
문제
수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.

7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.

수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

출력
N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.

예제 입력 1 
4
예제 출력 1 
2333
2339
2393
2399
2939
3119
3137
3733
3739
3793
3797
5939
7193
7331
7333
7393
'''
def decimal(s):
    r = True
    for i in range(2,s):
        if s%i == 0 :
            r = False
    return r

n = int(input())

for i in range(10**(n-1),10**(n)):
    s = str(i)
    passs = False
    for j in range(1,n+1):
        if decimal(int(s[0:j])) == True :
            passs = True
            pass
        else :
            passs = False
            break
    
    if passs == True :
        print(i)


def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, round(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def dfs(i, n):
    if n == 0:
        print(i)
    for j in range(1, 11, 2):
        t = i * 10 + j
        if prime(t):
            dfs(t, n - 1)

N = int(input())

first = [2, 3, 5, 7]
for i in first:
    dfs(i, N - 1)