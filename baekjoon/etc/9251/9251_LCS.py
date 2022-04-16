"""백준 9251번 LCS문제 https://www.acmicpc.net/problem/9251"""
"""문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열) 문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.


"""

import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

d = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if B[i-1] == A[j-1]:
            # d[i][j] = max(d[i-1][j], d[i][j-1]) + 1
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

# for i in d:
#     print(i)

print(d[-1][-1])