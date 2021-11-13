"""
문제 해결 아이디어
1 ~ n 까지의 큐 생성

step1. 큐 popleft()해서 맨 위 카드 버림
step2. 큐 popleft() 해서 나온 수를 큐에 append() 한다.

큐의 길익 1이 남을 때까지 step 1과 step 2 반복
주의 step1이 끝나고 카드 한장이 남으면 반복이 종료되어야 한다.
"""

import sys
from collections import deque

n = int(sys.stdin.readline().strip())

# 1 ~ n 인 큐 생성
cards = deque(list(range(1, n+1)))

def drop_card():
    cards.popleft()

def change_position():
    first_card = cards.popleft()
    cards.append(first_card)

if not len(cards) == 1:
    while True:
        drop_card()
        
        if len(cards) == 1:
            break

        change_position()

print(cards[0])