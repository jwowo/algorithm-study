from itertools import permutations
import sys

num = int(sys.stdin.readline().strip())
maps = []

for _ in range(num):
    maps.append(list(map(int, sys.stdin.readline().split())))

arr = [ x for x in range(num) ]
methods = (list(permutations(arr)))

# 접근 방법 1
# 모든 조합을 이용하여 다 돌려보고 최솟값 구하기 
# method를 돌려가며 maps 배열에 넣어서 이동시의 비용 구하고 최솟값 찾기

# 최솟값 변수 설정
min_cost = 1000000 * num

# 모든 조합
for i in range(len(methods)):
    method = methods[i]
    current_cost = 0

    # 각각의 조합
    for j in range(len(method)):
        # 시작도시
        if j == 0:
            start_city = method[j]
            
            if maps[ method[j] ][ method[j + 1] ] == 0:
                break
                current_cost += (1000000 * num)
                #print(f'cost {j} : { maps[ method[j] ][ method[j + 1] ] }')
            else:
                current_cost += maps[ method[j] ][ method[j + 1] ]
                #print(f'cost {j} : { maps[ method[j] ][ method[j + 1] ] }')

        # 마지막 도시일 경우
        elif j == len(method) - 1:
            # 그 도시로 못갈때 if 문 필요(maps 가 0일때)
            if maps[ method[j] ][ start_city ] == 0:
                break
                current_cost += (1000000 * num)
                #print(f'cost {j} : { maps[ method[j] ][ start_city ] }')
            else:
                current_cost += maps[ method[j] ][ start_city ]
                #print(f'cost {j} : { maps[ method[j] ][ start_city ] }')
                #print(f'마지막은 { method[j] } 도시에서 { start_city } 도시로 이동')
        
        # 중간 도시들 경유할 때
        else:
            if  maps[ method[j] ][ method[j+1] ] == 0:
                break
                current_cost += (1000000 * num)
                
                #print(f'cost {j} : { maps[ method[j] ][ method[j+1] ] }')
            else:
                current_cost += maps[ method[j] ][ method[j+1] ]
                #print(f'cost {j} : { maps[ method[j] ][ method[j+1] ] }')

    #print(f'{i} 번째, 순열 : {methods[i]}, cost : {current_cost}', end='\n\n')

    if current_cost < min_cost:
        min_cost = current_cost

#print(f'min cost : {min_cost}')
print(min_cost)