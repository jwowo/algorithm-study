import sys

input = sys.stdin.readline
n = int(input())
intervals = []

def calculate_num_area(intervals):
    coordinates = []
    stack = []

    for left, right in intervals:
        coordinates.append((0, left))
        coordinates.append((1, right))

    coordinates = sorted(coordinates, reverse=True)
    coordinates = sorted(coordinates, key=lambda x: x[1])

    print(coordinates)

    count = 1

    for lr, x in coordinates:
        # 원의 시작점
        if lr == 0:
            stack.append((0, x))
        # 원의 끝점
        else:
            inner_circle = 0

            # 온전한 원을 만났을때 
            while stack and stack[-1][0] == 2:
                _, complete_circle = stack.pop()
                inner_circle += complete_circle

            new_circle = 
            
            x - stack.pop()[1]
            if new_circle == inner_circle:
                count += 2
            else:
                count += 1

            stack.append((2, new_circle))

    return count

for _ in range(n):
    x, r = map(int, input().split())
    intervals.append((x-r, x+r))

print(calculate_num_area(intervals))



# import sys
# from bisect import *

# n = int(sys.stdin.readline())
# points = []

# for i in range(n):
#     x, r = map(int, sys.stdin.readline().split())
#     # points.append([x-r, x+r])
#     points.append(["{", x-r, 0, 0])
#     points.append([")", x+r, 0, 0])

# points.sort(key=lambda x : (x[1], x[0]))
# # a.sort(key = lambda x : (x[0], -x[1]))

# stack = []
# answer = 1

# for i in range(len(points)):
#     if points[i][0] == '{':
#         if stack:
#             if stack[-1][1] == points[i][1] or stack[-1][3] == points[i][1]:
#                 stack[-1][2] = 1
#             else:
#                 stack[-1][2] = 0
#         stack.append(points[i])

#     else:
#         half = stack.pop()
#         if stack and stack[-1][2] == 1:
#             stack[-1][3] = points[i][1]

#         if half[2] == 1 and half[3] == points[i][1]:
#             answer += 1
#         answer += 1

# print(answer)