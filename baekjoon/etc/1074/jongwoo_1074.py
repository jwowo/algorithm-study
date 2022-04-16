import sys

n, r, c = map( int, sys.stdin.readline().split())
count = 0

def z(n, x, y):
    global count

    if x == r and y == c:
        print(int(count))
        exit(0)

    if n == 1:
        count += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        count += n * n
        return

    z(n/2, x, y)
    z(n/2, x, y + n/2)
    z(n/2, x + n/2, y)
    z(n/2, x + n/2, y + n/2)

z(2 ** n, 0, 0)



"""
def rec(n, a, b):
    global idx

    if n == 1:
        arr[a][b] = idx
        idx += 1
        arr[a][b+1] = idx
        idx += 1
        arr[a+1][b] = idx
        idx += 1
        arr[a+1][b+1] = idx
        idx += 1

    else:
        rec(n-1, a, b)
        rec(n-1, a , b + 2 ** (n-1))
        rec(n-1, a + 2 ** (n-1), b)
        rec(n-1, a + 2 ** (n-1), b + 2 ** (n-1))

arr = [ [0] * 2 ** n for _ in range(2 ** n) ]

rec(n , 0, 0)
print(arr[r][c])
"""