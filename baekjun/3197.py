'''
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
'''

R,C = map(int,input().split())
lake = [list(input()) for _ in range(R)]
new_lake = [[0]*R for _ in range(C)]
for i in range(R) :
    for j in range(C) :
        if lake[i][j] == '.' :
            new_lake[i][j] = '.' :
        elif lake[i][j] == 'X' :
            di, dj = [-1,1,0,0] , [0,0,-1,1]
            for k in range(4) :
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < R and 0 <= nj < C and lake[ni][nj] == '.' :
                    new_lake[i][j] = '.'
                
