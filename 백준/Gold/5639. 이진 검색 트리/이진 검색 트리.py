import sys
sys.setrecursionlimit(10**9)
preorder = []
while True:                            
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break



def tree(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if preorder[i] > preorder[start]:
            mid = i
            break
    tree(start+1, mid-1)
    tree(mid,end)
    print(preorder[start])


tree(0, len(preorder)-1)