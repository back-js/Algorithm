'''
문제
은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력한다.

예제 입력 1 
100
예제 출력 1 
77
'''

n = int(input())

number = []

for i in range(n+1):
    s = str(i)
    if '0' in s or '1' in s or '2' in s or '3'in s or '5' in s or '6'in s or '8' in s or '9' in s :
        pass
    else :
        number.append(i)

print(max(number))
