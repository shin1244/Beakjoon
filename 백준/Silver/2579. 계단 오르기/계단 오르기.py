N = int(input())
arr = [0]+[int(input()) for _ in range(N)]

if N == 1:
    print(arr[1])
    exit()
if N == 2:
    print(arr[1]+arr[2])
    exit()

DP = [0] * (N+1)

DP[1] = arr[1]
DP[2] = arr[1] + arr[2]

DP[3] = max(arr[1]+arr[3], arr[2]+arr[3])
for i in range(4, N+1):
    DP[i] = max(DP[i-3]+arr[i-1]+arr[i],DP[i-2]+arr[i])

print(DP[-1])