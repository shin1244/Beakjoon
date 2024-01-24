import sys
input = sys.stdin.readline 
nodes, edges = list(map(int,input().split()))

arr = [list(map(int,input().split())) for _ in range(edges)]

link_dict = {i:i for i in range(1,nodes+1)}

def find(node):
    if link_dict[node] != node:
        link_dict[node] = find(link_dict[node])
    return link_dict[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        link_dict[max(root1, root2)] = min(root1, root2)

for i, j in arr:
    union(i, j)

print(len(set(find(node) for node in link_dict)))