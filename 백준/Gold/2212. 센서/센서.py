import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
pos = sorted(list(map(int, sys.stdin.readline().split())))

if m >= n:
    print(0)
    exit()

dist = []
for i in range(1, n):
    dist.append(pos[i] - pos[i-1])

dist.sort()
for _ in range(m-1):
    dist.pop()

print(sum(dist))