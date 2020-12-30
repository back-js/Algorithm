'''
Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로,
세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
'''

def solution(brown, yellow):
    value = []
    for i in range(1,yellow+1):
        n = i
        m = yellow/n
        if n >= m and m == int(m) :
            value.append([n,int(m)])

    for i in range(len(value)):
        n = value[i][0]
        m = value[i][1]
        if (n+m)*2 + 4 == brown:
            n,m = n+2,m+2
            return [n,m]


print(solution(24,24))

####
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]