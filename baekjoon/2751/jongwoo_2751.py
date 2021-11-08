import sys

def bubble_sort(arr):
    # 1. 근접한 두 이웃의 크기 비교하여 오른쪽 값이 더 작으면 교환
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

def selection_sort(arr):
    # 1. 정렬되지 않은 부분에서 가장 작은 수를 찾고, 
    # 2. 정렬된 부분 바로 다음 인덱스와 교환한다.
    n = len(arr)

    for i in range(n-1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # min_idx는 가장 작은 수의 인덱스
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    # 1. 두번째 index부터 마지막 인덱스까지 반복
    # 2. 해당 index의 값과 정렬된 부분을 역순으로 비교하면서
    # 3. 해당 index의 값이 더 작다면
    # 4. 정렬된 부분들의 값들을 오른쪽으로 한칸 옮긴다.
    # 5. 해당 index가 배열의 왼쪽 끝에 도달하거나 알맞은 위치 ( 정렬된 인덱스의 값이 더 작을 경우 ) 에 도달하면
    # 6. 그 위치에 값을 삽입한다.
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i

        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = temp 

def shell_sort(arr):
    # 1. insertion sort의 장점 살리고, 단점 보완
    # 2. h 값을 이용하여 그룹화 한 후 정렬
    # 3. h의 초기값 = n // 2 -> 반복하면서 n /= 2
    n = len(arr)
    h = n // 2

    while h > 0:
        for i in range(h, n):
            j = i - h
            temp = arr[i]

            while j >= 0 and arr[i] < arr[j]:
                arr[j+h] = arr[j]
                j -= h

            arr[j+h] = temp

        h //= 2

def quick_sort(arr, start, end):
    # 1. 첫번째 원소를 피벗으로 설정
    # 2. 2번째 인덱스부터 피벗보다 큰 값 찾음
    # 3. 마지막 인덱스부터 거꾸로 피벗보다 작은 값 찾음
    # 4. 둘 다 찾으면 찾은 두 값 위치 변경
    # 5. 만약 두 수를 찾다가 엇갈리게되면 찾은 작은 값과 피벗의 위치 변경 후 
    #       두 그룹으로 분할하여 각 그룹에 대하여 재귀적으로 quick_sort() 진행
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    # 왼쪽부터 p보다 큰 값, 오른쪽부터 p보다 작은 값을 찾으면서 하나씩 내려오는데
    # 엇갈릴 경우에 분할하기 때문에 엇갈리기전까지 while문으로 진행 
    while left <= right:
        # 왼쪽부터 p보다 큰 값 찾기
        while left < end and arr[left] <= arr[pivot]:
            left += 1
        # 오른쪽부터 p보다 작은 값 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈렸을때 pivot 과 left 위치 변경
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        # 엇갈리지 않았을때는 left와 right 위치 변경
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

# 파이썬의 장점을 살린 quick sort2()
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left_side = [ x for x in tail if x <= pivot]
    right_side = [ x for x in tail if x > pivot ]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

def counting_sort(arr):
    # 조건 : 입력 데이터의 크기 범위가 제한되어 있음. 정수 형태일때 표현 가능 
    # 1. 가능한 input의 최솟값부터 최댓값까지의 배열 생성 (배열의 인덱스가 최댓값)
    # 2. 정렬해야하는 배열을 돌면서 해당 숫자 count
    # 3. count한 배열을 돌면서 해당 index의 count 만큼 index 출력
    
    count = [ 0 for _ in range(10001)]

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        if count[i] != 0:
            for j in range(count[i]):
                print(i)




num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    arr.append(int(sys.stdin.readline()))

# bubble_sort(arr)
# selection_sort(arr)
# insertion_sort(arr)
# shell_sort(arr)
# quick_sort(arr, 0, len(arr) - 1)
# arr = quick_sort2(arr)
counting_sort(arr)

# for i in arr:
#     print(i)