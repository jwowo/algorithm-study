"""백준 2493번 탑

import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    
    if not stack:
        answer.append(0)

    stack.append([i, towers[i]])

print(' '.join(map(str, answer)))
"""

"""백준 1629번 곱셉
import sys

a, b, c = map(int, sys.stdin.readline().split())

def recursion(a, b, c):
    if b == 1:
        return a % c
    # 홀수일 때
    if b % 2 == 1:
        temp = recursion(a, b // 2, c)
        return (temp * temp * a) % c

    # 짝수일 때
    else:
        temp = recursion(a, b // 2, c)
        return (temp * temp) % c

print(recursion(a, b, c))
"""

"""백준 2630번 색종이 만들기
# 포인트
# 1. white와 blue의 개수를 global 변수로 선언
# 2. n은 2의 지수승이므로 종이를 4분할할 때 각각의 x, y 인덱스에 n // 2 만큼 더하기

import sys

def recursion(x, y, n):
    global blue, white

    check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                recursion(x, y, n // 2)
                recursion(x +  n // 2, y, n // 2)
                recursion(x, y + n // 2, n // 2)
                recursion(x + n // 2, y + n // 2, n // 2)
                return 

    if check == 1:
        blue += 1
        return
    else:
        white += 1
        return 

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

blue, white = 0, 0

recursion(0, 0, n)

print(white, blue)
"""

"""백준 8982 사냥꾼
import sys

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if fireman_pos[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
            
    return start 

m, n, l= map(int, sys.stdin.readline().split())

fireman_pos = list(map(int, sys.stdin.readline().split()))
animal_pos = []
count = 0

for _ in range(n):
    animal_pos.append(list(map(int, sys.stdin.readline().split())))

fireman_pos.sort()

for animal in animal_pos:
    position = binary_search(0, len(fireman_pos), animal[0])

    if abs(fireman_pos[position - 1] - animal[0]) + animal[1] <= l or abs(fireman_pos[position] - animal[0]) + animal[1] <= l:
        count += 1

print(count)
"""

"""백준 2470번 두 용액
import sys

def binary_search(start, end):
    min_value =  abs(num[start] + num[end])
    min_num = [num[start], num[end]]

    while start < end:
        sum = num[start] + num[end]

        if sum == 0:
            return num[start], num[end]

        if abs(sum) < min_value:
            min_value = abs(num[start] + num[end])
            min_num[0] = num[start]
            min_num[1] = num[end]

        if sum > 0:
            end -= 1
        else:
            start += 1
    return min_num

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

answer = binary_search(0, len(num) - 1)

print(' '.join(map(str, answer)))
"""

"""백준 10000번 원 영역
import sys

n = int(sys.stdin.readline())

def check_connection(coordinates):
    stack = []
    count = 1   # 원이 없어도 공간 하나는 있음

    for circle_type, coordinate in coordinates:
        # print(f'현재 좌표 : {coordinate}')
        # 원의 시작점이면 무조건 삽입
        if circle_type == 0:
            stack.append([circle_type, coordinate])

        # ***** 스택 문제는 pop() 할 때 어떤 조건을 만족하는지 연산, 확인 하는 과정이 중요 *****
        #
        # else: 
        #   원의 시작점이 아니라면 pop 할건데
        #   pop한 요소가 원이냐? 원의 시작점이냐? 가 중요
        #       -> 내 원의 시작 좌표와 내 원의 끝 좌표 사이에 원이 있다는 말은
        #       -> 스택에 쌓여있는 원들이 내 원 안에 속해있다는 의미 
        # 
        #   원이면 원인 것들을 계속 pop 하여 
        #       지름 정보를 (inner_circle)계속 더하여 저장 (겹쳐져있지 않기 때문에 가능)
        #      
        #   내 원(new_circle)의 시작점이 나오면 
        #       (원의 끝점 좌표 - 원의 시작점 좌표) 를 통해 내 원의 지름 구함
        #   
        #   내 원의 지름 vs 스택에 저장되어 있던 이전 원(inner_circle)들의 지름의 합을 비교하여
        #       지름이 같으면 이어져있다는 의미이므로 count += 2 
        #       아니면 이어져있지 않다는 의미이므로 count += 1
        #   
        #   그럼 내 원안에 속해있는 원에 대한 연속성 조사는 끝남
        #   내 원이 다른 큰 원안에 속해있는 작은 원일 수 있으므로 ( 2 (원임을 알려줌) , 원의 지름) 정보를 스택에 저장

        else:
            inner_circle = 0
            while stack and stack[-1][0] == 2:
                inner_circle += stack.pop()[1]

            new_circle = coordinate - stack.pop()[1]
            if new_circle == inner_circle:
                count += 2
            else:
                count += 1

            stack.append([2, new_circle])
            
    return count

coordinates = []

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    coordinates.append([0, x - r])
    coordinates.append([1, x + r])

coordinates.sort(key = lambda x : -x[0])
coordinates.sort(key = lambda x : x[1])

answer = check_connection(coordinates)

print(answer)
"""

"""백준 2110번 공유기 설치
# 문제 접근 방법
# 1. houses 리스트에 집들의 좌표를 저장하고 오름차순 정렬한다.
# 2. 공유기를 설치할 수 있는 최소 거리를 start (1칸), 최대 거리(가장 멀리있는 집의 좌표 - 가장 처음에 있는 집의 좌표)를 end로 설정
# 3. 첫번째 집부터 공유기 설치
# 4. 설치 가능한 공유기의 개수가 c개 이상이면 더 설치할 수 있으므로 공유기 설치 거리를 +1 해준다.
# 5. c개를 넘어가지 않는다면 공유기간 설치거리를 -1 해준다.
# 6. 1~5 과정을 반복하여 c개의 공유기가 설치될 수 있는 최대 거리를 반환한다.

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))

houses.sort()

start, end = 1, houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (end + start) // 2

    current_position = houses[0]
    count = 0

    for i in range(1, n):
        if houses[i] - current_position >= mid:
            count += 1
            current = houses[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
"""

"""백준 2805번 나무자르기
import sys
input = sys.stdin.readline

tree_count, required_amount = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()
max_height = trees[-1]
# print(max_height)

height_list = []

def binary_search(required_ammount, start, end):
    
    while start <= end:        
        cut_height = (start + end) // 2
        cut_amount = 0

        for i in range(tree_count):
            if trees[i] > cut_height:
                cut_amount += (trees[i] - cut_height)

        if cut_amount == required_ammount:
            height_list.append(cut_height)
            return
        elif required_ammount < cut_amount:
            height_list.append(cut_height)
            start = cut_height + 1
        else:
            end = cut_height - 1

    return

binary_search(required_amount, 0, max_height)
print(max(height_list))
"""

"""백준 1920번 수 찾기
import sys
input = sys.stdin.readline

n_count = int(input())
n = list(map(int, input().split()))

n.sort()

m_count = int(input())
m = list(map(int, input().split()))

def binary_seach(start, end, target):
    if start > end:
        return False
  
    mid = (start + end) // 2

    if n[mid] == target:
        return True

    elif target < n[mid]:
        return binary_seach(start, mid - 1, target)

    else:
        return binary_seach(mid + 1, end, target)

for i in m:
    if binary_seach(0, len(n) - 1, i):
        print(1)
    else:
        print(0)
"""