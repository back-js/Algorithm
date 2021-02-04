''''

문제
상근이는 우리나라에서 가장 유명한 놀이 공원을 운영하고 있다. 이 놀이 공원은 야외에 있고, 다양한 롤러코스터가 많이 있다.

어느 날 벤치에 앉아있던 상근이는 커다란 황금을 발견한 기분이 들었다. 자신의 눈 앞에 보이는 이 부지를 구매해서 롤러코스터를 만든다면,
 세상에서 가장 재미있는 롤러코스터를 만들 수 있다고 생각했다.

이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다. 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고,
가장 오른쪽 아래 칸에서 도착할 것이다. 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다.
 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.

각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다. 롤러코스터를 탄 사람이 얻을 수 있는 기
쁨은 지나간 칸의 기쁨의 합이다. 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 R과 C가 주어진다. (2 ≤ R, C ≤ 1000) 둘째 줄부터 R개 줄에는 각 칸을 지나갈 때 얻을 수 있는 기쁨이 주어진다. 이 값은 1000보다 작은 양의 정수이다.

출력
첫째 줄에 가장 가장 큰 기쁨을 주는 롤러코스터는 가장 왼쪽 위 칸부터 가장 오른쪽 아래 칸으로 어떻게 움직이면 되는지를 출력한다. 위는 U, 오른쪽은 R, 왼쪽은 L, 아래는 D로 출력한다. 정답은 여러 가지 일 수도 있다.

예제 입력 1
3 3
5 1 3
2 4 8
1 1 2
예제 출력 1
RRDLLDRR

'''
n, m = map(int,input().split())
happy = []
for i in range(n):
    s = list(map(int,input().split()))
    happy.append(s)

result =''

if n % 2 != 0 :
    for i in range(n-1):
        if i %2 == 0 :
            result += 'R'*(m-1)
            result += 'D'
        else :
            result += 'L'*(m-1)
            result += 'D'
    result += 'R'*(m-1)

elif n%2==0 and m%2 != 0 :
    for i in range(m-1):
        if i %2 == 0 :
            result += 'D'*(n-1)
            result += 'R'
        else :
            result += 'U'*(n-1)
            result += 'R'
    result += 'D'*(n-1)

elif n%2 ==0 and m%2 == 0 :
    a,b = -1,-1
    low = 10000
    for i in range(n):
        for j in range(m):
            if (i+j)%2 !=0:
                if happy[i][j] < low :
                    low = happy[i][j]
                    a,b = i,j
########

f
r % 2 == 1:
sys.stdout.write(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1:
sys.stdout.write(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))
elif r % 2 == 0 and c % 2 == 0:
# find position to jump
low = 1000
position = [-1, -1]
for i in range(r):
    if i % 2 == 0:
        for j in range(1, c, 2):
            if low > ground[i][j]:
                low = ground[i][j]
                position = [i, j]
    else:  # i % 2 == 1
        for j in range(0, c, 2):
            if low > ground[i][j]:
                low = ground[i][j]
                position = [i, j]

res = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
x = 2 * (position[1] // 2)  x,y=0,0
y = 0
xbound = 2 * (position[1] // 2) + 1 1
while x != xbound or y != r - 1:
    if x < xbound and [y, xbound] != position:
        x += 1
        res += 'R'
    elif x == xbound and [y, xbound - 1] != position:
        x -= 1
        res += 'L'
    if y != r - 1:
        y += 1
        res += 'D'

res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)

print(res)




print(result)