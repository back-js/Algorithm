def solution(key, lock):
    answer = True
    return answer

def rotation90(key):
    row = len(key)
    column = len(key[0])
    matrix = [[0]*column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            matrix[j][row - i - 1] = key[i][j]
    return matrix