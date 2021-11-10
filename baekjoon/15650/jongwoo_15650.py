import sys

n, m = map(int, sys.stdin.readline().split())
result = []

def rec(start, k):
    if k == m + 1:
        print(' '.join(map(str, result)))

    else:
        for i in range(start, n+1):

            # 이미 저장한 값인지 확인하는 루틴
            flag = True

            for j in result:
                if i == j:
                    flag = False
                    
            if not flag:
                continue

            result.append(i)
            rec(i, k + 1)
            result.pop()

rec(1,1)