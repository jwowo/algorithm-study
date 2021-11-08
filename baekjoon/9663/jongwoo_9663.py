# 문제 접근 방법
# 백트래킹 & DFS 이용
# ( 조건 1 )같은 열(세로)에는 하나의 퀸만 놓을 수 있다.
# 길이가 5인 배열 c 생성 ( 인덱스 : 열 인덱스, 값 : 행 인덱스 )
# ( e.g ) c[1] = 4 이면, ( 4 , 1 )에 퀸이 있음
# DFS를 돌면서 가로, 대각선에 퀸을 놓을 수 있는지 확인
# DFS를 돌면서 n 번째 퀸을 놓았을때 count += 1

import sys

n = int(sys.stdin.readline())
col = [ 0 for _ in range(n+1) ]
count = 0

def check_validation(x):
    # 같은 열이 있는지 & 대각선이 있는지 체크
    for i in range(1, x):
        # 기울기
        if ( col[i] == col[x] or abs(col[x] - col[i]) == (x - i) ):
            return False

    return True

def queen(x):
    global count

    if x > n:
        count += 1

    # c[0] -> c[1] -> ... -> c[n]
    else:
        for i in range(1, n+1):
            col[x] = i
            if check_validation(x):
                queen(x+1)
                
queen(1)
print(count)