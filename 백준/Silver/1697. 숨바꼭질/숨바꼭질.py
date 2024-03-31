from collections import deque

start, end = map(int, input().split(' '))

DP = set()

q = deque([[0, start]])

while q:
    cnt, now = q.popleft()
    DP.add(now)

    if now == end:
        print(cnt)
        break

    if now < 100000 and now+1 not in DP:
        q.append([cnt+1, now+1])
    if now > 0 and now-1 not in DP:
        q.append([cnt+1, now-1])
    if now <= 50000 and now*2 not in DP:
        q.append([cnt+1, now*2])