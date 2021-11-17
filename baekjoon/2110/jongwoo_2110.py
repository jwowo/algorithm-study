# n : 집의 개수, c : 공유기의 개수
# x : 집의 좌표
# 
# 공유기 c를 n 개의 집에 설치해서
# 가장 인접한 두 공유기 사이의 거리를 최대

"""
문제 접근 방법
1. houses 리스트에 집들의 좌표를 저장하고 오름차순 정렬한다.
2. 공유기를 설치할 수 있는 최소 거리를 start (1칸), 최대 거리(가장 멀리있는 집의 좌표 - 가장 처음에 있는 집의 좌표)를 end로 설정
3. 첫번째 집부터 공유기 설치
4. 설치 가능한 공유기의 개수가 c개 이상이면 더 설치할 수 있으므로 공유기 설치 거리를 +1 해준다.
5. c개를 넘어가지 않는다면 공유기간 설치거리를 -1 해준다.
6. 1~5 과정을 반복하여 c개의 공유기가 설치될 수 있는 최대 거리를 반환한다.
"""

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