"""
입력 : 
    n : 정점의 수 
    a : 1 과 0으로 이뤄진 길이가 n인 문자열 a (1 : 실내, 0 : 실외)
    u, v : 간선의 정보 (정점1, 정점2)
"""
"""
문제 해결 아이디어
시작점과 끝점이 다르기 때문에 
모든 노드중에서 실내인 노드에 대해서만 DFS 실행
DFS 실행중 실내(1)를 만나면 count += 1
"""


import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip()))

graph = [[] for _ in range(n + 1)]
count = 0

for _ in range(len(a) - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def dfs(x):
    global count
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            if a[i - 1] == 1:
                count += 1
                continue
            else:
                dfs(i)


# 인덱스 0부터 시작
for i in range(1, len(a) + 1):
    visited = [False] * (n + 1)
    # 시작점이 실외이면 (0) 건너뜀
    if a[i - 1] == 0:
        continue
    # 시작점이 실내이면 (1)
    else:
        dfs(i)

print(count)