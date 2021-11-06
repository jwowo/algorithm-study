import sys

def gcd( x : int, y : int ) -> int:
    if y == 0:
        return x
    else:
        return gcd( y, x % y )

    
a, b = map(int, sys.stdin.readline().split())

if b > a:
    a, b = b, a

result = gcd( int( a ) , int( b ) )

print('1' * result)
