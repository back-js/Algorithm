'''

문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은
 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1
40 30 20 50 60 10 20 30 40 50
6
10 20 10 30 20 50
예제 출력 1
4

'''
N = int(input())
L = list(map(int,input().split()))
result = 1
for i in range(len(L)) :
    stack = []
    stack.append(L[i])
    for j in range(i+1,len(L)):
        if L[j] > stack[-1] :
            stack.append(L[j])
    if len(stack) > result :
        result = len(stack)

print(result)

n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = dp[j]
    dp[i] += a[i]
print(max(dp))

A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8}
     1  101  3  53  0   0  0  0  0  0

0  0  0  0  0  0
10 20 10 30 20 50
1  2  1  3  2  4

