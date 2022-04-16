"""백준 피보나치 수5 https://www.acmicpc.net/problem/10870"""
"""문제
피보나치 수는 0과 1로 시작한다.
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램 작성
"""

import sys

input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    sys.exit()

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

def fibo(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

fibo(n)
print(dp[n])