# 높이가 다 다른 요소로 이뤄진 n x n 행렬이 있다.
# 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇개 만들어지는지 조사
# 비의 높이 이하의 지점은 물에 잠긴다.
# 2 <= n <= 100 정수
# 1 <= 각 요소의 높이 <= 100 정수

# 시간복잡도 : 100 * n^2 -> 100 * 100 * 100 = 1,000,000

# 스케치
import sys
sys.setrecursionlimit(10000000)
n = int(sys.stdin.readline().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


# 2차원 배열의 최댓값을 찾는 방법
max_height = max(map(max, arr))
# print(max_height)
# 0부터 max_height까지 돌면서
# 비교 사항
# 매개 변수 : rain_height ( 1 ~ max_height )
# 
# arr배열의 모든 요소를 방문하는
# 반복문 돌면서 
# 만약 아직 방문 안하고 and rain_height보다 높다면 
#   count+= 1, 방문 처리, 인접 노드도 모두 방문 처리
#   인접노드 방문은 1 <= 다음 nx와 ny <= 5 일 때

def dfs(x, y, rain_height):
    dx = [ -1, 0, 1, 0 ]
    dy = [ 0, 1, 0, -1 ]

    # 2차원 배열의 방향 이동시에 자주 사용되는 루틴
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < n) and (0 <= ny < n):
            if (visited[nx][ny] == False) and (arr[nx][ny] > rain_height):
                visited[nx][ny] = True
                dfs(nx, ny, rain_height)
ans = 1

for rain_height in range(max_height): 

    count = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (arr[i][j] > rain_height) and (visited[i][j] == False):
                count += 1
                visited[i][j] = True
                dfs(i, j, rain_height)

    ans = max(ans, count)

print(ans)
"""
max_height = 0
min_height = 100

# O(N^2)
for i in range(n):
    for j in range(n):
        max_height = max(max_height, arr[i][j])
        min_height = min(min_height, arr[i][j])

print(f'min height : {min_height}, max height : {max_height}')

result = 1 # 비가 오지 않았을 경우, 안전 영역은 1개
temp = []   # 강수량에 따른 행렬

def check_validation(temp, x, y):
    global result
    # 0인지 아닌지 확인
    if temp[x][y] > 0:
        result += 1
        temp[x][y] = 0
        
        check_validation(temp, x, y+1)
        check_validation(temp, x, y-1)
        check_validation(temp, x+1, y)
        check_validation(temp, x-1, y)
    
for rain_height in range(min_height, max_height):
    # 강수량에 따라 지도 작성 완료
    for i in range(n):
        for j in range(n):
            if arr[i][j] - rain_height <= 0:
                temp[i][j] = 0
            else:
                temp[i][j] = arr[i][j] - rain_height
    
    
    check_validation(temp,0,0)
    # for i in range(n):
    #     for j in range(n):
    #         check_validation(temp, i, j)
"""