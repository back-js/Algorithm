def solution(n,computer) :
    visited[i] = True
    for i in range(0,n):
        visited[i] = True
        for j in range(len(computer)):
            if computer[i][j] == 1 :
                visited[j] = True








computer = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]