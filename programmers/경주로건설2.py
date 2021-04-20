from collections import deque

def move(d,nd) :
    if (d == 'R' or d == 'L') and (nd == 'U' or nd =='D') :
        return 600
    elif (d == 'U' or d =='D')  and (nd == 'R' or nd == 'L') :
        return 600
    else :
        return 100


def search(x,y,c,d,board) :
    n = len(board)
    result = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    D = ['R','L','U','D']

    queue = deque()
    queue.append([x,y,c,d])
    visited = [[0 for i in range(n)] for _ in range(n)]
    visited[0][0] = 1

    while queue :
        x,y,c,d = queue.popleft()

        if x == n-1 and y == n -1 :
            result.append(c)

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n :
                if board[nx][ny] == 0 :
                    nc = c + move(d,D[i])

                    if visited[nx][ny]==0 or nc<visited[nx][ny]:
                        visited[nx][ny]=nc
                        queue.append([nx,ny,nc,D[i]])

    return min(result)

def solution(board) :
    an1 = search(0,0,0,'R',board)
    an2 = search(0,0,0,'D',board)
    return min(an1,an2)