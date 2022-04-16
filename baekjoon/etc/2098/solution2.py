import sys

input = sys.stdin.readline

N = int(input())
dists = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
dp = [[0] * N for _ in range(N)]
INF = float('inf')

def find_path(last, visited):
    if sum(visited) == N:
        return dists[last][0] or INF

    if dp[last][visited]

# print(sum(visited))
# visited[0] = True
# print(sum(visited))
