"""백준 1912번 연속합 https://www.acmicpc.net/problem/1912"""

"""문제
### 문제
- n개의 정수로 이루어진 임의의 수열이 주어진다.
- 우리는 이 중 연속된 며 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
- 단 수는 한 개 이상 선택해야 한다.
- 예를 들어
  - 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 
  - 여기서 정답은 12+21인 33이 정답이 된다.

### 입력
- N : 수열의 개수 ( 1 <= N <= 1,000 )
- N 개의 정수로 이루어진 수열 (수는 -1,000 보다 크거나 같고, 1,000 보다 작거나 같은 정수) 

### 출력
- 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 출력
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))

"""
import sys

input = sys.stdin.readline

N = int(input())
arr = [0]
arr += list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    if dp[i - 1] <= 0:
        dp[i] = arr[i]
    else:
        dp[i] = dp[i - 1] + arr[i]

print(max(dp[1:]))
"""