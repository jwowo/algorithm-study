import sys
import heapq

n = int(sys.stdin.readline())
roads = []

for _ in range(n):
    house, office = map(int, sys.stdin.readline().split())
    roads.append([min(house, office), max(house, office)])

heap = []
l = int(sys.stdin.readline())

roads.sort(key = lambda x : x[0])
roads.sort(key = lambda x : x[1])

result = 0

for road in roads:
    start_point = road[0]
    end_point = road[1]

    train_end = end_point - l

    if end_point >= train_end:
        heapq.heappush(heap, start_point)

    while heap and heap[0] < train_end:
        heapq.heappop(heap)

    result = max(result, len(heap))

print(result)
