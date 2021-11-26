"""백준 12865 평범한 배낭 : https://www.acmicpc.net/problem/12865"""
"""문제
준서는 여행을 가려고 한다.
가지고 다닐 배낭을 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 n개의 물건이 있다. 
각 물건은 무게 W와 가치 V를 가지는데
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
아직 행군을 해본 적이 없는 준서는 최대한 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
준서가 최대한 즐거운 여해을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자

n : 물품의 수 ( 1 <= n <= 100 )
k : 준서가 버틸 수 있는 무게 ( 1 <= k <= 100000 )
w : 물건의 무게 ( 1 <= w <= 100000 )
v : 물건의 가치 ( 1 <= v <= 1000 )
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

travel_goods = []
for _ in range(n):
    weight, value = map(int, input().split())
    travel_goods.append((weight, value))

# 메모이제이션을 위한 dp 테이블 생성
d = [0] * (k + 1)

for goods_weight, goods_value in travel_goods:
    for sack_weight in range(1, k + 1):

        # if sack_weight < goods_weight:
        #     d[sack_weight] = d[sack_weight - 1]
        if sack_weight < goods_weight:
            continue
        else:
            d[sack_weight] = max(
                d[sack_weight - goods_weight] + goods_value,
                d[sack_weight]
            )

        # print(goods_weight)
        # print(d)

print(d)
print(d[-1])
