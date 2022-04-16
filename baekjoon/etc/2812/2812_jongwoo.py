"""
이 문제는 n자리수의 숫자와 k가 주어졌을 때 k개의 숫자를 지웠을 때
가장 큰 숫자가 남도록 해야한다.

이 문제 해결하기 위해서 k개의 숫자를 지웠을 때, 
가장 큰 숫자가 남으려면 앞자리의 숫자가 커야한다는 아이디어에서 시작했다.

숫자를 앞에서부터 하나씩 스택의 top과 비교하여
현재 숫자가 스택의 top보다 크다면 스택의 top을 pop한다.
pop할 때마다 count를 증가하여 k번 pop 하고 
뒤에 숫자들은 그대로 스택에 추가한다.

그렇게 되면 k번 수를 제거할때마다 맨 앞자리의 수가 커지게 된다. 

** 중복된 수를 넣었을 때 1( n : 4, k : 2, num : 6666 )
** 중복된 수를 넣었을 때 2( n : 4, k : 2, num : 8841 )
출력시에 스택에 저장된 값을 
0 부터 n-k 까지(전체 숫자 개수 - 제거할 숫자 개수 ) 출력한다. 
"""
import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

stack = []
count = 0

for x in num:
    while stack and count < k:
        top = stack[-1]

        if top < x:
            stack.pop()
            count += 1

        else:
            break
    
    stack.append(x)

print(''.join(stack[:n-k]))