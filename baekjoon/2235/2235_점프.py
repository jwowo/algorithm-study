"""백준 2253번 점프 https://www.acmicpc.net/problem/2253"""
"""문제
N ( 2 <= N <= 10,000 ) 개의 돌들이 같은 간격으로 놓여 있다.
편의상 순서대로 1, 2, ,..., N 번 돌이라고 부르자.
당신은 현재 1번 돌 위에 있는데, 이 돌들 사이에서 점프를 하면서 N번째 돌로 이동을 하려 한다.
이때 다음 조건들이 만족되어야 한다.

1. 이동은 앞으로만 할 수 있다.
2. 제일 처음에 점프를 할 때에는 한 칸밖에 점프하지 못한다.
    즉, 1번 돌에서 2번 돌이 있는 곳으로 점프할 수 있다.
    그 다음부터는 가속/감속 점프를 할 수 있는데, 이전에 x칸 점프를 했다면, 
    다음번에는 속도를 줄여 x-1칸 점프라거나, x칸 점프하거나, 속도를 붙여 x + 1칸 점프를 할 수 있다.
    물론 점프를 할 때에는 한 칸 이상씩 해야 한다.
3. 각 돌들은 각기 그 크기가 다르고, 그 중 몇 개의 돌은 크기가 너무 작기 때문에 당신은 그러한 돌에는 올라갈 수 없다.

위 조건들을 만족하면서 1번 돌에서 N 번 돌까지 점프를 해 갈 때, 필요한 최소의 점프 횟수를 구하는 프로그램을 작성하시오.

N : 돌의 개수 ( 2 <= N <= 10,000 )
M : 크기가 맞지 않은, 크기가 작은 돌의 개수 ( 0 <= M <= N-2 )

첫째 줄에 필요한 최소의 점프 횟수를 출력한다.
만약 N번 돌까지 점프해갈 수 없는 경우에는 -1을 출력한다.
"""
# BFS를 이용한 풀이
from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
check = [[] for _ in range(N + 1)]
# 리스트로하면 시간초과남
small = set()
for _ in range(M):
    small.add(int(sys.stdin.readline().strip()))

### BFS 이용
def jumpRock(N, check, small):
    q = deque()
    q.append((1, 0, 0))
    while q:
        curr_rock, move, cnt = q.popleft()
        for jump in [move-1, move, move+1]:
            if jump > 0:
                next_rock = curr_rock + jump
                if next_rock == N:
                    return cnt + 1
                if next_rock > N:
                    continue
                if move not in check[next_rock] and next_rock not in small:
                    check[next_rock].append(jump)
                    q.append((next_rock, jump, cnt+1))

    return -1

print(jumpRock(N, check, small))
