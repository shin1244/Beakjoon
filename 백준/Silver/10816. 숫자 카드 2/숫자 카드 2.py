import sys
input=sys.stdin.readline

n = int(input())
arr1 = list(map(int,input().split(" ")))
m = int(input())
arr2 = list(map(int,input().split(" ")))

dict1 = {arr2[i]:0 for i in range(m)}

for i in arr1:
    if i in dict1:
        dict1[i] += 1

for i in arr2:
    print(dict1[i], end=" ")