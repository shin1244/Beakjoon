n, m = map(int,input().split(' '))

S1 = set()
S2 = set()

for i in range(n):
    S1.add(input())

for j in range(m):
    S2.add(input())

arr = list(S1&S2)

print(len(arr))
for i in sorted(arr):
    print(i)