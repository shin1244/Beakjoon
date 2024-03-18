import sys
input = sys.stdin.readline

n, m = map(int,input().split(' '))

S1 = set()
S2 = set()

for i in range(n):
    S1.add(input().rstrip())

for j in range(m):
    S2.add(input().rstrip())

arr = list(S1&S2)

print(len(arr))
for i in sorted(arr):
    print(i)