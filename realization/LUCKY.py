n = int(input())
n = str(n)
leng = int(len(n)/2)
n_list = list(n)

n_list = list(map(int, n_list))

first_sum = sum(n_list[0:leng])
second_sum = sum(n_list[leng:leng*2])

if first_sum == second_sum :
    print('LUCKY')
else :
    print('READY')