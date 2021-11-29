"""백준 11049번 행렬 곱셈 순서 https://www.acmicpc.net/problem/11049"""
"""문제
크기가 N x M인 행렬 A 와 M x K인 행렬 B 를 곱할 때 필요한 곱센 연산의 수는 
총 N x M x K이다.
행렬 N개를 곱하는데 필요한 곱셉 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.
같은 곱셉이지만, 곱셈을 하는 순서에 따라서 고셈 연산의 수가 달라진다.

행렬 N 개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수와 
최솟값을 구하는 프로그램을 작성하시고.

입력으로 주어진 행렬의 순서를 바꾸면 안된다.

N : 행렬의 개수 ( 1 <= N <= 500 )
r, c = 행렬의 크기 ( 1 <= r, c <= 500 )

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.
"""

"""문제 접근 방법
인접한 2개의 행렬은 따로 점화식 필요없이 dp 배열체 저장한다.

재귀적으로 행렬의 곱셈의 순서를 재귀적으로 만든다.
def dp(start, end):
    이미 값이 있다면 그 값 반환
    만약 start가 end보다 크거나 같다면 행렬하나를 곱하는 방법은 없기 때문에 0 반환
    점화식대로 for문 돌려서 min 값을 찾는다.
    for i in range(start, end):
"""

import sys

input = sys.stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]
matrix_info = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 1):
    dp[i][i + 1] = matrix_info[i][0] * matrix_info[i + 1][0] * matrix_info[i + 1][1]

def get_min_value(start, end):
    if dp[start][end] != 0:
        return dp[start][end]
    if start == end:
        return 0

    min_value = 2 ** 31
    for k in range(start, end):
        min_value = min(
            min_value,
            get_min_value(start, k) + get_min_value(k + 1, end) + matrix_info[start][0] * matrix_info[k + 1][0] * matrix_info[end][1]
        )
    dp[start][end] = min_value

    return min_value

print(get_min_value(0, N - 1))
