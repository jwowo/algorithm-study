import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    for s in scoville:
        heapq.heappush(heap, s)
    # print(heap)
    while heap:
        if len(heap) == 1 and heap[0] < K:
            return -1
        if heap[0] >= K:
            return answer
        first = heapq.heappop(heap);
        second = heapq.heappop(heap);
        heapq.heappush(heap, first + 2 * second)
        answer += 1
    return answer