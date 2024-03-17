import sys
input = sys.stdin.readline

arr = [input().rstrip().split(' ') for _ in range(int(input()))]

dic = {i:j for i, j in arr}

result = []

for i in dic:
    if dic[i] == 'enter':
        result.append(i)

for i in sorted(result, reverse=1):
    print(i)