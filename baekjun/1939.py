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


import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maps = [[] for _ in range(n+1)]

# 각 도시의 연결여부와 무게제한을 저장하는 배열 생성
for _ in range(m):
    y, x, w = map(int, sys.stdin.readline().split())
    maps[y].append((x,w))
    maps[x].append((y,w))
# 시작점, 끝점    
start, end = map(int, sys.stdin.readline().split())

# 통과할 수 있는 무게의 최솟값 / 최댓값을 지정한다. 문제에서 정해져 있다.
_min, _max = 1, 1000000000

def bfs(c):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    result = []
    while queue:
        y = queue.popleft()
        for x, w in maps[y]:
            # 갈 수 있는 곳이면서 무게 제한에 걸리지 않을 경우
            if x not in visited and w >= c:
                visited.add(x)
                queue.append(x)
    # 도착지점을 방문할 수 있는 경우면 True, 아니면 False 반환
    return True if end in visited else False

# 이분탐색으로 최댓값을 찾는다.
result = _min
while _min <= _max:
    mid = (_min + _max) // 2
    # 해당 무게로 start -> end까지 도착이 가능한 경우
    # 값을 저장하고, 최댓값을 구하기 위해 _min 값을 올린다.
    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(result)
