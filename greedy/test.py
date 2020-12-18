import operator

strings = ['sun', 'bed', 'car']
n=1
dict = {string : string[n] for string in strings}
sdict= sorted(dict.items(), key=operator.itemgetter(1))

print(sdict)