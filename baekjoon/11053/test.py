nums = [1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6, 8, 10, 124]

def binary_search(nums, target):
    """
    바이너리 서치는 해당 숫자를 찾아주지만 
    값이 2인 인덱스중에서 배열의 길이에 따라서
    어떤 인덱스가 출력될지 모른다.
    """
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid 

        elif target < nums[mid]:
            high = mid
        else:
            low = mid + 1

def lowerbound(nums, target):
    """
    arr = [1, 2, 2, 2, 2, 3, 5] 인 배열에서 target이 2라고 할 때
    이진 탐색을 이용하여 2를 찾았더라도 
    그 2는 제일 처음의 2가 아닐 수 있다
    처음의 2를 찾기 위해서 계속 탐색 범위를 좁혀간다.

    else문에서 
    아직 target 값을 못찾았다면
    탐색 범위를 좁힌다.

    무엇을 리턴할 것인가?
    while문을 빠져나오면 low == high일때 빠져나오므로 
    low와 high는 동일하다.

    """
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if target <= nums[mid]:
            high = mid 
        else:
            low = mid + 1

    return low

def upperbound(nums, target):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if target < nums[mid]:
            high = mid
        else:
            low = mid + 1

    return low


print(binary_search(nums, 2))
print(lowerbound(nums, 2))
print(upperbound(nums, 2))












def lowerBound(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if target <= nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return start

def upperBound(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return start

