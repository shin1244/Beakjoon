import sys
input = sys.stdin.readline


n, money = list(map(int,input().split()))

arr = [int(input()) for _ in range(n)]

result=0
for i in range(n-1, -1, -1):
    if arr[i] <= money:
        result += money // arr[i]
        money %= arr[i]

print(result)