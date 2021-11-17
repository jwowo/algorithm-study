"""
문제 해결 아이디어
k번째 사람을 죽여서 없앤다는 말은
k-1 칸을 움직인다는 의미

k-1번 만큼 첫번째 사람을 맨 뒤로 시키고
첫번째 사람을 죽인다
"""

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

people = deque(list(range(1, n + 1)))
result = []

while len(people) > 0:
    for i in range(k-1):
        out = people.popleft()
        people.append(out)

    result.append(people[0])
    people.remove(people[0])

print('<' + ', '.join(map(str, result)) + '>' )