'''

통계 자료를 처리할 때, 평균이 전체 집단의 특징을 꼭 잘 표현하는 것은 아니다.

예를 들어, 대다수의 국가에서는 적은 수의 사람이 국가 전체 소득의 꽤 많은 부분을 차지하기 때문에, 해당 국가의 평균 소득은 보통 사람들의 소득보다 높은 경우가 많다.

당신은, n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.


[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.

첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다.
이 정수들은 각각 1 이상 100,000 이하이다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

'''
count = int(input())
number_list = []
people_list = []

for i in range(count):
    number = int(input())
    number_list.append(number)
    people = list(map(int,input().split()))
    people_list.append(people)

for i in range(count):

    mean = sum(people_list[i]) / number_list[i]
    cnt = 0
    for j in people_list[i] :
        if j <= mean :
            cnt += 1
        else :
            pass
    print(f'#{i+1} {cnt}')