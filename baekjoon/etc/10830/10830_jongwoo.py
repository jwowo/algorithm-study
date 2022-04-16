"""
N x N 행렬 A
A의 B제곱을 구하는 프로그램
수가 커질 수 있으니 A^B의 각 원소를 1000으로 나눈 나머지 출력

첫째 줄에 행렬의 크기 N과 B ( 2 <= N <= 5, 1 <= B <= 100,000,000,000 )
둘째 줄부터 N개의 줄에 행렬의 각 원소 주어짐.
행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0
"""
import sys

n, b = map(int, sys.stdin.readline().split())
# arr = [[0 for _ in range(n)] for _ in range(n)]
arr = []

def matrix_mul(a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    
    remainder(result)
    return result

def remainder(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            a[i][j] %= 1000

def divide_conquer(a, b):
    if b == 1:
        return a
    
    temp = divide_conquer(a, b//2)
    
    if b % 2 == 0:
        return matrix_mul(temp, temp)
    else:
        return matrix_mul(matrix_mul(temp, temp), a)

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# print(arr)
remainder(arr)
result = divide_conquer(arr, b)

# print('\n'.join(map(lambda x: ' '.join(map(str, x)), divide_conquer(arr, b))))

print('\n'.join(map(lambda x: ' '.join(map(str, x)), arr)))
print(arr)

