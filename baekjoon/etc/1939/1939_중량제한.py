"""백준 1939번 중량 제한"""
"""문제
n 개의 섬으로 이루어진 나라
이들 중 몇 개의 섬 사이에는 다리 설치되어 있어 ㅏ드이 다닐 수 있다.

두 개의 섬에 공장을 세워두고 물품 생상
물품을 생산하다 보면 공장에서 다른 공장으로 생상 중이던 물품을 수숭해야함

각각의 다리마다 중량 제한이 있음
중량 제한 초과하면 다리가 무너짐

한번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값은?

n : 섬의 개수 ( 2 <= n <= 10,000 ) 
m : 다리의 개수 ( 1 <= m <= 100,000 )

a, b, c : a번 섬과 b번 섬 사이에 중량제한이 c인 다리가 존재
두 섬 사이에 여러 다리 가능
모든 다리 양방향

마지막 줄에는 공장이 위치해 있는 서므이 번호를 나타내는 서로 다른 두 정수가 주어짐
"""

"""문제 접근 방법
이 문제의 힌트는 다리의 중량 제한인 c가 10억(1,000,000,000) 이므로 
cpu가 1초에 약 1억의 수를 연산할 수 있다고 가정하면
시간복잡도가 O(C)일 때 약 10초가 걸리게 되어 시간 초과가 발생한다.

따라서 이 문제처럼 N이 엄청나게 클때는 
시간복잡도를 O(log N)으로 줄일 수 있는 이분 탐색의 가능성을 생각해봐야한다.

파라메트릭 서치란 ?
이분 탐색을 활용하여 결정 문제('YES' or 'NO')를 최적화 알고리즘으로 바꾸어 해결하는 기법이다.

이 문제는 파라메트릭 서치를 이용하여 
    한 번의 이동에서 옮길 수 있는 무게(0 ~ 1,000,000,000) 를 이분 탐색하여 
    이동 가능한 무게의 최댓값(bisect_right)을 찾는 문제이다.

    이동할 수 있으면 'YES' 를 반환, 정답에 저장한 후 무게를 늘려서 조건을 만족하는 더 큰 무게가 있는지 탐색한다.
    이동할 수 없으면 'NO' 를 반환하여 무게의 작게 만들고 조건을 만족하는지 탐색한다. 
"""

"""이분 탐색, BFS
import sys
from collections import deque

input = sys.stdin.readline

# 입력값 저장
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    island_1, island_2, weight = map(int, input().split())
    graph[island_1].append((island_2, weight))
    graph[island_2].append((island_1, weight))

# 입력 값 중에서 가장 큰 값 : max_weight
# 입력 값 중에서 가장 작은 값 : min_weight 
# 해도 되지만, 이분 탐색은 크기가 O(logN)으로 줄어들기 때문에 문제에서 주어진 최대, 최솟값 이용
min_weight = 1
max_weight = 1000000000

# 시작 도시와 도착 도시 
start_island, end_island = map(int, input().split())

# print(f'n : {n}, m : {m}')
# for i in graph:
#     print(i)
# print(f'min : {min_weight}, max : {max_weight}')
# print(f'start : {start_island}, end : {end_island}')

# BFS 
# 이동 가능하면 큐에 넣고, 방문, 
# 큐에서 꺼낸 도시가 도착도시이면, 방문이 가능하다는 의미이므로 return True
# 이동이 가능한 도시에 대해서 BFS 탐색을 다 했는데 탐색이 종료되지 않았다면 
    # 종료도시는 무게 제한 때문에 갈 수 없다는 의미이므로 return False
def bfs(mid_weight):
    queue = deque([start_island])
    # queue.append(start_island)
    visited = set()
    visited.add(start_island)

    while queue:
        island = queue.popleft()
        if island == end_island:
            return True
        # print(f'queue : {queue}')

        for next, weight in graph[island]:
            if next not in visited and mid_weight <= weight:
                visited.add(next)
                queue.append(next)
    
    return False

# 이분 탐색 진행
# mid = (max_weight + min_wieght) // 2
# if bfs() == True:
#   result = mid 로 갱신
result = min_weight

while min_weight <= max_weight:    # To Do (조건)
    mid = (min_weight + max_weight) // 2
    # flag = bfs(mid)

    if bfs(mid):
        result = mid
        min_weight = mid + 1
    else:
        max_weight = mid  - 1

print(result)
"""

import sys
from collections import deque

input = sys.stdin.readline

# 입력값 저장
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    island_1, island_2, weight = map(int, input().split())
    graph[island_1].append((island_2, weight))
    graph[island_2].append((island_1, weight))

min_weight = 1
max_weight = 1000000000

# 시작 도시와 도착 도시 
start_island, end_island = map(int, input().split())

INF = int(1e9)
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[i] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start_island)

# print(distance)
print(distance[end_island])

print(distance)
