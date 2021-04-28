def solution(m, n, board):
    for i in range(len(board)) : # 보드 리스트화
        board[i] = list(board[i])
    cnt = 0
    while True :
        pop_set = set([])
        for i in range(m-1) :
            for j in range(n-1) :
                if board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i][j+1] != 0 :
                    pop_set.add((i,j))
                    pop_set.add((i+1,j))
                    pop_set.add((i+1,j+1))
                    pop_set.add((i,j+1))
        if len(pop_set) == 0 :
            break
        cnt += len(pop_set)

        for a,b in pop_set :
            board[a][b] = 0

        down(m,n,board)
    print(cnt)

def down(m,n,board) :
    while True :
        k = False
        for i in range(m-1) :
            for j in range(n) :
                if board[i+1][j] == 0 and board[i][j] != 0 :
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    k = True
        if k == False :
            break
        

solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])
                
        

    