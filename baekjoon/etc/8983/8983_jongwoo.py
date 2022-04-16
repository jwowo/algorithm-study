"""
문제 해결 아이디어
1. 모든 동물을 for loop 돌린다.
2. x축을 이용하여 동물의 좌표와 가장 가까운 사대를 하나 찾는다 ( 이진 탐색 ) 
3. 찾은 사대를 이용하여 | x - a | + b < L 인지 확인하여 
    True 이면 count += 1
    False 이면 continue
"""

import sys

# m : 사대의 수 , n : 동물의 수, l : 사정거리
m, n, l = map(int, sys.stdin.readline().split())
# rifleman_position : 사대의 x좌표 위치
rifleman_position = list(map(int, sys.stdin.readline().split()))
# animal_position : 동물의 [x, y] 좌표 위치
animal_position = []
for _ in range(n):
    animal_position.append(list(map(int, sys.stdin.readline().split())))

# print(m, n, l)
# print(rifleman_position)
# print(animal_position)

rifleman_position.sort()

def find_nearest_rifle(rifleman_position, animal_x) :
    """
    Args
        rileman_position(list)  :   사대의 x 좌표 위치
        animal_x                :   동물의 x좌표 위치

    Returns
        gunman_1 (int)  :동물과 가장 가까운 사대 인덱스 1
        gunman_2 (int)  :동물과 가장 가까운 사대 인덱스 2 
    """

    start = 0
    end = len(rifleman_position) - 1

    nearest_left = rifleman_position[0]
    nearest_right = rifleman_position[-1]

    while start <= end:
        mid = (start + end) // 2

        if animal_x == rifleman_position[mid]:
            return [rifleman_position[mid], 0]

        elif animal_x > rifleman_position[mid]:
            start = mid + 1
            nearest_left = rifleman_position[mid]
        
        else:
            end = mid - 1
            nearest_right = rifleman_position[mid]

    return [nearest_left, nearest_right]


def is_valid(nearest_guns, gun_range, animal_x, animal_y):
    for gun_position in nearest_guns:
        distance = abs(gun_position - animal_x) + animal_y 

        if distance <= gun_range:
            return True

    return False

count = 0

for animal in animal_position:
    animal_x = animal[0]
    animal_y = animal[1]
    
    nearest_guns = find_nearest_rifle(rifleman_position, animal_x)
    
    # print('-----------------------------')
    # print(f'animal position : {animal_x}, {animal_y}')
    # print(f'gun1 position : {nearest_guns[0]}')
    # print(f'gun2 position : {nearest_guns[1]}')

    if is_valid(nearest_guns, l, animal_x, animal_y):
        count += 1

print(count)
