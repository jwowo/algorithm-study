"""문제
n 개의 수로 이루어진 수열 A1, A2, ... , An
연산자 : n - 1개 ( +, -, *, / )
"""

"""
입력 :
    n (int) : 수의 개수 ( 2 <= n <= 11 )
    a (list) : 수열
    op (list) : +, -, *, / 각각의 개수
"""

# 재귀를 이용한 풀이 방법 
import sys
from itertools import combinations, permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())

min_sum, max_sum  = 10**9, -10**9 - 1

def operation(sum, idx, plus, minus, mul, div):
    global max_sum
    global min_sum

    if idx == n:
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)
        return

    if 0 < plus:
        operation(sum + a[idx], idx + 1, plus - 1, minus, mul, div)
    if 0 < minus:
        operation(sum - a[idx], idx + 1, plus, minus - 1, mul, div)
    if 0 < mul:
        operation(sum * a[idx], idx + 1, plus, minus, mul - 1, div)
    if 0 < div:
        # 음수를 나눌 경우 C++14에 맞춰서 기준을 따라서
        # 음수를 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다.
        if sum < 0:
            temp = sum
            sum = -(-temp // a[idx])
            operation(sum, idx + 1, plus, minus, mul, div - 1)
        else:
            operation(sum // a[idx], idx + 1, plus, minus, mul, div - 1)

operation(a[0], 1, plus, minus, mul, div)

print(max_sum)
print(min_sum)