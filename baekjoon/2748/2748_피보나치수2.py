"""https://www.acmicpc.net/problem/2748"""
"""문제
피보나치 수는 0과 1로 시작한다. 
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째 부터는 바로 아 두 피보나치 수의 합이 된다.
"""
"""문제 접근 방법
DP에는 메모이제이션 방식(재귀, 하향식)과 타뷸레이션(반복문을 이용한 배열에 값 채우기, 상향식)가 있다.
"""

# 하향식
"""
import sys

num = int(sys.stdin.readline())

dp = [0] * 91
def fibo(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]

print(fibo(num))
"""

# 상향식

import sys

num = int(sys.stdin.readline())
dp = [0] * 91
def fibo(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(fibo(num))