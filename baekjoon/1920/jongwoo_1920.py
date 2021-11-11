import sys

# 문제 접근 방법
# N과 M의 범위는 10^5이다. N과 M 사이의 모든 수를 비교하는 방법은 시간 복잡도가 (10^5)^2 = 10^10 ( O(N^2) )
# 문제의 시간 제한이 1초이다. 1초에 1억번의 연산을 한다고 가정하면 1억 = 10^8 로 시간초과이다.
# 따라서 탐색 범위를 절반으로 줄이는 이진 탐색을 이용한다 
# 이진 탐색 시간 복잡도 O(log N) 

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().split()))

a.sort()

def find_number(arr, start, end, target):
    """
    Args:
        arr (list) : 숫자들이 저장되어 있는
        start (int) : 탐색을 진행할 첫 인덱스
        end (int) : 탐색을 진행할 마지막 인덱스
        target (int): 찾을 숫자
    Returns:
        bool : 찾는 숫자가 있으면 True, 없으면 False 
    """
    if start > end:
        return False

    middle = ( start + end ) // 2

    if arr[middle] == target:
        return True
    elif arr[middle] > target:
        return find_number(arr, start, middle - 1,  target)
    else:
        return find_number(arr, middle + 1, end, target)    


for i in x:
    if find_number(a, 0, len(a) - 1, i):
        print(1)
    else:
        print(0)
