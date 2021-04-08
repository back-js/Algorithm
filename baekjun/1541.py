'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

예제 입력 1 
55-50+40
예제 출력 1 
-35
'''
a=str(input())
lena = len(a)
array = []
if a[0] != '-' :
    for i in range(lena) :
        if a[i] == '-' :
            array.append(eval(a[0:i]))
            break

for i in range(lena) :
    if a[i] == '-' :
        for j in range(i+1,lena) :
            if a[j] == '-':
                array.append(-eval(a[i+1:j]))
                break
            else:
                if j == lena-1 :
                    array.append(-eval(a[i+1:]))

print(sum(array))

####

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)

###

a = input().split('-')
cnt = 0

cnt += eval(a[0])
for i in range(1,len(a)) :
    cnt -= eval(a[i])

print(cnt)