'''

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

예제 출력 2 
1

'''

N,M = map(int,input().split())
line = [[] for _ in range(N+1)]

for i in range(M) :
    i,j = map(int,input().split())
    line[i].append(j)
    line[j].append(i)

visited = [0] * (N+1)
cnt = 0

def dfs(s) :
    visited[s] = 1

    for i in line[s] :
        if visited[i] == 0 :
            dfs(i)     

for i in range(1,N+1) :
    if visited[i] == 0 :
        dfs(i)
        cnt += 1

print(cnt)

### 꺠지고 부셔져라

import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
cnt = 0
def dfs(i):
    visit[i] = 1
    for k in range(1, n + 1):
        if s[i][k] == 1 and visit[k] == 0:
            dfs(k)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1
for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)

