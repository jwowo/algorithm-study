# n : 집의 개수, c : 공유기의 개수
# x : 집의 좌표
# 
# 공유기 c를 n 개의 집에 설치해서
# 가장 인접한 두 공유기 사이의 거리를 최대
# 

# 문제접근방법
# 요소의 개수가 n 개인 [ 0, 1, ..., n -1 ] 인 리스트 생성 생성
# 공유기간의 거리를 0, distance로 set
# 이전 집과 지금 집의 거리가 distance 보다 크면
#   현재의 위치를 변경하고, 공유기 += 1
# 
# 최소거리를 설정하여 설치한 공유기의 개수가 필요한 공유가보다 크면
#   집 간 최소 거리를 늘림
# 필요한 공유기보다 확인한 개수가 적으면
#   집 간 최소 거리를 늘림  

import sys

n, c = map(int, sys.stdin.readline().split())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
# print(arr)

start = 1
end = arr[-1] - arr[0]

result = 1

while (start <= end):
    gap = (start + end) // 2

    current = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] - current >= gap:
            current = arr[i]
            count += 1

    if count >= c:
        result = gap
        start = gap + 1

    else:
        end = gap - 1

print(result)