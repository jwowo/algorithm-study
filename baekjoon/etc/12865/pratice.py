import sys

input = sys.stdin.readline

N, K = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for i, good in enumerate(goods):
    weight, value = good[0], good[1]

    # 물건의 무게가 배낭의 한도보다 크면 넘어간다
    if weight > K:
        continue

    # 배낭의 무게를 거꾸로 탐색한다.
    for sack_weight in range(K, 0, -1):
        # 해당 무게를 조합했을때 다른 물건들이 들어가있는지 확인
        # 다른 물건이 있으면 그 가치의 합으로 채워져있고,
        # 다른 물건이 없으면 0 이다. 
        if dp[sack_weight] == 0:
            continue

        # 현재 무게에서 물건의 무게를 더한 값이 배낭의 한계보다 작다면,
        # 현재 물건을 포함하지 않았을 때의 가치의 총합와
        # 현재 물건을 포함했을 때의 가치의 총합을 비교하여 갱신한다.
        if sack_weight + weight <= K:
            dp[sack_weight + weight] = max(
                dp[sack_weight + weight],
                dp[sack_weight] + value
            )

    dp[weight] = max(dp[weight], value)

print(max(dp))

