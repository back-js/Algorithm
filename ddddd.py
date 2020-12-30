
number = '4177252841'
k = 4
number = list(number)
result = []
choose = len(number) - k - 1

max_number = max(number[0:-choose])
result.append(max_number)
start_idx = number.index(max_number)

number = number[start_idx:]

choose += -1
print(number)
print(choose)