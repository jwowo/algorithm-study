import sys
from collections import deque
read = sys.stdin.readline

def bfs():
    q = deque()
    q.append(artic[0])

    visited = [[False] * M for _ in range(N)]
    visited[artic[0][0]][artic[0][1]] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    selected_iceberg = 0  # 탐색한 빙산
    reduce = []

    # 녹일 빙산 탐색
    while q:
        x, y = q.popleft()

        selected_iceberg += 1
        cnt = 0  # 인접한 바다 개수

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    cnt += 1
                elif arr[nx][ny] > 0 and not visited[nx][ny]:  # 육지인 경우
                    visited[nx][ny] = True
                    q.append((nx, ny))

        if cnt != 0:
            reduce.append((x, y, cnt))

    # 녹이기
    for x, y, h in reduce:
        arr[x][y] = arr[x][y] - h if arr[x][y] - h > 0 else 0
        if arr[x][y] == 0 and (x, y) in artic:
            artic.remove((x, y))

    return selected_iceberg

# 입력
N, M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]

# 풀이
answer = 0
artic = []  # 빙산

for x in range(1, N):
    for y in range(1, M):
        if arr[x][y] != 0:
            artic.append((x, y))

while True:
    # 덩어리가 2개 이상인 경우
    if len(artic) != bfs():
        break

    answer += 1

    if sum(map(sum, arr[1:-1])) == 0:  # 빙하가 다 녹을때까지 덩어리가 1개
        answer = 0
        break

# 출력
print(answer)

# # 백준 2573번 빙산
# """
# 지구 온난화
# 빙산 높이는 배열의 각각에 양의 정수로 저장됨
# 하나의 빙산이 처음으로 2개 이상의 빙산으로 나뉘는 최초의 시간
# """

# import sys
# from collections import deque
# from copy import deepcopy

# # n : row, m : col
# n, m = map(int, sys.stdin.readline().split())
# iceberg = [] # 빙산
# for _ in range(n):
#     iceberg.append(list(map(int, sys.stdin.readline().split())))

# new_iceberg = [[0] * m for _ in range(n)] 

# artic = []

# for x in range(1, n):
#     for y in range(1, m):
#         if iceberg[x][y] != 0:
#             artic.append((x, y))

# print('artic')
# print(artic)

# # print(iceberg)
# # print(new_iceberg)

# # 2차원 배열의 상하좌우 이동을 위한 변수
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]


# # 모든 좌표의 빙산이 다 녹았으면 T, 하나라도 녹지 않은 좌표가 있다면 F 
# def check_melt():
#     for i in range(n):
#         for j in range(m):
#             if iceberg[i][j] > 0:
#                 return False
#     return True


# # 해당 좌표에서의 상하좌우 0의 개수 반환
# def count_zero(x, y):
#     cnt = 0 # 인접한 바다 개수
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m:
#             if iceberg[nx][ny] == 0:
#                 cnt += 1

#     return cnt


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     # visited[x][y] = True 

#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             na = a + dx[i]
#             nb = b + dy[i]

#             if not visited[na][nb] and iceberg[na][nb]:
#                 queue.append((na, nb))
#                 visited[na][nb] = True

# # print(n, m)
# # print(iceberg)

# # print(check_melt())

# while True:
#     year = 1
#     count = 0

#     # 빙산이 다 녹았다면 0을 출력
#     if check_melt():
#         print(0)
#         sys.exit()

#     # 1. 빙산 녹이기
#     # 모든 좌표에서 녹는 정도를 구하고 new_iceberge에 저장
#     for i in range(n):
#         for j in range(m):
#             zero = iceberg[i][j] - count_zero(i, j)
#             new_iceberg[i][j] = zero if zero > 0 else 0

#     iceberg = deepcopy(new_iceberg)

#     # 모든 좌표에서 bfs를 돌리면서 빙산의 덩어리가 2개 이상이라면 현재 year 출력 후 종료
#     for i in range(n):
#         for j in range(m):
#             if iceberg[i][j]:
#                 visited = [ [False] * m for _ in range(n) ]
#                 count += 1
#                 bfs(i, j)
#             if count >= 2:
#                 # print('final : ',year)
#                 break

    
    
    
#     year += 1

#     if count >= 2:
#         break

# print(year)

