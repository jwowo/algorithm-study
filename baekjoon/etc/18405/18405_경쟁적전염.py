"""백준 18405번 경쟁적 전염"""
"""문제
n x n 크기 시험관
시험관은 1 x 1 크기의 칸
특정한 위치에는 바이러스가 존재할 수 있다.
모든 바이러스는 1번부터 k번까지의 바이러스 종류 중 하나에 속한다.
모든 바이러스는 1초마다 상하좌우의 방향으로 증식
매초마다 낮은 종류의 바이러스부터 먼저 증식
증식과정에서 특정칸에 이미 바이러스가 존자한다면 그곳에는 다른 바이러스가 들어갈 수 없다

시험관 크기와 바이러스의 위치 정보가 주어졌을 때, 
S초가 지난 후 (x,y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오

만약 s초가 지난 후 해당 위치에 바이러스가 존재하지 않는다면 0 출력
"""

import sys
import heapq
from collections import deque

input = sys.stdin.readline

# 문제 입력값 저장
n, k = map(int, input().split())
graph = []
visited = []

for i in range(1, n + 1):
    graph.append(list(map(int, input().split())))

s, target_x, target_y = map(int, input().split())

# print(n, k)
# print(graph)
# print(f'{s}초 후 {target_x}행, {target_y}열의 바이러스 번호는 ?)

queue = []

# 큐에 ( 바이러스 번호, 행, 열, 시간(초기 : 0) ) 저장
for i in range(n):
    for j in range(n):
        if graph[i][j]: 
            queue.append( (graph[i][j], i, j, 0) )

# 바이러스가 1번부터 퍼져야하므로 오름차순 정렬 후 deque 생성
queue.sort()
queue = deque(queue)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        virus_num, x, y, time = queue.popleft()

        # s초가 지나면 목표 지점 바이러스 번호 반환
        if time == s:
            return(graph[target_x - 1][target_y - 1])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 해당 위치가 시험관 안이고 다른 바이러스가 없다면
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus_num
                    # 다음 위치를 큐에 넣고 시간 + 1
                    queue.append((graph[x][y], nx, ny, time + 1))

    # 시간이 다 되기 전에 큐가 빈다면 목표 지점 바이러스 번호 반환
    return graph[target_x - 1][target_y - 1]

print(bfs())
