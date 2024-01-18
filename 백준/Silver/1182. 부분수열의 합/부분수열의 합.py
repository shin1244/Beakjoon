from itertools import combinations


num = list(map(int,input().split(' ')))[-1]
arr = list(map(int,input().split(' ')))
c = 0

for i in range(1, len(arr)+1):
    for j in list(combinations(arr, i)):
        if sum(j) == num:
            c += 1

print(c)