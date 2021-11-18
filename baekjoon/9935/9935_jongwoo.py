"""문자열 폭발
문제 접근 방법

1. 첫째줄에 입력받은 텍스트를 한글자씩 스택에 넣는다.
2. 한글자를 넣을때마다 폭탄의 맨마지막 문자와 같은지 비교한다.
3. if 스택에 넣은 글자 == 폭탄의 맨 마지막 문자 이면
4. stack의 마지막에서부터 폭탄의 길이수 만큼의 텍스트와 폭탄을 비교한다.
4-1. stack에 쌓여있던 텍스트와 폭탄의 텍스트가 같다면 폭탄의 글자 수 만큼 pop()해준다.
4-2. stack에 쌓여있던 텍스트와 폭탄의 텍스트가 다르다면 폭탄이 아니므로 
    다음 글자로 넘어가서 1~4의 과정을 반복한다.
"""

import sys

texts = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())

# print(f'text : {texts}')
# print(f'bomb : {bomb}')

stack = []

for text in texts:
    stack.append(text)

    if stack[-1] == bomb[-1]:
        compare_length = len(bomb)

        if stack[-compare_length:] == bomb:
            for i in range(compare_length):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')