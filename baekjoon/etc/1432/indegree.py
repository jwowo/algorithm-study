import sys
import heapq
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
v_info = [list(map(int, input().strip()))for _ in range(N)]
for i in range(N):
    for n in range(N):
        if v_info[i][n] == 1:
            graph[i+1].append(n+1)
            indegree[n+1] += 1
result = []
ans = [[] for _ in range(N+1)]
def topology_sort():
    q = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
topology_sort()
if len(result) != N:
    print(-1)
else:
    for index, b in enumerate(result):
        ans[b] = index+1
    for i in range(1, N+1):
        print(ans[i], end=' ')