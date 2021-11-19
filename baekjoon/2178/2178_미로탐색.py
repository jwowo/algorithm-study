"""
문제 
N x M 크기 배열의 미로가 있다.
1은 이동할 수 있는 칸이고, 0은 이동할 수 없는 칸이다.
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야하는 
최소 칸 수를 구하는 문제이다.

문제 접근 방법

출발 지점에서 목적지점까지 가는 길이 중간에 돌아가는 길이 없고 오직 하나뿐이라면
bfs 혹은 dfs 중 아무거나 사용해도 상관없겠지만
문제에서 

이 문제는 목적지까지 가는 최소 칸 수를 구하는 문제인데
사실 이 문제의 유형이 bfs인 것을 알고 풀어서 왜 dfs가 아닌 bfs로 풀어야하는지 잘 몰랐다.
나중에 알게 된 사실은 
bfs는 시작점에서 가까운 정점부터 순서대로 방문하는 탐색 알고리즘이기 때문에 
시작점에서 같은 거리만큼 떨어진 정점에 대해 같은 단계에서 탐색한다.
따라서 bfs 알고리즘은 최단거리 문제를 풀 때 사용한다.


 방문 탐색을 하는 과정에서 탐색의 결과가 최소인지를 어떻게 아는가?
    DFS가 아닌 BFS를 사용하면 각 단계에서의 거리는 최소가 된다.
1. (1, 1)에서 상하좌우로 이동가능한지 확인하여
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
2. 4방향으로 이동했을때 그래프의 값이 1이고,  visited가 False일때, count를 계속해서
    n, m에 도착하면 result 리스트에 append한다.
"""
""""
n : 가로, m : 세로
"""


import sys
from collections import deque


def bfs(maze, start_x, start_y, visited, n, m):
    # 시작 위치 큐에 넣고 방문처리한다
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        # 다음으로 이동할 위치가 이동가능하고 방문한적이 없으면 큐에 넣고 방문처리
        x, y = queue.popleft()
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 범위 안에 있고, 이동가능하고, 방문한적이 없는가? 
            if (0 <= nx < n) and (0 <= ny < m):
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


        if x == (n - 1) and y == (m - 1):
            return visited[x][y]


if __name__ == '__main__':
    # n : 가로, m : 세로
    n, m = map(int, sys.stdin.readline().split())
    maze = []
    visited = [ [0] * m for _ in range(n) ]    

    for _ in range(n):
        maze.append(list(map(int, sys.stdin.readline().strip())))

    # print(maze)
    # print(visited)

    print(bfs(maze, 0, 0, visited, n, m))




"""
import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
graph = []
count = 0

# Todo
visited = []

# visited도 모두 0으로 초기화하지말고 지도의 0을 이미 방문한거로 생각하면 어떨까?
# visited = [ [0] * n for _ in range(m) ]

def bfs(x, y):
    global count
    # 처음 위치 큐에 넣고 방문 처리
    queue = deque()
    queue.append((x, y))

    while queue:
        # 큐에서 하나씩 빼면서 방문하지않은 인접 노드 큐에 넣고 방문 처리
        current_x, current_y = queue.popleft()
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n: 
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))

                    count += 1
                    if nx == n - 1 and ny == m - 1:
                        break

# 지도 graph에 저장
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

# graph 자료형 'str' -> 'int' 으로 변경
for i in range(n):
    for j in range(m):
        graph[i][j] = int(graph[i][j])

bfs(0, 0)

print(graph)
"""

