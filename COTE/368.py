
'''
7
-15 -4 2 8 9 13 15
         3 4 5
2
'''

N = int(input())
point = list(map(int,input().split()))

def binary_search(array,start,end) :
    if array[0] == 0 :
        return 0
    elif array[N-1] == N-1 :
        return N-1
    
    while start <= end :
        mid = ( start + end ) // 2

        if array[mid] == mid :
            return mid
        
        elif array[mid] > mid :
            end = mid - 1
        
        elif array[mid] < mid :
            start = mid + 1

    return -1
print(binary_search(point,0,N-1))