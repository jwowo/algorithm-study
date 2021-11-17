import sys

n = int(sys.stdin.readline().strip())
arr = []

def push(x):
    arr.append(x)

def pop():
    if len(arr) == 0:
        return -1
    else:
        return arr.pop(-1)

def size():
    return len(arr)

def empty():
    if len(arr) == 0:
        return 1
    else:
        return 0

def top():
    if len(arr) == 0:
        return -1
    else:
        return arr[-1]

for _ in range(n):
    commands = list(sys.stdin.readline().split())
    command = commands[0]

    if command == 'push':
        number = int(commands[1])
        push(number)
    elif command == 'pop':
        print(pop())
    elif command == 'size':
        print(size())
    elif command == 'empty':
        print(empty())
    elif command == 'top':
        print(top())