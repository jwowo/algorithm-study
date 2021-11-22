"""백준 1916번 최소비용 구하기"""
"""문제
n개의 도시
한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스
a번째 도시에서 b번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고한다.
a번째 도시에서 b번째 도시까지 가는데 드는 최소 비용
도시의 번호는 1 ~ n까지
"""
"""입력
첫째 줄에 도시의 개수 n : 1 <= n <= 1000
둘째 줄에 버스의 개수 m : 1 <= m <= 100000
셋째 줄부터 m + 2줄까지 다음과 같은 버스의 정보
    출발 도시 번호, 도착 도시 번호, 비용 ( 0 <= 비용 < 1000000 )
m + 3번째 줄에는 구하고자 하는 출발점의 도시 번호와 도착점의 도시 번호
"""
"""문제 접근 아이디어
입력 받은 값들을 리스트에 저장하고 
다익스트라 알고리즘을 이용하여 최단거리 테이블을 갱신한다.
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발지와 목적지 정보 저장
start, target = map(int, input().split())

# 최단 거리 테이블 초기화
INF = int(1e9)
distance = [INF] * (n + 1)

# print(n, m)
# print(graph)
# print(start, target)
# print(distance)

"""다익스트라 알고리즘
1. 출발지에서 출발지로 가는 최단거리 0으로 초기화하고 우선순위 큐에 삽입
2. while heap: (BFS와 느낌은 비슷하다)
    3. 최소힙을 이용하여 최단거리가 가장 짧은 노드 꺼내기
    4. 현재 노드가 이미 처리된적 있으면 무시 (continue)
    5. 현재 노드와 다른 인접한 노드들 확인
    6. 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 
        최단거리 테이블보다 짧을 경우 최단 거리 테이블 갱신
"""
def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(start)

print(distance[target])