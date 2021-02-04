'''

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

예제 입력 1
5457
3
6 7 8
예제 출력 1
6

예제 입력 2
100
5
0 1 2 3 4
예제 출력 2
0

예제 입력 3
500000
8
0 2 3 4 6 7 8 9
예제 출력 3
11117


'''

target = int(input())
N = int(input())
s= list(input().split())

number = [0,1,2,3,4,5,6,7,8,9]

result = []
for i in range(1000000):
    broken = False
    for j in str(i):
        if j in s:
            broken = True
    if broken == True :
        pass
    else :
        result.append(abs(target-i))

print(min(min(result)+len(str(target-min(result))),abs(target-100)))

########################################################################################################
'''
n = int(input())
m = int(input())
ms = []
if m != 0:
    ms = list(input().split())

ans = 999999999
length = 0
for i in range(1000000):
    broken = False
    for s in str(i):
        if s in ms:
            broken = True
    if broken:
        pass
    else:
        if ans > abs(n - i):
            ans = abs(n - i)
            length = len(str(i))

ans = min(ans + length, abs(n - 100))

print(ans)
'''




