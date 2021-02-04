'''

첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

예제 입력 1
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

예제 출력 1
2

'''
N,M = map(int,input().split())
ice = []
for i in range(N):
    s = lsit(map(int,input().split()))
    ice.append(s)

def bfs() :
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 :
                dx,dy = [-1,1,0,0] , [0,0,-1,1]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny <M and ice[nx][ny] == 0 and ice[i][j] > 0 :
                        visited[i][j] += 1

            if visited[i][j] <= ice[i][j]:
                ice[i][j] -= visited[i][j]
            else :
                ice[i][j] = 0



while True:
    bfs()
    for i in range(N):
        for j in range(M):

