'''

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다.
각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 1
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
예제 출력 1
-1
예제 입력 2
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
예제 출력 2
4
예제 입력 3
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
예제 출력 3
0

'''
M,N,H = map(int,input().split())
matrix = [[] for _ in range(H)]

for i in range(H):
    for j in range(N) :
        s = list(map(int,input().split(" ")))
        matrix[i].append(s)

visited = [[[0]*M for _ in range(N)] for _ in range(H)]
queue = []

for z in range(H):
    for x in range(N):
        for y in range(M):
            if matrix[z][x][y] == 1 :
                queue.append([x,y,z])

dx,dy,dz = [-1,1,0,0,0,0] , [0,0,-1,1,0,0], [0,0,0,0,-1,1]

def bfs():
    while queue :
        x, y, z = queue.pop(0)
        visited[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and matrix[nz][nx][ny] ==0 and visited[nz][nx][ny]== 0 :
                visited[nz][nx][ny] = 1
                matrix[nz][nx][ny] = matrix[z][x][y] + 1
                queue.append([nx,ny,nz])
bfs()
broken = False

max_num = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if matrix[z][x][y] == 0 :
                broken = True
            max_num = max(max_num, matrix[z][x][y])

if broken == True :
    print(-1)
else :
    print(max_num-1)




####

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    while q:
        a, b, c = q.popleft()
        visit[c][a][b] = 1
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < n and 0 <= y < m and 0 <= z < h and s[z][x][y] == 0 and visit[z][x][y] == 0:
                q.append([x, y, z])
                s[z][x][y] = s[c][a][b] + 1
                visit[z][x][y] = 1
m, n, h = map(int, input().split())
s = [[] for i in range(h)]
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
q = deque()
isTrue = False
st = False

for i in range(h):
    for j in range(n):
        s[i].append(list(map(int, input().split())))
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 1:
                q.append([x, y, z])
bfs()
max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, s[z][x][y])

if isTrue == True:
    print(-1)
else:
    print(max_num - 1)
