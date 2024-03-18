import sys
input = sys.stdin.readline

n, m = map(int,input().split(' '))

dic1 = {}
dic2 = {}

for i in range(1, n+1):
    pokemon = input().rstrip()
    dic1[i] = pokemon
    dic2[pokemon] = i


arr = [input().strip() for _ in range(m)]

for i in arr:
    if i.isdigit():
        print(dic1[int(i)])
    else:
        print(dic2[i])