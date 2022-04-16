"""백준 10000번 원 영역"""
import sys

n = int(sys.stdin.readline())

def check_connection(coordinates):
    stack = []
    count = 1   # 원이 없어도 공간 하나는 있음

    for circle_type, coordinate in coordinates:
        # print(f'현재 좌표 : {coordinate}')
        # 원의 시작점이면 무조건 삽입
        if circle_type == 'start':
            stack.append([circle_type, coordinate])
        else:
            inner_circle = 0
            while stack and stack[-1][0] == 'circle':
                inner_circle += stack.pop()[1]

            new_circle = coordinate - stack.pop()[1]
            if new_circle == inner_circle:
                count += 2
            else:
                count += 1

            stack.append(['circle', new_circle])
            
    return count

coordinates = []

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    coordinates.append(['start', x - r])
    coordinates.append(['end', x + r])

coordinates.sort(key = lambda x : x[0])
coordinates.sort(key = lambda x : x[1])

answer = check_connection(coordinates)

print(answer)