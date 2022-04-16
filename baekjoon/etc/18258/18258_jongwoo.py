from collections import deque
import sys

n = int(sys.stdin.readline().strip())

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    if len(queue) == 0:
        return -1
    else:
        return(queue[0])

def back():
    if len(queue) == 0:
        return -1
    else:
        return(queue[-1])

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())