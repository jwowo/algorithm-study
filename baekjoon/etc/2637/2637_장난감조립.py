"""백준 2637번 장난감 조림"""
"""문제
여러가지 부품을 조립하여 장난감을 만든다.
장난감을 만드는데는 기본 부품가 그 기본 부품으로 만든 중간 부품이 사용된다.
기본 부품은 더 이상 작은 부품들로 나눌 수 없는 최소 단위 부품이다.
어떤 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어져 있을 때 
하나의 장난감 완제품을 조립하기 위하여 
필요한 기본 부품의 종류별 개수를 계산하는 프로그램을 작성하시오
"""

"""입력
n : 완제품의 번호 ( 3 <= n <= 100 ) 
    1 ~ (n-1) 까지는 기본 부품이나 중간 부품의 번호를 나타냄
m : 부품들간의 연결 정보 개수 ( 3 <= m <= 100 )
x, y, z : 어떤 부품을 완성하는 필요한 부품들 간의 관계가 3개의 자연수
        중간 부품이나 완제품 x를 만드는데 중간 부품 혹은 기본 부품 y가 k개 필요하다.
"""
""""문제 접근 방법
위상정렬과 DP를 이용하여 접근한다.
위상정렬을 통해 초기에 진입차수가 0 인 부품들이 기본 부품인 것을 알 수 있다.
기본 부품과 그래프간의 연결관계 `connections` 중간 부품을 만들고 
필요한 기본 부품들을 2차원 리스트 `graph` 에 업데이트한다.
기본 부품에서 부터 시작하여 중간 부품을 만들때마다 그전에 있던 기본 부품의 갯수를 계속 더해주면서
완제품에 필요한 기본 부품의 개수를 구한다.
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = int(input()), int(input())   # 완제품의 번호와 부품간의 연결관계 정보 개수 
connections = [[] for _ in range(n + 1)]    # 노드별 연결 정보
graph = [[0] * (n + 1) for _ in range(n + 1)]   # 가중치 입력 (필요한 부품의 개수 저장용)
indegree = [0] * (n + 1)    # 진입 차수

for _ in range(m):
    # 부품 연결관계 connections 리스트에 저장 후 진입차수 업데이트
    # next_module을 만들기 위해서는 current_module이 required_amount 개 만큼 필요하다
    next_module, current_module, required_amount = map(int, input().split())
    connections[current_module].append((next_module, required_amount))
    indegree[next_module] += 1

def topology_sort():
    queue = deque()

    # 초기 진입차수가 0인 노드들을 queue에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()

        # next_module : current를 재료로 사용하는 부품
        # required_amount : next_module을 만들기 위해 필요한 current의 개수
        for next_module, required_amount in connections[current]:

            # 현재 부품이 기본 부품일 때 (현재 부품을 만들기 위해 필요한 부품이 없는 경우)
            if graph[current].count(0) == n + 1:
                graph[next_module][current] += required_amount

            # 현 부품이 중간 부품이면  
            else:
                for i in range(1, n + 1):
                    # 기본 부품으로 중간 부품을 만드는데 필요한 개수 = 현재 부품을 만드는 기본 부품의 개수 * 현재 부품으로 중간 부품을 만드는데 필요한 개수
                    graph[next_module][i] += graph[current][i] * required_amount

            # 새롭게 진입 차수가 0이 되는 노드 큐에 삽입한다.
            indegree[next_module] -= 1
            if indegree[next_module] == 0:
                queue.append(next_module)

topology_sort()

# 기본 부품의 번호와 소요 개수 출력
for idx, val in enumerate(graph[n]):
    if val:
        print(idx, val)