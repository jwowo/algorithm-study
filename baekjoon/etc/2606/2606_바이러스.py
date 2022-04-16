"""백준 2606 바이러스"""

"""
문제 접근 방법
bfs해서 방문하지 않은 컴퓨터에 접근할때마다 count += 1 한다.
"""

import sys
from collections import deque

computers = int(sys.stdin.readline())
networks = int(sys.stdin.readline())
connections = [ [0] * (computers + 1) for _ in range(computers + 1) ]
visited = [False] * (computers + 1)
count = 0


def bfs(x):
    global count
    # 큐에 삽입하고 방문처리한다.
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        # 큐에서 빼서 인접한 노드를 큐에 넣고 방문처리
        v = queue.popleft()
        for i in range(1, computers + 1):
            if not visited[i] and connections[v][i] == 1:
                count += 1
                queue.append(i)
                visited[i] = True


for _ in range(networks):
    a, b = map(int, sys.stdin.readline().split())
    connections[a][b] = connections[b][a] = 1

bfs(1)
print(count)

"""
# Union find를 이용한 풀이
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
"""