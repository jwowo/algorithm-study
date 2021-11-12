"""
문제 접근 방법
1. left를 0, right를 len(array) -1 로 둔다.
2. 두 수를 더해가면서 0인지, 0보다 큰지, 0보다 작은지 비교한다.
3. 0 이라면 array[left]와 array[right]을 result에 저장후 함수 종료
4. answer에 초기값으로 입력 최대값을 설정하고, 두 수를 더한 값이 answer보다 작다면 두 수를 저장후 
5. 0 보다 크다면 right -= 1 하고 다시 탐색을 진행한다.
6. 0 보다 작다면 left += 1 하고 다시 탐색을 진행한다.

"""
import sys


def binary_search(array, left, right):
    """
    Args:
        array   (list)  : 용액의 값이 저장되어있는 정렬된 리스트
        start   (int)   : 탐색을 진행할 첫 인덱스
        end     (int)   : 탐색을 진행할 마지막 인덱스
        target  (int)   : 찾고자하는 값 
    """
    result = array[left] + array[right]
    min_left = left
    min_right = right

    while(left < right):
        sum = array[left] + array[right]

        if sum == 0:
            return left, right
            # answer.append(tuple(sum, left, right))
            # return answer

        if ( abs(sum) < abs(result) ):
            min_left, min_right = left, right
            result = abs(sum)
        
        if sum < 0:
            left += 1
        else:
            right -= 1

    return min_left, min_right


n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))

array.sort()

min_left, min_right = binary_search(array, 0, len(array) - 1)

print( array[ min_left ], array[ min_right] )