A = [ 1,5,3,6]
a = len(A)
for i in range(a):
    for j in range(i, a, 1):
        print(A[i:j+1])