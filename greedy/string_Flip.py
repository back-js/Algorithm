n = str(input())
list1 = list(n)
count0 = 0
count1 = 0

for i in range(len(list1)-1):
    if list1[i] == list1[i+1] :
        pass
    else :
        if list1[i] == '0':
            count0 +=1
        elif list1[i] == '1' :
            count1 +=1
print(min(count0,count1))
