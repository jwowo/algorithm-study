"""백준 18352번 특정 거리의 도시 찾기"""
"""문제
1 ~ n까지의 도시와 m개의 단방향 도로는 1 이다.
특정 도시 x부터 출발하여 도달할 수 있는 모든 도시 중에서,
최단 거리가 정확히 k인 모든 도시들의 번호를 출려하는 프로그램 작성하는 문제이다.

n : 도시의 개수 ( 2 <= n <= 300000 )
m : 도로의 개수 ( 1 <= m <= 1000000 )
k : 거리 정보 ( 1 <= k <= 300000 )
x : 출발 도시의 번호 ( 1 <= x < n )
"""

"""문제접근아이디어
우선순위 큐를 이용한 다익스트라 알고리즘을 이용하여
x번 도시에서 출발하여 다른 모든 도시로 가는 최단 경로를 distance 리스트에 저장하고
distance 리스트를 이용하여 x번 도시에서 거리가 k인 도시의 번호를 출력한다. 
"""
import sys
import heapq

# n : 도시 개수, m : 도로의 개수, k : 거리 정보, x : 출발 도시 번호
n, m, k, x = map(int, sys.stdin.readline().split())

# 간선 정보 2차원 리스트에 저장, 
# 모든 도시의 거리는 1 만큼 떨어져있으므로 그래프에 가중치는 1만큼 설정한다.
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

# 최단 거리 테이블 모두 무한으로 초기화
INF = int(1e9)
distance = [INF] * (n + 1)

# Dijkstra 알고리즘
def dijkstra(start):
    # 시작노드로 가는 최단 경로는 0으로 설정, 힙에 삽입
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        # 최소힙을 이용하여 최단 거리가 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(heap)

        # 현재 노드가 처리된적이 있다면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

# 다익스트라 알고리즘을 실행
# x에서 출발하여 n번 도시에 가는데 필요한 최단 거리 테이블 갱신
dijkstra(x)

# 도달할 수 없는 도시 체크를 위한 flag 변수 선언
flag = False

# 최단 경로 테이블을 돌면서 거리가 k인 도시 번호 출력
for i in range(1, n + 1):
    if distance[i] == k:
        flag = True
        print(i)

if flag == False:
    print(-1)