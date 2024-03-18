n = int(input())

arr = list(map(int,input().split(' ')))
DP = [0] * n
DP[0] = arr[0]

for i in range(1,n):
    if DP[i-1] < 0:
        DP[i] = arr[i]
    else:
        DP[i] = arr[i] + DP[i-1]

print(max(DP))