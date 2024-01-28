N = int(input())

arr = list(map(int,input().split()))

DP = [0] * N
for i in range(len(arr)):
    save_arr = []
    for j in range(i):
        if arr[j] < arr[i]:
            save_arr.append(DP[j])
    if save_arr:
        DP[i] = max(save_arr) + 1

print(max(DP)+1)