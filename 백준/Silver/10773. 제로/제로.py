import sys
input=sys.stdin.readline
n = int(input())

arr = []

for i in range(n):
    money = int(input())
    arr.append(money) if money != 0 else arr.pop()

print(sum(arr))