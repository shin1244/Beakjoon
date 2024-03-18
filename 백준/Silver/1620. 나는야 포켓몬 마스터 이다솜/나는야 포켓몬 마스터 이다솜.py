n, m = map(int,input().split(' '))

dic1 = {}
dic2 = {}

for i in range(1, n+1):
    pokemon = input()
    dic1[i] = pokemon
    dic2[pokemon] = i


arr = [input() for _ in range(m)]

for i in arr:
    if i.isdigit():
        print(dic1[int(i)])
    else:
        print(dic2[i])