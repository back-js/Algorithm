'''


예제 입력 1 
7
2 5 3 1 4 2 3
예제 출력 1 
67
다음과 같이 나누는 것이 P의 합을 최대화 한다: [2] [5 3 1 4] [2] [3]

예제 입력 2 
5
1 1 2 1 1
예제 출력 2 
5
출처 9
1 2 4 3 5 1 8 9 2
'''

N = int(input())
tree = list(map(int,input().split()))
P = 0

def pros(s):
    num = 1
    for i in s :
        num *= i
    return num

for i in range(N-3) :
    for j in range(i+1,N-2) :
        for k in range(j+1,N-1) :
            for s in range(k+1,N) :
                PP = pros(tree[i:j]) + pros(tree[j:k]) + pros(tree[k:s]) + pros(tree[s:])
                P = max(PP,P)

print(P)