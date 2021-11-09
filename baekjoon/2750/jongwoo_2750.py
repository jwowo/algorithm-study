n = int(input())
n_list = []

def bubble_sort(n_list):
    # 비교해야하는 횟수 # n개의 수는 n-1번 비교해야한다.
    for i in range(len(n_list) - 1):
        exchange = 0
        # 비교
        for j in range( len(n_list) - 1, i, -1 ):
            if n_list[j-1] > n_list[j]:
                n_list[j-1], n_list[j] = n_list[j], n_list[j-1] 
                exchange += 1

            # 이미 정렬이 다 된 상태
        if exchange == 0:
            break

def selection_sort(n_list):
    for i in range(len(n_list) - 1):
        min = i

        # 가장 작은 수 찾기
        for j in range(i + 1, len(n_list) ):
            if n_list[j] < n_list[min]:
                min = j

        n_list[min], n_list[i] = n_list[i], n_list[min] 

def insertion_sort(n_list):
    # 두번째 수 부터 끝까지 반복문
    # while문 맨 왼쪽에 도달할때까지 or 해당 idx보다 작은 값을 만난 경우
    # 해당 idx에 삽입, 큰 값 하나씩 오른쪽으로 옮김. 
    for i in range(1, len(n_list)):
        temp = n_list[i]
        j = i

        while j > 0 and n_list[j-1] > temp:
            n_list[j] = n_list[j-1]
            j -= 1

        n_list[j] = temp

# 입력받은 수
#  배열에 저장
for i in range(n):
    num = int(input())
    n_list.append(num)

# bubble_sort(n_list)
# selection_sort(n_list)
insertion_sort(n_list)

# 정렬된 숫자 하나씩 출력
for i in n_list:
    print(i)
