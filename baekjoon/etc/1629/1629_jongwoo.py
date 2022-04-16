import sys

a, b, c = map(int, sys.stdin.readline().split())

def divide(a, b, c):
    if b == 1:
        return a % c
    
    temp = divide(a, b // 2, c)

    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp) * a % c

result = divide(a, b, c)

print(result)
