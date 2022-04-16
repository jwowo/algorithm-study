import sys

n, m = map(int, sys.stdin.readline().split())
result = []

def rec(start, k):
    if k == m + 1:
        print(' '.join(map(str, result)))

    else:
        for i in range(start, n + 1):
            result.append(i)
            rec(i, k+1)
            result.pop()

rec(1, 1)