import sys
import heapq

# 자료구조 최대힙
heap = []

n = int(sys.stdin.readline().strip())
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num:
        heapq.heappush(heap, (-num, num))
    else:
        if heap:
            print(heapq.heappop(heap)[-1])
        else:
            print('0')