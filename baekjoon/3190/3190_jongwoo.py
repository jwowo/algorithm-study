import sys
from collections import deque

# n : n * n 보드
# k : 사과의 개수
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

snake = deque()
snake.append([0,0])

# 게임이 끝나는지 아닌지 확인
def is_game_over():
    pass

# 사과를 먹었는지 안먹었는지 확인 (필요한가?)
def ate_apple():
    pass

# 뱀의 머리를 한 칸 움직임
def move_snake(direction, change_direction):
    pass

time = 0

while True:
    time += 1
