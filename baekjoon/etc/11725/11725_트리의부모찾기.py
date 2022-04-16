"""
문제 
노드의 개수 n과 (n - 1)개의 트리 상에 연결된 두 정점이 주어진다.
트리의 루트를 1이라고 했을 때,
2번 노드부터 각 노드의 부모 노드 번호를 출력하는 문제이다.
"""

"""
- BFS 알고리즘 동작 과정 
  1. 탐색 시작 노드를 큐에 넣고 방문처리한다.
  2. 큐에서 노드를 꺼낸다.
  3. 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
  4. 2 -> 3 과정을 반복한다.


문제 접근 방법
dfs와 bfs 둘 다 가능하지만, bfs를 이용하여 풀었다.
기본적인 아이디어
    큐에서 꺼낸 노드(1)의 인접 노드 중에서 방문하지 않은 노드(2)를 큐에 삽힙하고 방문하는데,
    이때 (1)은 (2)의 부모 노드이다.

1. 노드의 부모 노드 번호를 저장한 answer 리스트를 생성한다.
   - 리스트의 인덱스 : 노드의 번호
   - 리스트의 값 : 트리에서 노드의 번호가 해당 리스트의 인덱스인 노드의 부모 노드 번호

2. bfs 알고리즘에서 큐에서 노드를 꺼낸 후 인접노드를 방문하기 때문에 
  큐에서 꺼낸 값을 parent 변수에 저장한다.

3. 큐에서 꺼낸 노드의 인접 노드 중에서 방문하지 않은 노드(child)들은 큐에서 꺼낸 노드(parent)의 자식 노드가 되므로,
   정답 배열에 값을 저장한다. `answer[child] = parent`

"""

import sys
from collections import deque

# 입력값 저장
n = int(sys.stdin.readline())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모 노드를 저장할 answer 배열 선언
answer = [0] * (n + 1)

# ----- bfs -----
# 1번 노드 큐에 넣고 방문처리 
queue = deque()
queue.append(1)
visited[1] = True

while queue:
    # 큐에서 꺼낸 노드(1)
    parent = queue.popleft()

    # (1)의 인접 노드중에서 방문하지 않은 노드(2)는 (1)의 자식 노드이므로
    # 큐에 삽입, 방문처리 후 정답 배열에 추가한다. 
    for child in graph[parent]:
        if not visited[child]:
            queue.append(child)
            visited[child] = True
            answer[child] = parent

for i in range(2, len(answer)):
    print(answer[i])