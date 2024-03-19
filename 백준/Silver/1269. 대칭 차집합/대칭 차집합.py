n, m = map(int,input().split(' '))
arr1 = list(map(int,input().split(' ')))
arr2 = list(map(int,input().split(' ')))

S1 = set(arr1)
S2 = set(arr2)

print(len(S1-S2) + len(S2-S1))