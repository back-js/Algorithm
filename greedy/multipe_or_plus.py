n = str(input())
list1 = list(n)
list1 = [int(i) for i in list1]
result = 1
for i in list1 :
    if i == 0 :
        result += i
    else :
        result *= i
print(result)