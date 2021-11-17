import sys
from collections import deque

input = sys.stdin.readline
# n : n * n 보드
# k : 사과의 개수
n = int(input())
k = int(input())

apples = []
moves = []

for _ in range(k):
    apples.append(list(map, input().split()))

l = int(input())

for _ in range(l):
    moves.append(list(input().split()))

snake = deque()
snake.append([0, 0, 'r'])

# 게임이 끝나는지 아닌지 확인
def is_game_over():
    pass

# 사과를 먹었는지 안먹었는지 확인 (필요한가?)
def ate_apple():
    pass

# 뱀의 머리를 한 칸 움직임
def move_snake(snake):
    head = snake[0]
    next_head = head
        
    if snake[0][2] == 'r':
        next_head[0] = head[0] + 1
    elif snake[0][2] == 'l':
        next_head[0] = head[0] - 1
    elif snake[0][2] == 'u':
        next_head[1] = head[1] + 1
    else:
        next_head[1] = head[1] - 1

    if next_head[0] < 0 or next_head[0] > n or next_head[1] < 0 or next_head[1] > n:
        return False

    next_head = 



time = 0

while True:
    time += 1

    move_snake(snake)
