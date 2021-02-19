'''

문제
정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.

A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 배열의 크기 n (1 ≤ n ≤ 4000)이 주어진다. 
다음 n개 줄에는 A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어진다. 
배열에 들어있는 정수의 절댓값은 최대 228이다.

출력
합이 0이 되는 쌍의 개수를 출력한다.

예제 입력 1 

예제 출력 1 
5
'''
n = int(input())

A = []
B = []
C = []
D = []
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
case = dict()
cnt = 0
for i in A :
    for j in B :
        if i+j in case :
            case[i+j] +=1
        else:
            case[i+j] = 1

for i in C :
    for j in D :
        if -(i+j) in case:
            cnt+=1

print(cnt)