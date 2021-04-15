N,K = map(int,input().split())

cycle = [i for i in range(1,N+1)]
result = []
while cycle :
    for i in range(K-1):
        a = cycle.pop(0)
        cycle.append(a)
    value  = cycle.pop(0)
    result.append(value)
print('<'+', '.join(map(str, result))+'>')