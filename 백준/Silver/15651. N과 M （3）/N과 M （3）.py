from itertools import *

n, m = input().split()

arr = list(range(1, int(n)+1))

for i in list(product(arr, repeat=int(m))):
    print(*i)