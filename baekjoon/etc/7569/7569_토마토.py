"""백준 7569번 토마토"""
"""문제
토마토를 보관하는 큰 창고가 있다.
격자모양 상자의 칸에 하나씩 넣고, 상자들을 수직으로 쌓아 올려 보관한다.

보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있다.

보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 
익은 토마토의 영향을 받아 익게 된다.

하나의 토마토가 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
대각선 방향의 토마토는 영향이 없다.
토마토가 혼자 저절로 익는 경우는 없다.

토마토들이 며칠이 지나면 다 익게 되는가?
"""
"""입력
- 첫째 줄
m : 상자의 가로 ( 2<= m <= 100 )
n : 상자의 세로 ( 2<= n <= 100 )
h : 상자의 높이 ( 1<= h <= 100 )
- 둘째 줄부터 
가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토들의 정보가 주어짐

1 : 익은 토마토
0 : 익지 않은 토마토
- : 토마토가 들어있지 않은 칸
"""
"""출력
토마토가 모두 익을 때까지 최소 며칠이 걸리는지 계산해서 출력
    저장될 때부터 모든 토마토가 익어있으면 0 출력
    토마토가 모두 익지는 목하는 상황이면 -1 출력
"""

"""
문제 접근 방법

3차원이기 때문에 인덱싱을 하는데 어려움이 있었다.
토마토가 있는 위치를 큐에 저장하고 bfs를 실행한다.

만약 0이 존재하면 -1을 출력하고 그게 아니라면 제일 큰 값에 -1을 해준 값을 출력한다.
(시작날이 1이기 때문)
"""

import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())

# 3차원 토마토 정보 저장
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이(h), 가로(x), 세로(y) 순
            if tomatoes[i][j][k] == 1:
                queue.append((i, j, k))

# x축, y축, z축 3차원 이동을 위한 방향 변수 설정
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomatoes[nz][nx][ny] == 0:
                    tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                    queue.append((nz, nx, ny))

bfs()



flag = False
answer = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 0:
                flag = True
                
            answer = max(answer, tomatoes[i][j][k])

# BFS 탐색으로 익은 토마토의 인접한 안 익은 토마토들에 대해 익게 만들었지만
# 만약 안익은 토마토( 0 ) 이 존재하면 -1을 출력하고 다 익었다면 제일 큰 값에 -1을 해준 값을 출력한다.
if flag:
    answer = -1
elif answer == 1:
    answer = 0
else:
    answer -= 1

print(answer)

