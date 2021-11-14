"""
날짜            :   2021년 11월 12일
문제 이해 시간  :   2:00pm - 2:pm
코딩 시간       :   :pm - :pm
디버깅 시간     :   :pm - :pm
"""

"""
문제 해결 아이디어
0. 입력된 리스트를 이용하여 LIS 배열을 만드는 것이 매우 중요하다.
1. 가장 긴 부분 수열을 저장할 LIS 배열을 만든다.
2. 입력받은 리스트의 요소를 0 ~ (n-1) 까지 조건에 맞게 LIS 배열에 넣는다. 
3. 해당 수의 위치를 lower bound로 찾는다.
3-1. 만약 해당 숫자가 LIS 배열의 마지막 인덱스보다 크다면 LIS 배열에 append() 한다. 
4. 
"""

"""
문제 해결 아이디어
0. 입력된 리스트를 이용하여 LIS 배열을 만드는 것이 매우 중요하다.
1. 가장 긴 부분 수열을 저장할 LIS 배열을 만든다.
2. 입력받은 리스트의 요소를 0 ~ (n-1) 까지 조건에 맞게 LIS 배열에 넣는다. 
3. 해당 수의 위치를 lower bound로 찾는다.
3-1. 만약 해당 숫자가 LIS 배열의 마지막 인덱스보다 크다면 LIS 배열에 append() 한다. 
4. 
"""

import sys

# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().split()))

n = 8
arr = [1, 100, 101, 2, 3, 4, 5, 6]
# arr = [10, 20, 10, 30, 20, 50]
# print(f'초기 배열 : {arr}')

lis_list = []

def binary_search_index(lis_list, value):
    start = 0
    end = len(lis_list) - 1

    target_idx = 1001

    while start <= end:
        mid = (start + end) // 2

        if lis_list[mid] == value:
            target_idx = mid
            break 

        elif lis_list[mid] > value:
            target_idx = min(target_idx, mid)
            end = mid - 1
        else:
            start = mid + 1

    lis_list[target_idx] = value
            
            
def check_lis(lis_list, value):
    # lis 배열에 값이 없을때 그냥 추가 (첫번째 인덱스)
    if (len(lis_list) == 0):
        lis_list.append(value)

    # lis 배열에서 가장 큰 수보다 입력받은 수가 더 크다면 마지막에 추가
    elif lis_list[-1] < value:
        lis_list.append(value)

    # lis 배열 안에 교체할 값이 있다면 binary_search_index()를 통해서 해당 인데스와 값 교환
    else:
        binary_search_index(lis_list, value)


for i in range(len(arr)):
    check_lis(lis_list, arr[i])
    # print(lis_list)

print(len(lis_list))