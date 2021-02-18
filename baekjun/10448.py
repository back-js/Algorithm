from itertools import product

N = int(input())
number = []

for i in range(N) :
    s = int(input())
    number.append(s)

def triangular_number(n):
    result = (n*(n+1))/2
    return int(result)

triangular_number_list = []
for i in range(1,50):
    s = triangular_number(i)
    triangular_number_list.append(s)

product_triangular = product(triangular_number_list, repeat=3)

product_list = list(product_triangular)
result = []
for i in product_list:
    s = sum(i)
    result.append(s)

for i in range(N):
    if number[i] in result:
        print('1')
    else :
        print('0')



####

triangle = [n*(n+1)//2 for n in range(1, 46)]
eureka = [0] * 1001

#미리 1000이하의 모든 유레카 수를 구한다
for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1

T = int(input())
for _ in range(T):
    print(eureka[int(input())])
    
