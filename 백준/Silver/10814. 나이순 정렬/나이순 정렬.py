import sys
input = sys.stdin.readline

arr = [input().rstrip().split(' ') for _ in range(int(input()))]

for i in sorted(arr, key=lambda x:int(x[0])):
    print(" ".join(i))