items, w = list(map(int,input().split()))

arr = [list(map(int,input().split())) for _ in range(items)]

DP = [0] * (w+1)

for iw, iv in arr:
    for i in range(w, 0, -1):
        if DP[i] != 0 and i+iw <= w:
            DP[i+iw] = max(DP[i] + iv, DP[i+iw])
    if 0 < iw < w+1:
        DP[iw] = max(DP[iw], iv)

print(max(DP))