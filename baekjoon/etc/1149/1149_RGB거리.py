"""
### 문제 출처 : https://www.acmicpc.net/problem/1149

### 문제
- RGB 거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 
1번 집부터 N번 집이 순서대로 있다.
- 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
- 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
  - 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
  - N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
  - i (2 <= i <= N-1 )번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

### 입력
- N : 집의 수 ( 2 <= N <= 1,000 )
- 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 한 줄에 하나씩 주어진다.
( 1,000 보다 작거나 같은 자연수 )  

### 출력
- 모든 집을 칠하는 비용의 최솟값을 출력하시오.

### 문제 접근 방법
- 현재 집의 색을 선택할 때, 이전 집이 빨강, 초록, 파랑의 경우에 대해서 각각의 경우에 선택할 수 있는 나머지 2개의 색들 중 최소의 비용을 선택하여 dp 테이블을 채워 나간다.\

### 코드

"""

import sys

input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = []
dp.append((costs[0][0], costs[0][1], costs[0][2]))

for i in range(1, N):
    candidateR, candidateG, candidateB = costs[i]
    preR, preG, preB = dp[-1]

    curR = candidateR + min(preG, preB)
    curG = candidateG + min(preR, preB)
    curB = candidateB + min(preR, preG)

    dp.append((curR, curG, curB))

finalR, finalG, finalB = dp[-1]

print(min(finalR, finalG, finalB))
