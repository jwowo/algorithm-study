"""
# 포인트
# 1. white와 blue의 개수를 global 변수로 선언
# 2. n은 2의 지수승이므로 종이를 4분할할 때 각각의 x, y 인덱스에 n // 2 만큼 더하기
"""
import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0

def recursion(x, y, n):
    """
    Args
        arr (list)  : 색종이의 색 정보가 저장되어있는 2차원 배열
        n (int)     : 색종이의 한변의 길이
    Returns
        (int) : 모든 원소의 색이 같을 경우 1 을 반환, 아닐 경우,
        상하좌우 4개로 나눠서 재귀적으로 개수를 구하여 그 4개의 합을 반환
    """
    global white, blue

    check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                recursion(x, y, n//2)
                recursion(x, y + n//2, n//2)
                recursion(x + n//2, y, n//2)
                recursion(x + n//2, y + n//2, n//2)
                return 

    if check == 1:
        blue += 1
        return 
    else:
        white += 1
        return 

recursion(0, 0, n)

print(white)
print(blue)