input()
arr1 = set(map(int, input().split(' ')))
input()
arr2 = list(map(int, input().split(' ')))

for i in arr2:
    if arr1 & set([i]):
        print(1)
    else:
        print(0)