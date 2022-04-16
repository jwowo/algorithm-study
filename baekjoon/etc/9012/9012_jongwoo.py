import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    ps = sys.stdin.readline().strip()

    stack = []
    flag = True

    for i in ps:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print('NO')
                flag = False
                break
            else:
                stack.pop()
    
    if flag == True:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
