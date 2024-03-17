arr = [input().split(' ') for _ in range(int(input()))]
for i in sorted(arr, key=lambda x:(int(x[0]),int(x[1]))):
    print(i[0], i[1])