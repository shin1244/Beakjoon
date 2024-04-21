from itertools import *

n, m = input().split()

arr = list(range(1, int(n)+1))

for i in list(combinations_with_replacement(arr, int(m))):
    print(*i)