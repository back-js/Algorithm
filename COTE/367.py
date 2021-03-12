N,x = map(int,input().split())
array = list(map(int,input().split(' ')))

def binary_search(array,target,start,end) :
    while start <= end :
        mid = (start+end) // 2

        if array[mid] == target :
            return mid

        elif array[mid] > target :
            end = mid - 1

        elif array[mid] < target :
            start = mid + 1
    return None

if binary_search(array,x,0,N-1) == None :
    print(-1)
else :
    v = binary_search(array,x,0,N-1)
    v1 = v
    v2 = v
    cnt = 1
    while True:
        v1 += 1
        if array[v1] == x :
            cnt += 1
        else :
            break
    while True :
        v2 += -1
        if array[v2] == x :
            cnt += 1
        else :
            break
    print(cnt)

        