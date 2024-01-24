n = int(input())
arr = [list(input().split(' ')) for i in range(n)]

tree_dict = {}
for p, c1, c2 in arr:
    tree_dict[p] = [c1, c2]

def tree1(start):
    now = tree_dict[start]
    print(start, end='')
    if now[0] != '.':
        tree1(now[0])
    if now[1] != '.':
        tree1(now[1])
def tree2(start):
    now = tree_dict[start]
    if now[0] != '.':
        tree2(now[0])
    print(start, end='')
    if now[1] != '.':
        tree2(now[1])
def tree3(start):
    now = tree_dict[start]
    if now[0] != '.':
        tree3(now[0])
    if now[1] != '.':
        tree3(now[1])
    print(start, end='')

tree1('A')
print()
tree2('A')
print()
tree3('A')