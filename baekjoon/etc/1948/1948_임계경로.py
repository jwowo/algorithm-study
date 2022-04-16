"""백준 1948번 임계경로"""
"""문제
월드 나라는 모든 도로가 일방통행인 도로이고 싸이클이 없다.
많은 사람들이 지도를 그리기 위해서 
어떤 시작 도시로부터 도착 도시까지 출발을 하여 가능한 모든 경로 탐색하고자 한다.

지도를 그리는 사람들이 사이가 좋아서 지도를 그리고 도착 도시에서 모두 다 만나기로 하였다.
그렇다고 할 때, 이들이 만나는 시간은 출발 도시로부터 출발할 후 최소 몇 시간 후에 만날 수 있는가?
즉 마지막에 도착하는 사람까지 도착하는 시간을 구하시오

또한 어떤 사람은 이 시간에 만나기 위하여 1분도 쉬지 않고 달려야 한다.
이런 사람들이 지나는 도로의 수를 출력해라.

출발 도시는 들어오는 도로가 0개이고, 도착 도시는 나가는 도로가 0개이다

"""
"""문제 입력
n : 도시의 개수 ( 1 <= n <= 10,000 )
m : 도로의 개수 ( 1 <= m <= 100,000 )
도시들의 연결 정보 (출발 도시 번호, 도착 도시 번호, 도로를 지나는데 걸리는 시간 )
지도를 그리는 사람들의 출발 도시, 도착 도시가 주어진다.

모든 도시는 출발 도시로부터 도달이 가능하고, 모든 도시로부터 도착 도시에 도달 가능하다.
"""

import sys
from collections import deque

input = sys.stdin.readline

# n : 도시의 개수, m : 도로의 개수
n = int(input())
m = int(input())

graph = [[] * (n + 1) for _ in range(n + 1)]
back_graph = [[] * (n + 1) for _ in range(n + 1)]

indegree = [0] * (n + 1)    # 진입차수
visited = [0] * (n + 1)     # 백트래킹시 큐에 중복 삽입 방지
result = [0] * (n + 1)  # 각 도시로 이동하는 임계 경로 저장을 위한 변수

# graph[출발 도시] = (도착 도시, 걸리는 시간)
# back_graph[도착 도시] = (출발 도시, 걸리는 시간)
# 진입 차수 초기화
for _ in range(m):
    start_city, target_city, weight = map(int, input().split())
    graph[start_city].append((target_city, weight))
    back_graph[target_city].append((start_city, weight))
    indegree[target_city] += 1

start, target = map(int, input().split())

queue = deque()
queue.append(start)

# 위상 정렬
def topology_sort():
    while queue:
        now = queue.popleft()
        for next, weight in graph[now]:
            # 현재 도시를 거쳐가느데 걸리는 시간과 이전의 다른 경로의 걸리는 시간을
            # 비교하여 큰 값을 임계 경로로 설정
            result[next] = max(result[next], result[now] + weight) 
            indegree[next] -= 1
            # 위상 정렬 수행 과정에서 진입차수가 0인 도시 발생시 큐에 삽입
            if indegree[next] == 0:
                queue.append(next)

    # 백트래킹
    queue.append(target)
    count = 0

    while queue:
        now = queue.popleft()
        for pre, weight in back_graph[now]:
            # ( 현재 도시까지의 임계경로 ) 과 
            # ( 현재 도시에서 인접한 도시까지의 임계 경로 + 현재 도시의 인접 도시에서 현재 도시로 이동하는데 걸리는 시간 )
            # 이 같으면 그 인접 도시는 임계 경로의 한 도시이다.
            if result[now] == result[pre] + weight:
                count += 1
                # 임계 경로의 도로 중복 카운트 방지
                if visited[pre] == 0:
                    queue.append(pre)
                    visited[pre] = 1
                    
    # 결과 출력
    print(result[target])
    print(count)

topology_sort()