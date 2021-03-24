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

#지원한 직무 관련 본인이 갖고 있는 전문지식/경험(심화전공, 프로젝트, 논문, 공모전 등)을 작성하고,
#이를 바탕으로 본인이 지원 직무에 적합한 사유를 구체적으로 서술해 주시기 바랍니다.1000자 (영문작성 시 2000자) 이내**

데이터마이닝 대용량데이터 처리경험

에이브레인 프로그래밍능력 열정 데이터처리



