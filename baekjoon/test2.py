def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
v = int(input())
e = int(input())
parent = [0] * (v + 1)
edges = []
virus = 0
for i in range(1, v + 1):
    parent[i] = i
for _ in range(e):
    a, b = map(int, input().split())
    edges.append((a, b))
for edge in edges:
    a, b = edge

    
    if find(a) != find(b):
        union(a, b)
for i in range(2, len(parent)):
    if find(parent[i]) == parent[1]:
        virus += 1
print(virus)