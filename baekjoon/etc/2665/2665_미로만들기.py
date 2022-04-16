"""백준 2665번 미로만들기"""
"""문제
n x n 바둑판 모양의 n^2개의 방이 있다
일부는 검은 방, 나머지는 흰방
검은방은 사면이 벽으로 싸여 있어 들어갈 수 없다
서로 붙어 있는 두개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다.

왼줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고,
아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰방이다

시작방에서 출발하여 끝방으로 가는것이 목적

시작방에서 끝 방으로 갈 수 없을때, 부득이 하게 검은 방 몇개를 흰 방으로 바꾸어야한다.
되도록이면 적은 수의 방의 색을 바꾸고 싶다
"""
"""문제 접근 방법
어쨌든 시작방에서 끝방으로 이동해야하는데 지나는 검은 방의 개수가 최소가 되고 싶다.
bfs를 이용하여 heapq에 넣는다.
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 2차원 리스트에서 상하좌우 이동을 위한 dirction x, direction y 변수 선언
dx = [1, -1 ,0, 0]
dy = [0, 0, 1, -1]

# 방문 여부 체크를 위한 visited 2차원 리스트
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y))

    while heap:
        count, cx, cy = heapq.heappop(heap)
        visited[cx][cy] = True

        # 도착지점에 도착했을 경우
        if cx == (n - 1) and cy == (n - 1):
            return count

        # 상하좌우로 한칸씩 이동하여 탐색 진행
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
                # 방문처리
                visited[nx][ny] = True
                # 흰 방
                if graph[nx][ny] == 1:
                    heapq.heappush(heap, (count, nx, ny))
                # 검은 방
                else:
                    heapq.heappush(heap, (count + 1, nx, ny))

print(bfs(0, 0))


"""
import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
# print(f'n : {n}')
# print(f'graph : {graph}')

# 2차원 리스트에서 상하좌우 이동을 위한 dirction x, direction y 변수 선언
dx = [1, -1 ,0, 0]
dy = [0, 0, 1, -1]

# 방문 여부 체크를 위한 visited 2차원 리스트
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((0, x, y))

    visited[x][y] = True

    while queue:
        count, cx, cy = queue.popleft()

        # 도착지점에 도착했을 경우
        if cx == (n - 1) and cy == (n - 1):
            return count

        # 상하좌우로 한칸씩 이동하여 탐색 진행
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
                visited[nx][ny] = True
                # 흰 방
                if graph[nx][ny] == 1:
                    queue.append((count, nx, ny))
                # 검은 방
                else:
                    queue.append((count + 1, nx, ny))
print(bfs(0, 0))
"""