from collections import deque

n, m = map(int,input().split(' '))

q = deque([n])
DP = [float("inf")] * 100001
DP[n] = 0

while q:
    now = q.popleft()
    if now == m:
        break
    if 0 < now*2 < 100001 and DP[now*2] > DP[now]:
        DP[now*2] = DP[now]
        q.append(now*2)
    if 0 <= now-1 < 100001 and DP[now-1] > DP[now]+1:
        DP[now-1] = DP[now]+1
        q.append(now-1)
    if 0 <= now+2 < 100001 and DP[now+1] > DP[now]+1:
        DP[now+1] = DP[now]+1
        q.append(now+1)

print(DP[m])