# 문제 접근 방법
# 가로 세로 길이 최대 100cm
# 둘째 줄에는 칼로 잘라야하는 점선의 개수
# 셋째 줄부터 마지막까지는 한줄에 점선이 하나씩 입력됨
# 가로는 0 (_), 세로는 1 (_) 

# 1-1. 가로의 길이 및 가로 자르는 위치를 값으로 하는 배열 생성
# 1-2. 세로도 동일
# 2-1. 각각 정렬한 뒤 가장 차이가 많이 나는 두 값의 차를 곱한다.

x = []
y = []

a, b = map(int, input().split())
x.append(a)
y.append(b)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        y.append(b)
    else:
        x.append(b)

x.append(0)
y.append(0)

x.sort()
y.sort()

max_x_len = 0
max_y_len = 0

for i in range( len(x) - 1 ):
    if x[i + 1] - x[i] > max_x_len:
        max_x_len = x[i + 1] - x[i]

for i in range( len(y) - 1 ):
    if y[i + 1] - y[i] > max_y_len:
        max_y_len = y[i + 1] - y[i]

print( max_x_len * max_y_len )
