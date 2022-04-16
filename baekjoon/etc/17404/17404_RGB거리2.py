"""백준 17404 RGB 거리 2 https://www.acmicpc.net/problem/17404"""
"""문제
### 문제
- RGB 거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 
1번 집부터 N번 집이 순서대로 있다.
- 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
- 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
  - 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
  - N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
  - i (2 <= i <= N-1 )번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

### 입력
- N : 집의 수 ( 2 <= N <= 1,000 )
- 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 한 줄에 하나씩 주어진다.
( 1,000 보다 작거나 같은 자연수 )  

### 출력
- 모든 집을 칠하는 비용의 최솟값
"""
import sys

input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
# dp = [float('inf')] * N

dr = [0, 0, 1, 1, 2, 2]
dg = [1, 2, 0, 2, 1, 0]
db = [2, 1, 2, 0, 0, 1]

ans = float('inf')

for i in range(6):
    cost = 0
    for j in range(N):
        if j % 3 == 0:
            cost += costs[j][dr[i]]   
        elif j % 3 == 1:
            cost += costs[j][dg[i]]
        else:
            cost += costs[j][db[i]]

    print(cost)
    ans = min(ans, cost)

print(ans)