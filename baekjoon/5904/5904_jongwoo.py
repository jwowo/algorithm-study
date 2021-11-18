"""Moo 게임
이 문제는 입력 n이 10억(10^9)이므로 시간복잡도가 O(N)이어도
10초가 걸린다.

'Moo 게임에서 n번째 숫자가 뭐야?' 라고 물어봤을때
'n번째 숫자는 k번째에서 만들어진 수열 Stage(k) 의 n번째 숫자야' 
라고 말해주면 된다.

우리는 각 stage에서 수열이 몇개씩 생기는지 알고 있다. (점화식 )
수열이 커져도 앞부분은 이전 수열과 동일하므로

(1) 몇번째 stage에서 수열의 길이가 target의 길이를 넘어서는지를 찾는다.

(2) target이 해당 stage에서 어느 구간에 있는지를 확인 후 
    재귀적으로 범위를 작게 분할하여 반환되는 값을 찾아나간다.

구간 :    (1)  |        (2)        |   (2)        
s(n) = s(n-1) + "moo" + ("o" * k) + S(n-1)
"""

import sys

target = int(sys.stdin.readline())

"""
----- (1) -----
s[0] -> s[1] -> s[2] -> s[3] 순으로 stage가 증가한다고 생각하면서
while문을 통해  몇번째 stage에서 target의 길이를 넘어서고, 
그 수열의 길이가 무엇인지를 찾는다.

알고 싶은 것 : 
    몇번째 stage에서 target의 길이를 넘어서는가?

알고 있는 것 :
    초기 stage는 0
    초기 length는 3
"""
stage = 0
length = 3

while length < target:
    stage += 1
    # 다음 length = 현재 length + 3("moo") + 현재 stage + 현재 length
    length = (2 * length) + 3 + stage

# print(f'target({target})은 {stage} 번째 수열에 속해있다. ')


"""
----- (2) -----
target인덱스가 S(stage) 수열에 속한다는 것을 알았다.
이제 target인덱스가

구간 :          (1)    |        (2)             |   (3)       
s(stage) = s(stage-1) + "m" + "oo" + ("o" * k) + S(stage-1) 의

(1) (2) (3) 에서 어느 구간에 있는지 확인해야한다.
"""

def find_value(target, stage, length):
    if stage == 0:
        if target == 1:
            return 'm'
        else:
            return 'o'

    # stage와 length를 이전 단계로 되돌린다.
    length = (length - 3 - stage) // 2
    stage -= 1

    # 구간 (1)에 속해있을 경우
    if target <= length:
        return find_value(target, stage, length)

    # 구간 (3)에 속해있을 경우 
    elif length + 3 + (stage + 1) < target:
        # +1 하는 이유는 현재 stage가 기준이기 때문
        return find_value(target - (length + 3 + (stage + 1)), stage, length)

    # 구간 (2)에 속해있을 경우
    else:
        if target == length + 1:
            return 'm'
        else:
            return 'o'

print(find_value(target, stage, length))
