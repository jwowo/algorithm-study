import sys

num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    arr.append(int(sys.stdin.readline()))

def quick_sort(arr, start, end):
    # 1.피벗은 첫번쨰 원소
    # 2.두번째 인덱스부터 오른쪽으로 피벗보다 큰 값 찾는다
    # 3.마지막 인덱스부터 왼쪽으로 피벗보다 작은 값 찾는다
    # 4. 찾다가 왼쪽인덱스와 오른쪽인덱스가 엇갈리면 왼쪽에 있는 값과 피벗의 위치를 변경한다.
    # 5. 엇갈리지 않으면 찾은 두 값의 위치를 변경한다.
    # 6. 작은 그룹과 큰 그룹을 각각 재귀적으로 quick_sort()한다.
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left < end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]

        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

def merge(arr, low, mid, high):
    temp = []
    l, h = low, mid

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < high:
        temp.append(arr[h])
        h += 1

    for i in range(low, high):
        arr[i] = temp[i - low]
            

def merge_sort(arr, low, high):
    # 1. 일단 다 나누고 나중에 합친다.
    # 2. 반으로 어떻게 나눌꺼야?
    if high - low < 2:
        return
    
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid, high)
    merge(arr, low, mid, high)

#quick_sort(arr, 0, len(arr) - 1)
merge_sort(arr, 0, len(arr))

for a in arr:
    print(a)