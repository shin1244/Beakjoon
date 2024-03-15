import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().rstrip()
    check = 0

    for i in s:
        check += 1 if i == '(' else -1
        if check < 0:
            check = -1
            break
    
    if check == 0:
        print("YES")
    else:
        print("NO")