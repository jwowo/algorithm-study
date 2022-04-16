"""백준 1197 최소 스패닝 트리"""
"""
정점의 개수 v
간선의 개수 e
정점 a, 정점 b, 가중치 c

문제 접근 방법
최소 신장 트리(MST, Minimum Spanning Tree)에 관한 문제이다.
MST 문제를 푸는 방법에는 
    간선의 길이를 기준으로 최솟값부터 찾아가는 크루스칼 알고리즘과
    노드를 기준으로 작은 간선을 선택해나가는 프림 알고리즘이 있다.

이 문제는 크루스칼 알고리즘과 그래프의 싸이클 체크를 위해 
Union Find를 이용하여 풀 예정이다.

1. 입력받은 간선의 가중치 기준으로 오름차순 정렬한다. 
    튜플 or 리스트 형태로 append( (가중치, a, b) )
2. 정렬된 리스트에서 두 정점에 대해 싸이클을 형성하는지를 Union Find를 통해 확인한다.
    1) 사이클을 형성하면 제외(continue) 한다.
    2) 사이클을 형성하지 않으면 MST집합에 추가하고, result에 가중치를 합해준다.
3. 모든 간선에 대해 1,2 과정을 반복 수행한다. 
   만약 간선의 개수가 (v - 1)개 라면 반복을 종료하고 result를 반환한다.
    (Kruskal 알고리즘에 따라 N개의 MST를 만드는데는 n-1개의 간선만 필요한 것이 증명되었다.)
"""

import sys

# parent 배열을 통해 x의 루트 노드를 재귀적으로 찾는다
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 해당 간선의 노드들로 싸이클이 발생하지 않아 MST집합에 포합시키는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v : 정점의 개수, e : 간선의 개수
# edgs : [(가중치, 노드 a, 노드 b)] 모든 간선을 담을 변수
# result : 최소 신장 트리의 가중치의 합을 저장할 변수
v, e = map(int, sys.stdin.readline().split())
edges = []
result = 0
# count = 0

# 각 노드의 부모노드 저장으 위한 변수
parent = [ x for x in range(v + 1)]
# print(f'parent 리스트 : {parent}')

for _ in range(e):
    a, b, weight = map(int, sys.stdin.readline().split())
    edges.append((weight, a, b))

# kruskal 알고리즘을 사용하기 위해 간선의 가중치를 기준으로 오름차순 정렬
edges.sort()

# 가중치가 낮은 간선부터 각 간선에 대해 싸이클 여부를 확인하고 MST 집합에 넣는다
for edge in edges:
    weight, a, b = edge

    # cycle : 싸이클 여부를 확인할 변수
    cycle = False

    # 싸이클링 도는 경우
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
    # 싸이클이 안도는 경우 합집화한다.
    else:
        union_parent(parent, a, b)

    if not cycle:
        result += weight

print(result)