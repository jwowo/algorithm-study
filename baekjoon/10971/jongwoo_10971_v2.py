from itertools import permutations
import sys

num = int(sys.stdin.readline().strip())
maps = []

for _ in range(num):
    maps.append(list(map(int, sys.stdin.readline().split())))

methods = permutations(range(num))

# 접근 방법 1
# 모든 조합을 이용하여 다 돌려보고 최솟값 구하기 
# method를 돌려가며 maps 배열에 넣어서 이동시의 비용 구하고 최솟값 찾기

# 최솟값 변수 설정
min_cost = 1000000 * num

# 모든 조합
for method in methods:
    current_cost = maps[ method[-1] ][ method[0] ]
    flag = True

    # 다시 돌아오는 길이 막혀있다면
    if maps[method[-1]][method[0]] == 0:
        continue

    # 각각의 조합
    for j in range(len(method)-1):  
        from_c = method[j]
        to_c = method[j+1]

        if maps[ from_c ][ to_c ] == 0:
            flag = False
            break

        current_cost += maps[from_c][to_c]

        if current_cost > min_cost:
            flag = False
            break

    if flag == False:
        continue


    if current_cost < min_cost:
        min_cost = current_cost

print(min_cost)