import sys, re
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.': break
    brackets = re.findall(r"\[|\]|\(|\)", s)

    arr = []
    for i in brackets:
        if i in ['(', ')']:
            if i == '(': 
                arr.append("(")
            elif not arr or arr.pop() != '(': 
                arr = [-1]
                break
        elif i in ['[', ']']:
            if i == '[': 
                arr.append("[")
            elif not arr or arr.pop() != '[': 
                arr = [-1]
                break


    if len(arr):
        print('no')
    else:
        print('yes')