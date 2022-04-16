"""백준 1931번 회의실 배정 https://www.acmicpc.net/problem/1931"""
"""문제
한 개의 회의실이 있는데, 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들고자한다.
각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 
회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자
회의는 한번 시작하면 중간에 중단될 수 없다.
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다.
이 경우에는 시작하자마자 끝나는 것으로 생각한다.

N : 회의의 수( 1 <= N <= 100,000 )
회의의 정보 (시작 시간, 끝나는 시간, 두 시간은 2^31 - 1 보다 작거나 같은 자연수 또는 0 )

최대 사용할 수 있는 회의의 최대 개수를 출력하시오
"""

"""
처음에 생각한 방법
1. 회의시작 시간 순으로 정렬한다. 
2. 회의 시작 시간이 빠른 것 부터 끝까지 탐색한다.
3. 현재 회의의 끝나는 시간보다 다음 회의가 더 빨리 끝나면 현재 회의의 끝나는 시간을 다음 회의의 끝나는 시간으로 변경한다.
(현재 회의 대신에 다음 회의를 진행한 것으로 생각한다)
4. 3의 과정을 반복하다가 다음 회의의 시작시간이 현재 회의의 끝나는 시간보다 크다면, 
현재 회의가 종료되고 다음 회의가 시작될 수 있다는 의미이므로
시행한 회의의 수에 1을 더하고, 현재 회의의 시작시간 및 끝나는 시간을 업데이트한다
5. 3-4의 과정을 반복한다.

하지만 이렇게 풀면 불필요한 코드, 비교과정이 생긴다.

개선한 풀이 방법
1. 종료 시간을 기준으로 오름차순 정렬하고 종료시간이 같다면 시작 시간을 기준으로 오름차순 정렬한다.
    (이렇게 하면 위에서 설명한 3의 과정을 할 필요가 없어진다.)
2. 회의 종료 시간이 빠른 것부터 끝까지 탐색한다.
3. 다음 회의의 시작시간(`next_start_time`)이 현재 회의의 종료시간(`current_end_time`) 이 후에 있다면
회의의 개수에 하나를 더한다.(`ans += 1`) 

이렇게 풀면 위의 풀이보다 더 직관적이다.

고민 
시작 시간 리스트와 끝나는 시간 리스트를 따로 만들어야 할까? 
아니면 리스트에 튜플 형태(시작시간, 끝나는 시간)로 넣어야할까?
큐를 사용해야할까 ?
"""

# 최적화 / 수정한 코드
import sys

input = sys.stdin.readline

N = int(input())
conferences = []

for _ in range(N):
    start, end = map(int, input().split())
    conferences.append((start, end))

# 회의 종료 시간을 기준으로 오름차순 정렬하고 종료시간이 같다면 시작 시간을 기준으로 오름차순 정렬
conferences.sort(key = lambda x : (x[1], x[0]))

# 제일 먼저 끝나는 회의의 시작 및 종료 시간 저장
current_start_time = conferences[0][0]
current_end_time = conferences[0][1]
ans = 1

for i in range(1, N):
    # 다음 회의의 시작 및 종료 시간 
    next_start_time, next_end_time = conferences[i]

    # 다음 회의의 시작 시간이 현재 회의의 종료 시간보다 크다면 업데이트 및 회의 개수에 1을 더한다.
    if next_start_time >= current_end_time:
        current_start_time = next_start_time
        current_end_time = next_end_time
        ans += 1

print(ans)


""" 처음에 푼 코드
import sys

input = sys.stdin.readline

N = int(input())
ans = 0
conferences = []

for _ in range(N):
    start, end = map(int, input().split())
    conferences.append((start, end))

conferences.sort(key = lambda x : (x[0], x[1]))

for idx, time_info in enumerate(conferences):
    start_time, end_time = time_info

    if idx == 0:
        current_end_time = end_time
        ans += 1
        continue

    if end_time < current_end_time:
        current_end_time = end_time
        continue

    elif start_time >= current_end_time:
        current_end_time = end_time
        ans += 1

print(ans)
"""
