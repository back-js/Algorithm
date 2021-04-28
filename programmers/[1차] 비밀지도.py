def solution(n, arr1, arr2):
    n_arr1 = change(n,arr1)
    print(n_arr1)
    n_arr2 = change(n,arr2)
    print(n_arr2)
    answer = ['' for i in range(n)]

    for i in range(n) :
        for j in range(n) :
            if n_arr1[i][j] == '1' or n_arr2[i][j] == '1' :
                answer[i] += '#'
            else :
                answer[i] += ' '

    print(answer)


def change(n,arr):
    n_arr = []
    for i in arr :
        b = format(i,'b')
        if len(b) == n :
            n_arr.append(b)
        else :
            while len(b) < n :
                b = '0' + b
            n_arr.append(b)
    return n_arr

solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])