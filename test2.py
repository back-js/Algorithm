import sys


s=  sys.stdin.readline().rstrip()[1:-1].split(',')
ss = list(map(int, s))
print(type(ss))
print(ss)