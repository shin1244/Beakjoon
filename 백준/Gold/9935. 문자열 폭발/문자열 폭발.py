import sys, re
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

bomb_len = len(bomb)
stack = []
for i in s:
    stack += i
    if stack[-bomb_len:] == list(bomb):
        del stack[-bomb_len:]

print("".join(stack)) if stack else print('FRULA')