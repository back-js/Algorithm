N = int(input())
A = []
B = []
Am = []
Bm = []
for i in range(N-1) :
    a,b,am,bm = map(int,input().split())
    A.append(a)
    B.append(b)
    Am.append(am)
    Bm.append(bm)

la,lb = map(int,input().split())
A.append(la)
B.append(lb)

As = A[0]
Position = True # A 위치
for i in range(N-1) : # start A
    if Position == True :
        if B[i+1] + Am[i] <= A[i+1] :
            As += B[i+1] + Am[i]
            Position = False
        else :
            As += A[i+1]
    elif Position == False :
        if A[i+1] + Bm[i] <= B[i+1] :
            As += A[i+1] + Bm[i]
            Position = True
        else :
            As += B[i+1]

Bs = B[0]
Position = False # B 위치
for i in range(N-1) : # start B
    if Position == True :
        if B[i+1] + Am[i] <= A[i+1] :
            Bs += B[i+1] + Am[i]
            Position = False
        else :
            Bs += A[i+1]
    elif Position == False :
        if A[i+1] + Bm[i] <= B[i+1] :
            Bs += A[i+1] + Bm[i]
            Position = True
        else :
            Bs += B[i+1]

print(min(sum(A),As,Bs))




