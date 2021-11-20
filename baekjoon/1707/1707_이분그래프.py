"""
문제 
그래프의 정점의 집합을 둘로 분할
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있다.
이런 그래프를 이분 그래프

그래프가 입력으로 주어짐 이 그래프가 이분 그래프인가 아닌가?
"""

"""
입력
k : 테스트 케이스 개수 ( 1 <= k <= 5 )
v : 정점의 개수 ( 1 <= v <= 20000 )
e : 간선의 개수 ( 1 <= e <= 200000 )

각 정점에는 1부터 v까지 차례로 번호가 붙어있다.
둘 째줄부터 e개의 줄에 간선 정보.
각 줄에 인접한 두 정점의 번호 u, v(u != v)가 빈칸을 사이에 두고 주어짐

맨 처음에 상태를 저장할 배열 선언 [ 0 : 아직 그룹화 안함, 1 : 검정, 2 : 흰색 ]
bfs를 돌면서 
    처음에 큐에서 pop하고 그 상태를 '1'로 설정 (부모노드)
    자식 노드가 0이면 자식 노드 상태를 '2'로 변경
    자식노드가 2이면 pass
    자식 노드 상태가 1이면 break 하고 return 'No'
    
    끝까지 갔는데 괜찮으면 return 'ㅛㄷㄴ
"""

import sys
from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    # 상태 지정을 해줘야할 듯
    status[x] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            # if not visited[i]:
            # 아직 상태가 없을 경우 부모 노드와 반대로 설정한다.
            if status[i] == 0:
                if status[v] == 1:
                    status[i] == 0
                else:
                    status[i] == 1
            # 부모 노드와 자식 노드의 상태가 같을 경우
            elif status[v] == status [i]
                return False
            # q
            else:
            queue.append(i)
            


k = int(sys.stdin.readline())

for _ in range(k):
    # v : 정점의 개수, e : 간선의 개수
    v, e = map(int, sys.stdin.readline().split())
    # graph : 인접 노드 정보, visited : 방문 정보, status : 집합 정보 
    graph = [[] for _ in range(v + 1)]
    # visited = [False] * (v + 1)
    status = [0] * (v + 1)
    # 간선의 정보 입력 받음
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(graph)
