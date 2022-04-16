import sys
import heapq

"""
두개의 힙울 아용하여 중간 값 관리
왼쪽 힙 : left, 오른쪽 힙: right
left와 right의 보유 원소 개수가 같으면 left에 삽입
이외에는 right에 삽입
만약 left의 가장 큰 값과 right의 가장 작은 값 비교하여 left의 가장 큰 값이 더 크면 
left의 가장 큰 값과 right의 가장 작은 값 바꿔줌
그럼 right의 가장 큰 값은 중간값이기 때문에 효율적이다.
"""
"""
짝수개를 외쳤다면 중간에 있는 두 수중에서 작은수를 말해야하기 때문에 
항상 min_h(최대힙)의 루트노드(최대값)을 뽑기 위해서
min_h과 max_h 개수가 

left max의 갑과 right min의 갑을 비교한 후 keft max의 값이 더 크면
right min값과 교체한다.

left의 max값을 출력한다.
"""
n = int(sys.stdin.readline().strip())
max_h, min_h = [], []

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(min_h) == len(max_h):
        heapq.heappush(max_h, (-num, num))
    else:
        heapq.heappush(min_h, (num, num))

    if len(min_h) >= 1 and len(max_h) >= 1 and max_h[0][1] > min_h[0][1]:
        max_value = heapq.heappop(max_h)[1]
        min_value = heapq.heappop(min_h)[1]
        heapq.heappush(max_h, (-min_value, min_value))
        heapq.heappush(min_h, (max_value, max_value))

    print(max_h[0][1])