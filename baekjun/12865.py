n, k = map(int, input().split(' '))
matrix = [ [0]*(k+1) for _ in range(n+1) ]

for i in range(1,n+1) :
    w,v = map(int,input().split())
    for j in range(1,k+1) :
        if j < w :
            matrix[i][j] = matrix[i-1][j]
        else :
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-w]+v)

print(matrix[n][k])