import operator

def solution(strings, n):
    dict = {string : string[n] for string in strings}
    print(dict)
    sdict = sorted(dict.items(), key=operator.itemgetter(1))

strings = ['sun', 'bed', 'car']
solution(strings, 1)