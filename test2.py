K,P,N = map(int,input().split())


for i in range(N) :
    K *= P

print(K%1000000007)
