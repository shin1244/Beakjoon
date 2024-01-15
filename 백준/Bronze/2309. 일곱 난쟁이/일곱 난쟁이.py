arr = [int(input()) for _ in range(9)]


def beakJoon(arr):
    hobit = sum(arr)
    for i in range(9):
        for j in range(i+1,9):
            if hobit - arr[i] - arr[j] == 100:
                return [i, j]

a, b = beakJoon(arr)
result = [arr[item] for item in range(9) if item != a and item != b]

for i in sorted(result):
    print(i)