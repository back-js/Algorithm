'''
예제 입력 1 
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
예제 출력 1 
0
0
3
0
0
8
6
3

'''
N,M,x,y,K= map(int,input().split())

matrix = []
for i in range(N) :
    s = list(map(int,input().split()))
    matrix.append(s)

move = list(map(int,input().split()))
dice = [0,0,0,0,0,0]
 
while move :
    m = move.pop(0)

    if m ==1 :
        x = x
        y = y + 1
        n_dice = [dice[0],dice[4],dice[2],dice[5],dice[3],dice[1]]
        dice = n_dice
        print(dice[1])
        if matrix[x][y] == 0 :
            matrix[x][y] = dice[3]
        elif matrix[x][y] != 0 :
            dice[3] = matrix[x][y]
            matrix[x][y] = 0
    elif m == 2 :
        x = x
        y = y - 1
        n_dice = [dice[0],dice[5],dice[2],dice[4],dice[1],dice[3]]
        dice = n_dice
        print(dice[1])
        if matrix[x][y] == 0 :
            matrix[x][y] = dice[3]

        elif matrix[x][y] != 0 :
            dice[3] = matrix[x][y]
            matrix[x][y] = 0


    elif m == 3 :
        x = x - 1
        y = y
        n_dice = [dice[3],dice[0],dice[1],dice[2],dice[4],dice[5]]
        dice = n_dice
        print(dice[1])

        if matrix[x][y] == 0 :
            matrix[x][y] = dice[3]
        elif matrix[x][y] != 0 :
            dice[3] = matrix[x][y]
            matrix[x][y] = 0

    elif m == 4 :
        x = x + 1
        y = y
        n_dice = [dice[1],dice[2],dice[3],dice[0],dice[4],dice[5]]
        dice = n_dice
        print(dice[1])
        if matrix[x][y] == 0 :
            matrix[x][y] = dice[3]
        elif matrix[x][y] != 0 :
            dice[3] = matrix[x][y]
            matrix[x][y] = 0