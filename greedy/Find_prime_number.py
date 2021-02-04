'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요

numbers	return
17	3
011	2

'''
from itertools import permutations

value = []
def solution(numbers):
    num = list(numbers)
    for i in range(1,len(num)+1):
        new_num = list(permutations(num, i))
        for j in new_num:
            if prime(int(''.join(j))) is not None:
                value.append(int(''.join(j)))
    return len(set(value))

def prime(n):
    k = ''
    for i in range(2,n):
        if n % i == 0:
            k= None
            break
        else :
            pass
            K=n
    if n ==1 or n==0 :
        k= None
    return k

print(solution('011'))