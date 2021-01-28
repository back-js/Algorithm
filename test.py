M,N,H = map(int,input().split())
matrix = [[] for _ in range(H)]
from collections  import deque
for i in range(H):
    for j in range(N) :
        s = list(map(int,input().split(" ")))
        matrix[i].append(s)

visited = [[[0]*M for _ in range(N)] for _ in range(H)]
queue = deque([])

for z in range(H):
    for x in range(N):
        for y in range(M):
            if matrix[z][x][y] == 1 :
                queue.append([x,y,z])

dx,dy,dz = [-1,1,0,0,0,0] , [0,0,-1,1,0,0], [0,0,0,0,-1,1]

def bfs():
    while queue :
        x, y, z = queue.popleft()
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