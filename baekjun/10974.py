'''

N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

예제 입력 1  복사
3
예제 출력 1  복사
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

'''

from itertools import permutations

number = []
N = int(input())

for i in range(1,N+1):
    number.append(i)

P = list(permutations(number,N))
P_str=[]
for i in P:
    s=[]
    for j in i:
        s.append(str(j))
    P_str.append(s)

for i in range(len(P)):
    print(' '.join(P_str[i]))

