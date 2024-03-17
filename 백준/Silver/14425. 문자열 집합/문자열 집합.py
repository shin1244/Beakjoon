import sys
input = sys.stdin.readline

n, m = map(int, input().split())

S = set()

result = 0

for _ in range(n):
    S.add(input())

for _ in range(m):
    i = input()
    if i in S:
        result += 1

print(result)