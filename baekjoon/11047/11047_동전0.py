"""백준 11047번 동전0 https://www.acmicpc.net/problem/11047"""
"""문제
준규가 가지고 있는 동전은 총 N종류, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이때 필요한 동전의 개수의 최솟값을 구하는 프로그램을 작성하시오

N : 동전의 종류 (1 <= N <= 10)
K : 만들려고 하는 그 가치의 합 (1 ≤ K ≤ 100,000,000)
동전의 가치 Ai가 오름차순으로 주어진다.

K원을 만드는데 필요한 동전 개수의 최솟값 출력
"""
"""
배낭 문제처럼 무게와 가치가 물건마다 다르지 않다.
문제에서는 동전의 개수의 최솟값을 구하고 싶다.
그렇다면 큰 동전부터 하나씩 k와 비교해가며 
크기가 큰 동전부터 하나씩 비교하면서 넣는다 
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
    
ans = 0
list_ = []

for coin in coins[::-1]:
    if K == 0:
        break

    # K 를 coin 으로 나눈 몫만큼 ans에 추가하고 (ans += K // coin)
    # K에는 나머지 저장 ( K %= coin )
    if coin <= K:
        ans += K // coin
        K %= coin

print(ans)


""" 시간 초과 코드
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
    
ans = 0
list_ = []

for coin in coins[::-1]:
    if K == 0:
        break

    while coin <= K:
        K -= coin
        ans += 1
        list_.append(coin)

print(ans)
"""
