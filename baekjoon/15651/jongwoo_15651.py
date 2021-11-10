import sys

n, m = map(int, sys.stdin.readline().split())

# def recursion(k)
# k번째 수를 나열하면 그 수열 출력
# k번째까지 못갔으면 k번째까지 반복
arr= []

def recursion(k):
    if k == m + 1:
        print(' '.join(map(str, arr)))

    else:
        for i in range(1, n+1):
            arr.append(i)
            recursion(k + 1)
            arr.pop()

recursion(1)