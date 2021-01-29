'''

예제 입력 1
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

예제 출력 1
5

'''

N = int(input())
height = []

for i in range(N):
    s = list(map(int,input().split()))
    height.append(s)

def bfs(a,b):
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    queue = [(a,b)]
    while queue :
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and copy[nx][ny] == 0 :
                copy[nx][ny] = 1
                queue.append((nx,ny))

max_cnt =0
for k in range(0,101):
    cnt = 0
    copy = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if height[i][j] <= k :
                copy[i][j] = 1
    for i in range(N):
        for j in range(N):
            if copy[i][j] == 0 :
                bfs(i,j)
                cnt+=1
    max_cnt = max(max_cnt,cnt)



print(max_cnt)



