'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
'''
S1 = str(input())
S2 = str(input())
len1 = len(S1) 
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] 
for i in range(1, len1 + 1): 
    for j in range(1, len2 + 1): 
        if S1[i - 1] == S2[j - 1]: 
            matrix[i][j] = matrix[i - 1][j - 1] + 1 
        else: 
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
print(matrix[-1][-1])