import sys
from typing import Text
# N : 물품의 수, K : 최대 무게
N, K = map(int, sys.stdin.readline().split())
# 무게 테이블을 만든다.
table = [0] * (K + 1)
# 물품들을 하나 씩 살펴본다.
for _ in range(N) :
    # 물품의 무게와 가치를 입력 받는다.
    weight, value = map(int, sys.stdin.readline().split())
    # 만약 입력받은 물품의 무게가 견딜 수 있는 최대 무게보다 크다면 아래 과정 진행하지 않는다.
    if weight > K :
        continue
    # 가능한 무게를 하나 씩 확인한다.
    for possible_weight in range(K+1) :
        # 가능한 무게와 입력 받은 물품의 무게를 더한 것이 최대 무게를 넘지 않고,
        # 가능한 무게의 value가 0이 아니라면 
        if possible_weight + weight <= K and table[possible_weight] != 0:
            # 가능한 무2 게와 입력 받은 물품의 무게를 더한 무게의 value는
            # 기존의 다른 조합으로 해당 무게의 value를 도출한 값과, 지금의 조합을 비교해서 최대 인 것으로 바꾼다.  
            # print(weight, value,possible_weight )
            table[possible_weight + weight] = max(table[possible_weight + weight], table[possible_weight] + value)
            break
    # 조합 없이 물품 1개만 넣었을 때의 value는 다음과 같이 넣어준다.
    table[weight] = max(table[weight], value)
print(max(table))