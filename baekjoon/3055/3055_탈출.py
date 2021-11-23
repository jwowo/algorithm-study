"""백준 3055번 탈출"""
"""문제
이민혁 마법 구술을 얻어 홍수를 일으킬 것이다.
고슴도치 한마리 살고 있다.
고슴도치는 친구 비버의 굴로 가능한 빨리 도망가 홍수를 피하고자 한다.
티떱 숲의 지도는 R행 C열
    비어있는 곳은 '.'으로 표시
    물이 차있는 곳은 '*'으로
    돌은 'x'로 표시
비버의 굴은 'D'로
고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동(위, 아래, 오른쪽, 왼쪽)
물도 매분마다 비어있는 칸으로 확장한다
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 현을 공유)은 물이 차게 된다.
물과 고슴도치는 돌을 통과할 수 없다.
고슴도치는 물로 차있는 구역으로 이동할 수 없고,
물도 비버의 소굴로 이동할 수 없다

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하시오

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 아동할 수 있으면 고슴도치가 물에 빠지기 때문이다.
"""
"""입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.
다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다.
'D'와 'S'는 하나씩만 주어진다.
"""
"""출력
고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간 출력
만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS" 출력
"""
"""문제접근방법
물의 BFS와 도치의 BFS를 두개 한다.
물은 돌이나 비버굴에 들어가지 못햇
도치는 물이나 돌에 들어가지 못햇
    만약 사방이 물 or 티떱숲 범위 or 돌이면 KAKTUS
"""

# queue에 고슴도치 위치를 넣어준후에 물에 위치를 넣어줬다 고슴도치가 먼저 이동하고 물이 차도록 만듬
# => 고슴도치가 이동했더라도 물이 이동할 위치라면 고슴도치를 덮어쓰기 때문

# 2차원 리스트 상하좌우 이동시에 다른 조건이 많을 경우에는 
# 조건의 가장 큰 것(공통적인) 을 가장 위로 뽑고 그 다음에 세세한 조건들을 단다.



import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
# forest = []
# for _ in range(r):
#     forest.append(list(input().strip()))
forest = [list(input().strip()) for _ in range(r)]

time = [[0]* c for _ in range(r)]

queue = deque()

# 고슴도치위치 (S), 물의 위치 (S) 큐에 넣고 
# 비버 굴(D) 위치 target에 저장
for row in range(r):
    for col in range(c):
        if forest[row][col] == "S":
            queue.appendleft((row, col))
        elif forest[row][col] == "*":
            queue.append((row, col))
        elif forest[row][col] == 'D':
            target = (row, col)

# 2차원 리스트 상하좌우 이동을 위한 direction 변수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(target):
    while queue:
        x, y = queue.popleft()

        # target인 비버굴에 도착했을 경우 걸린 시간을 반환
        if forest[target[0]][target[1]] == "S":
            return(time[target[0]][target[1]])

        # 상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 숲의 범위를 벗어나지 않는 선에서
            if 0 <= nx < r and 0 <= ny < c:
                # 도치일 경우
                # 이동할 곳이 돌과 물이 아니라면 도치의 위치를 이동한뒤 큐에 넣고, 걸린 시간 +1 해준다.
                if forest[x][y] == "S" and (forest[nx][ny] == '.' or forest[nx][ny] == 'D'):
                    forest[nx][ny] = "S"
                    queue.append((nx, ny)) 
                    time[nx][ny] = time[x][y] + 1

                # 물일 경우
                # 이동할 곳이 돌과 비버굴이 아니라면 물의 위치를 이동한뒤 큐에 넣고, 걸린 시간 +1 해준다.
                elif forest[x][y] == "*" and (forest[nx][ny] == "." or forest[nx][ny] == "S"):
                    forest[nx][ny] = "*"
                    queue.append((nx, ny))

    return "KAKTUS"

print(bfs(target))
