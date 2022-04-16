"""
입력 :
    n : 정점의 개수 ( 1 <= n <= 1000 )
    m : 간선의 개수 ( 1 <= m <= 10000 )
    v : 탐색을 시작할 정점의 번호 ( 1 <= v <= n )

출력 :
    첫째줄에 DFS, 둘째줄에 BFS 수행한 결과
"""

import sys
from collections import deque

def dfs(graph, x, visited):
    visited[x] = True
    print(x, end=' ')

    for i in range(1, n + 1):
        if not visited[i] and graph[x][i] == 1:
            dfs(graph, i, visited)        

def bfs(graph, start, visited):
    # 시작 노드를 큐에 넣고, 방문 처리.
    queue = deque([start])
    visited[start] = True

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아서 출력하기
        v = queue.popleft()
        print(v, end=' ')        
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True
                

n, m, v = map(int, sys.stdin.readline().split())

# 그래프 초기화
graph = [ [0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
    
# 방문 확인을 위한 visited 리스트 생성
# dfs 하기전에 visited 배열 다시 False로 초기화 필요 or 새로운 배열 필요
bfs_visited = [False] * (n + 1)
dfs_visited = [False] * (n + 1)

# 결과 저장용 리스트
bfs_res = []
dfs_res = []

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)