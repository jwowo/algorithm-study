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

def fibo(n):
    if n < 2:
        return n
    
    return fibo(n - 1) + fibo(n - 2)

print(fibo(n))