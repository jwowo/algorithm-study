import sys

sys.setrecursionlimit(10**8)

def get_squared_distance(a, b):
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)


def divide(start, end):
    if end - start == 1:
        return get_squared_distance(points[start], points[end])

    mid_idx = (start + end) // 2
    min_distance = min(divide(start, mid_idx), divide(mid_idx, end))

    candidates = []

    for i in range(start, end + 1):
        if (points[mid_idx][0] - points[i][0]) ** 2 < min_distance:
            candidates.append(points[i]) 

    candidates.sort(key = lambda x : x[1])

    for i in range(len(candidates) - 1):
        for j in range(i + 1, len(candidates)):            
            # if (points[j][1] - points[i][1]) ** 2 > min_distance:
            #     break
            # else:
            #     point_distance = get_squared_distance(points[i], points[j])
            #     min_distance = min(min_distance, point_distance)

            y_distance = points[i][1] - points[j][1]

            if y_distance * y_distance < min_distance:
                point_distance = get_squared_distance(points[i], points[j])
                min_distance = min(min_distance, point_distance)
            else:
                break

    return min_distance

n = int(sys.stdin.readline())
points = []

for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))

points.sort()

answer = divide(0, n - 1)
print(answer)