import sys
input = sys.stdin.readline
arr = [list(map(int,input().split(' '))) for _ in range(int(input()))]
for i in sorted(arr, key=lambda x:(x[0],x[1])):
    print(i[0], i[1])