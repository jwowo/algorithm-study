"""스카이 라인"""

import sys
import heapq

n = int(sys.stdin.readline())

# points = [ 좌표, 높이, 상태 (시작 or 끝) ]
# 직사각형의 시작 데이터와 끝 데이터(더미데이터) 삽입
points = []
for _ in range(n):
    L, H, R = map(int, sys.stdin.readline().split())
    points.append([L, -H, R])
    points.append([R, 0, 0])

points.sort()
# print(points)

# heap : heapq (-height, x) -> 최대 힙으로 구현
# result : (x, height) -> 현재까지의 높이
#끝 지점 비교를 위해 [0,float('inf')] 값을 넣어놓음. 건물들이 이어져있지 않을 때
heap = [[0, float('inf')]] 
result = [[0,0]]

for start, negH, end in points:
    # 이미 지나간 데이터 삭제
    while heap[0][1] <= start:
        heapq.heappop(heap)

    # 시작일때 직사각형이 높이와 끝나는 위치 힙에 삽입
    if negH:
        heapq.heappush(heap, [negH, end])

    # 매번의 이벤트(삽입 및 삭제) 마다 높이 변화 시 result에 현재의 최대 높이값 힙에 추가
    if result[-1][1] != -heap[0][0]:
        result.append([start, -heap[0][0]])

# 힙에 맨 처음에 
print(result[1:])

"""스카이라인 승환님 코드

import sys
import heapq
n = int(sys.stdin.readline())
arr = []
for i in range(n):
  a = list(map(int, sys.stdin.readline().split()))
  arr.append([a[0], a[2], a[1]])
arr.sort()
heap = []
ans = []
i, n = 0, len(arr)
while i < n or heap:
  # heap이 비었을 때 혹은 최대 넓이의 오른쪽 좌표가 arr[i]의 왼쪽 좌표보다 클 때 heappush
  if (not heap) or (i < n and arr[i][0] <= -heap[0][1]):
    temp = arr[i][0]
    while i <  n and arr[i][0] == temp:
      # 최대힙에 ( -높이, 오른쪽 좌표 ) 삽입 
      heapq.heappush(heap, (-arr[i][2], -arr[i][1]))
      i += 1
    
  # arr[i]의 왼쪽좌표가 heap[0]의 오른쪽 좌표보다 클 때
  else:
    temp = -heap[0][1]
    while heap and -heap[0][1] <= temp:
      heapq.heappop(heap)
  # print(heap)
  height = len(heap) and -heap[0][0]

  # 높이가 달라졌을때마다 정답에 추가
  if not ans or height != ans[-1][1]:
    ans.append([temp, height])

# 정답 출력
for a in ans:
  print(*a, end= ' ')
"""