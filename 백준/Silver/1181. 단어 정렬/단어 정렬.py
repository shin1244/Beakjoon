arr = [input() for _ in range(int(input()))]
arr = list(set(arr))
arr = sorted(arr, key=lambda x: [len(x), x])

[print(i) for i in arr]