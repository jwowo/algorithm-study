"""백준 9084번 동전 https://www.acmicpc.net/problem/9084"""
"""문제
우리나라 화페, 특히 동전의 단위로는 1원, 5원, 10원, 50원, 100원, 500원이 있다.
이 동전들로는 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다.
(1원짜리 30개) 또는 (10원짜리 2개와 5원짜리 2개) 등의 방법이 가능하다.
동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램 작성

t : 테스트 케이스 개수
n : 동전의 가지수 ( 1 < = n <= 20 )
동전의 각 금액이 오름차순으로 정렬되어 주어짐 (1원 ~ 10000원)
m : 동전으로 만들어야 하는 금액 ( 1 <= m <= 10000 )
"""

"""문제 접근 방법
동전이 작은 순으로 작은 동전으로만 사용해서 해당 m원을 구성하는 경우의 수를 더해간다.
"""

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    d = [0] * (m + 1)
    d[0] = 1


    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                d[i] += d[i - coin]
        
        print(coin, d)

    print(d[m])








"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * 10001
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], m + 1):
            dp[j] += dp[j - coins[i]]

    print(dp[m])
"""