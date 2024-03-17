import sys
input = sys.stdin.readline

input()
arr = list(map(int,input().split(' ')))
r = sorted(list(set(arr)))

dic = {r[i]:i for i in range(len(r))}

for i in arr:
    print(dic[i], end=" ")