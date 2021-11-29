"""백준 1700번 멀티탭 스케줄링 https://www.acmicpc.net/problem/1700"""
"""문제
기숙사에 살고 있는 준규는 한 개의 멀티탭 이용
준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 
여러 개의 전기용품 사용하면서 어쩔 수 없이 각종 전기용품의 프러그를 뺐다 꽂았다 하는 불편함을 겪고 있음
준규는 생활 패턴을 분석하여 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 
이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활현경을 만들려고 한다.

3구 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,
1. 키보드
2. 헤어드라이기
3. 핸드폰 충전기
4. 디지털 카메라 충전기
5. 키보드
6. 헤어드라이기

키보드, 헤어드라이기 핸드폰 충전기의 플러그를 순서대로 꼳은 다음 
디지털 카메라 충전기 플러그를 꽂기전에 핸드폰 충전기를 빼는 것이 최적일 것으로 
플러그는 한 번만 빼면 된다.

N : 멀티탭 구멍의 개수 ( 1 <= N <= 100 )
K : 전기 용품의 총 사용횟수 ( 1 <= K <= 100 )
전기 용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다.
"""

"""문제 접근 방법


1. 멀티탭에 해당 전자제품이 꽂혀있을 경우
    skip
2. 멀티탭에 빈 구멍이 있는 경우
    빈 공간에 전자제품 꽂는다
3. 멀티탭에 빈 공간이 없을 경우
    1) 멀티탭에 꽂혀있는 전자제품 중 이후에 사용하는 것이 없는 경우
        사용하지 않는 제품 빼고 새 제품 꽂는다
    2) 멀티탭에 꽂혀있는 전기용품이 이후에도 사용되는 경우
        전기 용품 중 가장 나중에 사용하는 전자제품 뽑고 새로운 전자제품 꽂는다

"""

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
orders = list(map(int, input().split()))

multitap = []
count = 0

for i, current_device in enumerate(orders):
    # 1. 지금 사용할 전자제품이 이미 멀티탭에 꽂혀있다면 skip
    if current_device in multitap:
        continue

    # 2. 멀티탭에 여유 플러그가 아직 남아있으면 삽입
    elif len(multitap) < N:
        multitap.append(current_device)
        continue
        
    # 3. 멀티탭에 공간이 없을 경우
    else:
        candidate_del_multitap_index = 0
        max_index = 0

        for j, using_device in enumerate(multitap):
            # 1) 멀티탭에 꽂혀있는 전자제품 중 이후에 사용하는 것이 없는 경우
            # 사용하지 않는 제품 빼고 새 제품 꽂는다
            if using_device not in orders[i + 1:]:
                candidate_del_multitap_index = j
                break

            # 2) 멀티탭에 꽂혀있는 모든 전기용품들이 이후에도 사용되는 경우
            # 멀티탭에 꽂혀있는 전자제품 중 가장 나중에 사용하는 전자제품 뽑고 새로운 전자제품 꽂는다   
            else:
                if orders[i + 1:].index(using_device) > max_index:
                    candidate_del_multitap_index = j
                    max_index = orders[i + 1:].index(using_device)

        del multitap[candidate_del_multitap_index]
        multitap.append(current_device)
        count += 1

print(count)