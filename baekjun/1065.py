'''

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1
110
예제 출력 1
99

예제 입력 2
1
예제 출력 2
1
33
'''
S = int(input())
if 0 < S <= 100 :
    print(S)
else :
    cnt = 99
    for N in range(100,S+1):
        N = str(N)
        step = []
        for i in range(len(N)-1) :
            s = int(N[i])-int(N[i+1])
            step.append(s)

        for i in range(1,len(step)):
            if step[i-1] == step[i]:
                pass
            else :
                break
            cnt +=1
    print(cnt)




