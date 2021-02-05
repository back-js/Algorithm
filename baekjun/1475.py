'''

문제
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 필요한 세트의 개수를 출력한다.

예제 입력 1
9999
예제 출력 1
2

'''
N = list(map(int,str(input())))

r = []
w = []

for i in range(10):
    if i == 6 or i == 9 :
        s = N.count(i)
        w.append(s)

    else:
        s = N.count(i)
        r.append(s)
if sum(w)%2 == 0 :
    ww = int(sum(w)/2)
else :
    ww = int(sum(w)/2)+1

rr = max(r)

print(max(rr,ww))


