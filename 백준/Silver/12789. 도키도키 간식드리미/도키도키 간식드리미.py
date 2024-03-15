import sys
input=sys.stdin.readline

n = int(input())
arr = list(map(int,input().rstrip().split(' ')))

stack = []
check_arr = list(range(1,n+1))

while arr:
    if check_arr[0] == arr[0]:
        check_arr.pop(0)
        arr.pop(0)
    elif stack and stack[-1] == check_arr[0]:
        check_arr.pop(0)
        stack.pop()
    else:
        stack.append(arr[0])
        arr.pop(0)

if not stack:
    print("Nice")
elif stack == list(range(stack[0], stack[-1]-1, -1)):
    print("Nice")
else:
    print("Sad")