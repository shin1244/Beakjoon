import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split(" ")))
q = deque([i+1,arr[i]] for i in range(len(arr)))
result = []

while q:
    idx, paper = q.popleft()
    result.append(idx)

    if paper > 0:
        q.rotate(-(paper-1))
    else:
        q.rotate(-paper)

print(' '.join(map(str,result)))