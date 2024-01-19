n = int(input())
arr = [input().split(' ') for _ in range(n)]

graph = {}

for i in arr:
    graph[i[0]] = [i[1] if i[1] != '.' else None, i[2] if i[2] != '.' else None]


def pre(start): #부모 왼 오
    if start:
        result.append(start)
        pre(graph[start][0])
        pre(graph[start][1])

def ino(start): #왼 부모 오
    if start:
        ino(graph[start][0])
        result.append(start)
        ino(graph[start][1])

def pos(start): #왼 오 부모
    if start:
        pos(graph[start][0])
        pos(graph[start][1])
        result.append(start)

result = []
pre('A')
print(''.join(result))
result = []
ino('A')
print(''.join(result))
result = []
pos('A')
print(''.join(result))