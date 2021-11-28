"""백준 2098번 외판원 순회 https://www.acmicpc.net/problem/2098"""

"""문제
외판원 순회 문제는 영어로 Traveling Salesman Problem(TSP) 라고 불리는 문제로
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자

1번 부터 n번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다.
(길이 없을 수도 있다)
한 외판원이 어느 한 도시에서 출발해 n개의 도시를 모두 거쳐 다시 원래의 도시로 
돌아오는 순회 여행 경로를 계획하려고 한다.
단, 한번 갔던 도시로는 다시 갈 수 없다. 
(맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간 이동하는데 드는 비용은 행렬 W[i][j] 형태로 주어진다.
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.

비용은 대칭적이지 않다. 
즉 W[i][j]와 W[j][i]는 다를 수 있다. 모든 도시간의 비용은 양의 정수이다.
W[i][j]는 항상 0 이다.
도시 i 에서 도시 j 로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j] = 0 이다.

n과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원 순회 여행 경로를 구하는 프로그램을 작성하시오
"""

import sys

input = sys.stdin.readline

N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
VISITED_ALL = (1 << N) -1
cache = [[None] * (1 << N) for _ in range(N)]
INF = float('inf')

def find_path(last, visited):
    if visited == VISITED_ALL:
        return dist[last][0] or INF

    if cache[last][visited] is not None:
        return cache[last][visited]

    temp = INF
    
    for city in range(N):
        if visited & (1 << city) == 0 and dist[last][city] != 0:
            temp = min(
                temp,
                find_path(city, visited | (1 << city)) + dist[last][city])

    cache[last][visited] = temp
    return temp

print(find_path(0, 1 << 0))