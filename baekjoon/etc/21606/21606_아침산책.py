"""
입력 : 
    n : 정점의 수 
    a : 1 과 0으로 이뤄진 길이가 n인 문자열 a (1 : 실내, 0 : 실외)
    u, v : 간선의 정보 (정점1, 정점2)
"""

"""
문제 해결 아이디어 2 
실내 <-> 실내이면서, 중간에 실내를 거치지 않는 길의 개수를 구하는 문제
1. 실외를 하나의 컴포넌트로 생각하여, 그 주변에 인접한 실내의 개수를 dfs로 count한다.
주변 인접 실내의 개수가 5개이면, 답에 5*4를 해주면 된다.
같은 길이어도, 출발점과 도착점이 뒤바뀐 길도 다른 길로 계싼하는 문제이기 때문에 2로 나눠줄 필요가 없다.
2. 실내 <-> 실내 길 사이에 실외가 하나도 없을 경우에는 위 방법으로 count되지 않기 때문에 2로 나눠줄 필요가 없다.
실내이면서 주변 인접 실내인 경우를 count 한다.
"""
import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip()))

graph = [[] for _ in range(n + 1)]
visited = [ False ] * (n + 1)
result = 0

for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

    if a[x-1] == 1 and a[y-1] == 1:
        result += 2

#dfs 함수
def dfs(x):
    global count
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            if a[i - 1] == 1:
                count += 1
                # continue
            else:
                # visited[i] = True
                dfs(i)

    # result += count * count - count

for i in range(1, n + 1):
    if not visited[i] and a[i - 1] == 0:
        count = 0
        dfs(i) 
        result += count * (count - 1)

print(result)











"""
문제 해결 아이디어 1 - 60점
시작점과 끝점이 다르기 때문에 
모든 노드중에서 실내인 노드에 대해서만 DFS 실행
DFS 실행중 실내(1)를 만나면 count += 1
"""
"""
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip()))

graph = [[] for _ in range(n + 1)]
count = 0

for _ in range(len(a) - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def dfs(x):
    global count
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            if a[i - 1] == 1:
                count += 1
                continue
            else:
                dfs(i)


# 인덱스 0부터 시작
for i in range(1, len(a) + 1):
    visited = [False] * (n + 1)
    # 시작점이 실외이면 (0) 건너뜀
    if a[i - 1] == 0:
        continue
    # 시작점이 실내이면 (1)
    else:
        dfs(i)

print(count)
"""