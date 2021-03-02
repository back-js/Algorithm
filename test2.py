N,M, = map(int,input().split())

b = list(map(int,input().split()))
b.insert(0,0)

visited = [0] * 10000

for i in range(n):