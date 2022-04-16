import sys

n, m = map(int, sys.stdin.readline().split())
arr= []

# def recursion(k) (재귀함수)
# 만약 M개를 모두 고름 -> 조건에 맞는 탐색을 한 가지 성공!
# 아직 M개를 고르지 않음 -> K 번째부터 M번째 원소를 조건에 맞게 고르는 방법 시도
def recursion(k):
    if k == m + 1:
        # arr[1...M] 배열이 새롭게 탐색된 결과
        print(' '.join(map(str, arr)))

    else:
        # 1 ~ N 까지를 k번 원소로 한번씩 정하고,
        # 매번 k+1 번부터 M번 원소로 재귀호출 해주기
        for i in range(1, n+1):
            arr.append(i)
            recursion(k + 1)
            arr.pop()

recursion(1)