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


num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    arr.append(int(sys.stdin.readline()))

# bubble_sort(arr)
# selection_sort(arr)
# insertion_sort(arr)
shell_sort(arr)

for i in arr:
    print(i)