def solution(board, moves):
    buket = [0]
    count = 0

    for j in moves:
        j = j - 1
        for i in range(len(board)):
            if board[i][j] == 0:
                pass
            elif board[i][j] != 0:
                if board[i][j] == buket[-1]:
                    del buket[-1]
                    count+=1
                else :
                    buket.append(board[i][j])
                board[i][j] = 0
                break

    result = count *2
    return result