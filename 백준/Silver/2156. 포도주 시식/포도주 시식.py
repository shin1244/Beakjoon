n = int(input())


arr = [0]+[int(input()) for _ in range(n)]
if n == 1:
    print(arr[1])
    exit()

DP = [0] * (n+1)
DP[1] = arr[1]
DP[2] = arr[1] + arr[2]

for i in range(3, n+1):
    DP[i] = max(arr[i]+arr[i-1]+DP[i-3], DP[i-1], arr[i]+DP[i-2])

print(max(DP))