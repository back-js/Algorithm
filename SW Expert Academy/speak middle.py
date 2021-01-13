N = int(input())
numbers = []
stack = []
for i in range(N):
    s = int(input())
    numbers.append(s)
    numbers.sort()
    if len(numbers) % 2 == 0 :
        medium = min(numbers[int(len(numbers)/2)],numbers[int((len(numbers)/2)-1)])
    else :
        medium = numbers[len(numbers)//2]
    stack.append(medium)

for i in stack:
    print(i)