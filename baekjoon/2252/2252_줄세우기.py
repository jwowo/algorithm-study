"""문제
n명의 학생들을 키 순서대로 줄 세운다
각 학생의 키를 직접 잴 수 없어서
두 학생의 키를 비교하는 방법 사용

모든 학생들을 다 비교하지 못하고 일부 학생들의 키만을 비교
일부 학생들의 키를 비교한 결과 주어지면, 줄 세우는 프로그램 작성

입력
    n : 학생 수 ( 1 <= n <= 32,000 )
    m : 키를 비교한 횟수 ( 1 <= m <= 100,000 )
    키를 비교한 두 학생의 번호 A, B : 힉생 A 가 학생 B 앞에 서야 한다.

출력
    학생들을 키 순서대로 줄 세운 결과 출력
    답이 여러 가지일 경우 아무거나 출력
"""
"""문제 접근 방법
위상 정렬을 이용하여 키가 작은 학생부터 출력한다.
"""


import sys
from collections import deque

input = sys.stdin.readline

# 노드의 개수와 간선의 개수를 입력 받기
n, m = map(int, input().split())

# 각 노드에 연결된 간선 정보를 담기 위한 연겨 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 모든 노드에 대한 진입차수는 0으로 초기화
# 학생들의 번호는 1부터 시작하기 때문에 인덱싱을 위해 학생 수 +1 만큼 선언 및 초기화
indegree = [0] * (n + 1)

# 키가 작은 사람이 키가 큰 사람을 가리키게 지정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
    # 진입 차수를 1 증가
    # 키가 작은 사람이 키가 큰 사람을 가리키는 방향그래프이므로 키 작은 사람의 진입차수 증가시킴
    indegree[b] += 1


# 위상 정렬
def topology_sort():
    queue = deque()
    result = []     # 알고리즘 수행 결과를 담을 리스트

    # 초기에 진입차수가 0인 노드 큐에 삽입한다.
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    #큐가 빌 떄까지 반복
    while queue:
        # 큐에서 원소 꺼내기
        now = queue.popleft()
        result.append(now)

        # 큐에서 꺼낸 노드와 연결된 노드들의 진입차수 하나씩 빼기
        for i in graph[now]:
            indegree[i] -= 1

            # 이 과정에서 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

