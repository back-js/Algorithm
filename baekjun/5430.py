import sys
N = int(input())

for i in range(N) :
    f = list(input())
    n = int(input())
    aa = sys.stdin.readline().rstrip()[1:-1].split(',')
    if len(aa) > 2 :
        a = list(map(int, aa))
    else :
    for i in f :
        if i == 'R' :
            if len(a) != 0 :
                a.reverse()

        elif i == 'D' :
            if len(a) == 0 :
                print('error')
                break
            else :
                a.pop(0)
    if len(a) == 0 :
        pass
    else :
        print(a)
