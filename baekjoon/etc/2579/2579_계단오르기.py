"""백준 2579 계단오르기 https://www.acmicpc.net/problem/2579"""
"""문제
계단오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
각각의 계딴에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
 
규칙
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
2. 연속돈 세 개의 계단을 모두 밟아서는 안된다. 단 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

각 계단에 쓰여 있는 점수가 주어질 떄 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램 작성

계단의 개수 : 300 이하의 자연수
계단에 쓰여 있는 점수 : 10,000 이하의 자연수 이다.
"""

import sys

input = sys.stdin.readline
N = int(input())
W = [0]
for _ in range(N):
    W.append(int(input()))

dp = [0] * (N + 3)

# N == 1 edge case 
if N == 1:
    print(W[1])
    sys.exit()

# 기저 사례 
dp[1] = W[1]
dp[2] = W[1] + W[2]

# 점화식 (연속 3칸 점프 안됨)
for i in range(3, N + 1):
    dp[i] = max(
        dp[i - 2] + W[i],
        dp[i - 3] + W[i - 1] + W[i]
    )

print(dp[N])
