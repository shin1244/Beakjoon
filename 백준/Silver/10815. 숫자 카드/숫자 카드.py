import sys
input = sys.stdin.readline

input()
arr1 = input().rstrip().split(' ')
input()
arr2 = input().rstrip().split(' ')

s = set(arr1)
for i in arr2:
    print(1, end=" ") if i in s else print(0, end=" ")