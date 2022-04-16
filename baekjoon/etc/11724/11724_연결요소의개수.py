import sys
from collections import deque
"""
n : 정점의 개수
m :  간선의 개수
u, v : 간선의 양 끝점
"""

n, m = map(int, sys.stdin.readline().split())
graph = [ [0] * (n + 1) for _ in range(n + 1) ]
# print(graph)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

visited = [ False ] * (n + 1)
count = 0

"""
문제 해결 아이디어

for loop (1 -> n): 돌면서 
    if not visited 이면 
        count += 1
        bfs 돈다.
"""

def bfs(x):
    # 큐에 삽입하고 방문처리한다
    queue = deque([x])
    visited[x] = True

    while queue:
        # 큐에서 빼서 인접한 노드들 큐에 넣고 방문처리
        v = queue.popleft()
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True



for i in range(1, n + 1):
    # 방문하지 않았으면 
    if not visited[i]:
        count += 1
        bfs(i)

print(count)