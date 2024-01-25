item, w = list(map(int,input().split()))

arr = [list(map(int,input().split())) for _ in range(item)]

result_arr = []
for i in range(w+1):
    result_arr.append(0)

for weight, value in arr:
    for k in range(w, 0, -1):
        if result_arr[k] != 0 and k+weight <= w:
            result_arr[k+weight] = max(result_arr[k] + value, result_arr[k+weight])
    if 0 < weight < w+1:
        result_arr[weight] = max(result_arr[weight], value)

print(max(result_arr))