# 문제 이해 시간 : 2021-11-09   03:55pm - 04:00pm
# 풀이 생각 시간 : 2021-11-09   04:00pm - 04:20pm
# 코딩 시간 : 2021-11-09        04:20pm - 04:42pm
# 디버깅 시간 : 2021-11-09      pm - pm

# 문제 접근 방법
	# 1.itertools 에서 combinations를 통해 9C2 조합을 찾는다.
	# 2.찾은 9C2 조합에서 합이 100일 경우 해당 인덱스의 난쟁이를 출력한다.

import sys
from itertools import combinations

# input 저장
dwarfs = []
idx_arr = []
result = []

for i in range(9):
    dwarfs.append(int(sys.stdin.readline().strip()))    
    idx_arr.append(i)

dwarfs.sort()

combination_list = (list(combinations(idx_arr, 7)))

for i in range(len(combination_list)):
    combination = combination_list[i]
    sum = 0

    for j in range(7):
        sum += dwarfs[combination[j]]

    if sum == 100:
        result = combination

for i in result:
    print(dwarfs[i])




