"""
문제해결 아이디어
( 와 [ 가 들어오면 스택에 넣는다.
) 와 ]의 곱하는 숫자가 다르므로 분리하여 생각한다.
각 경우 스택이 1이상인 경우 스택의 맨위 요소를 뽑아 (인지 [인지 확인한다.
맨위가 (혹은 [ 일때는 숫자를 넣고 앞에 숫자들이 있는 경우 
그 숫자들의 합을 구해 합에 2나 3을 곱한다.
"""

import sys

text = sys.stdin.readline().strip()
stack = []
answer = 0

for s in text:
    if s == ')':
        temp = 0
        if len(stack) == 0:
            print(0)
            sys.exit(0)
        
        while len(stack) != 0:
            top = stack.pop()
            # 짝이 맞지 않는 괄호가 나오면
            if top == '[':
                print(0)
                sys.exit(0)
            # 짝이 맞는 괄호가 나왔을때
            elif top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(temp * 2)
                break
            
            # 중간에 다른 숫자가 삽입되어 있을때
            else:
                temp += top

    elif s == ']':
        temp = 0
        if len(stack) == 0:
            print(0)
            sys.exit(0)

        while len(stack) != 0:
            top = stack.pop()
            
            # 짝이 맞지 않는 경우
            if top == '(':
                print(0)
                sys.exit(0)
            
            # 이미 이전에 완성된 괄호들은 temp에 저장한다.
            # 최종적으로 짝이 맞으면 temp에 3을 곱한다.
            elif top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(temp * 3)
                break
            
            # 중간에 다른 이미 완성된 괄호들이 있는 경우
            else:
                temp += top

    elif s == '(' or s == '[':
        stack.append(s)
    else:
        print(0)
        sys.exit(0)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        sys.exit(0)
    else:
        answer += i
    
print(answer)

