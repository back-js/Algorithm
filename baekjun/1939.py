'''

문제
N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 
물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 
그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 
양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M(1≤M≤100,000)이 주어진다. 다음 M개의 줄에는 다리에 대한 정보를 나타내는 
세 정수 A, B(1≤A, B≤N), C(1≤C≤1,000,000,000)가 주어진다. 이는 A번 섬과 B번 섬 사이에 중량제한이
 C인 다리가 존재한다는 의미이다. 서로 같은 두 도시 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 
 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 공장이 있는 두 섬을 연결하는 경로는 
 항상 존재하는 데이터만 입력으로 주어진다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
3 3
1 2 2
3 1 3
2 3 2
1 3
예제 출력 1 
3

'''

N, M = map(int,input().split())
matrix = [[0]*(N+1) for i in range(M+1)]

for i in range(M) :
    i,j,k = map(int,input().split())
    matrix[i][j] = k
    matrix[j][i] = k

start, arrive = map(int,input().split())

visited = [0] * (N+1)
result = 10000000
visited[start] = 1
cnt = 0

def dfs(s) :
    global cnt, result
    if s == arrive :
        if cnt < result :
            result = cnt
    else :
        for i in range(1,N+1) :
            if matrix[s][i] != 0 and visited[i] == 0 :
                cnt += matrix[s][i]
                visited[i] = 1
                dfs(i)
                cnt -= matrix[s][i]
                visited[i] = 0
dfs(start)

print(result)

#####


from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, th):
    q = deque()
    c = [0 for _ in range(n)]
    q.append(x)
    c[x] = 1
    while q:
        x = q.pop()
        for nx, w in a[x]:
            if c[nx] == 0 and w >= th:
                c[nx] = 1
                q.append(nx)

    if c[y-1] == 1:
        return 1
    else:
        return 0

n, m = map(int, input().split())
a = [[] for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    a[x-1].append([y-1, w])
    a[y-1].append([x-1, w])

x, y = map(int, input().split())

left, right = 1, 0
for i in a[y-1]:
    right = max(right, i[1])

while left <= right:
    mid = (left + right) // 2
    if bfs(x-1, mid):
        ans = mid
        left = mid + 1
    else:
        right = mid -1
print(ans)
