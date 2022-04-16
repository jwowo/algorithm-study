"""
결국 최소 비교 횟수가 제일 작으려면
매 비교시 마다 제일 작은 두 수만 계속해서 더한다.
결국 우선순위 큐안에 1개의 원소만 남을때까지

result에는 현재까지의 비교 횟수를 저장한다.
"""

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

result = 0

while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)

    result += (num1 + num2)
    heapq.heappush(heap, (num1 + num2))

print(result)
    